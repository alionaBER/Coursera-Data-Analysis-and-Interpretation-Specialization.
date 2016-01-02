# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import pandas
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 

data = pandas.read_csv('Data_Extract_From_World_Development_Indicators_Data.csv', low_memory=False)
data = data[:214]

data['EG.ELC.ACCS.ZS'] = pandas.to_numeric(data['EG.ELC.ACCS.ZS'])
data['IT.NET.USER.P2'] = pandas.to_numeric(data['IT.NET.USER.P2'])
data['SE.PRM.TENR'] = pandas.to_numeric(data['SE.PRM.TENR'])

data['GNI_BIN'] = pandas.cut(data['NY.GNP.PCAP.CD'], (0, 1045, 4125, 12735, 130000), labels=["1=Low-income","2=Lower-middle-income","3=Upper-middle-income", '4=High-income'])
print('Country groupped by GNI')
c_GNI = data['GNI_BIN'].value_counts(sort=False, dropna=False)
print(c_GNI)

#renaming variable
data['PRM'] = data['SE.PRM.TENR']
data['NET'] = data['IT.NET.USER.P2']
data['ELC'] = data['EG.ELC.ACCS.ZS']

#investigation whether enrollent rate is different in income groups
data1 = data[['PRM', 'GNI_BIN']].dropna()
model1 = smf.ols(formula='PRM ~ C(GNI_BIN)', data=data1).fit()
print (model1.summary())

print ('means for PRM by income group')
m1= data1.groupby('GNI_BIN').mean()
print (m1)

print ('standard deviations for PRM by income group')
sd1 = data1.groupby('GNI_BIN').std()
print (sd1)

mc1 = multi.MultiComparison(data1['PRM'], data1['GNI_BIN'])
res1 = mc1.tukeyhsd()
print(res1.summary())

#investigation whether Internet user rate is different in income groups
data2 = data[['NET', 'GNI_BIN']].dropna()

model2 = smf.ols(formula='NET ~ C(GNI_BIN)', data=data2).fit()
print (model2.summary())

print ('means for NET by income group')
m2= data2.groupby('GNI_BIN').mean()
print (m2)

print ('standard deviations for NET by income group')
sd2 = data2.groupby('GNI_BIN').std()
print (sd2)

mc2 = multi.MultiComparison(data2['NET'], data2['GNI_BIN'])
res2 = mc2.tukeyhsd()
print(res2.summary())

#investigation whether electricity access is different in income groups
data3 = data[['ELC', 'GNI_BIN']].dropna()

model3 = smf.ols(formula='ELC ~ C(GNI_BIN)', data=data3).fit()
print (model3.summary())

print ('means for ELC by income group')
m3= data3.groupby('GNI_BIN').mean()
print (m3)

print ('standard deviations for ELC by income group')
sd3 = data3.groupby('GNI_BIN').std()
print (sd3)

mc3 = multi.MultiComparison(data3['ELC'], data3['GNI_BIN'])
res3 = mc3.tukeyhsd()
print(res3.summary())

