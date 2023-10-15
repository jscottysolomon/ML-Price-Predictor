import os
import numpy as np
import pandas as pd
import csv
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

# import RegExp

__author__ = "J. Scotty Solomon"
__date__ = "25-September-23"
__assignment = "SER494: Homework 2 Q4 Programming"

# stop_words = set(stopwords.words('english'))
csvFile = "data_original/funds.csv"
yahooFinance = "https://finance.yahoo.com/quote/"
options = "/history?period1=1265846400&period2=1697155200&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true"

# options
scroll_count = 6

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url = ["https://query1.finance.yahoo.com/v7/finance/download/","?period1=1265846400&period2=1697155200&interval=1mo&events=history&includeAdjustedClose=true"]



# temp = "https://finance.yahoo.com/quote/SQQQ/history?period1=1265846400&period2=1697155200&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true"

temp = "https://query1.finance.yahoo.com/v7/finance/download/SQQQ?period1=1265846400&period2=1697155200&interval=1mo&events=history&includeAdjustedClose=true"


def web_scrapping(url, fundName):
    response = requests.get(url, headers=headers)

    if(response.status_code == 200):
        filePath = "data_original/" + fundName + ".csv"

        with open(filePath, 'wb') as file:
            file.write(response.content)
    else: 
        print("Could not connect to page")

def webDriver(driver, url):
    driver.get(url)
    

    # for _ in range(scroll_count):
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Add a delay to allow the new content to load (you may need to adjust this)
        # time.sleep(2)

    # Get the page source after scrolling
    page_source = driver.page_source
    # print(page_source)

    filePath = "test.html"

    with open(filePath, 'w', encoding='utf-8') as file:
        file.write(page_source)

# def
    

def csv_driver(fileName):
    with open(fileName, encoding="utf8") as csvfile:
        
        reader = csv.DictReader(csvfile)
        for row in reader:
            ticker = (row['symbol'])
            market = (row['market'])
            if(ticker != '' and market == "us_market"):  
                searchURL = url[0] + ticker + url[1]
                print(searchURL)
                web_scrapping(searchURL, ticker)
                # return

            

def initializeDriver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # This line enables headless mode

    # Initialize the WebDriver with the headless option
    driver = webdriver.Chrome(options=chrome_options)

    return driver

# web_scrapping(temp)
# csv_driver()
# webDriver(temp)

if __name__ == '__main__':

    if not os.path.exists("data_original/"):
        os.mkdir("data_original/")

    csv_driver(csvFile)

    
    # web_scrapping(temp,"SQQQ")
    # driver = initializeDriver()
    
    # webDriver(driver, temp)
    # driver.quit()
