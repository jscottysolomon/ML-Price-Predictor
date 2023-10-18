import os
import numpy as np
import pandas as pd
import csv
import random
import requests
import hashlib

__author__ = "J. Scotty Solomon"
__date__ = "25-September-23"
__assignment = "SER494: Milestone 2"

# stop_words = set(stopwords.words('english'))
csvFile = "data_original/funds.csv"
yahooFinance = "https://finance.yahoo.com/quote/"
options = "/history?period1=1265846400&period2=1697155200&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true"

# options
LIST_LENGTH = 1000

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url = ["https://query1.finance.yahoo.com/v7/finance/download/","?period1=1265846400&period2=1697155200&interval=1mo&events=history&includeAdjustedClose=true"]

def web_scrapping(url, fundName):
    response = requests.get(url, headers=headers)

    if(response.status_code == 200):
        filePath = "data_original/funds/" + fundName + ".csv"

        with open(filePath, 'wb') as file:
            file.write(response.content)
    else: 
        print("Could not connect to page")

def csv_driver(fileName):
    allTickers = []
    with open(fileName, encoding="utf8") as csvfile:
        
        reader = csv.DictReader(csvfile)
        for row in reader:
            ticker = (row['symbol'])
            market = (row['market'])
            category = (row['category_group'])
            if(ticker != '' and market == "us_market" and category != ''): 
                allTickers.append(ticker) 
    
    tickers = random.sample(allTickers, LIST_LENGTH)

                
    for ticker in tickers:
        searchURL = url[0] + ticker + url[1]
        print(searchURL)
        web_scrapping(searchURL, ticker)
                # return
def createFundList():
    files = os.listdir(path='.\\data_original\\funds')
    fundNames = []
    
    for x in files:
        fileName = x.split(".")
        fundNames.append(fileName[0])

    with open("data_processed/funds.csv", mode='w', newline=' ') as file:
        writer = csv.writer(file)

        for x in fundNames:
            writer.writerow([x])

def createCSV():
    tickers = []
    funds = os.listdir(path='.\\data_original\\funds')
    for x in funds:
        fileName = x.split(".")
        fundName = fileName[0]
        tickers.append(fundName)
    
    with open("data_processed/funds.csv", mode='w', newline='') as file:
        writer = csv.writer(file)

        for fund in tickers:
            writer.writerow([fund])

def manualWebScrape(fileName):
    if not os.path.exists("data_original/funds/"):
        os.mkdir("data_original/funds/")
        
    with open(fileName, encoding="utf8") as csvfile:
        
        reader = csv.DictReader(csvfile)
        for row in reader:
            ticker = (row['ticker'])

            searchURL = url[0] + ticker + url[1]
            print(searchURL)
            web_scrapping(searchURL, ticker)

def md5Hash():
    hashString = ''

    md5_hash = hashlib.md5()

    # Original Ticker Lists
    with open("data_original\\funds.csv", 'rb') as file:
        while True:
            data = file.read(8192)  # Read 8KB at a time
            if not data:
                break
            md5_hash.update(data)

    hashString += "data_original\\funds.csv" + ": " + md5_hash.hexdigest() + "\n"

    hashFiles = os.listdir(path='.\\data_original\\funds')

    # Scrapped CSV Files
    for file in hashFiles: 
        fileName = ".\\data_original\\funds\\" + file       
        with open(fileName, 'rb') as file:
            while True:
                data = file.read(8192)  # Read 8KB at a time
                if not data:
                    break
                md5_hash.update(data)

        hashString += fileName + ": " + md5_hash.hexdigest() + "\n"

    with open("data_processed/hashes.txt","w") as file:
        file.write(hashString)


if __name__ == '__main__':

    # 

    # csv_driver(csvFile)

    # createCSV()
    # manualWebScrape("data_processed/funds.csv")
    md5Hash()

    
    # web_scrapping(temp,"SQQQ")
    # driver = initializeDriver()
    
    # webDriver(driver, temp)
    # driver.quit()
