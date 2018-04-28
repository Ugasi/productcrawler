# -*- coding: utf-8 -*-
"""
Spider for parsing all products from Tokmanni
"""
from scrapy import Spider, Request
from Crawler.items.productitem import ProductItem
from Crawler.utils import tokmannixpath as xpath

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
            for item in product_wrapper.xpath(xpath.PRODUCT_ITEM):
                yield self.extract_product(category, item)
            next_page = product_wrapper.xpath(xpath.NEXT_PAGE).extract_first()
            if next_page:
                yield Request(response.urljoin(next_page), callback=self.parse_products)

    @staticmethod
    def extract_product(category, item):
        """
        Extract product information for single product
        """
        product = ProductItem()
        name = item.xpath(xpath.ITEM_NAME).extract_first()
        price = item.xpath(xpath.ITEM_PRICE).extract_first()
        manufacturer = item.xpath(xpath.ITEM_MANUFACTURER).extract_first()
        product_code = item.xpath(xpath.ITEM_CODE).extract_first()
        product_url = item.xpath(xpath.ITEM_URL).extract_first()
        product_image = item.xpath(xpath.ITEM_IMAGE).extract_first()
        product["name"] = name.replace("\n", "").strip()
        product["price"] = price
        product["manufacturer"] = manufacturer
        product["product_code"] = product_code
        product["category"] = category
        product["product_url"] = product_url
        product["product_image"] = product_image
        return product
