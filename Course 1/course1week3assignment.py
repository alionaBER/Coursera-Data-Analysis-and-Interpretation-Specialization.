# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:24:56 2015

@author: alenachurakova
"""

import pandas

pandas.set_option('display.float_format', lambda x:'%f'%x)

data = pandas.read_csv('Data_Extract_From_World_Development_Indicators_Data.csv', low_memory=False)
data = data[:214]

#split into thee groups access to electricity
data['ELC.BIN3'] = pandas.qcut(data['EG.ELC.ACCS.ZS'], 3, labels=["1=low","2=medium","3=high"])
print('All countries: counts for ELC.BIN3, Access to electricity (% of population), binned (3 category)')
c_ELC_BIN3 = data['ELC.BIN3'].value_counts(sort=False, dropna=False)
print(c_ELC_BIN3)
print('All countries: percentages for ELC.BIN3, Access to electricity (% of population), binned (3 category)')
p_ELC_BIN3 = data['ELC.BIN3'].value_counts(sort=False, normalize=True, dropna=False)
print(p_ELC_BIN3)

#quartile split for internet access
data['NET.QRT'] = pandas.qcut(data['IT.NET.USER.P2'], 4, labels=["1=0%tile","2=25%tile","3=50%tile","4=75%tile"])
print('All countries: counts for NET.QRT, Access to Internet users (per 100 people), quartiles')
c_NET_QRT = data['NET.QRT'].value_counts(sort=False, dropna=False)
print(c_NET_QRT)
print('All countries: percentages for NET.QRT, Access to Internet users (per 100 people), quartiles')
p_NET_QRT = data['NET.QRT'].value_counts(sort=False, normalize=True, dropna=False)
print(p_NET_QRT)

#quartile split for enrollment rate
data['PRM.QRT'] = pandas.qcut(data['SE.PRM.TENR'], 4, labels=["1=0%tile","2=25%tile","3=50%tile","4=75%tile"])
print('All countries: counts for PRM.QRT, Adjusted net enrollment rate, primary (% of primary school age children), quartiles')
c_PRM_QRT = data['PRM.QRT'].value_counts(sort=False, dropna=False)
print(c_PRM_QRT)
print('All countries: percentages for PRM.QRT, Adjusted net enrollment rate, primary (% of primary school age children), quartiles')
p_PRM_QRT = data['PRM.QRT'].value_counts(sort=False, normalize=True, dropna=False)
print(p_PRM_QRT)

#crosstabs 
print(pandas.crosstab(data['PRM.QRT'], data['SE.PRM.TENR']))
