# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:28:15 2016

@author: alenachurakova
"""

import pandas
import scipy.stats

data = pandas.read_csv('Data_Extract_From_World_Development_Indicators_Data.csv', low_memory=False)
data = data[:214]

data = data[['EG.ELC.ACCS.ZS', 'IT.NET.USER.P2', 'SE.PRM.TENR', 'NY.GNP.PCAP.CD']]

data['EG.ELC.ACCS.ZS'] = pandas.to_numeric(data['EG.ELC.ACCS.ZS'])
data['IT.NET.USER.P2'] = pandas.to_numeric(data['IT.NET.USER.P2'])
data['SE.PRM.TENR'] = pandas.to_numeric(data['SE.PRM.TENR'])
data['NY.GNP.PCAP.CD'] = pandas.to_numeric(data['NY.GNP.PCAP.CD'])

data_nona=data.dropna()

print ('association between access to elecricity and school enrollment rate')
print (scipy.stats.pearsonr(data_nona['EG.ELC.ACCS.ZS'], data_nona['SE.PRM.TENR']))
print ('       ')
print ('association between internet user rate and school enrollment rate')
print (scipy.stats.pearsonr(data_nona['IT.NET.USER.P2'], data_nona['SE.PRM.TENR']))
print ('       ')
print ('association between GNI per person and school enrollment rate')
print (scipy.stats.pearsonr(data_nona['NY.GNP.PCAP.CD'], data_nona['SE.PRM.TENR']))