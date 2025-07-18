import requests, json, time, os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
HEADERS = { "Authorization": f"Bearer {SLACK_BOT_TOKEN}" }

def get_joined_public_channels():
    url = "https://slack.com/api/conversations.list"
    params = { "types": "public_channel", "limit": 1000 }
    joined_channels = []

    while True:
        resp = requests.get(url, headers=HEADERS, params=params).json()
        for c in resp.get("channels", []):
            if c.get("is_member"):
                joined_channels.append({ "id": c["id"], "name": c["name"] })
        cursor = resp.get("response_metadata", {}).get("next_cursor")
        if cursor:
            params["cursor"] = cursor
            time.sleep(1)
        else:
            break

    return joined_channels

def get_channel_messages(channel_id):
    url = "https://slack.com/api/conversations.history"
    params = { "channel": channel_id, "limit": 1000 }
    messages = []

    while True:
        resp = requests.get(url, headers=HEADERS, params=params).json()
        messages.extend(resp.get("messages", []))
        cursor = resp.get("response_metadata", {}).get("next_cursor")
        if cursor:
            params["cursor"] = cursor
            time.sleep(1)
        else:
            break

    return messages

def main():
    channels = get_joined_public_channels()
    print(f"Found {len(channels)} channels @Channel Collector is in.")

    for c in channels:
        print(f"Collecting #{c['name']}...")
        msgs = get_channel_messages(c['id'])
        with open(f"{c['name']}.json", "w", encoding="utf-8") as f:
            json.dump(msgs, f, indent=2)
        print(f"Saved {len(msgs)} messages to {c['name']}.json")

if __name__ == "__main__":
    main()

    