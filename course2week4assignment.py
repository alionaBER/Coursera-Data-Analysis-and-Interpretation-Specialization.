# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:24:07 2016

@author: alenachurakova
"""

import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt


data = pandas.read_csv('Data_Extract_From_World_Development_Indicators_Data.csv', low_memory=False)
data = data[:214]

data = data[['EG.ELC.ACCS.ZS','IT.NET.USER.P2', 'SE.PRM.TENR', 'NY.GNP.PCAP.CD']]

data['EG.ELC.ACCS.ZS'] = pandas.to_numeric(data['EG.ELC.ACCS.ZS'])
data['SE.PRM.TENR'] = pandas.to_numeric(data['SE.PRM.TENR'])
data['NY.GNP.PCAP.CD'] = pandas.to_numeric(data['NY.GNP.PCAP.CD'])
data['IT.NET.USER.P2'] = pandas.to_numeric(data['IT.NET.USER.P2'])

#creating groupping by income
data['GNI_BIN'] = pandas.cut(data['NY.GNP.PCAP.CD'], (0, 1045, 4125, 12735, 130000), labels=["1=Low-income","2=Lower-middle-income","3=Upper-middle-income", "4=High-income"])
print('Country groupped by GNI')
c_GNI = data['GNI_BIN'].value_counts(sort=False, dropna=False)
print(c_GNI)

data_nona=data.dropna()
c_GNI_nona = data_nona['GNI_BIN'].value_counts(sort=False)
print(c_GNI_nona)

sub1=data_nona[(data_nona['GNI_BIN']== "1=Low-income")]
sub2=data_nona[(data_nona['GNI_BIN']== "2=Lower-middle-income")]
sub3=data_nona[(data_nona['GNI_BIN']== "3=Upper-middle-income")]
sub4=data_nona[(data_nona['GNI_BIN']== "4=High-income")]

print ('Association between access to elecricity and school enrollment rate \nfor low-income economies')
print (scipy.stats.pearsonr(sub1['EG.ELC.ACCS.ZS'], sub1['SE.PRM.TENR']))
print ('       ')
print ('Association between access to elecricity and school enrollment rate \nfor lower-middle-income economies')
print (scipy.stats.pearsonr(sub2['EG.ELC.ACCS.ZS'], sub2['SE.PRM.TENR']))
print ('       ')
print ('Association between access to elecricity and school enrollment rate \nfor upper-middle-income economies')
print (scipy.stats.pearsonr(sub3['EG.ELC.ACCS.ZS'], sub3['SE.PRM.TENR']))
print ('       ')
print ('Association between access to elecricity and school enrollment rate \nfor high-income economies')
print (scipy.stats.pearsonr(sub4['EG.ELC.ACCS.ZS'], sub4['SE.PRM.TENR']))

#%%
scat0 = seaborn.regplot(x='EG.ELC.ACCS.ZS', y='SE.PRM.TENR', data=data)
plt.xlabel('Access to elecricity')
plt.ylabel('Primary school enrollment rate')
plt.title('Scatterplot for the association between plt.xlabel access to elecricity and primary school enrollment rate')
print (scat0)
plt.ylim((50,101))
plt.xlim((-1,101))
#%%
scat1 = seaborn.regplot(x='EG.ELC.ACCS.ZS', y='SE.PRM.TENR', data=sub1)
plt.xlabel('Access to elecricity')
plt.ylabel('Primary school enrollment rate')
plt.title('Scatterplot for the association between access to elecricity and \nprimary school enrollment rate for low-income economies')
print (scat1)
plt.ylim((50,101))
plt.xlim((-1,101))
#%%
scat2 = seaborn.regplot(x='EG.ELC.ACCS.ZS', y='SE.PRM.TENR', data=sub2)
plt.xlabel('Access to elecricity')
plt.ylabel('Primary school enrollment rate')
plt.title('Scatterplot for the association between access to elecricity and \nprimary school enrollment rate for lower-middle-income economies')
print (scat2)
plt.ylim((50,101))
plt.xlim((-1,101))
#%%
scat3 = seaborn.regplot(x='EG.ELC.ACCS.ZS', y='SE.PRM.TENR', data=sub3)
plt.xlabel('Access to elecricity')
plt.ylabel('Primary school enrollment rate')
plt.title('Scatterplot for the association between access to elecricity and \nprimary school enrollment rate for upper-middle-income economies')
print (scat3)
plt.ylim((50,101))
plt.xlim((-1,101))
#%%
scat4 = seaborn.regplot(x='EG.ELC.ACCS.ZS', y='SE.PRM.TENR', data=sub4)
plt.xlabel('Access to elecricity')
plt.ylabel('Primary school enrollment rate')
plt.title('Scatterplot for the association between access to elecricity and \nprimary school enrollment rate for high-income economies')
print (scat4)
plt.ylim((50,101))
plt.xlim((-1,101))


print ('association between internet user rate and school enrollment rate for low-income economies')
print (scipy.stats.pearsonr(sub1['IT.NET.USER.P2'], sub1['SE.PRM.TENR']))
print ('       ')
print ('association between internet user rate and school enrollment rate for lower-middle-income economies')
print (scipy.stats.pearsonr(sub2['IT.NET.USER.P2'], sub2['SE.PRM.TENR']))
print ('       ')
print ('association between internet user rate and school enrollment rate for upper-middle-income economies')
print (scipy.stats.pearsonr(sub3['IT.NET.USER.P2'], sub3['SE.PRM.TENR']))
print ('       ')
print ('association between internet user rate and school enrollment rate for high-income economies')
print (scipy.stats.pearsonr(sub4['IT.NET.USER.P2'], sub4['SE.PRM.TENR']))

#%%
scat0 = seaborn.regplot(x='IT.NET.USER.P2', y='SE.PRM.TENR', data=data)
plt.xlabel('Internet user rate')
plt.ylabel('Primary school enrollment rate')
plt.title('Scatterplot for the association between internet user rate and primary school enrollment rate')
print (scat0)
#%%
scat1 = seaborn.regplot(x='IT.NET.USER.P2', y='SE.PRM.TENR', data=sub1)
plt.xlabel('Internet user rate')
plt.ylabel('Primary school enrollment rate')
plt.title('Scatterplot for the association between internet user rate and \nprimary school enrollment rate for low-income economies')
print (scat1)
#%%
scat2 = seaborn.regplot(x='IT.NET.USER.P2', y='SE.PRM.TENR', data=sub2)
plt.xlabel('Internet user rate')
plt.ylabel('Primary school enrollment rate')
plt.title('Scatterplot for the association between internet user rate and \nprimary school enrollment rate for lower-middle-income economies')
print (scat2)
#%%
scat3 = seaborn.regplot(x='IT.NET.USER.P2', y='SE.PRM.TENR', data=sub3)
plt.xlabel('Internet user rate')
plt.ylabel('Primary school enrollment rate')
plt.title('Scatterplot for the association between internet user rate and \nprimary school enrollment rate for upper-middle-income economies')
print (scat3)
#%%
scat4 = seaborn.regplot(x='IT.NET.USER.P2', y='SE.PRM.TENR', data=sub4)
plt.xlabel('Internet user rate')
plt.ylabel('Primary school enrollment rate')
plt.title('Scatterplot for the association between internet user rate and \nprimary school enrollment rate for high-income economies')
print (scat4)