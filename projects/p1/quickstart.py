from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from market_price import *


class Read_sheet:
    # If modifying these scopes, delete the file token.json.
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    SAMPLE_RANGE_NAME = 'Class Data!A2:E'


    def reed_google(self):
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=creds.authorize(Http()))

        # Call the Sheets API
        SPREADSHEET_ID = '1CyKmY9WTw_WbrnzjJZl2p7OWqBQZgtXPjvU4AVKp70A'
        RANGE_NAME = 'RR!A1:Q'
        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                    range=RANGE_NAME).execute()
        values = result.get('values', [])


        return values
