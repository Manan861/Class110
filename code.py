import csv 
import pandas as pd
import statistics 
import plotly.figure_factory as ff
import random 

df=pd.read_csv("data.csv")
data=df["average"].tolist()
def randomSetOfMean(counter):
    dataset=[]
    for i in range (0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    standardDeviation=statistics.stdev(dataset)
    return mean

def showFigure(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["average"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range (0,1000):
        setOfMeans=randomSetOfMean(100)
        mean_list.append(setOfMeans)
    
    showFigure(mean_list)

def stdD():
    mean_list=[]
    for i in range (0,1000):
        setOfMeans=randomSetOfMean(100)
        mean_list.append(setOfMeans)

    standardDeviation=statistics.stdev(mean_list)
    print(standardDeviation)

    mean=statistics.stdev(mean_list)
    print(mean)

stdD()
setup()



    


