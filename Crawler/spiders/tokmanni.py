# -*- coding: utf-8 -*-
"""
Spider for parsing all products from Tokmanni
"""
from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from Crawler.utils import tokmannixpath as xpath
from Crawler.items.productitem import ProductItem

class TokmanniSpider(Spider):
    """
    Spider for parsing all products from Tokmanni
    """

    name = "tokmanni"
    allowed_domains = ["tokmanni.fi"]
    start_urls = ["https://www.tokmanni.fi"]

    def parse(self, response):
        category_wrapper = response.xpath(xpath.CATEGORY_WRAPPER)
        for category in category_wrapper.xpath(xpath.CATEGORY):
            category_url = category.css(xpath.CATEGORY_URL).extract_first()
            yield Request(response.urljoin(category_url), callback=self.parse_products)

    def parse_products(self, response):
        """
        Parse every product from page
        """
        category = response.xpath(xpath.CATEGORY_NAME).extract_first()
        product_wrapper = response.xpath(xpath.PRODUCT_WRAPPER)
        if product_wrapper:
            for product in product_wrapper.xpath(xpath.PRODUCT_ITEM):
                yield self.extract_product(category, product)
            next_page = product_wrapper.xpath(xpath.NEXT_PAGE).extract_first()
            if next_page:
                yield Request(response.urljoin(next_page), callback=self.parse_products)

    @staticmethod
    def extract_product(category, product):
        """
        Extract product information for single product
        """
        loader = ItemLoader(ProductItem(), product)
        loader.add_xpath("name", xpath.ITEM_NAME)
        loader.add_xpath("price", xpath.ITEM_PRICE)
        loader.add_xpath("manufacturer", xpath.ITEM_MANUFACTURER)
        loader.add_xpath("product_code", xpath.ITEM_CODE)
        loader.add_value("category", category)
        loader.add_xpath("product_url", xpath.ITEM_URL)
        loader.add_xpath("product_image", xpath.ITEM_IMAGE)
        return loader.load_item()
