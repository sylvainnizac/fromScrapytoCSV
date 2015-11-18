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

        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        item = ScrapytocsvItems()
        #print type(jsonresponse)
        #print type(jsonresponse['offers'])
        temp = jsonresponse['offers']
        #print type(temp[0])
        #print temp[0]
        off = temp[0]

        item['offer'] = off['id']
        item['title'] = off['title']
        item['country'] = off['country']
        location_name = off['title']
        postal_code = off['title']
        education_level = off['title']
        experience_level = off['title']
        contract_type = off['title']
        job_description = off['title']
        profile_description = off['title']

        #print offer, title, country

        return item



