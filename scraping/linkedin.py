#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from datetime import date
import os
import re

#TODO: only save results if they've been posted since the
#last time I scraped

#TODO: make this script take the desired destination as an
#argument

start_dir = '/home/dromansk/projects/Python/scraping/output/linkedin'

#remove all false links from my scraping results
def hidden_check(i, links):
	for classes in links[i].get('class'):
		if re.search(".*hidden.*", classes):
			del links[i]
			hidden_check(i, links)

#currently my search is a hardcoded url that already
#contains all the options I personally want to search for.
#in the future I will be making this function into something
#more generic where the end user can input their own search
#paramters and have the function scrape from those results

def crawl_linkedin():
	search = BeautifulSoup(requests.get("https://www.linkedin.com/jobs/search/?f_E=1%2C2&f_JT=F%2CP%2CI&geoId=102095887&keywords=sre&location=California%2C%20United%20States&sortBy=DD").text, 'html.parser')
	links = search.find('ul', class_='jobs-search__results-list')
	links = links.find_all('a')
	os.chdir(start_dir)
	today = str(date.today())
	#create the output directory for our results
	if os.path.exists(today) == False:
		os.mkdir(str(date.today()))
	os.chdir(str(date.today()))
	for i in range(0, 20, 1):
		hidden_check(i, links)
		link = links[i].get('href')
		desc = BeautifulSoup(requests.get(link).text, 'html.parser')
		title = desc.select("#main-content > section.core-rail > div > section.top-card-layout > div > div.top-card-layout__entity-info-container > div > h1")
		desc = desc.find('div', class_='show-more-less-html__markup')
		filename = str(i + 1).zfill(2) + ' ' + title[0].string + ".txt"
		print("creating: " + filename)
		file = open(filename, 'w')
		file.write(link + '\n\n')
		for string in desc.stripped_strings:
			file.write(string + '\n')
		file.close
