import plotly.figure_factory as ff
import statistics as st
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()

meanpop=st.mean(data)
print("population mean: ",meanpop)

def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

def show_fig(meanlist):
    df = meanlist
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    meanList = []
    for i in range(0,100):
        meanSet= randomSetOfMean(30)
        meanList.append(meanSet)
    show_fig(meanList)
    print("sample mean: ", st.mean(meanList))
setup()