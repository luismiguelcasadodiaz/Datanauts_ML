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
from keras.models import Sequential
from keras.layers import Dense


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

print("Val shapes X={} Y={}".format(X_test.shape, Y_test.shape))


# train

print("Training")
# Sequential Model
# 180 neurons, cause the data set has 180 minutes.
# input Shape hold all independent variables.
model = Sequential([
    Dense(180, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(180, activation='relu'),
    Dense(1, activation='sigmoid'),
])
# Optimization sgd
# Loss 
# metrics to tracj accracy


model.compile(optimizer='sgd',
              loss='binary_crossentropy',
              metrics=['accuracy'])

hist = model.fit(X_train, Y_train,
          batch_size=32, epochs=100,
          validation_data=(X_val, Y_val))


#Training

hist = model.fit(X_train, Y_train,
          batch_size=32, epochs=100,
          validation_data=(X_val, Y_val))
print("Model evaluation")
evaluation = model.evaluate(X_test, Y_test)[1]
print(evaluation)

print("Visualization")

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='upper right')
plt.show()
plt.savefig("data/split/RNN_loss.png")



plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='lower right')
plt.show()
plt.savefig("data/split/RNN_acc.png")
