#!/usr/bin/env python3

#this was an idea I had to attempt to download the entirety
#of a long-defunct webcomic. This specific script has a
#multitude of issues that it runs into simply due to the
#intricacies of webscraping and how they don't line up well
#with the way the internet archive keeps snapshots of pages
#from all throughout the website's lifespan. Due to this,
#I had to restart the script starting from several different
#points in the page's history and writing a couple methods
#that worked for downloading most pages from most iterations
#of the website's layout. There's one update, however, that
#unfortunately never got snapshotted by the internet archive
#so that one entry is completely lost to time unless it can
#somehow magically resurface

#I'm rethinking my approach currently so I can make the script
#run start to finish, grabbing every possible update in one go

#filter through https://web.archive.org/web/*/http://www.customerservicer.net/*
#some day to search for the one missing update

from bs4 import BeautifulSoup
import requests

def comic_get(i, soup):
	comic = soup.select("#comic > a > img")
	if comic == []:
		comic_get_oldstyle(i, soup)
	else:
		comic_url = comic[0].get('src')
		comic_data = requests.get(comic_url)
		res_file = open(str(i) + '-' + comic[0].get('title') + '.gif', 'wb')
		i -= 1
		for chunk in comic_data.iter_content(100000):
			res_file.write(chunk)
		res_file.close()
		last = soup.find_all(class_='comic-nav')
		if last != None and last[1].find('a').get('href') != None:
			comic_get(i, BeautifulSoup(requests.get(last[1].find('a').get('href')).text, 'html.parser'))

def comic_get_oldstyle(i, soup):
	comic = soup.select("#comic-1 > img")
	comic_url = comic[0].get('src')
	comic_data = requests.get(comic_url)
	res_file = open(str(i) + '-' + comic[0].get('title') + '.gif', 'wb')
	i -= 1
	for chunk in comic_data.iter_content(100000):
		res_file.write(chunk)
	res_file.close()
	last = soup.select("#content > div.nav > div.nav-previous > a")
	if last == []:
		last = soup.select("#sidebar-undercomic > div.comic_navi_wrapper > table > tbody > tr > td.comic_navi_left > a.navi.navi-prev")
	comic_get(i, BeautifulSoup(requests.get(last[0].get('href')).text, 'html.parser'))

page = requests.get("https://web.archive.org/web/20120705000149/http://www.customerservicer.net/?p=216")
soup = BeautifulSoup(page.text, 'html.parser')
i = 24
comic_get(i, soup)
