import plotly.express as pe
import csv
import numpy as np

def getData(dataPath):
    cupsOfCoffee = []
    hoursOfSleep = []

    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)

        for row in csvReader:
            hoursOfSleep.append(float(row['sleep in hours']))
            cupsOfCoffee.append(float(row['Coffee in ml']))

    return{'x': hoursOfSleep, 'y': cupsOfCoffee}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Your correlation is: ', correlation[0,1])

def main():
    data='cups of coffee vs hours of sleep.csv'
    dataSource = getData(data)
    findCorrelation(dataSource)

main()