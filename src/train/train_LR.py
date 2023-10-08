#!/usr/local/bin/python3

import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn.pipeline import make_pipeline
from statsmodels.stats.diagnostic import normal_ad
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson
from scipy import stats


def model_evaluation(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    
    MAE = metrics.mean_absolute_error(y_test, y_pred)
    MSE = metrics.mean_squared_error(y_test, y_pred)
    RMSE = np.sqrt(MSE)
    R2_Score = metrics.r2_score(y_test, y_pred)
    
    return pd.DataFrame([MAE, MSE, RMSE, R2_Score], index=['MAE', 'MSE', 'RMSE' ,'R2-Score'], columns=[model_name])

def compare_plot(df_comp):
    df_comp.reset_index(inplace=True)
    df_comp.plot(y=['Actual','Predicted'], kind='bar', figsize=(20,7), width=0.8)
    plt.title('Predicted vs. Actual Target Values for Test Data', fontsize=20)
    plt.ylabel('Kp Index', fontsize=15)
    plt.show()
    plt.savefig("data/split/LR_Comp.png")


os.chdir("../..")

print("Reading Train, Test & Val Dataset ....")

with open('data/split/X_train.pkl', 'rb') as f:
    X_train = pickle.load(f)

with open('data/split/Y_train.pkl', 'rb') as f:
    Y_train = pickle.load(f)

print("Train shapes X={} Y={}".format(X_train.shape, Y_train.shape))

with open('data/split/X_val.pkl', 'rb') as f:
    X_val = pickle.load(f)

with open('data/split/Y_val.pkl', 'rb') as f:
    Y_val = pickle.load(f)

print("Val shapes X={} Y={}".format(X_val.shape, Y_val.shape))

with open('data/split/X_test.pkl', 'rb') as f:
    X_test = pickle.load(f)

with open('data/split/Y_test.pkl', 'rb') as f:
    Y_test = pickle.load(f)

print("Test shapes X={} Y={}".format(X_test.shape, Y_test.shape))


# train

print("Training")

linear_reg = LinearRegression()
linear_reg.fit(X_train, Y_train)
"""
print("Calculating Interceptions")
interceptions = pd.DataFrame( \
        data = np.append(linear_reg.intercept_ , linear_reg.coef_), \
        index = ['Intercept']+[str(col)+" Coef." for col in X_train.T], \
        columns=['Value']).sort_values('Value', ascending=False \
        )
print(interceptions)
"""



print("Model evaluation")
evaluation = model_evaluation(linear_reg, X_val, Y_val, 'Linear Reg.')
print(evaluation)



print("Visualization")
y_test_pred = linear_reg.predict(X_test)
df_comp = pd.DataFrame({'Actual':Y_test, 'Predicted':y_test_pred})
compare_plot(df_comp)
