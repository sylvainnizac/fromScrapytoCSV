# -*- coding: utf-8 -*-
import scrapy
import json
from ScrapytoCSV.items import ScrapytocsvItems


class InitialSpider(scrapy.Spider):
    """
    test spider on a single url, giving a json response
    """
    name = "Initial"
    allowed_domains = ["multiposting.fr"]
    start_urls = (
        'http://www.multiposting.fr/fr/get-job-list',
    )

    def parse(self, response):
        """
        parse the json data into a series of dicts
        :param response: crawled data
        :return:a dict containing the list of offers
        """

        jsonresponse = json.loads(response.body)

        items = []

        # parsing data, the encode() method prevents errors from french special chars
        for off in jsonresponse['offers']:
            item = ScrapytocsvItems()
            try:
                item['offer'] = off['id']
            except:
                item['offer'] = ""

            try:
                item['title'] = off['title'].encode('utf-8')
            except:
                item['title'] = ""

            try:
                item['country'] = off['country'].encode('utf-8')
            except:
                item['country'] = ""

            try:
                item['location_name'] = off['city'].encode('utf-8')
            except:
                item['location_name'] = ""

            try:
                item['postal_code'] = off['postal_code']
            except:
                item['postal_code'] = ""

            try:
                item['education_level'] = off['study_level'].encode('utf-8')
            except:
                item['education_level'] = ""

            try:
                item['experience_level'] = off['experience'].encode('utf-8')
            except:
                item['experience_level'] = ""

            try:
                item['contract_type'] = off['contract_type'].encode('utf-8')
            except:
                item['contract_type'] = ""

            try:
                item['job_description'] = off['description'].encode('utf-8')
            except:
                item['job_description'] = ""

            try:
                item['profile_description'] = off['requested_profile'].encode('utf-8')
            except:
                item['profile_description'] = ""

            items.append(item)

        back = {'offers' : items}

        return back



