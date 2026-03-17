import requests
import os
from datetime import datetime

# Cloud Secrets
KEY_ID = os.getenv("KEY_ID")
SECRET = os.getenv("SECRET")
PROJECT_ID = os.getenv("PROJECT_ID")

VM_IDS = [
    os.getenv("VM_1_ID"),
    os.getenv("VM_2_ID"),
    os.getenv("VM_3_ID")
]

# Telegram Secrets
TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")

def send_tg_message(text):
    if not TG_TOKEN or not TG_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    payload = {"chat_id": TG_CHAT_ID, "text": text, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Failed to send TG message: {e}")

def get_token():
    url = "https://iam.api.cloud.ru/api/v1/auth/token"
    payload = {"keyId": KEY_ID, "secret": SECRET}
    try:
        res = requests.post(url, json=payload)
        return res.json().get("access_token")
    except Exception as e:
        print(f"Auth error: {e}")
        return None

def check_and_start():
    token = get_token()
    if not token:
        send_tg_message("⚠️ <b>VM Inspector Error</b>\nFailed to get Cloud.ru auth token")
        return

    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    for vm_id in VM_IDS:
        if not vm_id:
            continue
            
        status_url = f"https://compute.api.cloud.ru/api/v1/vms/{vm_id}?project_id={PROJECT_ID}"
        
        try:
            vm_data = requests.get(status_url, headers=headers).json()
            
            if "state" not in vm_data:
                print(f"API Error for {vm_id}: {vm_data}")
                continue
                
            current_state = vm_data.get("state")
            vm_name = vm_data.get("name", "Unknown VM")
            
            print(f"Checking {vm_name}... Status: {current_state}")

            if current_state != "running":
                # VM startup attempt
                put_url = f"https://compute.api.cloud.ru/api/v1/vms?project_id={PROJECT_ID}"
                body = [{"id": vm_id, "state": "running"}]
                response = requests.put(put_url, headers=headers, json=body)
                
                if response.status_code in [200, 204]:
                    msg = (f"🚨 <b>VM State: <code>{current_state.upper()}</code></b>\n"
                           f"Name: <code>{vm_name}</code>\n"
                           f"ID: <code>{vm_id}</code>\n\n"
                           f"🚀 <b>VM Start Attempt:</b>\n"
                           f"Action: <code>running</code> command sent\n"
                           f"API Code: <b>{response.status_code}</b>")
                else:
                    msg = (f"🚨 <b>VM Start Failed</b>\n"
                           f"Name: <code>{vm_name}</code>\n"
                           f"ID: <code>{vm_id}</code>\n"
                           f"State: <b>{current_state}</b>\n"
                           f"API Code: <b>{response.status_code}</b>")
                
                send_tg_message(msg)
                print(f"Sent notification for {vm_name}")
                
        except Exception as e:
            print(f"Error processing VM {vm_id}: {e}")

if __name__ == "__main__":
    check_and_start()