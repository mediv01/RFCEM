## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
from CvPythonExtensions import *
import CvUtil
import ScreenInput
import PyHelpers
import time
import Consts as con
import XMLConsts as xml
import RFCUtils
import Victory as vic
import UniquePowers

PyPlayer = PyHelpers.PyPlayer

iNumPlayers = con.iNumPlayers

# globals

up = UniquePowers.UniquePowers()
utils = RFCUtils.RFCUtils()
gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

def isDecline(iPlayer):
    return utils.getHumanID() != iPlayer and gc.getGame().getGameTurn() >= con.tCollapse[iPlayer]

def calculateTopCities_population():
    lCities = []
    for iLoopPlayer in range(iNumPlayers):
        for city in utils.getCityList(iLoopPlayer):
            if (1 == 1):
                iValue = city.getPopulation()
            else:
                iValue = ((city.getCulture(iLoopPlayer) / 5) + (city.getYieldRate(YieldTypes.YIELD_FOOD) + city.getYieldRate(YieldTypes.YIELD_PRODUCTION) \
                                                                + city.getYieldRate(YieldTypes.YIELD_COMMERCE))) * city.getPopulation()
            lCities.append((city, iValue))
    lCities.sort(key=lambda x:-x[1])
    lCities = lCities
    return lCities

def calculateTopCities_culture():
    lCities = []
    for iLoopPlayer in range(iNumPlayers):
        for city in utils.getCityList(iLoopPlayer):
            if (1 == 1):
                iValue = city.getCulture(iLoopPlayer)
            else:
                iValue = ((city.getCulture(iLoopPlayer) / 5) + (city.getYieldRate(YieldTypes.YIELD_FOOD) + city.getYieldRate(YieldTypes.YIELD_PRODUCTION) \
                                                                + city.getYieldRate(YieldTypes.YIELD_COMMERCE))) * city.getPopulation()
            lCities.append((city, iValue))
    lCities.sort(key=lambda x:-x[1])
    lCities = lCities
    return lCities

def calculateTopCities_production():
    lCities = []
    for iLoopPlayer in range(iNumPlayers):
        for city in utils.getCityList(iLoopPlayer):
            if (1 == 1):
                iValue = city.getYieldRate(YieldTypes.YIELD_PRODUCTION)
            else:
                iValue = ((city.getCulture(iLoopPlayer) / 5) + (city.getYieldRate(YieldTypes.YIELD_FOOD) + city.getYieldRate(YieldTypes.YIELD_PRODUCTION) \
                                                                + city.getYieldRate(YieldTypes.YIELD_COMMERCE))) * city.getPopulation()
            lCities.append((city, iValue))
    lCities.sort(key=lambda x:-x[1])
    lCities = lCities
    return lCities


def calculateTopCities_COMMERCE():
    lCities = []
    for iLoopPlayer in range(iNumPlayers):
        for city in utils.getCityList(iLoopPlayer):
            if (1 == 1):
                iValue = city.getYieldRate(YieldTypes.YIELD_COMMERCE)
            else:
                iValue = ((city.getCulture(iLoopPlayer) / 5) + (city.getYieldRate(YieldTypes.YIELD_FOOD) + city.getYieldRate(YieldTypes.YIELD_PRODUCTION) \
                                                                + city.getYieldRate(YieldTypes.YIELD_COMMERCE))) * city.getPopulation()
            lCities.append((city, iValue))
    lCities.sort(key=lambda x:-x[1])
    lCities = lCities
    return lCities


def calculateTopCities_FOOD():
    lCities = []
    for iLoopPlayer in range(iNumPlayers):
        for city in utils.getCityList(iLoopPlayer):
            if (1 == 1):
                iValue = city.getYieldRate(YieldTypes.YIELD_FOOD)
            else:
                iValue = ((city.getCulture(iLoopPlayer) / 5) + (city.getYieldRate(YieldTypes.YIELD_FOOD) + city.getYieldRate(YieldTypes.YIELD_PRODUCTION) \
                                                                + city.getYieldRate(YieldTypes.YIELD_COMMERCE))) * city.getPopulation()
            lCities.append((city, iValue))
    lCities.sort(key=lambda x:-x[1])
    lCities = lCities
    return lCities


