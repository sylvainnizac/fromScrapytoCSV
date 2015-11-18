# -*- coding: utf-8 -*-
import scrapy


class InitialSpider(scrapy.Spider):
    name = "Initial"
    allowed_domains = ["http://multiposting.fr/fr/a_propos/recrutement"]
    start_urls = (
        'http://multiposting.fr/fr/a_propos/recrutement',
    )

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
