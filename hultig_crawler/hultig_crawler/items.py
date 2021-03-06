# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class HultigCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urls = scrapy.Field(output_processor=TakeFirst(),)
    title = scrapy.Field(output_processor=TakeFirst(),)
    tags = scrapy.Field(output_processor=TakeFirst(),)
    text = scrapy.Field(output_processor=TakeFirst(),)
    time = scrapy.Field(output_processor=TakeFirst(),)
    pass
