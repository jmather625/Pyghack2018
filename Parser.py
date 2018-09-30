import json



def groupBuildings():

    allBuildingsList = []
    newBuilding = []
    with open ('dataFile.json', 'r') as f:
        dict = json.load(f)

        for i in range(len(dict)):

            if i == len(dict) - 1:
                newBuilding.append(dict[i]["linearlyWeightedScale"])
                allBuildingsList.append(newBuilding)
                break

            if (dict[i]['buildingName'] == dict[i + 1 ]['buildingName']):
                newBuilding.append(dict[i]["linearlyWeightedScale"])
            else:
                newBuilding.append(dict[i]["linearlyWeightedScale"])
                allBuildingsList.append(newBuilding)
                newBuilding = []

    return allBuildingsList


def filter():
    buildingsList = groupBuildings()
    print(buildingsList)
    count = 0
    # print(buildingsList)
    for i in range(len(buildingsList) - 1):
         if ((max(buildingsList[i]) - min(buildingsList[i])) / (max(buildingsList[i])) >= 0.05):
            for j in range(len(buildingsList[i]) - 1):

                if (((buildingsList[i][j + 1] - buildingsList[i][j]) / buildingsList[i][j + 1]) >= 0.05):
                    print(buildingsList[i][j], buildingsList[i][j + 1])
                    count += 1

    print(count)


print(filter())
