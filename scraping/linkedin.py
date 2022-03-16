#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from datetime import date
import os
import re

def hidden_check(i, links):
	for classes in links[i].get('class'):
		if re.search(".*hidden.*", classes):
			del links[i]
			hidden_check(i, links)

search = BeautifulSoup(requests.get("https://www.linkedin.com/jobs/search/?f_E=1%2C2&f_JT=F%2CP%2CI&geoId=102095887&keywords=sre&location=California%2C%20United%20States&sortBy=DD").text, 'html.parser')
links = search.find('ul', class_='jobs-search__results-list')
links = links.find_all('a')
os.chdir('/home/dromansk/projects/Python/scraping/output/linkedin')
today = str(date.today())
if os.path.exists(today) == False:
	os.mkdir(str(date.today()))
os.chdir(str(date.today()))
for i in range(0, 20, 1):
	hidden_check(i, links)
	link = links[i].get('href')
	file = open('result ' + str(i), 'w')
	file.write(link + '\n\n')
	desc = BeautifulSoup(requests.get(link).text, 'html.parser')
	desc = desc.find('div', class_='show-more-less-html__markup')
	for string in desc.stripped_strings:
		file.write(string)
	file.close
