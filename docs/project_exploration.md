#### SER494: Exploratory Data Munging and Visualization
#### TODO (title)
#### J. Scotty Solomon
#### 18-October-2023

## Basic Questions

I used a dataset to gain ticker names for funds. The dataset was created by Jeroen Bouma, a Financial Risk Analyst. The main fields that I used from the data set were the symbol (ticker name), category (fund type), and market (I exclusivley included funds from the U.S. market). There are 57,882 rows in the csv that I downloaded, which can be accessed [here](https://github.com/JerBouma/FinanceDatabase/blob/main/database/funds.csv). The MD5 hash for this file is 5b2ea0d2addd282441bea4824ff4d3ed.

The second dataset I used came from Yahoo Finance. Yahoo Finance used to have a developer API, but they got rid of it. Still, you're able to request information for a mutual fund via a url and you're given a csv. I data scrapped the csv files and saves them in data_original/funds/. For each fund, the csv data stores data on the the opening, closing, min, and max values on the first of the month, with the date the data represents being stored in the date column. Due to the sheer volume of files, the MD5 hashes were calculated via a python script in wf_datagen and are stored in data_processed/hashes.txt
**Dataset Author(s):** TODO

## Interpretable Records
### Mutual Fund Data
|Date       |	    Open|	High|   Low|    Close|  Adj Close|	
|---        |	    ---|	---	|   ---|    ---|     ---|	  
|01-03-10   |	    8.51|	8.76|	8.51|   8.71|   6.604554|

**Interpretation:** 

The following data comes from a csv file retrieved from the Yahoo Finance website. The **date** column corresponds to the date in which the data is pulled. **Open** corresponds to the price at which the fund opened on the given date. **High** corresponds to the highest price that the fund reach on the specified date. **Low** represents the lowest price the fund reached during the specified date. **Adj Close** represents the value of the closed mutual fund, adjusted for inflation.

The above data example comes from the AAAAX fund. We can manually verify that this data is correct by viewing the fund on Google Finance. On March 5th, 2010, (the closest date that Google Finance displays), the fund was valued at $8.63 and on April 1st. We can reasonably assume that the data for the AAAAX fund from Yahoo Finance is accurate, since it aligns with the data from Google Finance.

### Record 2
|symbol|name|currency|summary|manager_name|manager_bio|category_group|category|family|exchange|market
|---|-----|------|---|---|---|---|---|---|---|---|
AAAAX|DWS RREEF Real Assets Fund - Class A|USD|"The investment seeks total return [...]|John  Vojticek|Co-Head of Liquid Real Assets [...]|Equities|World|DWS|NAS|us_market
|

**Interpretation:** 

The above data comes from the funds.csv that was created by Jeroen Bouma. The imporant rows that I used were as follow:
+ Symbol: Ticker Name
+ Category: Investment Type
+ Market: The world market that this fund is traded on

Some of the data is more easily verifiable than others. On Morningstar.com, John Vojticek is listed as the manager of the fund. The official fund name matches the one found in the CSV. We see that the fund doesn't include any bonds, so the category of equities is accurate. 29.6% of the fund's equity is foreign, so the designation as "world" is accurate.

The fund description and manager bio are harder to verify. Still, that data wasn't used for any sort of data analysis. Overall, the collected data makes sense and seems succinct.

## Background Domain Knowledge

Actively managed mutual funds are curated by investment managers. The performance of mutual funds are often compared to the performance of the [S&P 500](https://www.investopedia.com/terms/s/sp500.asp), which is a collection of the 500 largest publicly traded companies in the United States.

There are several types of actively mutual funds. Equity funds are made up of stocks. They usually have the most risk associated with them. However, they have the capacity for the highest (and lowest) return. Fixed Income funds are made up entirely of bonds, meaning that they have less risk than Equity funds but they usually also have lower returns. Mixed or hybrid funds invest in a combination of stocks and bonds. They can have varying degrees of risk depending on the split between bonds and stocks that the fund employs.

"Actively" managed mutual funds are funds that are managed by professional portfolio managers who make decisions about which stocks or bonds to invest in. Passive mutual funds (or index funds) typically attempt to replicate the S&P 500. Actively managed mutual funds tend to have higher fees associated with them, whereas index funds tend to have lower fees due to minimal maintenance costs.

The S&P 500 typically experiences varying annual returns, with historical averages suggesting an average annual increase of approximately 10%, though it can fluctuate significantly from year to year. Most actively managed mutual funds attempt to "beat out" the S&P 500, since the S&P 500 is typically used as an comparison index. In contrast, index funds attempt to match the S&P 500.

The U.S.' approach to retirement relies entirely on the stock market. Most retirement plans include some type of investment in actively managed mutual funds, though they're not strictly required.

Lastly, it's important to note that the data collected goes up to the beginning of September of 2023. Recently, the S&P 500 has been [on the decline](https://www.google.com/finance/quote/.INX:INDEXSP), which does affect the overall statistics found within this project.

## Data Transformation

No substantial transformations were applied to data that was scrapped from Yahoo Finance.

### Transformation: Tickers
**Description:** The original funds.csv data contains funds that hand blank categories or markets, so those funds were ignored. I created a python script that took a list of all of the funds that matched what I was looking for, put them in a list, and created a random subarray that contained 1,000 tickers.

**Soundness Justification:** the funds.csv had over 30,000 funds that matched the criteria I was looking for. Scrapping the data for each fund would realistically take way too long and I did not want to impose an undue burden onto peer reviewers. I scrapped about 12,000 funds in about 4 hours, and didn't think it would be realistic to expect others to replicate this. 

Regardless, the performance of one-thousand random funds should be enough, especially since each fund then has up to 13 years of historical data saved in a csv.


## Visualization
### Visual Lifetime x Lifetime Appreciation
**Analysis:** This visualization seems to suggest that funds with a longer lifetime tend to have a higher lifetime appreciation. This makes sense, since those funds have more time to actually appreciate. 

Note: The data collected only spans back to 2010, so there's a big line of funds that are about 13 years old. 

### Visual Lifetime x Lifetime Median Yearly Appreciation
**Analysis:** This visualization suggests that most funds congregate around and appreciation factor of 1.0, meaning they don't go up or down in price. It's interesting to note that newer funds have a drastically higher or lower range of appreciation, since they don't have as many years to balance out a really good or really bad year.

Note: The data collected only spans back to 2010, so there's a big line of funds that are over 13 years old. 

### Median Yearly Appreciation X Total Appreciation
**Analysis:** This visual suggests that mutual funds that mutual funds with a median yearly return between 1.0 and 1.1 are the most likely to have the highest total appreciation. This may be because those with appreciation of over 1.5 have more risk, so even though they have good years, they still have really bad years, which causes their overall return to be lower than those that just consistently bring in a modest return.

### Median Yearly Appreciation X Total Revenue
**Analysis:** This seems to suggest that most returns hover around just breaking even, with most gaining value but some losing value. Funds overall don't appreciate that much in value, which makes sense, since you're supposed to buy multiple shares of a fund for retirement, so a lifetime increase of $50 is more impactful when it's across several shares and not just one.

### Total Appreciation X Total Revenue
**Analysis:** This visualization is pretty straightforward. Funds that have appreciated more in value have higher revenue whereas those with depreciated over their life have lost value.