#!/usr/bin/env python3

import os
import linkedin

start_dir = '/home/dromansk/projects/Python/scraping/'

#create our output directories if they don't exist
os.chdir(start_dir)
if os.path.exists('output') == False:
	os.mkdir('output')
os.chdir('output')
if os.path.exists('linkedin') == False:
	os.mkdir('linkedin')
linkedin.crawl_linkedin()
