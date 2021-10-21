import plotly.express as px
import csv
import pandas as pd
import numpy as np

df = pd.read_csv("data4.csv")
fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
fig.show()

def getDataSource(dataPath):
    coff = []
    weekNo = []
    with open(dataPath) as f:
        data = csv.DictReader(f)
        for row in data:
            coff.append(float(row["sleep in hours"]))
            weekNo.append(float(row["Coffee in ml"]))
    return{"x":coff,"y":weekNo}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between coffee and amount of sleep", correlation[0,1])

def setUp():
    dataPath = "data4.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setUp()