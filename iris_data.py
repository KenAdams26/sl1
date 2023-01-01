#1.Scatter Plot for Iris Dataset
import pandas as pd
Iris=pd.read_csv("Iris.csv")
Iris.plot(kind='scatter',
          x='SepalLengthCm',
          y='SepalWidthCm')
