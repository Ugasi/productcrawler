# -*- coding: utf-8 -*-
import scrapy

class TokmanniSpider(scrapy.Spider):
    name = "tokmanni"
    allowed_domains = ["tokmanni.fi/"]
    start_urls = ["https://www.tokmanni.fi/"]

    def parse(self, response):
        for category in response.xpath("//div[@class='drilldown']").xpath(".//li[contains(@class, 'level') and not(contains(@class, 'parent'))]"):
            yield {"category": category.css("a::attr(href)").extract_first()}
