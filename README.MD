# 🛰️ Channel Collector

A simple Python tool to collect message history from Slack public channels where the bot is a member.

---

- Collects all messages (with pagination) from specified Slack channels
- Saves channel history to JSON files

---

## 🚀 Setup

### 1. Clone the repo

```bash
git clone https://github.com/victorlepri/channel-collector.git
cd channel-collector
```

### 2. Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Slack token

```bash
SLACK_BOT_TOKEN=xoxb-your-token-here
```

### 5. Running the Script

```bash
python channel-collector.py
```