import plotly.express as px
import csv
import pandas as pd
import numpy as np

df = pd.read_csv("data3.csv")
fig = px.scatter(df,x="Marks In Percentage", y="Days Present")
fig.show()

def getDataSource(dataPath):
    marks = []
    rollNo = []
    with open(dataPath) as f:
        data = csv.DictReader(f)
        for row in data:
            marks.append(float(row["Days Present"]))
            rollNo.append(float(row["Marks In Percentage"]))
    return{"x":marks,"y":rollNo}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Days present and marks", correlation[0,1])

def setUp():
    dataPath = "data3.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setUp()