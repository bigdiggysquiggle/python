#!/usr/bin/env python3

#designed to be a wrapper for job-scraping scripts as I
#complete new scripts

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import linkedin
import drive_handling
from datetime import date

SCOPES = ['https://www.googleapis.com/auth/drive']
start_dir = '/home/dromansk/projects/Python/scraping/'


#create our output directories if they don't exist
os.chdir(start_dir)
drive = drive_handling.drive_setup(SCOPES)
drive_dir = drive.files().list(q='name = "job descriptions"').execute()
if os.path.exists('output') == False:
	os.mkdir('output')
os.chdir('output')
if os.path.exists('linkedin') == False:
	os.mkdir('linkedin')
#linkedin.crawl_linkedin()
os.chdir(start_dir + '/output/linkedin/' + str(date.today()))
drive_handling.drive_fill(drive_dir, drive)
