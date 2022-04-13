# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 20:46:31 2021

@author: WCHC3A
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import datetime
df = pd.read_excel(r"C:\Users\wchc3a.MULTIHOSP\Downloads\2022 budget\New.xlsx", sheet_name='Sheet1')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True) #set date as index
df.head()
df1=df['Bone Marrow']
df2=df['Transplant']
df3=df['ECMO']
import matplotlib.pyplot as plt
plt.xlabel("Date")
plt.ylabel("Bone Marrow")
plt.title("Bone Marrow")
plt.plot(df1)
#df.plot(style='k.')
#plt.show()
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df1, model='multiplicative')
result.plot()
plt.show()
from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    #Determing rolling statistics
    rolmean = timeseries.rolling(12).mean()
    rolstd = timeseries.rolling(12).std()
    #Plot rolling statistics:
    plt.plot(timeseries, color='blue',label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.show(block=False)
    
    #perform dickey fuller test  
    print("Results of dickey fuller test")
    adft = adfuller(timeseries['Bone Marrow'],autolag='AIC')
    # output for dft will give us without defining what the values are.
    #hence we manually write what values does it explains using a for loop
    output = pd.Series(adft[0:4],index=['Test Statistics','p-value','No. of lags used','Number of observations used'])
    for key,values in adft[4].items():
        output['critical value (%s)'%key] =  values
    print(output)
    
test_stationarity(df1)

df1_log = np.log(df1)
moving_avg = df1_log.rolling(12).mean()
std_dev = df1_log.rolling(12).std()
plt.plot(df1_log)
plt.plot(moving_avg, color="red")
plt.plot(std_dev, color ="black")
plt.show()


df1_log_moving_avg_diff = df1_log-moving_avg
df1_log_moving_avg_diff.dropna(inplace=True)

test_stationarity(df1_log_moving_avg_diff)
weighted_average = df1_log.ewm(halflife=12, min_periods=0,adjust=True).mean()

logScale_weightedMean = df1_log-weighted_average
from pylab import rcParams
rcParams['figure.figsize'] = 10,6
test_stationarity(logScale_weightedMean)

df1_log_diff = df1_log - df1_log.shift()
plt.title("Shifted timeseries")
plt.xlabel("Date")
plt.ylabel("Bone Marrow")
plt.plot(df1_log_diff)#Let us test the stationarity of our resultant series
df1_log_diff.dropna(inplace=True)
test_stationarity(df1_log_diff)

from statsmodels.tsa.stattools import acf,pacf
# we use d value here(data_log_shift)
acf = acf(df1_log_diff, nlags=15)
pacf= pacf(df1_log_diff, nlags=15,method='ols')#plot PACF
plt.subplot(121)
plt.plot(acf) 
plt.axhline(y=0,linestyle='-',color='blue')
plt.axhline(y=-1.96/np.sqrt(len(df1_log_diff)),linestyle='--',color='black')
plt.axhline(y=1.96/np.sqrt(len(df1_log_diff)),linestyle='--',color='black')
plt.title('Auto corellation function')
plt.tight_layout()#plot ACF
plt.subplot(122)
plt.plot(pacf) 
plt.axhline(y=0,linestyle='-',color='blue')
plt.axhline(y=-1.96/np.sqrt(len(df1_log_diff)),linestyle='--',color='black')
plt.axhline(y=1.96/np.sqrt(len(df1_log_diff)),linestyle='--',color='black')
plt.title('Partially auto corellation function')
plt.tight_layout()

from statsmodels.tsa.arima_model import ARIMA
model = ARIMA(df1_log, order=(3,1,3))
result_AR = model.fit(disp = 0)
plt.plot(df1_log_diff)
plt.plot(result_AR.fittedvalues, color='red')
plt.title("sum of squares of residuals")
print('RSS : %f' %sum((result_AR.fittedvalues-df1_log_diff["Bone Marrow"])**2))


result_AR.plot_predict(1,50)
x=result_AR.forecast(steps=15)
print(x)










