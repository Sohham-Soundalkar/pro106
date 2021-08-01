import plotly.express as pe
import csv
import numpy as np

def getData(dataPath):
    studentMarks = []
    daysPresent = []

    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)

        for row in csvReader:
            daysPresent.append(float(row['Days Present']))
            studentMarks.append(float(row['Marks In Percentage']))

    return{'x': daysPresent, 'y': studentMarks}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Your correlation is: ', correlation[0,1])

def main():
    data='Student Marks vs Days Present.csv'
    dataSource = getData(data)
    findCorrelation(dataSource)

main()