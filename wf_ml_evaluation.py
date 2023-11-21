import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime
import pickle
# from wf_ml_training import createLinearIndividualModels
import wf_ml_training as tr
import math

from wf_ml_prediction import createIndividualPrediction 
from wf_ml_prediction import createPolyPrediction
from wf_ml_prediction import createLaggedPrediction
from wf_ml_prediction import createCollectivePredictions

splitPercent = 0.8

def individual():
    fundsFiles = os.listdir(path='./data_original/funds')
    columnNames = {'Date': str,'Open':float, 'High':float,'Low':float,'Close':float,'Adj Close':float,'Volume':int}

    i = 0

    for x in fundsFiles:
        # print(fileName)
        # fileName = "data_original/" + x

        # print(fileName)

        fileName = os.path.join("data_original", "funds",x)
        
        df = pd.read_csv(fileName, names=columnNames, skiprows=1)

        first_date = df['Date'].min()
        last_date = df['Date'].max()  

        splitIndex = int(splitPercent * len(df))

        df['Date'] = pd.to_datetime(df['Date']) 
        df['delta_date'] = (df['Date'] - pd.to_datetime(first_date)).dt.days

        
        
        
        X_train = df['delta_date'].iloc[:splitIndex]
        Y_train = df['Open'].iloc[:splitIndex]

        X_test = df['delta_date'].iloc[splitIndex:]
        Y_test = df['Open'].iloc[splitIndex:]

        X_train_array = X_train.values.reshape(-1, 1)
        X_test_array = X_test.values.reshape(-1, 1)

        tr.createLinearIndividualModels(x, "individual", X_train_array, Y_train)
        tr.createPolyModel(x, "polynomial", X_train_array, Y_train)

        #Time
        df['lagged_price'] = df['Open'].shift(1)

        df = df.dropna()

        X = df[['delta_date','lagged_price']]
        X_train = X.iloc[:splitIndex]

        tr.createLinearIndividualModels(x, "lagged", X_train, Y_train)

        i += 1
        
        

def collective():
    fundsFiles = os.listdir(path='./data_original/funds')
    columnNames = {'Date': str,'Open':float, 'High':float,'Low':float,'Close':float,'Adj Close':float,'Volume':int}
    splitPercent = 0.8
    X_train = np.array([])
    Y_train = np.array([])

    model = LinearRegression()
    i = 0

    for x in fundsFiles:
        fileName = os.path.join("data_original", "funds",x)
        
        df = pd.read_csv(fileName, names=columnNames, skiprows=1)

        first_date = df['Date'].min()
        # last_date = df['Date'].max()

        splitIndex = int(splitPercent * len(df))

        # startPrice = df.loc[0,'Open']
        # relativeEndPrice = df.loc[splitIndex,'Open']
        # deltaDays = (pd.to_datetime(df.loc[splitIndex,'Date']) - pd.to_datetime(df.loc[0,'Date'])).days
        # appreciation = relativeEndPrice / startPrice

        df['Date'] = pd.to_datetime(df['Date']) 
        df['delta_date'] = (df['Date'] - pd.to_datetime(first_date)).dt.days

        # df['Appreciation_Open'] = df['Open'].pct_change().cumsum()
        # df['Appreciation_Open'] = df['Open'].fillna(method='ffill').pct_change().cumsum()
        df['Appreciation_Open'] = df['Open'].ffill().pct_change().cumsum()

        df = df.dropna()

        try:

            X = df[['delta_date', 'Open', 'Appreciation_Open']]
            X_train = X.iloc[:splitIndex-1]
            Y_train = X['Open'].iloc[splitIndex] / X['Open'].iloc[splitIndex-1]

            length = len(X)
            # print(i)
            model = tr.addToModel(model,X_train,Y_train)
        except Exception as e:
            print(e)


    tr.writeModel(model,"collective","collective")


if __name__ == '__main__':
    # individual()
    collective()
    # createIndividualPrediction()
    # createPolyPrediction()
    # createLaggedPrediction()
    # createCollectivePredictions()