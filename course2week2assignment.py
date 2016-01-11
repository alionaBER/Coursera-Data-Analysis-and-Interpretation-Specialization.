# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:58:04 2016

@author: alenachurakova
"""

import pandas
import scipy.stats

data = pandas.read_csv('Data_Extract_From_World_Development_Indicators_Data.csv', low_memory=False)
data = data[:214]

data['SE.PRM.TENR'] = pandas.to_numeric(data['SE.PRM.TENR'], errors='coerce')
data['NY.GNP.PCAP.CD'] = pandas.to_numeric(data['NY.GNP.PCAP.CD'], errors='coerce')

#data['GNI_BIN'] = pandas.cut(data['NY.GNP.PCAP.CD'], (0, 1045, 4125, 12735, 130000), labels=["1=Low","2=Lower-middle","3=Upper-middle", '4=High'])
data['GNI_BIN'] = pandas.cut(data['NY.GNP.PCAP.CD'], (0, 1045, 4125, 12735, 130000), labels=["1","2","3","4"])
print('Country groupped by GNI')
c_GNI = data['GNI_BIN'].value_counts(sort=False, dropna=False)
print(c_GNI)

data['PRM.M'] = pandas.qcut(data['SE.PRM.TENR'], 2, labels=["0","1"])
c_PRM = data['PRM.M'].value_counts(sort=False, dropna=False)
print(c_PRM)

# set variable types 
data['GNI_BIN'] = pandas.to_numeric(data['GNI_BIN'], errors='coerce')
data['PRM.M'] = data['PRM.M'].astype('category')

# contingency table of observed counts
ct=pandas.crosstab(data['PRM.M'],data['GNI_BIN'])
print (ct)

# column percentages
colsum=ct.sum(axis=0)
colpct=ct/colsum
print(colpct)

# chi-square test
print ('chi-square value, p value, expected counts')
cs= scipy.stats.chi2_contingency(ct)
print (cs)

#post hoc analysis
#comparison of low and lower-middle income
recode1v2 = {1: 1, 2: 2}
data['COMP1v2']= data['GNI_BIN'].map(recode1v2)

# contingency table of observed counts
ct1v2=pandas.crosstab(data['PRM.M'], data['COMP1v2'])
print (ct1v2)

print ('chi-square value, p value, expected counts')
cs1v2= scipy.stats.chi2_contingency(ct1v2)
print (cs1v2)

#comparison of low- and upper-middle-income
recode1v3 = {1: 1, 3: 3}
data['COMP1v3']= data['GNI_BIN'].map(recode1v3)
ct1v3=pandas.crosstab(data['PRM.M'], data['COMP1v3'])
print ('chi-square value, p value, expected counts')
cs1v3= scipy.stats.chi2_contingency(ct1v3)
print (cs1v3)

#comparison of low- and high-income
recode1v4 = {1: 1, 4: 4}
data['COMP1v4']= data['GNI_BIN'].map(recode1v4)
ct1v4=pandas.crosstab(data['PRM.M'], data['COMP1v4'])
print ('chi-square value, p value, expected counts')
cs1v4= scipy.stats.chi2_contingency(ct1v4)
print (cs1v4)

#comparison of lower-middle and upper-middle-income
recode2v3 = {2: 2, 3: 3}
data['COMP2v3']= data['GNI_BIN'].map(recode2v3)
ct2v3=pandas.crosstab(data['PRM.M'], data['COMP2v3'])
print ('chi-square value, p value, expected counts')
cs2v3= scipy.stats.chi2_contingency(ct2v3)
print (cs2v3)

#comparison of lower-middle and high-income
recode2v4 = {2: 2, 4: 4}
data['COMP2v4']= data['GNI_BIN'].map(recode2v4)
ct2v4=pandas.crosstab(data['PRM.M'], data['COMP2v4'])
print ('chi-square value, p value, expected counts')
cs2v4= scipy.stats.chi2_contingency(ct2v4)
print (cs2v4)


#comparison of upper-middle and high-income
recode3v4 = {3: 3, 4: 4}
data['COMP3v4']= data['GNI_BIN'].map(recode3v4)
ct3v4=pandas.crosstab(data['PRM.M'], data['COMP3v4'])
print ('chi-square value, p value, expected counts')
cs3v4= scipy.stats.chi2_contingency(ct3v4)
print (cs3v4)