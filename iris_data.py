# Write a Python program to prepare Scatter Plot for Iris Dataset

import pandas as pd
iris=pd.read_csv("iris.csv")
iris.plot(kind ="scatter" ,
x='SepalLengthCm',
y ='PetalLengthCm')
