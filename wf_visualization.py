import os
import csv

# print()

def processCSV(files):
    i = 0
    outPerformed = 0
    underPerformed = 0

    for x in files:
        try:
            fileName = "data_original\\" + x
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

            # print(data)
            length = len(data[0])
            curr = 0

        # print("Date\t Open \tHigh \t Low \t Close")
        # while (curr < length):
        #     print(data[0][curr], " ", data[2][curr]," ",data[3][curr]," ",data[3][curr]," ",data[4][curr])
        #     curr+= 1
        
            date = data[0][0].split("-")
            startYear = int(date[0])

            date = data[0][length - 1].split("-")
            endYear = int(date[0])

            startValue = float(data[1][0])
            endValue = float(data[1][length - 1])

            totalYears  = endYear - startYear

            # expectedAppreciation = totalYears * 0.10
            expectedEndValue = startValue + (totalYears * 0.10 * startValue)
            print("Expected: ", expectedEndValue, "Actual: ", endValue)
            if(endValue >= expectedEndValue):
                print("did as good as S&P")
                outPerformed += 1
            else:
                print("should have invested in S&P")
                underPerformed += 1
        except Exception as e:
            pass

            
        i+= 1

        # if(i > 3):
        #     # 
        #     break
            # print("opened ", fileName)

    print("Beat or Tied S&P: ", outPerformed)
    print("Underperformed: ", underPerformed)
          

if __name__ == '__main__':
     files = os.listdir(path='.\\data_original')

     processCSV(files)