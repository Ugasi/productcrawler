"""
Xpath helpers for Tokmanni
"""

CATEGORY_WRAPPER = "//div[@class='drilldown']"
CATEGORY = ".//li[contains(@class, 'level') and not(contains(@class, 'parent'))]"
CATEGORY_URL = "a::attr(href)"
CATEGORY_NAME = "//span[@class='base']/text()"

PRODUCT_WRAPPER = "//div[@class='products wrapper grid products-grid']"
PRODUCT_ITEM = ".//li[@class='item product product-item']"

ITEM_NAME = ".//a[@class='product-item-link']/text()"
ITEM_PRICE = ".//span[@data-price-type='finalPrice']/@data-price-amount"
ITEM_MANUFACTURER = ".//span[@class='brand-name']/text()"
ITEM_CODE = ".//form[@data-role='tocart-form']/@data-product-sku"
ITEM_URL = ".//a[@class='product-item-link']/@href"
ITEM_IMAGE = ".//img/@src"

NEXT_PAGE = "//a[@title='Seuraava']/@href"
