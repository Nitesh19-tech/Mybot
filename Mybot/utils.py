import json
import os
import random
import pandas as pd
from django.conf import settings

def load_responses():
    """Load responses from JSON and CSV files"""
    base_dir = os.path.join(settings.BASE_DIR, "Mybot", "data")  # ✅ Correct folder path
    json_files = ["intents.json", "New-data.json"]  # ✅ JSON files
    csv_file = "qa_data.csv"  # ✅ CSV file containing Q&A

    all_responses = {"intents": []}  # ✅ Initialize empty response structure

    # ✅ Load JSON files
    for file_name in json_files:
        file_path = os.path.join(base_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, encoding="utf-8") as file:
                data = json.load(file)
                if "intents" in data:
                    all_responses["intents"].extend(data["intents"])  # ✅ Merge intents list
        else:
            print(f"❌ File Not Found: {file_path}")

    # ✅ Load CSV file
    csv_path = os.path.join(base_dir, csv_file)
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path)  # ✅ Read CSV file
            for _, row in df.iterrows():
                intent = {
                    "tag": f"q{row['Question_ID']}",  # ✅ Unique tag for each Q&A
                    "patterns": [row["Questions"].strip()],  # ✅ Question as pattern
                    "responses": [row["Answers"].strip()]  # ✅ Answer as response
                }
                all_responses["intents"].append(intent)
            print("✅ Loaded CSV File Successfully")
        except Exception as e:
            print(f"❌ Error reading CSV file: {e}")
    else:
        print(f"❌ CSV File Not Found: {csv_path}")

    return all_responses

def get_bot_reply(user_query):
    """Find the appropriate bot reply based on user query"""
    print(f"📝 User Query: {user_query}")  # Debug log
    responses_data = load_responses()  # ✅ Load merged JSON & CSV responses
    user_query = user_query.lower()

    bot_reply = "मुझे समझ नहीं आया।"

    for intent in responses_data["intents"]:
        if user_query in [pattern.lower() for pattern in intent.get("patterns", [])]:
            bot_reply = random.choice(intent.get("responses", ["मुझे समझ नहीं आया।"]))
            break

    print(f"🤖 Bot Reply: {bot_reply}")  # Debug log
    return bot_reply
