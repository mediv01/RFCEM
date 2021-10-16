from Consts import *
from Barbs import *
import Victory as vic

localText = CyTranslator()


def getBirthDate(x, y):
    tList = [500, 1800]
    tBirthDate = [500,
                  500,
                  632,
                  680,
                  711,
                  810,
                  843,
                  856,
                  864,
                  872,
                  880,
                  895,
                  910,
                  936,
                  960,
                  966,
                  1016,
                  1040,
                  1066,
                  1139,
                  1164,
                  1210,
                  1224,
                  1236,
                  1282,
                  1356,
                  1380,
                  1581,
                  500]
    tCollapseDate = (
        1453,  # Byzantium - Ottoman conquest of Constantinople
        1800,  # Frankia
        1517,  # Arabia - to make room for the Ottomans
        1396,  # Bulgaria - Bulgaria UHV 3
        1492,  # Cordoba - Cordoba UHV 3
        1800,  # Venice
        1473,  # Burgundy - Burgundy UHV 3
        1648,  # Germany - to make room for Prussia
        1478,  # Novgorod
        1523,  # Norway
        1300,  # Kiev - Kiev UHV 1
        1542,  # Hungary - 1541, Ottoman conquest of Buda
        1800,  # Spain
        1800,  # Denmark
        1650,  # Scotland
        1780,  # Poland
        1500,  # Genoa
        1800,  # Morocco
        1800,  # England
        1800,  # Portugal
        1474,  # Aragon
        1800,  # Sweden
        1800,  # Prussia
        1569,  # Lithuania - Lithuania UHV 3
        1800,  # Austria
        1800,  # Turkey
        1800,  # Moscow
        1800,  # Dutch
        1800  # Pope
    )

    if (x < len(tBirthDate)):
        tList[0] = tBirthDate[x]

    if (y < len(tCollapseDate)):
        tList[1] = tCollapseDate[y]

    return tList


def SearchCore(x, y):
    tList = []
    for i in range(len(tCoreAreasTL)):
        tfind = 0
        x1 = tCoreAreasTL[i][0]
        y1 = tCoreAreasTL[i][1]
        x2 = tCoreAreasBR[i][0]
        y2 = tCoreAreasBR[i][1]
        if ((x >= x1 and x <= x2) and (y >= y1 and y <= y2)):
            tList.append(i)
            tfind = 1
        if (tfind == 0):
            if ((x, y) in lExtraPlots[i]):
                tList.append(i)
            pass

    return tList
    # print(x1,y1)
    pass


def SearchBirthPlace(x, y):
    tList = []
    for i in range(len(tCapitals)):
        if x is tCapitals[i][0] and y is tCapitals[i][1]:
            tList.append(i)

    return tList


def SearchMinorCityBirth(x, y):
    tList = []
    iGameTurnList = list(dIndependentCities.keys())
    for iGameTurn in iGameTurnList:
        for tCity in dIndependentCities[iGameTurn]:
            lVariations, iCiv, iPop, iUnit, iNumUnits, iReligion, iWorkers = tCity
            for iCity in range(len(lVariations)):
                iChosenCity = iCity
                tCoords, sName, iPos = lVariations[iChosenCity]
                if tCoords[0] == x and tCoords[1] == y:
                    tList.append(iGameTurn)

    return tList

    pass


def checkProvincesStates(iPlayer, tProvince):
    tProvinces = [tProvince]
    pPlayer = gc.getPlayer(iPlayer)
    for iProv in tProvinces:
        if pPlayer.getProvinceCurrentState(iProv) < con.iProvinceConquer:
            return False
    return True

