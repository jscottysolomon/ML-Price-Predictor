import pickle
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import statistics as stats
import math

splitPercent = 0.8

def createIndividualPrediction():
    fundsFiles = os.listdir(path='./data_original/funds')
    columnNames = {'Date': str,'Open':float, 'High':float,'Low':float,'Close':float,'Adj Close':float,'Volume':int}
    mse = []
    r2 = []
    mae = []

    i = 0

    for x in fundsFiles:
        model = None

        fileName = os.path.join("data_original", "funds",x)
        
        df = pd.read_csv(fileName, names=columnNames, skiprows=1)
        pickleFile = os.path.join("models", "individual", (x + ".pkl"))

        try:
        # if os.path.exists(pickleFile):
            with open(pickleFile, 'rb') as file:
                model = pickle.load(file)
                # print("Opened successfully", fileName)

            splitIndex = int(splitPercent * len(df))
            first_date = df['Date'].min()

            df['Date'] = pd.to_datetime(df['Date']) 
            df['delta_date'] = (df['Date'] - pd.to_datetime(first_date)).dt.days
            X_test = df['delta_date'].iloc[splitIndex:]
            Y_test = df['Open'].iloc[splitIndex:]

            X_test_array = X_test.values.reshape(-1, 1)

            y_pred = model.predict(X_test_array)
            # temp_mse = (mean_squared_error(Y_test, y_pred))
            # temp_r2 = (r2_score(Y_test, y_pred))
            # temp_mae = mean_absolute_error(Y_test, y_pred)

            # print(temp_mse, temp_r2, temp_mae)

            mse.append(mean_squared_error(Y_test, y_pred))
            r2.append(r2_score(Y_test, y_pred))
            mae.append(mean_absolute_error(Y_test, y_pred))
            
            # mse)

        except Exception as e:
            pass

    print(min(r2), max(r2), stats.median(r2))
    print(min(mse), max(mse), stats.median(mse))
    print(min(mae), max(mae), stats.median(mae))

def createLaggedPrediction():
    fundsFiles = os.listdir(path='./data_original/funds')
    columnNames = {'Date': str,'Open':float, 'High':float,'Low':float,'Close':float,'Adj Close':float,'Volume':int}
    mse = []
    r2 = []
    mae = []

    i = 0

    for x in fundsFiles:
        model = None

        fileName = os.path.join("data_original", "funds",x)
        
        df = pd.read_csv(fileName, names=columnNames, skiprows=1)
        pickleFile = os.path.join("models", "lagged", (x + ".pkl"))

        try:
        # if os.path.exists(pickleFile):
            with open(pickleFile, 'rb') as file:
                model = pickle.load(file)
                # print("Opened successfully", fileName)

            splitIndex = int(splitPercent * len(df))
            first_date = df['Date'].min()

            df['Date'] = pd.to_datetime(df['Date']) 
            df['delta_date'] = (df['Date'] - pd.to_datetime(first_date)).dt.days
            

            df['lagged_price'] = df['Open'].shift(1)

            df = df.dropna()

            X = df[['delta_date','lagged_price']]

            X_test = X.iloc[splitIndex:]
            Y_test = df['Open'].iloc[splitIndex:]

            y_pred = model.predict(X_test)

            # temp_mse = (mean_squared_error(Y_test, y_pred))
            # temp_r2 = (r2_score(Y_test, y_pred))
            # temp_mae = mean_absolute_error(Y_test, y_pred)

            # print(temp_mse, temp_r2, temp_mae)

            mse.append(mean_squared_error(Y_test, y_pred))
            r2.append(r2_score(Y_test, y_pred))
            mae.append(mean_absolute_error(Y_test, y_pred))
            
            # mse)

        except Exception as e:
            print(e)
            pass

    r2 = list(filter(lambda x: not math.isnan(x), r2))

    print(min(r2), max(r2), stats.median(r2))
    print(min(mse), max(mse), stats.median(mse))
    print(min(mae), max(mae), stats.median(mae))

