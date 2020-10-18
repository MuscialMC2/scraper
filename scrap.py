from selenium import webdriver
import pandas as pd
import datetime
import time

driver = webdriver.Chrome("/home/gaetan/dev/utils/chromedriver")
listId = pd.read_csv("sources/noduplicatesIbdb.csv")
base_uri = "https://www.ibdb.com/broadway-production/"
now = datetime.datetime.now()
date_time = now.strftime("%m%d%Y_%H%M%S")

for id in listId:
    convertedId = str(id)
    driver.get(base_uri + convertedId)
    content = driver.page_source
    with open('saves/' + convertedId + '.html', 'w') as f:
        f.write(content)
    time.sleep(1)
driver.close()
