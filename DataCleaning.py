# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:25:50 2019

@author: Bandar
"""

import pandas as pd 
import numpy as num
import matplotlib as plt 
from matplotlib import pyplot

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

pdf = pd.read_csv("https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv",names = headers)




pdf.replace("?", num.nan, inplace = True)



avg_norm_loss = pdf["normalized-losses"].astype("float").mean(axis=0)
pdf["normalized-losses"].replace(num.nan,avg_norm_loss, inplace =True)


ave_bore = pdf["bore"].astype(float).mean(axis =0)
pdf["bore"].replace(num.nan, ave_bore, inplace = True)


ave_horsepower = pdf["horsepower"].astype(float).mean(axis =0)
pdf["horsepower"].replace(num.nan,ave_horsepower, inplace = True)

ave_peak = pdf["peak-rpm"].astype(float).mean(axis =0)
pdf["peak-rpm"].replace(num.nan, ave_peak,inplace = True)

mode= pdf["num-of-doors"].value_counts().idxmax()
pdf["num-of-doors"].replace(num.nan,mode,inplace = True)

pdf.dropna(subset = ["price"], axis = 0 , inplace = True)
pdf.reset_index(drop=True, inplace=True)
print(pdf.dtypes)

pdf[["bore", "stroke"]] =pdf[["bore", "stroke"]].astype("float")
pdf[["normalized-losses"]] = pdf[["normalized-losses"]].astype("int")
pdf[["price"]] = pdf[["price"]].astype("float")
pdf[["peak-rpm"]] = pdf[["peak-rpm"]].astype("float")
#print(pdf.dtypes)
pdf['city-L/100km'] = 235/pdf["city-mpg"]

pdf["highway-mpg"] = 235/pdf["highway-mpg"]
pdf.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)

pdf['length'] = pdf['length']/pdf['length'].max()
pdf['width'] = pdf['width']/pdf['width'].max()
pdf['height'] = pdf['height']/pdf['height'].max()
pdf["horsepower"]=pdf["horsepower"].astype(int, copy=True)

#plt.pyplot.hist(pdf["horsepower"])
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
bins = num.linspace(min(pdf["horsepower"]), max(pdf["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']
pdf['horsepower-binned'] = pd.cut(pdf['horsepower'], bins, labels=group_names, include_lowest=True )
pdf[['horsepower','horsepower-binned']].head(20)
pdf["horsepower-binned"].value_counts()


pyplot.bar(group_names, pdf["horsepower-binned"].value_counts())

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

dummy = pd.get_dummies(pdf["fuel-type"])
dummy.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
pdf = pd.concat([pdf, dummy], axis=1)
pdf.drop("fuel-type", axis = 1, inplace=True)
print(dummy)
print(pdf.head())
missingData = pdf.isnull()
print(missingData.head())


for column in missingData.columns.values.tolist():
 print(column)
 print(missingData[column].value_counts())
 print("")
 
 path ="C:/Users/Bandar/Desktop/Python Code/1a.csv"
 pdf.to_csv(path)
 