def getScreenHelp():
    aHelp = []


    #游戏基本信息
    if(xml.PYTHON_SCREEN_VICTORY_TIPS_00 == 1):
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_BASIC", ()))
        iHandicap = gc.getGame().getHandicapType()
        aHelp.append(' Handicap Level (1-3): '+str(iHandicap+1))
        iScenario=utils.getScenario()
        txtScenario=['AD500', 'AD1200']
        aHelp.append(' Scenario : ' + str(txtScenario[iScenario]))


    #部落村庄信息：
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_11> 0):

        goody_list=[]
        for x in range(gc.getMap().getGridWidth()):
            for y in range(gc.getMap().getGridHeight()):
                plot = gc.getMap().plot(x, y)
                isgoody=plot.isGoody()
                regionid = -1
                if(isgoody):
                    goody_list.append([regionid,x,y])

        if goody_list:
            aHelp.append(' ')
            aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_GOODY", ()))
        goody_list.sort(key=lambda x:x[0])


        for i in range(len(goody_list)):
            regionid=goody_list[i][0]
            x=goody_list[i][1]
            y = goody_list[i][2]
            if regionid >= 0:
                regionname = ' '
                aHelp.append('Goody ['+str(i)+'] in X:' + str(x) + '  Y: ' + str(y) + ' RegionName: ' + regionname)
            else:
                aHelp.append('Goody in X:' + str(x) + '  Y: ' + str(y))


    # 5.军事实力
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_05 >0):
        aHelp.append(' ')
        techlist=[]
        valuelist=[]
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive()):
                iTechValue = gc.getPlayer(iCiv).getPowerHistory(gc.getGame().getGameTurn()-1)
                valuelist.append(iTechValue)
                techlist.append([iCiv,iTechValue])
            pass
        AveragePoint=1
        if(len(valuelist)>0 and sum(valuelist)>0):
            AveragePoint=sum(valuelist)/len(valuelist)
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_ARMYRANK", ()))


        techlist.sort(key=lambda x:-x[1])
        for i in range(len(techlist)):
            if (i < xml.PYTHON_SCREEN_VICTORY_TIPS_05 ):
                iCiv = techlist[i][0]
                iTechValue=techlist[i][1]
                civname=gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                if (isDecline(iCiv)):
                    civname=civname+'[F]'

                rank_percent=iTechValue*100/AveragePoint
                aHelp.append(' RANK ('+str(i+1)+') : '+civname+'             with '+str(iTechValue)+'  ('+str(rank_percent)+'%)')


    # 5.文化实力
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_05 >0):
        aHelp.append(' ')
        techlist=[]
        valuelist=[]
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive()):
                iTechValue = gc.getPlayer(iCiv).getCultureHistory(gc.getGame().getGameTurn()-1)
                valuelist.append(iTechValue)
                techlist.append([iCiv,iTechValue])
            pass
        AveragePoint=1
        if(len(valuelist)>0 and sum(valuelist)>0):
            AveragePoint=sum(valuelist)/len(valuelist)
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CULTURERANK", ()))


        techlist.sort(key=lambda x:-x[1])
        for i in range(len(techlist)):
            if (i < xml.PYTHON_SCREEN_VICTORY_TIPS_05):
                iCiv = techlist[i][0]
                iTechValue=techlist[i][1]
                civname=gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                if (isDecline(iCiv)):
                    civname=civname+'[F]'

                rank_percent=iTechValue*100/AveragePoint
                aHelp.append(' RANK ('+str(i+1)+') : '+civname+'             with '+str(iTechValue)+'  ('+str(rank_percent)+'%)')


    #6 世界最大城市排名
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_06>0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_POP", ()))
        lCities=calculateTopCities_population()
        i_num_city=0
        for iCity in lCities:
            if (i_num_city<xml.PYTHON_SCREEN_VICTORY_TIPS_06):
                i_num_city+=1
                civname=iCity[0].getName()+'  ['+str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0))+']'
                iValue=iCity[1]
                rank_percent=100
                aHelp.append(' RANK ('+str(i_num_city)+') : '+civname+'             with '+str(iValue)+' ')
        pass


    #7.世界文化最高城市排名
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_07>0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_CUL", ()))
        lCities=calculateTopCities_culture()
        i_num_city=0
        for iCity in lCities:
            if (i_num_city<xml.PYTHON_SCREEN_VICTORY_TIPS_07):
                i_num_city+=1
                civname=iCity[0].getName()+'  ['+str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0))+']'
                iValue=iCity[1]
                rank_percent=100
                aHelp.append(' RANK ('+str(i_num_city)+') : '+civname+'             with '+str(iValue)+' ')
        pass

    #8.世界工业产量最高城市排名
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_08 >0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_PRO", ()))
        lCities=calculateTopCities_production()
        i_num_city=0
        for iCity in lCities:
            if (i_num_city<xml.PYTHON_SCREEN_VICTORY_TIPS_08):
                i_num_city+=1
                civname=iCity[0].getName()+'  ['+str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0))+']'
                iValue=iCity[1]
                rank_percent=100
                aHelp.append(' RANK ('+str(i_num_city)+') : '+civname+'             with '+str(iValue)+' ')
        pass

    #9.世界商业产出最高城市排名
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_09 >0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_COM", ()))
        lCities=calculateTopCities_COMMERCE()
        i_num_city=0
        for iCity in lCities:
            if (i_num_city<xml.PYTHON_SCREEN_VICTORY_TIPS_09):
                i_num_city+=1
                civname=iCity[0].getName()+'  ['+str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0))+']'
                iValue=iCity[1]
                rank_percent=100
                aHelp.append(' RANK ('+str(i_num_city)+') : '+civname+'             with '+str(iValue)+' ')
        pass

    #10.世界食物产出最高城市排名
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_10 >0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_FOOD", ()))
        lCities=calculateTopCities_FOOD()
        i_num_city=0
        for iCity in lCities:
            if (i_num_city<xml.PYTHON_SCREEN_VICTORY_TIPS_10):
                i_num_city+=1
                civname=iCity[0].getName()+'  ['+str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0))+']'
                iValue=iCity[1]
                rank_percent=100
                aHelp.append(' RANK ('+str(i_num_city)+') : '+civname+'             with '+str(iValue)+' ')
        pass

    utils.logwithid(1,'1234')











    return aHelp