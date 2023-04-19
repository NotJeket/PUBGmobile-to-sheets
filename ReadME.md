﻿**PUBG Match Stats to Google Sheets**

This script collects match stats data from a specified API endpoint for a PlayerUnknown's Battlegrounds (PUBGmobile) match, and writes the data to a Google Sheets document using the Google Sheets API.

**Diagram**

![Aspose Words f6f0bb7b-76ee-42dc-ab2d-805f02054eea 001](https://user-images.githubusercontent.com/37781149/233157425-0d0222e2-6ce4-4e40-98d5-1f498fbeb9f7.png)

**Requirements**

- Python 3.x
- requests library
- gspread library
- Google API credentials JSON file
- A Google Sheets document to write the data to

**Installation**

1. Clone or download the repository to your local machine
1. Install the required libraries by running pip install -r requirements.txt in the command line
1. Replace the url variable with the API endpoint for the desired PUBG match
1. Replace the PATH TO FILE in the creds = ServiceAccountCredentials.from\_json\_keyfile\_name('PATH TO FILE', scope) line with the path to your Google API credentials JSON file
1. Replace the NAME OF SHEET in the sheet = gc.open("NAME OF SHEET").sheet1 line with the name of your Google Sheets document

**Usage**

Run the script in the command line using python pubg\_match\_stats.py.

**License**

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.

