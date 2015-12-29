# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:55:27 2015

@author: alenachurakova
"""

import pandas
import seaborn
import matplotlib.pyplot as plt

#Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows', None)
# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

data = pandas.read_csv('Data_Extract_From_World_Development_Indicators_Data.csv', low_memory=False)
data = data[:214]

data['EG.ELC.ACCS.ZS'] = pandas.to_numeric(data['EG.ELC.ACCS.ZS'])
data['IT.NET.USER.P2'] = pandas.to_numeric(data['IT.NET.USER.P2'])
data['SE.PRM.TENR'] = pandas.to_numeric(data['SE.PRM.TENR'])

#descriptive statistics for quantitative variables
print 'describe Access to electricity (% of population)'
desc_ELC = data['EG.ELC.ACCS.ZS'].describe()
print desc_ELC

print 'describe Access to Internet users (per 100 people)'
desc_NET = data['IT.NET.USER.P2'].describe()
print desc_NET

print 'describe Adjusted net enrollment rate, primary (% of primary school age children)'
desc_PRM = data['SE.PRM.TENR'].describe()
print desc_PRM

#Univariate histogram for quantitative variable:
seaborn.distplot(data['EG.ELC.ACCS.ZS'].dropna(), kde=False);
plt.xlabel('Access to electricity (% of population)')
plt.title('Access to electricity')

seaborn.distplot(data['IT.NET.USER.P2'].dropna(), kde=False);
plt.xlabel('Access to Internet users (per 100 people)')
plt.title('Access to Internet users')

seaborn.distplot(data['SE.PRM.TENR'].dropna(), kde=False);
plt.xlabel('Adjusted net enrollment rate, primary (% of primary school age children)')
plt.title('Adjusted net enrollment rate, primary')

#scatterplot school enrollment rate and internet
scat1 = seaborn.regplot(x="IT.NET.USER.P2", y="SE.PRM.TENR", fit_reg=False, data=data, color="g")
plt.xlabel('Access to Internet users (per 100 people)')
plt.ylabel('Adjusted net enrollment rate, primary (% of primary school age children)')
plt.title('Scatterplot for the association between primary school enrollment rate and Internet use rate')
plt.ylim((50,101))
plt.xlim((-1,101))

#scatterplot school enrollment rate and elecricity
scat2 = seaborn.regplot(x="EG.ELC.ACCS.ZS", y="SE.PRM.TENR", fit_reg=False, data=data)
plt.xlabel('Access to electricity (% of population)')
plt.ylabel('Adjusted net enrollment rate, primary (% of primary school age children)')
plt.title('Scatterplot for the association between primary school enrollment rate and access to electricity')
plt.ylim((50,101))
plt.xlim((-1,101))

#scatterplot school enrollment rate and GNI
scat3 = seaborn.regplot(x="NY.GNP.PCAP.CD", y="SE.PRM.TENR", fit_reg=False, data=data)
plt.xlabel('GNI per capita, Atlas method (current US$)')
plt.ylabel('Adjusted net enrollment rate, primary (% of primary school age children)')
plt.title('Scatterplot for the association between primary school enrollment rate and GNI per capita')
plt.ylim((50,101))
plt.xlim((-20,120000))

print data[(data['NY.GNP.PCAP.CD']>= 100000)]