import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

def groupBuildings():

    allBuildingsList = []
    # newBuilding = []
    with open ('dataFile.json', 'r') as f:
        dict = json.load(f)


        # for i in range(len(dict)):
        #
        #     if i == len(dict) - 1:
        #
        #         item = { "time" : dict[i]["timeElapsed"], "weight": dict[i]["linearlyWeightedScale"] }
        #         newBuilding.append(item)
        #
        #         allBuildingsList.append(newBuilding)
        #         break
        #
        #     if (dict[i]['buildingName'] == dict[i + 1 ]['buildingName']):
        #         item = { "time" : dict[i]["timeElapsed"], "weight": int(dict[i]["linearlyWeightedScale"]) }
        #         newBuilding.append(item)
        #     else:
        #         item = { "time" : dict[i]["timeElapsed"], "weight": dict[i]["linearlyWeightedScale"] }
        #         newBuilding.append(item)
        #         allBuildingsList.app

        currentWeights = []
        currentTimes = []

        for i in range(len(dict)-1):

            if i == len(dict) - 1:
                currentWeights.append(int(dict[i]["linearlyWeightedScale"]))
                currentTimes.append(int(dict[i]["timeElapsed"]))
                dictToAppend = {"weights":currentWeights, "times":currentTimes}
                allBuildingsList.append(dictToAppend)


            if (dict[i]['buildingName'] == dict[i + 1 ]['buildingName']):
                currentWeights.append(int(dict[i]["linearlyWeightedScale"]))
                currentTimes.append(int(dict[i]["timeElapsed"]))
            else:
                currentWeights.append(int(dict[i]["linearlyWeightedScale"]))
                currentTimes.append(int(dict[i]["timeElapsed"]))
                dictToAppend = {"weights":currentWeights, "times":currentTimes}
                allBuildingsList.append(dictToAppend)
                currentWeights = []
                currentTimes = []


    print(allBuildingsList)
    return allBuildingsList


def filter():
    buildingsList = groupBuildings()

    count = 0
    # print(buildingsList)
    # for i in range(len(buildingsList) - 1):
    #     weights = []
    #     times = []
    #     for j in range(len(buildingsList[i])):
    #
    #         weights.append(buildingsList[i][j]["weight"])
    #         times.append(buildingsList[i][j]["time"])
    #
    #     if ((max(weights) - min(weights)) / (max(weights)) >= 0.00):
    #         for k in range(len(weights) - 1):
    #             if (((weights[k+1] - weights[k]) / weights[k+1]) >= 0.00):
    #                 print(weights[k], weights[k+1])
    #                 print(times[k], times[k+ 1])
    #                 print()



    for i in range(len(buildingsList) - 1):

        j = 0
        while j < len(buildingsList[i]["weights"]) :


        #    print(dict['weights'])
            if len(buildingsList[i]["weights"]) == j + 1:
                break


            if buildingsList[i]["weights"][j] > buildingsList[i]["weights"][j + 1]:
                print(buildingsList[i]["weights"][j], buildingsList[i]["weights"][j+1])
                buildingsList[i]["weights"].pop(j+1)
                buildingsList[i]["times"].pop(j+1)
            j += 1

    return buildingsList


def timeWindow():
    buildingsList = filter()

    for i in range(0, max(timeArr), 31536000):
        for j in range(len(weightArr)):
            #3156000 seconds in a year
            #default window of 2 years
            timeWindows = 31536000 * 2
            maxTime = i + timeWindows
            if (timeArr[i] <= maxTime and timeArr[i] > i):
                print()


def testModeling(timeList, weightList):
    # model = sm.OLS(weightList, timeList).fit()
    # model.summary()

    slope, intercept, r_value, p_value, std_err = stats.linregress(timeList, weightList)
    print(slope)



groupBuildings()
print(filter())
print(testModeling([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
