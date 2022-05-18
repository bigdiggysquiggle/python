#!/usr/bin/env python3
import os
import shutil

#due to the fact that the webcomic creator stopped updating
#the archive page, there are 12 webcomics that aren't listed
#there. Of those, 10 of them don't have their name in a
#convenient location for my main scraping script (I intend to
#rework that in the future). For now I'm comfortable just
#entering those 10 names by hand

f = open('nametab.txt', 'r')
tab = f.readlines()
tab = tab[1::2]
directory = os.listdir('dest')
os.chdir('dest')
for file in directory:
	ind = int(file.split('-')[0])
	try:
		shutil.move(file, str(ind) + '-' + tab[ind - 1].strip() + '.gif')
	except:
		print('missing title for ' + str(ind))
