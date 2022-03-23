#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chrome_start
import sys

def user_input():
	print('Filenames:')
	return input().split(' ')
caps = DesiredCapabilities.CHROME
caps["pageLoadStrategy"] = "none"
driver = chrome_start.chrome_start(caps)
if (len(sys.argv) < 2):
	file_set = user_input()
else:
	file_set = sys.argv[1:]
for file in file_set:
	driver.switch_to.new_window('tab')
	with open(file, 'r') as link:
		driver.get(link.readline())
