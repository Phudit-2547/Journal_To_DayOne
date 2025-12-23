# Journal_To_DayOne
## Moving Journal Entries from Apple Journal App to Day One App

- Apple Journal has a few limitations, so thought of using Day One App.
- To move journal entries, export it from Apple's Journal.
- Only suppported format is HTML.
- Exported Zip Folder - AppleJournalEntries.
- In that we have index.html, Entries Folder and Photos.
- In Entries Folder, we have all journal entries in HTML format.
- I had some date issue with the date mentioned in file name and journal content date, that also addressed here.
- But cross check once before you use this code.

- Here we will extract HTML content to text using BeautifulSoup in Python.
- And create JSON file with Journal entries, as Day One accepts JSON format.

### ⚠️ Important Step Before Running
You **must** update the folder path in the script to match your local file system.
1. Open `journal_to_dayone.py`.
2. Find the line:
   ```python
   # SET YOUR FOLDER PATH HERE
   folder_path = "/AppleJournalEntries/Entries"
   ```
3. Change `/AppleJournalEntries/Entries` to the actual path where your exported entries are located.

### Sample Day One acceptable JSON Format:
```
{
  "metadata": {
    "version": "1.0"
  },
  "entries": [
    {
      "uuid": "123e4567-e89b-12d3-a456-426614174000",
      "creationDate": "2023-10-07T10:30:00Z",
      "modifiedDate": "2023-10-07T11:00:00Z",
      "text": "This is my first journal entry.",
      "tags": ["personal", "thoughts"],
      "location": {
        "latitude": 37.7749,
        "longitude": -122.4194,
        "placeName": "San Francisco, CA",
        "country": "United States"
      },
      "photos": [
        {
          "identifier": "photo1.jpg",
          "type": "jpeg",
          "creationDate": "2023-10-07T10:35:00Z",
          "md5": "d41d8cd98f00b204e9800998ecf8427e",
          "isPrimary": true
        }
      ],
      "starred": true,
      "timeZone": "America/Los_Angeles"
    }
  ]
}
```
### Output of this Code:
```
{
  "metadata": {
    "version": "1.0",
    "platform": "Apple Journal Entries JSON Import"
  },
  "entries": [
    {
      "creationDate": "2024-01-14T12:00:00Z",
      "text": "Sunday, January 14, 2024 \nToday is Bhoghi\n\nI miss home and family.",
      "tags": [
        "Apple_Journal"
      ],
      "location": null,
      "weather": null,
      "photos": []
    }
   ]
  }
```

- Zip this JSON file inside a folder and import it in DayOne App.
- Happy Journaling!
