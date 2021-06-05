from os import name
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
import statistics
import random

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)
population_sd=statistics.stdev(data)
print("the population mean is:",population_mean)
print("the popultion sd is: ",population_sd)

def randomSetOfMeans(counter):
    dataset=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def showFig(meanList):
    df=meanList
    mean=statistics.mean(meanList)
    print("The mean of the sampling data is: ",mean)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,15],mode="lines",name="Sampling Mean"))
    fig.show()

def standardDeviation():
    mean_list=[]
    for i in range(0,100):
        set_of_means = randomSetOfMeans(30)
        mean_list.append(set_of_means)
    sd = statistics.stdev(mean_list)
    print("Standard Deviation of Sampling Distribution: ", sd)

def setup():
    meanList=[]
    for r in range(0,100):
        setOfMean=randomSetOfMeans(30)
        meanList.append(setOfMean)
    showFig(meanList)
    mean=statistics.mean(meanList)
    print("The mean of the sampling data is: ",mean)
    standardDeviation()
    

setup()