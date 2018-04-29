"""
Scrapy product item class
"""
from scrapy import Item, Field
from scrapy.loader.processors import TakeFirst

class ProductItem(Item):
    """
    Scrapy product item class
    """
    name = Field(output_processor=TakeFirst())
    price = Field(output_processor=TakeFirst())
    manufacturer = Field(output_processor=TakeFirst())
    product_code = Field(output_processor=TakeFirst())
    category = Field(output_processor=TakeFirst())
    product_url = Field(output_processor=TakeFirst())
    product_image = Field(output_processor=TakeFirst())
