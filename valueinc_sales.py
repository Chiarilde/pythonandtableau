#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:43:11 2022

@author: ChiaraNardelli
"""

import pandas as pd
data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

data.info()

#Mathematical operations on Tableau
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6


ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem

CostPerTransaction = NumberOfItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased*SellingPricePerItem

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

data['CostPerTransaction'] = CostPerTransaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

data['Markup'] = ( data['ProfitPerTransaction'] ) /data['CostPerTransaction']

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

day = data['Day'].astype(str)
year = data['Year'].astype(str)

print(day.dtype)
print(year.dtype)


mydate = day+'-'+data['Month']+'-'+year

data['Date'] = mydate

data.iloc[0]

split_col = data['ClientKeywords'].str.split(',' , expand=True)

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

data['ItemDescription'] = data['ItemDescription'].str.lower()

seasons = pd.read_csv('value_inc_seasons.csv' , sep=';')

data = pd.merge(data, seasons, on = 'Month')

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)

data = data.drop(['Year','Month'], axis = 1)

data.to_csv('ValueInc_Cleaned.csv', index=False)







