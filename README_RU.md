[![Members](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=&logo=discord&logoColor=white&labelColor=black&color=%23f3f3f3&query=$.approximate_member_count&url=https%3A%2F%2Fdiscord.com%2Fapi%2Finvites%2FENB7RbxVZE%3Fwith_counts%3Dtrue)](https://discord.gg/ENB7RbxVZE)&nbsp;[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge&logo=5865F2&logoColor=black&labelColor=black&color=%23f3f3f3)](https://github.com/AndrewShedov/vm-inspector/blob/main/LICENSE)

# VM Inspector

[En](https://github.com/AndrewShedov/vm-inspector/blob/main/README.md)<br>

Легкий и безопасный инструмент для мониторинга и автоматического поддержания состояния `running` виртуальных машин в VPC.<br>


### 🛠 Технологический стек
- **Language:** Python 3.10
- **API Integration:** [Cloud.ru SVC Public API](https://cloud.ru/docs/virtual-machines/ug/topics/api-ref-v3)
- **Infrastructure:** GitHub Actions ([автоматизация запусков](https://github.com/AndrewShedov/vm-inspector/actions/workflows/vm-inspector.yml))
- **Alerting:** Telegram Bot API


### 🌟 Возможности

- **Multi-VM Monitoring:** Одновременное наблюдение за несколькими ВМ. Количество наблюдаемых ВМ не ограниченно и зависит только от возможных лимитов в GitHub и Cloud.ru.
- **Smart Auto-Start:** Автоматическая отправка команды `running`, если ВМ в состоянии `!= running`.
- **Instant Alerts:** Структурированные уведомления в Telegram о каждом событии простоя.
- **Transparent Logic:** Скрипт выводит точные коды ответов API и предпринятые действия.


### 🛡 Архитектура безопасности

- **Secrets Management:** Все API-ключи и токены хранятся в GitHub Repository Secrets и не попадают в логи.
- **Safe Logging:** Минималистичный вывод данных предотвращает утечку конфиденциальной информации.
- **Idempotency:** Команды на запуск отправляются только тогда, когда это необходимо, чтобы избежать лишних запросов к API.

### 📈 Примеры мониторинга в Telegram

- **Обнаружена остановка ВМ**<br>
Если инспектор видит, что ВМ выключена, он инициирует запуск командой `running`:

<p align="center">
<img src="https://raw.githubusercontent.com/AndrewShedov/vm-inspector/main/assets/stop_detected.png" alt="🚨 VM State: STOPPED"/>
</p>

[LIVE](https://t.me/ShedovTop_VMInspector/5)

- **Ошибка запуска ВМ в процессе изменения состояния**<br>
Если ВМ находится в статусе `stopping`, `starting` и т.д, облако может отклонить запрос (`API Code: 422`), в таком случае инспектор уведомит об этом:

<p align="center">
<img src="https://raw.githubusercontent.com/AndrewShedov/vm-inspector/main/assets/start_failed.png" alt="🚨 VM Start Failed"/>
</p>

[LIVE](https://t.me/ShedovTop_VMInspector/4)

### 🚀 Инструкция по установке

1. **Подготовка репозитория**<br>
Сделайте Fork данного репозитория в свой GitHub-аккаунт или создайте новый проект и скопируйте в него файлы [vm-inspector.py](https://github.com/AndrewShedov/vm-inspector--private/blob/main/vm-inspector.py) и [.github/workflows/vm-inspector.yml](https://github.com/AndrewShedov/vm-inspector--private/blob/main/.github/workflows/vm-inspector.yml).
2. **Настройка GitHub Secrets**<br>
Для безопасной работы без хранения ключей в коде, необходимо добавить учетные данные в настройки вашего репозитория.
Перейдите в `Settings > Secrets and variables > Actions > New repository secret` и создайте следующие секреты:
- `KEY_ID и SECRET`: API-ключи Cloud.ru.
- `PROJECT_ID`: ID проекта в облаке.
- `VM_1_ID, VM_2_ID, VM_3_ID`: ID отслеживаемых ВМ.
- `TG_TOKEN`: токен Telegram-бота.
- `TG_CHAT_ID`: ID канала для уведомлений.
3. **Настройка уведомлений в Telegram**<br>
3.1. **Создание бота:** Найдите **@BotFather** в Telegram, отправьте команду `/newbot`, создайте своего бота и сохраните полученный **API Token** (пример: `123456:ABC-DEF...`).<br>
3.2. **Получение Chat ID:** Создайте канал и добавьте туда своего бота в качестве администратора.<br>
3.3. Добавьте в канал сервисного бота **@username_to_id_bot**, не давайте боту никаких прав.<br>
3.4. Зайдите в бота **@username_to_id_bot**, напишите сообщение - `/start`, выберите в меню **канал** и получите **ID** (начинается с `-`).<br>

> После получения **ID**, бота **@username_to_id_bot** можно удалить из канала.<br>

4. **Запуск и проверка**<br>
**Автоматический запуск:** Скрипт работает по расписанию, указанному в файле **vm-inspector.yml** (`- cron: '0,30 * * * *'`). При настройке `0,30 * * * *` проверка происходит каждые 30 минут. При высокой нагрузке на инфраструктуру **GitHub Actions**, интервал может увеличиваться в пределах 1-3 часов.

> **Ручной запуск:** Для мгновенной проверки, перейдите во вкладку **Actions**, выберите **VM Inspector** в левом меню и нажмите кнопку **Run workflow**.

### 📋 Результаты работы каждого запуска (логи `print(f...)` можно просмотреть в GitHub Actions:

1. Откройте вкладку **Actions**.
2. Выберите любой запуск **VM Inspector**.
3. Нажмите на задачу **inspect-vm**.
4. Разверните пункт **Run inspector script**.
<br>


[![SHEDOV.TOP](https://img.shields.io/badge/SHEDOV.TOP-black?style=for-the-badge)](https://shedov.top/) 
[![CRYSTAL](https://img.shields.io/badge/CRYSTAL-black?style=for-the-badge)](https://crystal.you/AndrewShedov)
[![Discord](https://img.shields.io/badge/Discord-black?style=for-the-badge&logo=discord&color=black&logoColor=white)](https://discord.gg/ENB7RbxVZE)
[![Telegram](https://img.shields.io/badge/Telegram-black?style=for-the-badge&logo=telegram&color=black&logoColor=white)](https://t.me/ShedovTop)
[![X](https://img.shields.io/badge/%20-black?style=for-the-badge&logo=x&logoColor=white)](https://x.com/AndrewShedov)
[![VK](https://img.shields.io/badge/VK-black?style=for-the-badge&logo=vk)](https://vk.com/ShedovTop)
[![VK Video](https://img.shields.io/badge/VK%20Video-black?style=for-the-badge&logo=vk)](https://vkvideo.ru/@ShedovTop)
[![YouTube](https://img.shields.io/badge/YouTube-black?style=for-the-badge&logo=youtube)](https://www.youtube.com/@AndrewShedov)