def SearchUHVProvince(provinceID, iPlayer):
    iPlayer = utils.getHumanID()
    tList = []

    UHVProvinceList = []
    UHVProvinceList2 = []
    UHVProvinceList3 = []

    if (iPlayer == iByzantium):
        UHVProvinceList = vic.tByzantumControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []
    elif (iPlayer == iFrankia):
        UHVProvinceList = vic.tFrankControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []

    elif (iPlayer == iArabia):
        UHVProvinceList = vic.tArabiaControlI
        UHVProvinceList2 = vic.tArabiaControlII
        UHVProvinceList3 = []

    elif (iPlayer == iBulgaria):
        UHVProvinceList = vic.tBulgariaControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []

    elif (iPlayer == iCordoba):
        UHVProvinceList = vic.tCordobaIslamize
        UHVProvinceList2 = []
        UHVProvinceList3 = []

    elif (iPlayer == iVenecia):
        UHVProvinceList = vic.tVenetianControl
        UHVProvinceList2 = vic.tVenetianControlII
        UHVProvinceList3 = []

    elif (iPlayer == iBurgundy):
        UHVProvinceList = vic.tBurgundyControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []
    elif (iPlayer == iGermany):
        UHVProvinceList = vic.tGermanyControl
        UHVProvinceList2 = vic.tGermanyControlII
        UHVProvinceList3 = []

    elif (iPlayer == iNovgorod):
        UHVProvinceList = vic.tNovgorodControl
        UHVProvinceList2 = vic.tNovgorodControlII
        UHVProvinceList3 = []

    elif (iPlayer == iKiev):
        UHVProvinceList = vic.tKievControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []

    elif (iPlayer == iNorway):
        UHVProvinceList = vic.tNorwayControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []


    elif (iPlayer == iHungary):
        UHVProvinceList = vic.tHungarynControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []

    elif (iPlayer == iSpain):
        UHVProvinceList = vic.tSpainConvert
        UHVProvinceList2 = []
        UHVProvinceList3 = []
    elif (iPlayer == iDenmark):
        UHVProvinceList = vic.tDenmarkControlI
        UHVProvinceList2 = vic.tDenmarkControlIII
        UHVProvinceList3 = []


    elif (iPlayer == iScotland):
        UHVProvinceList = vic.tScotlandControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []
    elif (iPlayer == iPoland):
        UHVProvinceList = vic.tPolishControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []
    elif (iPlayer == iGenoa):
        UHVProvinceList = vic.tGenoaControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []
    elif (iPlayer == iMorocco):
        UHVProvinceList = vic.tMoroccoControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []



    elif (iPlayer == iEngland):
        UHVProvinceList = vic.tEnglandControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []
    elif (iPlayer == iPortugal):
        UHVProvinceList = vic.tPortugalControlI
        UHVProvinceList2 = vic.tPortugalControlII
        UHVProvinceList3 = []


    elif (iPlayer == iAragon):
        UHVProvinceList = vic.tAragonControlI
        UHVProvinceList2 = vic.tAragonControlII
        UHVProvinceList3 = []


    elif (iPlayer == iSweden):
        UHVProvinceList = vic.tSwedenControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []
    elif (iPlayer == iPrussia):
        UHVProvinceList = vic.tPrussiaControlI
        UHVProvinceList2 = []
        UHVProvinceList3 = []

    elif (iPlayer == iAustria):
        UHVProvinceList = vic.tAustriaControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []

    elif (iPlayer == iTurkey):
        UHVProvinceList = vic.tOttomanControlI
        UHVProvinceList2 = vic.tOttomanControlII
        UHVProvinceList3 = vic.tOttomanControlIII


    elif (iPlayer == iMoscow):
        UHVProvinceList = vic.tMoscowControl
        UHVProvinceList2 = []
        UHVProvinceList3 = []

    scontrol = 0
    if checkProvincesStates(iPlayer,provinceID):
        bcontrol = True
        scontrol = 100

    if provinceID in UHVProvinceList:
        val = int(1+scontrol)
        tList.append(val)

    if provinceID in UHVProvinceList2:
        val = int(2+scontrol)
        tList.append(val)

    if provinceID in UHVProvinceList3:
        val = int(3+scontrol)
        tList.append(val)

    return tList
    pass

# tList=SearchCore(42,47)

# def squareSearch( self, tTopLeft, tBottomRight, function, argsList ): #by LOQ
#     """Searches all tile in the square from tTopLeft to tBottomRight and calls function for every tile, passing argsList."""
#     tPaintedList = []
#     for tPlot in self.getPlotList(tTopLeft, tBottomRight):
#         bPaintPlot = function(tPlot, argsList)
#         if bPaintPlot:
#             tPaintedList.append(tPlot)
#     return tPaintedList
