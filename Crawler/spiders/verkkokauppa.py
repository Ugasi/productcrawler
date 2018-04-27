# -*- coding: utf-8 -*-
import scrapy

class VerkkokauppaSpider(scrapy.Spider):
    name = "verkkokauppa"
    allowed_domains = ["verkkokauppa.com"]
    start_urls = ["http://verkkokauppa.com/"]

    def parse(self, response):
        for category in response.css("a.link__category-item"):
            yield {"category": category.css("a ::text").extract_first()}
