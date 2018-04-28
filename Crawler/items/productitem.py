"""
Scrapy product item class
"""
from scrapy import Item, Field

class ProductItem(Item):
    """
    Scrapy product item class
    """
    name = Field()
    price = Field()
    manufacturer = Field()
    product_code = Field()
    category = Field()
    product_url = Field()
    product_image = Field()
