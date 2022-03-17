#!/usr/bin/env python3

#this is the home for functions that interact directly with
#my google drive

#drive_setup connects to and authenticates with my drive

#drive_fill uploads the results from my webscrapers into
#their properly organized folders

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from datetime import date
import os

def drive_setup(SCOPES):
	if not SCOPES:
		raise Exception("No scope")
	creds = None
	if os.path.exists('token.json'):
		creds = Credentials.from_authorized_user_file('token.json', SCOPES)
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		with open('token.json', 'w') as token:
			token.write(creds.to_json())
	return build('drive', 'v3', credentials = creds)

def drive_fill(DRIVE_DIR, DRIVE):
	print('from: ' + str(date.today()))
	DEST_META = {'name': str(date.today()), 'mimeType': "application/vnd.google-apps.folder", 'parents': [DRIVE_DIR['files'][0]['id']]}
	DEST = DRIVE.files().create(body=DEST_META, fields="id").execute()
	ID = DEST.get('id')
	for file in os.listdir():
		print('upload: ' + file)
		META = {"name": file, "parents": [ID]}
		DATA = MediaFileUpload(file)
		UPLOAD = DRIVE.files().create(body=META, media_body=DATA, fields='id').execute()
