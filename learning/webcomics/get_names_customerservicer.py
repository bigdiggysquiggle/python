#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

#this script simply gets the list of names and headings from
#the webcomic's archive page. In The Future TM I will be
#reimplimenting this and the renaming script to use the
#generated name table to create proper directories and such
#but for now I'm just manually finishing the formatting before
#using the other script to finish the renaming process

site = BeautifulSoup(requests.get("https://web.archive.org/web/20160529231936/http://www.customerservicer.net/?page_id=425").text, 'html.parser')
names = site.select('#post-425 > div > div.entry')
name_tab = names[0].stripped_strings
file = open("nametab.txt", 'w')
for line in name_tab:
	file.write(line + '\n')