def createPolyPrediction():
    fundsFiles = os.listdir(path='./data_original/funds')
    columnNames = {'Date': str,'Open':float, 'High':float,'Low':float,'Close':float,'Adj Close':float,'Volume':int}
    mse = []
    r2 = []
    mae = []

    i = 0

    for x in fundsFiles:
        model = None

        fileName = os.path.join("data_original", "funds",x)
        
        df = pd.read_csv(fileName, names=columnNames, skiprows=1)
        pickleFile = os.path.join("models", "polynomial", (x + ".pkl"))

        try:
        # if os.path.exists(pickleFile):
            with open(pickleFile, 'rb') as file:
                model = pickle.load(file)
                # print("Opened successfully", fileName)

            splitIndex = int(splitPercent * len(df))
            first_date = df['Date'].min()

            df['Date'] = pd.to_datetime(df['Date']) 
            df['delta_date'] = (df['Date'] - pd.to_datetime(first_date)).dt.days
            X_test = df['delta_date'].iloc[splitIndex:]
            Y_test = df['Open'].iloc[splitIndex:]

            X_test_array = X_test.values.reshape(-1, 1)

            degree = 2
            polyFeatures = PolynomialFeatures(degree=degree,include_bias=False)
            polyFeatures.fit(X_test_array)
            X_poly = polyFeatures.transform(X_test_array)

            y_pred = model.predict(X_poly)

            # temp_mse = (mean_squared_error(Y_test, y_pred))
            # temp_r2 = (r2_score(Y_test, y_pred))
            # temp_mae = mean_absolute_error(Y_test, y_pred)

            # print(temp_mse, temp_r2, temp_mae)

            mse.append(mean_squared_error(Y_test, y_pred))
            r2.append(r2_score(Y_test, y_pred))
            mae.append(mean_absolute_error(Y_test, y_pred))

            print(x)
            
            # mse)

        except Exception as e:
            print(e)

    print(min(r2), max(r2), stats.median(r2))
    print(min(mse), max(mse), stats.median(mse))
    print(min(mae), max(mae), stats.median(mae))

def createCollectivePredictions():
    fundsFiles = os.listdir(path='./data_original/funds')
    columnNames = {'Date': str,'Open':float, 'High':float,'Low':float,'Close':float,'Adj Close':float,'Volume':int}

    pickleFile = os.path.join("models", "collective", "collective.pkl")

    global_y_expected = []
    global_y_predicted = []

    model = None

    with open(pickleFile, 'rb') as file:
        model = pickle.load(file)

    i = 0

    for x in fundsFiles:
        ii = 0


        fileName = os.path.join("data_original", "funds",x)
        
        df = pd.read_csv(fileName, names=columnNames, skiprows=1)

        splitIndex = int(splitPercent * len(df))
        first_date = df['Date'].min()
        

        df['Date'] = pd.to_datetime(df['Date']) 
        df['delta_date'] = (df['Date'] - pd.to_datetime(first_date)).dt.days
        df['Appreciation_Open'] = df['Open'].ffill().pct_change().cumsum()
        df = df.dropna()

        try:

            X = df[['delta_date', 'Open', 'Appreciation_Open']]
            X_train = X.iloc[splitIndex-1]
            Y_train = X['Open'].iloc[splitIndex] / X['Open'].iloc[splitIndex-1]
            

            length = len(X) - len(X_train)
            while(ii < (length-1)):
                X_test = X.iloc[:(splitIndex+ii)]
                
                y_expected = X['Open'].iloc[splitIndex+ii+1] / X['Open'].iloc[splitIndex+ii]
                y_pred = model.predict(X_test)

                global_y_expected.append(y_expected)
                global_y_expected.append(y_pred)

                print(y_expected, y_pred)

                ii += 1
                pass


            # print(i)
            # model = tr.addToModel(X_train,Y_train)
        except Exception as e:
             if(i < 10):
                print(e)

        i += 1
            # pass