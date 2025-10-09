import os
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import json

def extract_text_from_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text(strip=False)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def process_journal_entry(text):
    try:
        text = text.strip()

        # Extract date from first line
        date_line = text.partition('\n')[0].strip() # Sunday, January 14, 2024
        date_str = date_line.split(', ', 1)[1]  # January 14, 2024
        # Set time to 12:00 (noon) to avoid timezone cutoff issues
        parsed_date = datetime.strptime(date_str, "%B %d, %Y") + timedelta(hours=12)
        creation_date = parsed_date.strftime("%Y-%m-%dT%H:%M:%SZ") # 2025-10-08T12:00:00Z

        return {
            "creationDate": creation_date,
            "text": text,
            "tags": ["Apple_Journal"],
            "location": None,
            "weather": None,
            "photos": []
        }

    except Exception as e:
        print(f"Error processing entry: {e}")
        return None

def process_all_html_files(folder_path):
    all_entries = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.html'):
            file_path = os.path.join(folder_path, filename)
            extracted_text = extract_text_from_html(file_path)
            if extracted_text:
                entry = process_journal_entry(extracted_text)
                if entry:
                    all_entries.append(entry)

    final_json = {
        "metadata": {
            "version": "1.0",
            "platform": "Apple Journal Entries JSON Import"
        },
        "entries": all_entries
    }

    return final_json

# SET YOUR FOLDER PATH HERE
folder_path = "C:/Users/admin/OneDrive/Desktop/AppleJournalEntries/Entries"

# Process all HTML files and get the final JSON
journal_entries_json = process_all_html_files(folder_path)

# Save to a single JSON file
output_path = os.path.join(folder_path, "Apple_Journal_Entries.json")
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(journal_entries_json, f, indent=2)
print(json.dumps(journal_entries_json, indent=2))