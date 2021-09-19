
from Consts import *
from Barbs import *

localText = CyTranslator()
def SearchCore(x,y):
    tList = []
    for i in range(len(tCoreAreasTL)):
        tfind=0
        x1=tCoreAreasTL[i][0]
        y1=tCoreAreasTL[i][1]
        x2=tCoreAreasBR[i][0]
        y2=tCoreAreasBR[i][1]
        if ((x>=x1 and x<=x2) and (y>=y1 and y<=y2)):
            tList.append(i)
            tfind=1
        if (tfind==0):
            if ((x,y) in lExtraPlots[i]):
                tList.append(i)
            pass
            
    return tList
        #print(x1,y1)
    pass



def SearchMinorCityBirth(x,y):
    tList=[]
    iGameTurnList=list(dIndependentCities.keys())
    for iGameTurn in iGameTurnList:
        for tCity in dIndependentCities[iGameTurn]:
            lVariations, iCiv, iPop, iUnit, iNumUnits, iReligion, iWorkers = tCity
            for iCity in range(len(lVariations)):
                iChosenCity = iCity
                tCoords, sName, iPos = lVariations[iChosenCity]
                if tCoords[0]==x and tCoords[1]==y:
                    tList.append(iGameTurn)

    return tList

    pass

#tList=SearchCore(42,47)

# def squareSearch( self, tTopLeft, tBottomRight, function, argsList ): #by LOQ
#     """Searches all tile in the square from tTopLeft to tBottomRight and calls function for every tile, passing argsList."""
#     tPaintedList = []
#     for tPlot in self.getPlotList(tTopLeft, tBottomRight):
#         bPaintPlot = function(tPlot, argsList)
#         if bPaintPlot:
#             tPaintedList.append(tPlot)
#     return tPaintedList