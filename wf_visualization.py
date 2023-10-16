import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import statistics as stats
import pandas as pd

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
        openings = []
        

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

    
    # print(fundData)    
    
    for x in fundData:
        length = len(x[0])
        try:
            if(x[OPEN][0]==0):
                lifetimeAppreciation.append(-1)
            else:
                lifetimeAppreciation.append(x[OPEN][length-1]/x[OPEN][0])
            lifetimeDollarIncrease.append(float(x[OPEN][length-1])-float(x[OPEN][0]))

            dateFormat = "%Y-%m-%d"

            lifetime.append(datetime.strptime(x[DATE][length-1],dateFormat) - 
                            datetime.strptime(x[DATE][0],dateFormat))
            
            curr = 12
            yearlyReturn = []
            while(curr < length):
                if(x[OPEN][curr-12] == 0):
                    if x[OPEN][curr] != 0:
                        yearlyReturn.append(1)
                    else:
                        pass
                yearlyReturn.append(float(x[OPEN][curr])/float(x[OPEN][curr-12]))

                curr += 12
            
            medianYearlyAppreciation.append(stats.median(yearlyReturn))
            
        except Exception as e:
            print(e)
            pass

    

    if not os.path.exists("data_processed/"):
        os.mkdir("data_processed/")
        
    fileString = "Statistic: Minimum, Maximum, Average\n"
    fileString += "Lifetime Appreciation: " + str(min(lifetimeAppreciation)) + "," + str(max(lifetimeAppreciation)) + "," + str(stats.median(lifetimeAppreciation)) + "\n"
    fileString += "Lifetime Dollar Increase: " + str(min(lifetimeDollarIncrease)) + "," + str(max(lifetimeDollarIncrease)) + "," + str(stats.median(lifetimeDollarIncrease)) + "\n"
    fileString += "Median Yearly Return: " + str(min(medianYearlyAppreciation)) + "," + str(max(medianYearlyAppreciation)) + "," + str(stats.median(medianYearlyAppreciation)) + "\n"
    fileString += "Median Yearly Return: " + str(min(lifetime)) + "," + str(max(lifetime)) + "," + str(stats.median(lifetime)) + "\n"

    print(fileString) 

    df = pd.DataFrame({
        'Lifetime': lifetime,
        'Median Yearly Return': medianYearlyAppreciation,

    })

    correlation_matrix = df.corr(method='pearson')
    print(correlation_matrix)

    # print(lifetimeAppreciation)
    # print(lifetimeDollarIncrease)
    # print(max(lifetime))
    # print(stats.median(medianYearlyAppreciation))

# def median(lst):


def processCSV(files, indexData):
    i = 0

    for x in files:

        try:
            fileName = "data_original\\funds\\" + x
            fundData = [[],[],[],[],[]]

            print(x)
            

            with open(fileName, encoding="utf8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    fundData[0].append(row['Date'])
                    fundData[1].append(row['Open'])
                    fundData[2].append(row['High'])
                    fundData[3].append(row['Low'])
                    fundData[4].append(row['Close'])

            length = len(fundData[0])

            for x in indexData:
                indexLength = len(x[0])
                curr = 0
                fundLength = len(fundData[0])
                fundCurr = 0
                outPerformed = 0
                underPerformed = 0

                
                # print(date)
                while (curr < indexLength and fundCurr < fundLength):
                    # Matching Starting Dates
                    date = fundData[DATE][fundCurr]
                    # print(x[OPEN])
                    
                    # print(date, " ", [x][0][0][curr])
                    dateFormat = "%Y-%m-%d"

                    fundDate = datetime.strptime(date, dateFormat)
                    indexDate = datetime.strptime(x[DATE][curr], dateFormat)

                    if(fundDate == indexDate):
                        if(fundCurr > 12):
                            try:
                                fundAppreciation = (float(fundData[OPEN][fundCurr]) / float(fundData[OPEN][fundCurr - 12]))
                                indexAppreciation = (float(x[OPEN][curr]) / float(x[OPEN][curr - 12]))

                                print(date, " ", fundData[OPEN][fundCurr], " ",fundData[OPEN][fundCurr - 12], " ", fundAppreciation, "|\t", x[OPEN][curr], " ", x[OPEN][curr - 12], " ", indexAppreciation)
                                # print(fundAppreciation, " " , indexAppreciation)
                                if(indexAppreciation > fundAppreciation):
                                    underPerformed += 1
                                else:
                                    outPerformed += 1
                            except Exception as e:
                                pass
                        
                        curr +=12
                        fundCurr += 12
                    elif(fundDate > indexDate):
                        curr += 1
                        
                    else:
                        fundCurr += 1
                # 
            # print("    Fund outperformed S&P ", (outPerformed / (outPerformed + underPerformed)),"% of the time" )
            percent.append(outPerformed/ (outPerformed + underPerformed))               

            for x in indexData:
                pass
        except Exception as e:
            # print(e)
            pass

        # print("Outperformed S&P ", (outPerformed / (outPerformed + underPerformed)),"% of the time" )
        if(i >= 1000):
            break
            
        i+= 1

    
    fifty = 0
    seventyFive = 0
    ninety = 0
    hundred = 0

    quarters = [0,0,0,0,0]

    for x in percent:
        if(x >= 0.5 and x < 0.75):
            fifty += 1
        if(x >= 0.75 and x < 0.9):
            seventyFive += 1
        if(x >= 0.9 and x < 1):
            seventyFive += 1
        if(x == 1):
            hundred += 1

        if(x >= 0.5):
            quarters[0] += 1
        elif(x >= 0.25):
            quarters[1] += 1
        elif(x >= 0.1): 
            quarters[2] += 1
        elif(x > 0 and x < 0.1):
            quarters[3] += 1
        else:
            quarters[4] += 1

    labels = ["50-100%", "25-49%", "10-24%", "Less than 10%", "0%"]

    plt.title("Percent of time that a fund outperforms the S&P 500")

    print(fifty)
    print(seventyFive)
    print(ninety)
    print(hundred)
    plt.pie(quarters, labels=labels, autopct='%1.1f%%')
    plt.savefig("visuals/comparison.png")
    plt.show()
    

if __name__ == '__main__':
    fundsFiles = os.listdir(path='.\\data_original\\funds')
    # indexFiles = os.listdir(path='.\\data_original\\index')

    # indexData = getIndexData(indexFiles)
    visualization(fundsFiles)