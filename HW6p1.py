# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:01:13 2019

@author: egarcia2
"""
import numpy as np
import matplotlib as mt
import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv("RollingSystemDemand_20191022_0034.csv")
df = df.reset_index()
df = df.dropna()
df1 = pd.read_csv("RollingSystemDemand_20191022_0035.csv")
df1 = df1.reset_index()
df1 = df1.dropna()
index = df1.index[df.values[-2,1] == df1['HDR']]
df2 = df1[index[0]+1:]
df3 = df.append(df2, ignore_index = True)
df3['HDR'] = pd.to_datetime(df3['HDR'].astype(str), format='%Y%m%d%H%M%S')
df3 = df3.drop(['index'], axis=1)
df3 = df3.set_index('HDR')
df4 = df3.resample('.42D').mean()
df5 = df3.resample('.04182D').mean()
df4 = df4.reset_index()
df5 = df5.reset_index()
print(df4.plot(kind='bar',x='HDR',y='ROLLING SYSTEM DEMAND'))
print(df5.plot(kind='bar',x='HDR',y='ROLLING SYSTEM DEMAND'))