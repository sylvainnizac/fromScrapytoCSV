# -*- coding: utf-8 -*-
import scrapy
import json
from ScrapytoCSV.items import ScrapytocsvItems


class InitialSpider(scrapy.Spider):
    name = "Initial"
    allowed_domains = ["multiposting.fr"]
    start_urls = (
        'http://www.multiposting.fr/fr/a_propos/recrutement',
    )

    def parse(self, response):

        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        print response

        for sel in response.xpath('//ul[@class="jobs"]/li'):
            title = sel.xpath('h3/text()').extract()
            content = sel.xpath('p/text()').extract()
            print 'test'
            print title
            print content
            print 'test'


class InitialSpiderJSON(scrapy.Spider):
    name = "InitialJSON"
    allowed_domains = ["multiposting.fr"]
    start_urls = (
        'http://www.multiposting.fr/fr/get-job-list',
    )

    def parse(self, response):

        jsonresponse = json.loads(response.body)

        temp = jsonresponse['offers']
        items = []

        for off in temp:
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

        yield back



