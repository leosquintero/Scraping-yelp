# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YelpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    phone = scrapy.Field()
    area = scrapy.Field()
    services = scrapy.Field()
    link = scrapy.Field()
    address = scrapy.Field()
    website = scrapy.Field()
    reviews = scrapy.Field()
    stars = scrapy.Field()
    lastrev = scrapy.Field()
    categories = scrapy.Field()