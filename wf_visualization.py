import os
import csv
from datetime import datetime

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

                                # print(date, " ", fundData[OPEN][fundCurr], " ",fundData[OPEN][fundCurr - 12], " ", fundAppreciation, "|\t", x[OPEN][curr], " ", x[OPEN][curr - 12], " ", indexAppreciation)
                                # print(fundAppreciation, " " , indexAppreciation)
                                if(fundAppreciation > indexAppreciation):
                                    # print("Fund")
                                    outPerformed += 1
                                elif(indexAppreciation > fundAppreciation):
                                    # print("Index")
                                    underPerformed += 1
                                else:
                                    print("tie")
                            except Exception as e:
                                pass
                        
                        curr +=1
                        fundCurr += 1
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

            
        i+= 1


    print(percent)

    
    fifty = 0
    twenty_five = 0
    ten = 0
    lessThan = 0
    zero = 0

    for x in percent:
        if(x >= 0.5):
            fifty += 1
        elif(x >= 0.25):
            twenty_five += 1
        elif(x >= 0.1):
            ten += 1
        elif(x < 0.1 and x > 0):
            lessThan += 1
        else:
            zero += 1

    print(fifty)
    print(twenty_five)
    print(ten)
    print(lessThan)
    print(zero)

if __name__ == '__main__':
    fundsFiles = os.listdir(path='.\\data_original\\funds')
    indexFiles = os.listdir(path='.\\data_original\\index')

    indexData = getIndexData(indexFiles)
    processCSV(fundsFiles, indexData)