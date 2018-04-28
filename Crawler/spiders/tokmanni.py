# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from Crawler.items import ProductItem

class TokmanniSpider(Spider):
    name = "tokmanni"
    allowed_domains = ["tokmanni.fi"]
    start_urls = ["https://www.tokmanni.fi"]

    def parse(self, response):
        category_wrapper = response.xpath("//div[@class='drilldown']");
        for category in category_wrapper.xpath(".//li[contains(@class, 'level') and not(contains(@class, 'parent'))]"):
            category_url = category.css("a::attr(href)").extract_first()
            yield Request(response.urljoin(category_url), callback = self.parse_products)

    def parse_products(self, response):
        category = response.xpath("//span[@class='base']/text()").extract_first()
        product_wrapper = response.xpath("//div[@class='products wrapper grid products-grid']")
        if product_wrapper:
            for item in product_wrapper.xpath(".//li[@class='item product product-item']"):
                yield self.extract_product(category, item)
            next_page = product_wrapper.xpath("//a[@title='Seuraava']/@href").extract_first()
            if next_page:
                yield Request(response.urljoin(next_page), callback = self.parse_products)

                
    def extract_product(self, category, item):
        product = ProductItem()
        name = item.xpath(".//a[@class='product-item-link']/text()").extract_first()
        price = item.xpath(".//span[@data-price-type='finalPrice']/@data-price-amount").extract_first()
        manufacturer = item.xpath(".//span[@class='brand-name']/text()").extract_first()
        product_code =item.xpath(".//form[@data-role='tocart-form']/@data-product-sku").extract_first()
        product_url = item.xpath(".//a[@class='product-item-link']/@href").extract_first()
        product_image = item.xpath(".//img/@src").extract_first()
        product["name"] = name.replace("\n", "").strip()
        product["price"] = price
        product["manufacturer"] = manufacturer
        product["product_code"] = product_code
        product["category"] = category
        product["product_url"] = product_url
        product["product_image"] = product_image
        return product