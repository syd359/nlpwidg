import os
import re
from subprocess import check_call, call

'''
Execute the scrapy to scrape the news/annoucement
'''

def execute_scrapy():
    check_call(r'''cd ..
    cd shangwubu
    scrapy crawl shangwubu_news
    ''', shell=True)

def small_test():
    print('Start scrapy crawl')
    print('---------------------------')
    path = os.path.dirname(__file__)
    call('scrapy crawl small_shangwubu -o small_result.csv', cwd=path, shell=True)

if __name__ == '__main__':
    small_test()
    print('crawl ends')