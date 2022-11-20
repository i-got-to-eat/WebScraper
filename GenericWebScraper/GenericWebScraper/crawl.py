# Note to Self 
## Theres decoupling here for the folders and the remove duplidate link details
## Bugs if any of these are modified




from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv("EnvironmentVariables.env")

spiderProcesses = CrawlerProcess(get_project_settings())

spiderNames = ["spider"]

for spider in spiderNames:
    print(f'Starting up Spider: {spider}')    
    spiderProcesses.crawl(spider)

spiderProcesses.start()
exit()
for spider in spiderNames:
    fileName = f'.{os.getenv("OUTPUT_PATH")}{spider}.csv'
    filteredFileName = f'.{os.getenv("OUTPUT_PATH")}{spider}_filtered.csv'
    print(f'Removing Duplicate Link Details in column [URLTextFromSourcePage] in {spider}.CSV')
    try:
        file = pd.read_csv(fileName)
        file = file.drop_duplicates(subset['URLTextFromSourcePage'])
        file.to_csv(filteredFileName)
    finally:
        print(f'Error occurred when removing duplicates from {spider}.csv')

print("Scraping Complete")





