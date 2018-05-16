import os
import re
from subprocess import check_call

'''
Execute the scrapy to scrape the news/annoucement
'''

def execute_scrapy():
    check_call(
    r'''cd ..
    cd shangwubu
    scrapy crawl shangwubu_news
    ''', shell=True)