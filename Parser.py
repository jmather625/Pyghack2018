import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
import matplotlib.pyplot as plt

def groupBuildings(fileName):

    allBuildingsList = []
    # newBuilding = []
    with open (fileName, 'r') as f:
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

    return allBuildingsList


def filter(fileName):
    buildingsList = groupBuildings(fileName)

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
                # print(buildingsList[i]["weights"][j], buildingsList[i]["weights"][j+1])
                buildingsList[i]["weights"].pop(j+1)
                buildingsList[i]["times"].pop(j+1)
            j += 1


    return buildingsList


def timeWindow(fileName):
    buildingsList = filter(fileName)
    #23 years, 31536000 seconds per year
    maxTime = 725328000
    timeIncrement = 31536000
    #0th index is 1st year, 1st index is 2nd year, up to 23rd index is 22nd year
    #slopeList will be added to by slopes from each building, then averaged by dividing by number of buildings
    slopeList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    relevantBuildingsList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(buildingsList)):
        if (len(buildingsList[i]["times"])) < 2:
            continue
        for j in range(0, maxTime, timeIncrement):
            for k in range(len(buildingsList[i]["times"]) - 1):
                subArrayIndices = []
                while (j <= buildingsList[i]["times"][k] and buildingsList[i]["times"][k] <= j + timeIncrement):
                    subArrayIndices.append(k)
                    k += 1
                    if k == len(buildingsList[i]["times"])-1:
                        subArrayIndices.append(k)
                        break

                if len(subArrayIndices) >= 2:
                    #print(subArrayIndices)
                    #print(len(buildingsList[i]["times"]))
                    timeList = []
                    weightList = []

                    for item in subArrayIndices:
                        #print(item)
                        #print(type(item))
                        #print("item:", buildingsList[i]["times"])
                        timeList.append(buildingsList[i]["times"][item])
                        #print("timeList:", timeList)
                        weightList.append(buildingsList[i]["weights"][item])
                        #print("weightList:", weightList)
                        #places slope in right index
                        #multiply to get yearly decrease
                    slopeList[int(j / timeIncrement)] += slopeFunction(timeList, weightList)*timeIncrement
                    relevantBuildingsList[int(j / timeIncrement)] += 1

    for n in range(len(slopeList)):
        if relevantBuildingsList[n] == 0:
            continue
        else:
            slopeList[n] = slopeList[n] / relevantBuildingsList[n]


    graphSlopes(slopeList)
    return slopeList


def slopeFunction(timeList, weightList):
    # model = sm.OLS(weightList, timeList).fit()
    # model.summary()
    slope, intercept, r_value, p_value, std_err = stats.linregress(timeList, weightList)

    # print(slope)
    return slope


def graphSlopes(arrSlopes):

    timeInc = []
    for i in range(len(arrSlopes)):
        timeInc.append(1 * i)

    year = [1960, 1970, 1980, 1990, 2000, 2010]

    plt.plot(timeInc, arrSlopes, color='orange')
    plt.xlabel('Time Intervals')
    plt.ylabel('Rate of Deterioration')
    plt.title('Deterioration Over Time')
    plt.show()



# graphSlopes([44.91, 58.09, 78.07, 107.7, 138.5, 170.6])

# print(filter())



if __name__== "__main__":
    timeWindow("dataFile.json")
    # timeWindow("key3dataFilev2.json")
