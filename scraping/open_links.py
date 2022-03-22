#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chrome_start
import sys

def user_input():
	print('Filenames:')
	return input().split(' ')

driver = chrome_start.chrome_start()
if (len(sys.argv) < 2):
	file_set = user_input()
else:
	file_set = sys.argv[1:]
for file in file_set:
	driver.switch_to.new_window('tab')
	with open(file, 'r') as link:
		driver.get(link.readline())
