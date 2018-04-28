"""
Runner for individual spider
"""
from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'tokmanni', '-o', 'tokmanni.json'])
