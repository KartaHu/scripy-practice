# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    author = scrapy.Field()
    imgsrc= scrapy.Field()
    title= scrapy.Field()
    weburl = scrapy.Field()
    updatetime= scrapy.Field()
    updateround= scrapy.Field()
    #details = scrapy.Field()
    year = scrapy.Field()    
    region = scrapy.Field()
    index = scrapy.Field()
    category = scrapy.Field()
    author = scrapy.Field()
    updateto = scrapy.Field()
    idea = scrapy.Field()
    #id = scrapy.Field()
    #pass
#[0]year [1]region [2]index [3]category [4]author [5]updateto