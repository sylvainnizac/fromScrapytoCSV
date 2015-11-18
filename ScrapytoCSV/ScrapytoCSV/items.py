# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytocsvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    offer = scrapy.Field()
    title = scrapy.Field()
    country = scrapy.Field()
    location_name = scrapy.Field()
    postal_code = scrapy.Field()
    education_level = scrapy.Field()
    experience_level = scrapy.Field()
    contract_type = scrapy.Field()
    job_description = scrapy.Field()
    profile_description = scrapy.Field()

