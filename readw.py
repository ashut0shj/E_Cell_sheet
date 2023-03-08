from __future__ import print_function

from googleapiclient.discovery import build

from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds=None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


SAMPLE_SPREADSHEET_ID = '17XcPX6xo4xAg54hRyEygHVW7p3uVWFUpc2qv9YXAaqw'
SAMPLE_RANGE_NAME = "Sheet1!A1:D4"



service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

aa=[[123,456],[5678,87665],['gbf','fgbf']]

rangeup=str(input(" Enter the range for update : "))
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                range=rangeup, 
                                valueInputOption="USER_ENTERED", 
                                body={"values": aa  })

response = request.execute()


for i in response:
    print(i)


'''print('Name, Major:')
for row in values:
    # Print columns A and E, which correspond to indices 0 and 4.
    print('%s, %s' % (row[0], row[4]))'''


