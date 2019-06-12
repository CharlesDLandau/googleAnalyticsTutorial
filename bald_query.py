#!/usr/bin/env python3

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = './client_secrets.json'


def initialize_analyticsreporting():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)

    # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics


def get_report(analytics, body):
    return analytics.reports().batchGet(
      body=body
    ).execute()


if __name__ == '__main__':
    import sys
    VIEW_ID = sys.argv[1]
    analytics = initialize_analyticsreporting()
    response = get_report(analytics, {
            'reportRequests': [
                {
                  'viewId': VIEW_ID,
                }]
          })
    print(response)
