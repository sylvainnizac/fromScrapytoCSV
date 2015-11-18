# -*- coding: utf-8 -*-

import json
import csv

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapytocsvPipeline(object):

    def __init__(self):
        self.file = open('items.csv', 'wb')

    def process_item(self, item, spider):

        fieldnames = item.keys()
        writer = csv.DictWriter(self.file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(item)
