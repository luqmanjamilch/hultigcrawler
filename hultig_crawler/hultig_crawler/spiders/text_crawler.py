# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from hultig_crawler.items import HultigCrawlerItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re


class TextCrawlerSpider(CrawlSpider):

    name = 'hultig_crawler'
    allowed_domains = ['ubi.pt']
    start_urls = ['https://www.ubi.pt/']
    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)


    def parse_item(self, response):

        pages = response.xpath("/html")
        for page in pages:
            now = datetime.now()
            newpage = page.xpath("/html").extract()
            newp = str(newpage)
            soup = BeautifulSoup(newp, "html.parser")
            
            
            

            item = ItemLoader(item=HultigCrawlerItem())
            rawtext = soup.get_text(strip=True) 
            textup = rawtext.replace('\n', ' ').replace("\\n", ' ').replace("\t", '').replace("\\t", '').replace("\\","")
            

            URLs = response.request.url
            title = page.xpath("//title/text()").getall()
            tags = page.xpath("/html//a/text()").getall()
            text= re.sub(' +', ' ', textup)
            time = now.strftime("%Y-%m-%d %H:%M:%S")
            

            item.add_value('urls', URLs)
            item.add_value('title', title)
            item.add_value('tags', tags)
            item.add_value('text', text)
            item.add_value('time', time)
            yield item.load_item()
        #next_page = response.css('a::attr(href)').get()
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse)
        #rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)
