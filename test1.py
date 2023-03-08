from __future__ import print_function

from googleapiclient.discovery import build

from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds=None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


SAMPLE_SPREADSHEET_ID = '1s4k_MePOZIaEL94T1FM1401ten1AOibGZuvZWUPiN3k'
SAMPLE_RANGE_NAME = "Ayush!A1:I"



service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])
data=[]
for i in values:
    try:
    
        data.append([i[0],i[1]])
    except:
        pass
    
for i in data:
    print(i)