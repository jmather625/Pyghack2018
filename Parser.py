import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

def groupBuildings():

    allBuildingsList = []
    newBuilding = []
    with open ('dataFile.json', 'r') as f:
        dict = json.load(f)

        for i in range(len(dict)):

            if i == len(dict) - 1:

                item = { "time" : dict[i]["timeElapsed"], "weight": dict[i]["linearlyWeightedScale"] }
                newBuilding.append(item)

                allBuildingsList.append(newBuilding)
                break

            if (dict[i]['buildingName'] == dict[i + 1 ]['buildingName']):
                item = { "time" : dict[i]["timeElapsed"], "weight": int(dict[i]["linearlyWeightedScale"]) }
                newBuilding.append(item)
            else:
                item = { "time" : dict[i]["timeElapsed"], "weight": dict[i]["linearlyWeightedScale"] }
                newBuilding.append(item)
                allBuildingsList.append(newBuilding)
                newBuilding = []

    return allBuildingsList


def filter():
    buildingsList = groupBuildings()

    count = 0
    # print(buildingsList)
    for i in range(len(buildingsList) - 1):
        weights = []
        times = []
        for j in range(len(buildingsList[i])):

            weights.append(buildingsList[i][j]["weight"])
            times.append(buildingsList[i][j]["time"])

        if ((max(weights) - min(weights)) / (max(weights)) >= 0.00):
            for k in range(len(weights) - 1):
                if (((weights[k+1] - weights[k]) / weights[k+1]) >= 0.00):
                    print(weights[k], weights[k+1])
                    print(times[k], times[k+ 1])
                    print()



def timeWindow(weightArr, timeArr):
    for i in range(0, max(timeArr), 31536000):
        for j in range(len(weightArr)):
            timeWindows = 31536000 * 2
            maxTime = i + timeWindows
            if (timeArr[i] <= maxTime and timeArr[i] > i):
                print()


def testModeling(timeList, weightList):
    # model = sm.OLS(weightList, timeList).fit()
    # model.summary()

    slope, intercept, r_value, p_value, std_err = stats.linregress(timeList, weightList)
    print(slope)




print(filter())
print(testModeling([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
