import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime
import pickle

def createLinearIndividualModels(fileName, folder, X_train, Y_train):
    try:
        model = LinearRegression()

        model.fit(X_train, Y_train)

        modelFileName = os.path.join("models", folder, (fileName + ".pkl"))

        with open(modelFileName, 'wb') as file:
            pickle.dump(model, file)
    except Exception as e:
        pass
        

def createPolyModel(fileName, folder, X_train, Y_train):
    try:
        degree = 2
        polyFeatures = PolynomialFeatures(degree=degree,include_bias=False)
        polyFeatures.fit(X_train)
        X_poly = polyFeatures.transform(X_train)

        model = LinearRegression()

        model.fit(X_poly, Y_train)

        modelFileName = os.path.join("models", folder, (fileName + ".pkl"))

        with open(modelFileName, 'wb') as file:
            pickle.dump(model, file)
    except Exception as e:
        pass
        # print(e)

def addToModel(model, X_train, Y_train):
    try:
        ret = model
        ret.fit(X_train, Y_train)
        return ret
    except Exception as e:
        # print(e)
        return model
    
def writeModel(model, folder, fileName):
    try:

        modelFileName = os.path.join("models", folder, (fileName + ".pkl"))

        with open(modelFileName, 'wb') as file:
            pickle.dump(model, file)
    except Exception as e:
        pass
        # print(e)
        


# fundsFiles = os.listdir(path='./data_original/funds')
# columnNames = {'Date': str,'Open':float, 'High':float,'Low':float,'Close':float,'Adj Close':float,'Volume':int}
# splitPercent = 0.8

# i = 0

# for x in fundsFiles:
#     # print(fileName)
#     # fileName = "data_original/" + x

#     # print(fileName)

#     fileName = os.path.join("data_original", "funds",x)
    
#     df = pd.read_csv(fileName, names=columnNames, skiprows=1);

#     first_date = df['Date'].min()
#     last_date = df['Date'].max()

#     splitIndex = int(splitPercent * len(df))

#     # reference_date = datetime(2020, 1, 1)  # Replace with your reference date

#     # # Calculate the number of days since the reference date
#     # df['Days_since_reference'] = (df['Date'] - reference_date).dt.days

#     df['Date'] = pd.to_datetime(df['Date']) 
#     df['delta_date'] = (df['Date'] - pd.to_datetime(first_date)).dt.days
    
    
#     X_train = df['delta_date'].iloc[:splitIndex]
#     Y_train = df['Open'].iloc[:splitIndex]

#     X_test = df['delta_date'].iloc[splitIndex:]
#     Y_test = df['Open'].iloc[splitIndex:]

#     # X_train = X_train.reshape(-1, 1)
#     X_train_array = X_train.values.reshape(-1, 1)
#     X_test_array = X_test.values.reshape(-1, 1)
    
#     if(df['Date'].isna().any()):
#             print("drop")

#     try:

#         model = LinearRegression()

#         model.fit(X_train_array, Y_train)
#         y_pred = model.predict(X_test_array)
#         mse = mean_squared_error(Y_test, y_pred)


#         modelFileName = os.path.join("models", (x + ".pkl"))

#         print("train length", len(X_train), " Test length", len(X_test))

#         with open(modelFileName, 'wb') as file:
#             pickle.dump(model, file)
        
#         print("Mse: ", mse)

#     except Exception as e:
#         print(e)

#     # 

#     if(i < 10):
#         # print(df)
#         # print(df['Date'].min())   
#         # print(df['delta_date'])   
#         # print("train")
#         # print(X_train_array)  
#         # print("test")
#         # print(X_test)
#         pass

#     i += 1

# # print(fundsFiles)