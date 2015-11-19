# -*- coding: utf-8 -*-

import csv

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapytocsvPipeline(object):

    def __init__(self):
        self.file = open('items.csv', 'wb')

    def process_item(self, item, spider):
        """
        insert data in the .csv file.
        :param item: data from the crawler
        :param spider: not used
        :return: nothing but creates a csv file
        """
        fieldnames = ['offer','title','country','location_name','postal_code','education_level','experience_level',
                      'contract_type','job_description','profile_description']

        writer = csv.DictWriter(self.file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(item['offers'])

