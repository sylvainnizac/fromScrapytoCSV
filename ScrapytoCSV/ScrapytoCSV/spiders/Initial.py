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
            item['offer'] = off['id']
            item['title'] = off['title'].encode('utf-8')
            item['country'] = off['country'].encode('utf-8')
            item['location_name'] = off['city'].encode('utf-8')
            item['postal_code'] = off['postal_code']
            item['education_level'] = off['study_level'].encode('utf-8')
            item['experience_level'] = off['experience'].encode('utf-8')
            item['contract_type'] = off['contract_type'].encode('utf-8')
            item['job_description'] = off['description'].encode('utf-8')
            item['profile_description'] = off['requested_profile'].encode('utf-8')
            items.append(item)

        back = {'offers' : items}

        return back



