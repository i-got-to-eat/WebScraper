# Note to self
## Need to find the exact exception 

import re
import os 
import scrapy
from GenericWebScraper.items import GenericwebscraperItem
from scrapy import Selector 
from dotenv import load_dotenv

load_dotenv("../../EnvironmentVariables.env")
SKIP_NOTATION = ["#", ".pdf", ".doc", ".docx", ".txt", "mailto:", "tel:"]


class Spider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["brainyquote.com"]
    start_urls = ["http://www.brainyquote.com/topics/music-quotes"]

    custom_settings = {
        "scrapy.spidermiddlewares.depth.DepthMiddleware": 900,
        "FEED_FORMAT":"csv",
        "LOG_LEVEL": "ERROR",
        "FEED_URI": f'.{os.getenv("OUTPUT_PATH")}{name}.csv',
        "LOG_FILE": f'.{os.getenv("OUTPUT_PATH")}{name}.log'
    }

    #def start_requests(self):
    #    return [scrapy.FormRequest("http://www.example.com/login",
    #                               formdata={'user': 'john', 'pass': 'secret'},
    #                               callback=self.logged_in)]
   


    def parse(self, response):
        CSVFile = GenericwebscraperItem()
        
        print(f'Visiting site ... {str(response.url)})')
        
        for aTag in response.xpath('//a').getall():
            aTagLowerCase = aTag.lower()

            CSVFile["SourceURL"] = response.url
            CSVFile["SourcePageH1"] = response.xpath("//h1/text()").getall()
            CSVFile["SourcePageTitle"] = response.xpath("//title/text()").get()
            CSVFile["URLFromSourcePageRaw"] = Selector(text=a).xpath("//a/@href"),get()
            CSVFile["URLFromSourcePageFormatted"] = response.urljoin(Selector(text=a).xpath("//a/@href").get())
            CSVFile["URLTextFromSourcePage"] = Selector(text=a).xpath("//a/text()").get()
            yield CSVFile


        for aTag in response.xpath('//a').getall():
            if any( x in aTagLowerCase for x in SKIP_NOTATION):
                continue
            try:
                yield scrapy.Request(link, self.parse)
            except:
                yield scrapy.Request(response.urljoin(link), self.parse)
            finally:
                pass
            
            

        
