#!/usr/bin/env python3

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import requests
from datetime import date
import os
import re

#TODO: only save results if they've been posted since the
#last time I scraped
#---implemented temp workaround. url now only gets results
#	from the last 24 hours

#TODO: make this script take the desired destination as an
#argument

start_dir = '/home/dromansk/projects/Python/scraping/output/linkedin'

def get_job(link, i):
	desc = BeautifulSoup(requests.get(link).text, 'html.parser')
	title = desc.select("#main-content > section.core-rail > div > section.top-card-layout > div > div.top-card-layout__entity-info-container > div > h1")
	if (not title):
		title = desc.select("body > div.application-outlet > div.authentication-outlet > div > div.job-view-layout.jobs-details > div.grid > div > div:nth-child(1) > div > div.p5 > h1")
	desc = desc.find('div', class_='show-more-less-html__markup')
	filename = str(i).zfill(2) + ' ' + title[0].string + ".txt"
	filename = filename.replace('/', ' -or- ')
	print("creating: " + filename)
	file = open(filename, 'w')
	file.write(link + '\n\n')
	for string in desc.stripped_strings:
		file.write(string + '\n')
	file.close

#currently my search is a hardcoded url that already
#contains all the options I personally want to search for.
#in the future I will be making this function into something
#more generic where the end user can input their own search
#parameters and have the function scrape from those results

def crawl_linkedin():
	os.chdir(start_dir)
	today = str(date.today())
	#create the output directory for our results
	if os.path.exists(today) == False:
		os.mkdir(str(date.today()))
	os.chdir(str(date.today()))

	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get("https://www.linkedin.com/jobs/search/?f_E=1%2C2&f_JT=F%2CP%2CI&f_TPR=r86400&geoId=102095887&keywords=sre&location=California%2C%20United%20States&sortBy=DD")
	res_list = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[2]/ul")
	listings = driver.find_elements(By.TAG_NAME, 'li')
	i = 1
	for listing in listings:
		for link in listing.find_elements(By.CLASS_NAME, 'base-card__full-link'):
			get_job(link.get_attribute('href'), i)
			i += 1
	driver.quit()
