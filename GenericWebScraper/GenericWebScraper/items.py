# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GenericwebscraperItem(scrapy.Item):
    SourceURL = scrapy.Field()
    SourcePageH1 = scrapy.Field()
    SourcePageTitle = scrapy.Field()
    URLFromSourcePageRaw = scrapy.Field()
    URLFromSourcePageFormatted = scrapy.Field()
    URLTextFromSourcePage = scrapy.Field()



