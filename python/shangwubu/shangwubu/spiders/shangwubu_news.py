import scrapy
import re
from shangwubu.items import ShangwubuItem
from robobrowser import RoboBrowser
import jieba

class ShangwubuSpider(scrapy.Spider):
    name = "shangwubu_news"
    start_urls = [
        'http://www.mofcom.gov.cn/article/ae/ai/?'
    ]

    allowed_domains = [
        'mofcom.gov.cn'
    ]

    # browser = RoboBrowser(history=True)
    # browser.open('http://www.mofcom.gov.cn/article/ae/ai/?')
    # response = browser.response

    def parse(self, response):
        '''
        1. title
        2. post_time
        3. url
        4. content
        5. keywords ???
        '''

        # browser = RoboBrowser(history=True)
        # browser.open(self.start_urls[0])
        # self.response = browser.response.text

        # print(response)

        for el in response.css('div.listBox li'):
            item = ShangwubuItem()
            item['title'] = el.css('a::text').extract_first()
            item['post_time'] = el.css('span::text').extract_first()
            url = el.css('a::attr(href)').extract_first()
            if url:
                item['url'] = 'http://www.mofcom.gov.cn/' + url
            else:
                item['url'] = url

            content_page = el.css('a::attr(href)').extract_first()
            content_page_url = response.urljoin(content_page)
            yield scrapy.Request(content_page_url, meta={'item': item}, callback=self.parse_content)
        
        # next_page
        next_page_number = response.css('div.listBox script::text').extract_first()
        pattern = 'currentpage = "(.*?)";'
        next_page = int(re.findall(pattern, next_page_number)[0]) + 1
        if next_page < 201:
            url = 'http://www.mofcom.gov.cn/article/ae/ai/?' + str(next_page)
            next_page_url = response.urljoin(url)
            yield scrapy.Request(next_page_url, callback=self.parse)
            


    
    def parse_content(self, response):
        '''
        1. category
        2. content
        '''
        
        # item = response.meta['item']
        # x = response.xpath('//script[@type="text/javascript"]/text()').extract()
        # target = re.findall(x, "var contype = (.*?);")
        # item['category'] = target

        
        item = response.meta['item']
        item['content'] = response.css('div.artCon P::text').extract()
        yield item
