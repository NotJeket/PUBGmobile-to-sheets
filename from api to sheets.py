import requests
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

#loop statement:
try:
    while True:
        # Get JSON data from URL
        url = "<URL GOES HERE>"
        response = requests.get(url)
        data = response.json()

        # Extract data from JSON using list comprehension
        player_data = data['allinfo']['TotalPlayerList']
        player_teamId = [player['teamId'] for player in player_data]
        player_team_name = [player['teamName'] for player in player_data]
        player_userid = [player['uId'] for player in player_data]
        player_names = [player['playerName'] for player in player_data]
        player_kills = [player['killNum'] for player in player_data]
        player_nade_kills = [player['killNumByGrenade'] for player in player_data]
        player_has_died = [player['bHasDied'] for player in player_data]
        player_nade_use = [player['useFragGrenadeNum'] for player in player_data]
        player_smoke_use = [player['useSmokeGrenadeNum'] for player in player_data]
        player_moly_use = [player['useBurnGrenadeNum'] for player in player_data]
        player_steps = [player['marchDistance'] for player in player_data]
        player_damage = [player['damage'] for player in player_data]

        # Authorize using the Google Sheets API and open the specified sheet
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('<JSON KEY FILE PATH HERE>', scope)
        gc = gspread.authorize(creds)
        sheet = gc.open("<SHEETS TITLE HERE>").sheet1

        # sheet naming updates:
        header = ["Player Team Id", "Player Team Name", "Player User Id", "Player Names", "Player Kills",
                  "Player Nade Kills", "Is DEAD?", "Player Nade Use", "Player Smoke Use", "Player Moly Use",
                  "Player Damage", "Player Distance"]
        sheet.update('A1:L1', [header])

        # Write player data to sheets
        data = [
            player_teamId,
            player_team_name,
            player_userid,
            player_names,
            player_kills,
            player_nade_kills,
            player_has_died,
            player_nade_use,
            player_smoke_use,
            player_moly_use,
            player_damage,
            player_steps
        ]
        columns = list(zip(*data))
        sheet.update('A2:L100', columns)

        # Print a message to show that the data has been updated
        print("Data updated at:" + time.strftime("%H:%M:%S", time.localtime()))
        # Wait for 1 second before repeating the loop
        time.sleep(1)
except KeyboardInterrupt:
    print("Data Update Interrupted")
