# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 15:56:59 2015

@author: alenachurakova
"""

import pandas

pandas.set_option('display.float_format', lambda x:'%f'%x)

data = pandas.read_csv('Data_Extract_From_World_Development_Indicators_Data.csv', low_memory=False)
data = data[:214]

data.tail()

print(len(data))
print(len(data.columns))

#access to electricity
data['ELC.BIN'] = pandas.cut(data['EG.ELC.ACCS.ZS'], (0, 20, 40, 60, 80, 100))
print('All countries: counts for ELC.BIN, Access to electricity (% of population), binned')
c_ELC = data['ELC.BIN'].value_counts(sort=False, dropna=False)
print(c_ELC)
print('All countries: percentages for ELC.BIN, Access to electricity (% of population), binned')
p_ELC = data['ELC.BIN'].value_counts(sort=False, normalize=True, dropna=False)
print(p_ELC)

#internet access
data['NET.BIN'] = pandas.cut(data['IT.NET.USER.P2'], (0, 20, 40, 60, 80, 100))
print('All countries: counts for NET.BIN, Access to Internet users (per 100 people), binned')
c_NET = data['NET.BIN'].value_counts(sort=False, dropna=False)
print(c_NET)
print('All countries: percentages for NET.BIN, Access to Internet users (per 100 people), binned')
p_NET = data['NET.BIN'].value_counts(sort=False, normalize=True, dropna=False)
print(p_NET)

#literacy rate - too high percentage of missing data
data['LT.BIN'] = pandas.cut(data['SE.ADT.1524.LT.ZS'], (0, 20, 40, 60, 80, 100))
print('All countries: counts for LT.BIN, Literacy rate, youth total (% of people ages 15-24), binned')
c_LT = data['LT.BIN'].value_counts(sort=False, dropna=False)
print(c_LT)
print('All countries: percentages for LT.BIN, Literacy rate, youth total (% of people ages 15-24), binned')
p_LT = data['LT.BIN'].value_counts(sort=False, normalize=True, dropna=False)
print(p_LT)

#enrollment rate
data['PRM.BIN'] = pandas.cut(data['SE.PRM.TENR'], (0, 20, 40, 60, 80, 100))
print('All countries: counts for PRM.BIN, Adjusted net enrollment rate, primary (% of primary school age children), binned')
c_PRM = data['PRM.BIN'].value_counts(sort=False, dropna=False)
print(c_PRM)
print('All countries: percentages for PRM.BIN, Adjusted net enrollment rate, primary (% of primary school age children), binned')
p_PRM = data['PRM.BIN'].value_counts(sort=False, normalize=True, dropna=False)
print(p_PRM)

#subset Low and lower-middle-income economies
sub1 = data[(data['NY.GNP.PCAP.CD']<= 4125)]
sub = sub1.copy()

#subset access to electricity
sub['ELC.BIN'] = pandas.cut(data['EG.ELC.ACCS.ZS'], (0, 20, 40, 60, 80, 100))
print('Low and lower-middle-income economies: counts for ELC.BIN, Access to electricity (% of population), binned')
c_ELC = sub['ELC.BIN'].value_counts(sort=False, dropna=False)
print(c_ELC)
print('Low and lower-middle-income economies: percentages for ELC.BIN, Access to electricity (% of population), binned')
p_ELC = sub['ELC.BIN'].value_counts(sort=False, normalize=True, dropna=False)
print(p_ELC)

#subset internet access
sub['NET.BIN'] = pandas.cut(data['IT.NET.USER.P2'], (0, 20, 40, 60, 80, 100))
print('Low and lower-middle-income economies: counts for NET.BIN, Access to Internet users (per 100 people), binned')
c_NET = sub['NET.BIN'].value_counts(sort=False, dropna=False)
print(c_NET)
print('Low and lower-middle-income economies: percentages for NET.BIN, Access to Internet users (per 100 people), binned')
p_NET = sub['NET.BIN'].value_counts(sort=False, normalize=True, dropna=False)
print(p_NET)

#subset enrollment rate
sub['PRM.BIN'] = pandas.cut(data['SE.PRM.TENR'], (0, 20, 40, 60, 80, 100))
print('Low and lower-middle-income economies: counts for PRM.BIN, Adjusted net enrollment rate, primary (% of primary school age children), binned')
c_PRM = sub['PRM.BIN'].value_counts(sort=False, dropna=False)
print(c_PRM)
print('Low and lower-middle-income economies: percentages for PRM.BIN, Adjusted net enrollment rate, primary (% of primary school age children), binned')
p_PRM = sub['PRM.BIN'].value_counts(sort=False, normalize=True, dropna=False)
print(p_PRM)

#to detect country with relatively high internet users in the low income subset
sub2 = sub[(sub['IT.NET.USER.P2']>= 40)]
print(sub2)



