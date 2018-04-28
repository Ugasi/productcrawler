# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class ProductItem(Item):
    name = Field()
    price = Field()
    manufacturer = Field()
    product_code = Field()
    category = Field()
    product_url = Field()
    product_image = Field()