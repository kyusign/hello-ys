"""Google Sheets API helper."""

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def append_rows(spreadsheet_id: str, rows, creds):
    """Append rows to a Google Sheet."""
    service = build("sheets", "v4", credentials=creds)
    body = {"values": rows}
    try:
        service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range="Sheet1!A1",
            valueInputOption="RAW",
            body=body,
        ).execute()
    except HttpError as e:
        print("Failed to append rows", e)
