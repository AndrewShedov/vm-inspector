[![Members](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=&logo=discord&logoColor=white&labelColor=black&color=%23f3f3f3&query=$.approximate_member_count&url=https%3A%2F%2Fdiscord.com%2Fapi%2Finvites%2FENB7RbxVZE%3Fwith_counts%3Dtrue)](https://discord.gg/ENB7RbxVZE)&nbsp;[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge&logo=5865F2&logoColor=black&labelColor=black&color=%23f3f3f3)](https://github.com/AndrewShedov/vm-inspector/blob/main/LICENSE)

# VM Inspector

[Ru](https://github.com/AndrewShedov/vm-inspector/blob/main/README_RU.md)<br>

A lightweight and secure tool designed to monitor and automatically maintain the `running` state of virtual machines in a VPC.<br>

### 🛠 Tech Stack
- **Language:** Python 3.10
- **API Integration:** [Cloud.ru SVC Public API](https://cloud.ru/docs/virtual-machines/ug/topics/api-ref-v3)
- **Infrastructure:** GitHub Actions ([workflow automation](https://github.com/AndrewShedov/vm-inspector/actions))
- **Alerting:** Telegram Bot API

### 🌟 Features

- **Multi-VM Monitoring:** Simultaneously monitors multiple VMs. The number of monitored VMs is unlimited and depends only on GitHub and Cloud.ru limits.
- **Smart Auto-Start:** Automatically sends a `running` command if a VM is in a `!= running` state.
- **Instant Alerts:** Structured Telegram notifications for every downtime event.
- **Transparent Logic:** The script reports exact API response codes and actions taken.

### 🛡 Security Architecture

- **Secrets Management:** All API keys and tokens are stored in GitHub Repository Secrets and never appear in logs.
- **Safe Logging:** Minimalistic output prevents leakage of sensitive information.
- **Idempotency:** Start commands are sent only when necessary to avoid redundant API requests.

### 📈 Telegram Monitoring Examples

- **VM Downtime Detected**<br>
If the inspector detects that a VM is off, it initiates a launch using the `running` command:

<p align="center">
<img src="https://raw.githubusercontent.com/AndrewShedov/vm-inspector/main/assets/screenshot_1.png" alt="🚨 VM State: STOPPED" width="500"/>
</p>

[LIVE](https://t.me/ShedovTop_VMInspector/5)

- **VM Start Failed (State Transition)**<br>
If a VM is in `stopping`, `starting`, etc., the cloud may reject the request (`API Code: 422`). In this case, the inspector will notify you:

<p align="center">
<img src="https://raw.githubusercontent.com/AndrewShedov/vm-inspector/main/assets/screenshot_2.png" alt="🚨 VM Start Failed" width="500"/>
</p>

[LIVE](https://t.me/ShedovTop_VMInspector/4)

### 🚀 Setup Instructions

1. **Repository Preparation**<br>
Fork this repository to your GitHub account or create a new project and copy the [vm-inspector.py](https://github.com/AndrewShedov/vm-inspector/blob/main/vm-inspector.py) and [.github/workflows/vm-inspector.yml](https://github.com/AndrewShedov/vm-inspector/blob/main/.github/workflows/vm-inspector.yml) files.
2. **GitHub Secrets Configuration**<br>
To ensure secure operation without hardcoding keys, add credentials to your repository settings.
Go to `Settings > Secrets and variables > Actions > New repository secret` and create the following secrets:
- `KEY_ID` and `SECRET`: Cloud.ru API keys.
- `PROJECT_ID`: Cloud Project ID.
- `VM_1_ID`, `VM_2_ID`, `VM_3_ID`: Monitored VM IDs.
- `TG_TOKEN`: Telegram bot token.
- `TG_CHAT_ID`: Notification channel ID.
3. **Telegram Notification Setup**<br>
3.1. **Create a Bot:** Find **@BotFather** in Telegram, send the `/newbot` command, create your bot, and save the **API Token** (e.g., `123456:ABC-DEF...`).<br>
3.2. **Get Chat ID:** Create a channel and add your bot as an administrator.<br>
3.3. Add the **@username_to_id_bot** service bot to the channel, do not grant any permissions to the bot.<br>
3.4. Open **@username_to_id_bot**, type `/start`, select **channel** in the menu, and get the **ID** (starts with `-`).<br>

> After obtaining the **ID**, you can remove **@username_to_id_bot** from the channel.<br>

4. **Launch and Verification**<br>
**Automatic Launch:** The script runs on a schedule defined in **vm-inspector.yml** (`- cron: '0,30 * * * *'`). With this setting, checks occur every 30 minutes. Under high **GitHub Actions** infrastructure load, the interval may increase to 1–3 hours.

> **Manual Launch:** For an immediate check, go to the **Actions** tab, select **VM Inspector** in the left menu, and click the **Run workflow** button.

### 📋 Job results (logs `print(f...)` can be viewed in [GitHub Actions](https://github.com/AndrewShedov/vm-inspector/actions/runs/23169801436/job/67318770105)::

1. Open the **Actions** tab.
2. Select any **VM Inspector** run.
3. Click on the **inspect-vm** job.
4. Expand the **Run inspector script** section.
<br>



[![SHEDOV.TOP](https://img.shields.io/badge/SHEDOV.TOP-black?style=for-the-badge)](https://shedov.top/) 
[![CRYSTAL](https://img.shields.io/badge/CRYSTAL-black?style=for-the-badge)](https://crystal.you/AndrewShedov)
[![Discord](https://img.shields.io/badge/Discord-black?style=for-the-badge&logo=discord&color=black&logoColor=white)](https://discord.gg/ENB7RbxVZE)
[![Telegram](https://img.shields.io/badge/Telegram-black?style=for-the-badge&logo=telegram&color=black&logoColor=white)](https://t.me/ShedovTop)
[![X](https://img.shields.io/badge/%20-black?style=for-the-badge&logo=x&logoColor=white)](https://x.com/AndrewShedov)
[![VK](https://img.shields.io/badge/VK-black?style=for-the-badge&logo=vk)](https://vk.com/ShedovTop)
[![VK Video](https://img.shields.io/badge/VK%20Video-black?style=for-the-badge&logo=vk)](https://vkvideo.ru/@ShedovTop)
[![YouTube](https://img.shields.io/badge/YouTube-black?style=for-the-badge&logo=youtube)](https://www.youtube.com/@AndrewShedov)