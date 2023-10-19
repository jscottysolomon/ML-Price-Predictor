import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import statistics as stats
import pandas as pd
from collections import Counter

DATE = 0
OPEN = 1
HIGH = 2
LOW = 3
CLOSE = 4

percent = []

def getIndexData(files):
    indexFunds = []
    for x in files:
        fileName = "data_original\\index\\" + x
        data = [[],[],[],[],[]]

        with open(fileName, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data[0].append(row['Date'])
                data[1].append(row['Open'])
                data[2].append(row['High'])
                data[3].append(row['Low'])
                data[4].append(row['Close'])
        indexFunds.append(data)

    return indexFunds

def visualization(files):
    lifetimeAppreciation = []
    medianYearlyAppreciation = []
    lifetimeDollarIncrease = []
    lifetime = []
    fundData = []

    i = 0
    for x in files:
        fileName = "data_original\\funds\\" + x
        data = [[],[],[],[],[]]

        print(x)
        
        # Extracting Each row from csv
        with open(fileName, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            try:
                for row in reader:
                    data[OPEN].append(float(row['Open']))
                    data[DATE].append(row['Date'])
                    data[HIGH].append(float(row['High']))
                    data[LOW].append(float(row['Low']))
                    data[CLOSE].append(float(row['Close']))
            except Exception as e:
                pass

        fundData.append(data)

        i += 1
        if(i > 1000):
            break
  
    for x in fundData:
        length = len(x[0])
        try:
            # Lifetime Appreciation Calculation
            if(x[OPEN][0]==0):                
                temp = 1
                while(temp < length):
                    if(x[OPEN][temp] != 0):
                        lifetimeAppreciation.append(x[OPEN][length-1]/x[OPEN][temp])
                        break
                    temp += 1

                if(temp >= length):
                    lifetimeAppreciation.append(1)
            else:
                lifetimeAppreciation.append(x[OPEN][length-1]/x[OPEN][0])

            # Total Revenue
            lifetimeDollarIncrease.append(float(x[OPEN][length-1])-float(x[OPEN][0]))

            # Fund Age
            dateFormat = "%Y-%m-%d"

            delta = (datetime.strptime(x[DATE][length-1],dateFormat) - 
                            datetime.strptime(x[DATE][0],dateFormat))
            
            years = delta.total_seconds() / 31556952
            lifetime.append(years)
            
            # Getting All Yearly Return
            curr = 12
            yearlyReturn = []
            while(curr < length):
                if(float(x[OPEN][curr-12]) == 0):
                    temp = 1
                    while(temp < length):
                        if(x[OPEN][temp] != 0):
                            yearlyReturn.append(x[OPEN][length-1]/x[OPEN][temp])
                            break
                        temp += 1

                    if(temp >= length):
                        yearlyReturn.append(0)
                else:
                    yearlyReturn.append(float(x[OPEN][curr])/float(x[OPEN][curr-12]))

                curr += 12
            # Calculate median yearly return
            if(len(yearlyReturn) == 0):
                medianYearlyAppreciation.append(1)
            else:
                medianYearlyAppreciation.append(stats.median(yearlyReturn))
            
        except Exception as e:
            print(e)
            pass

    fundType = []
    i = 0
    fundLength = len(files)

    # Getting fund types from original file
    with open("data_original/funds.csv", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = (row['symbol'])
            category = (row['category_group'])
            fundName = files[i].split(".")
            if(fundName[0] == name):
                if(category != ''):
                    fundType.append(category)
                    # print(category)
                i += 1
            
            if(i >= fundLength):
                break
    
    fundTuple = tuple(fundType)
    stringCounts = Counter(fundTuple)

    # Histogram data
    cats = list(stringCounts.keys())
    counts = list(stringCounts.values())

    # Qualitative Stats Data
    mostUsed = stringCounts.most_common(1)
    leastUsed = stringCounts.most_common()[-1]       
    uniqueCategories = len(stringCounts)


    if not os.path.exists("data_processed/"):
        os.mkdir("data_processed/")
        
    # Creating Stats Strings
    fileString = "Statistic: Minimum, Maximum, Average\n"
    fileString += "Lifetime Appreciation: " + str(min(lifetimeAppreciation)) + "," + str(max(lifetimeAppreciation)) + "," + str(stats.median(lifetimeAppreciation)) + "\n"
    fileString += "Lifetime Dollar Increase: " + str(min(lifetimeDollarIncrease)) + "," + str(max(lifetimeDollarIncrease)) + "," + str(stats.median(lifetimeDollarIncrease)) + "\n"
    fileString += "Median Yearly Return: " + str(min(medianYearlyAppreciation)) + "," + str(max(medianYearlyAppreciation)) + "," + str(stats.median(medianYearlyAppreciation)) + "\n"
    fileString += "Lifetime: " + str(min(lifetime)) + "," + str(max(lifetime)) + "," + str(stats.median(lifetime)) + "\n\n"

    # Qualitative data
    fileString += "Qualitative: Number of Categories, Most Common, Least Common\n"
    fileString += "Fund Category: " + str(uniqueCategories) + ", " + str(mostUsed) + ", " + str(leastUsed)

    # Writing stats to file
    print(fileString) 
    with open("data_processed/summary.txt","w") as file:
        file.write(fileString)

    # Making Correlation Matrix
    df = pd.DataFrame({
        'Lifetime': lifetime,
        'Median Yrly Return': medianYearlyAppreciation,
        '$ Increase': lifetimeDollarIncrease,
        '% Appreciation': lifetimeAppreciation

    })

    correlation_matrix = df.corr(method='pearson')
    correlations = str(correlation_matrix)

    # Writing Correlations Matrix
    with open("data_processed/correlations.txt","w") as file:
        file.write(correlations)

    # Making Visuals
    plt.scatter(lifetime,medianYearlyAppreciation)
    plt.title("Lifetime x Median Yearly Appreciation")
    plt.xlabel("Lifetime by Years")
    plt.ylabel("Median Yearly Appreciation")
    plt.savefig("visuals/Lifetime_x_YearlyAppreciation.png")
    plt.clf()

    plt.scatter(lifetime,lifetimeDollarIncrease)
    plt.title("Lifetime x Total Revenue")
    plt.xlabel("Lifetime by Years")
    plt.ylabel("Total Revenue in Dollars")
    plt.savefig("visuals/Lifetime_x_Revenue.png")
    plt.clf()

    plt.scatter(lifetime,lifetimeAppreciation)
    plt.title("Lifetime x Lifetime Appreciation")
    plt.xlabel("Lifetime by Years")
    plt.ylabel("Lifetime Appreciation")
    plt.savefig("visuals/Lifetime_x_TotalAppreciation.png")
    plt.clf()

    plt.scatter(medianYearlyAppreciation,lifetimeDollarIncrease)
    plt.title("Median Yearly Appreciation x Total Revenue")
    plt.xlabel("Median Yearly Appreciation")
    plt.ylabel("Total Revenue in Dollars")
    plt.savefig("visuals/YrAppreciation_x_Revenue.png")
    plt.clf()

    plt.scatter(medianYearlyAppreciation,lifetimeAppreciation)
    plt.title("Median Yearly Appreciation x Total Appreciation")
    plt.xlabel("Median Yearly Appreciation")
    plt.ylabel("Total Appreciation")
    plt.savefig("visuals/YrAppreciation_x_totalAppreciation.png")
    plt.clf()

    plt.scatter(lifetimeAppreciation,lifetimeDollarIncrease)
    plt.title("Total Appreciation x Total Revenue")
    plt.xlabel("Lifetime Appreciation")
    plt.ylabel("Lifetime Revenue")
    plt.savefig("visuals/totalAppreciation_x_totalRevenue.png")
    plt.clf()

    # Histogram of Qualitative data
    plt.bar(cats, counts)
    plt.xlabel("Categories")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.title("Frequency of Fund Types")
    plt.tight_layout()
    plt.savefig("visuals/fundTypes.png")
    plt.clf()

if __name__ == '__main__':
    fundsFiles = os.listdir(path='.\\data_original\\funds')
    visualization(fundsFiles)