# Introduction
This repository contains files for the individual course project in SER494: Data Science for Software Engineers 2023 created by Scotty Solomon for partial fulfillment of the course requirements.

At this time, this project has not been cleared by the course staff (R. Acuna) for public release, and must be kept within a private repository.

## Data Source

The source of the tickers used can be found [here](https://github.com/JerBouma/FinanceDatabase/blob/main/database/funds.csv). The data was created by Jeroen Bouma, a financial risk analyst, and was last edited 7 months ago. He created a community-based database that hosts tickers for stocks, efts, mutual funds, et cetera.

## Web Scrapping

Data was scrapped from Yahoo Finance. They host historical data for a variety of mutual funds on their website. Yahoo Finance gives users the options to request historical data over the last 20 twenty years, and displays that data to them in the form of tables on an html file. However, Yahoo Finance enables users also allows users to download said data into a csv file.

Requests for CSV files are easily replicatable. The general format of a url for a CSV can be found below:
```
https://query1.finance.yahoo.com/v7/finance/download/SQQQ?period1=1265846400&period2=1697155200&interval=1mo&events=history&includeAdjustedClose=true"
```

The ticker for each mutual fund is changed in order to request a csv for each fund. The query options after the ticket request monthly data for the mutual fund that dates back to February 11, 2010 and requests adjusted closed prices for inflation.

## Data Format

|Date       |	    Open|	High|   Low|    Close|  Adj Close|	Volume|
|---        |	    ---|	---	|   ---|    ---|     ---|	    ---|
|01-03-10   |	    8.51|	8.76|	8.51|   8.71|   6.604554|	0|
|01-04-10	|8.79	|8.91	|8.79	|8.86	|6.718294	|0


The **date** is the corresponding date for which the data is tied to.

The **open** is the dollar amount the mutual fund sold for when trading opened for the day

The **high** is the highest amount he fund sold for throughout the day.

The **Low** is the lowest amount the fund sold for throughout the day.

The **Close** is the amount the fund closed at when trading ended for the day.

The **Adj Close** is the closed amount adjusted for inflation.

## Interpretable Records

The data example from the Data Format sections comes from the first two entries of the AAAAX file. We can manually verify that this data is correct by viewing the fund on Google Finance. On March 5th, 2010, the fund was valued at $8.63 and on April 1st, 2010 it was valued at $8.79. We can reasonablly assume that the data for the AAAAX fund from Yahoo Finance is accurate, since it aligns with the data from Google Finance.

## Data Munging

Each fund is stored in a csv file in which the title of the csv corresponds to the name of the fund. The data in the csv is succinct and not irregular. The only optional data munging would be to create one large csv file that contains data from all of the csv files. However, I chose not to do this. 

As it stands, each fund is contained within its own self contained file. A combined file would mean that the data would all be in one file, but the benefits would end there. If I needed to access a specific file, I would have to iterate through 165 rows per fund in order to get to the next one. Whereas I currently am able to directly open the file for a fund I wanted using the fund name as an identifier.
