# -*- coding: utf-8 -*-
import scrapy


class VerkkokauppaSpider(scrapy.Spider):
    name = 'verkkokauppa'
    allowed_domains = ['verkkokauppa.com']
    start_urls = ['http://verkkokauppa.com/']

    def parse(self, response):
        pass
