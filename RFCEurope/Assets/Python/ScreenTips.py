## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
from GlobalDefinesAlt import *
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
    lCities.sort(key=lambda x: -x[1])
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
    lCities.sort(key=lambda x: -x[1])
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
    lCities.sort(key=lambda x: -x[1])
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
    lCities.sort(key=lambda x: -x[1])
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
    lCities.sort(key=lambda x: -x[1])
    lCities = lCities
    return lCities


def getTechValue(BuyTechPlayer, tradeitemID, sellTechPlayer=utils.getHumanID()):
    tradetypeID = TRADE_TECHNOLOGIES
    techmoney = gc.getAIdealValuetoMoney(sellTechPlayer, BuyTechPlayer, tradetypeID, tradeitemID)
    return techmoney


def canTradeTech(BuyPlayer, tradeitemID, SellPlayer=utils.getHumanID()):
    team = gc.getTeam(gc.getPlayer(SellPlayer).getTeam())
    if not team.isHasTech(tradeitemID):
        return False

    tradeData = TradeData()
    tradeData.ItemType = TradeableItems.TRADE_TECHNOLOGIES
    tradeData.iData = tradeitemID

    bTechTrade = (gc.getPlayer(SellPlayer).canTradeItem(BuyPlayer, tradeData, False))
    if not bTechTrade:
        return False

    return True


def getScreenHelp():
    aHelp = []

    # 游戏基本信息
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_00 == 1):
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_BASIC", ()))
        iHandicap = gc.getGame().getHandicapType()
        aHelp.append(' Handicap Level (1-3): ' + str(iHandicap + 1))
        iScenario = utils.getScenario()
        txtScenario = ['AD500', 'AD1200']
        aHelp.append(' Scenario : ' + str(txtScenario[iScenario]))

    # 部落村庄信息：
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_11 > 0):

        goody_list = []
        for x in range(gc.getMap().getGridWidth()):
            for y in range(gc.getMap().getGridHeight()):
                plot = gc.getMap().plot(x, y)
                isgoody = plot.isGoody()
                regionid = -1
                if (isgoody):
                    goody_list.append([regionid, x, y])

        if goody_list:
            aHelp.append(' ')
            aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_GOODY", ()))
        goody_list.sort(key=lambda x: x[0])

        for i in range(len(goody_list)):
            regionid = goody_list[i][0]
            x = goody_list[i][1]
            y = goody_list[i][2]
            if regionid >= 0:
                regionname = ' '
                aHelp.append('Goody [' + str(i) + '] in X:' + str(x) + '  Y: ' + str(y) + ' RegionName: ' + regionname)
            else:
                aHelp.append('Goody in X:' + str(x) + '  Y: ' + str(y))

    # 2.十字军进度
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_02 == 1):
        aHelp.append(' ')
        aHelp.append('十字军进度提醒：')
        crusade_turn_list = [xml.i1096AD - 5, xml.i1147AD - 7, xml.i1187AD - 8, xml.i1202AD - 4, xml.i1229AD - 3, xml.i1271AD - 5]
        crusade_name = ['第一次十字军东征(AD1096) ',
                        '第二次十字军东征(AD1147) ',
                        '第三次十字军东征(AD1187) ',
                        '第四次十字军东征(AD1202) ',
                        '第五次十字军东征(AD1229) ',
                        '第六次十字军东征(AD1271) ',
                        ]
        for i in range(len(crusade_turn_list)):
            crusade_turn = crusade_turn_list[i]
            iGameTurn = max(crusade_turn - gc.getGame().getGameTurn(), -1)
            txt = crusade_name[i] + '开始于回合: ' + str(crusade_turn) + '   剩余回合:  ' + str(iGameTurn)
            aHelp.append(txt)

    # 3.瘟疫进度
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_03 == 1):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_PLAGUE", ()))
        from StoredData import sd

        for i in range(5):
            plague_turn = sd.scriptDict['lGenericPlagueDates'][i]
            iGameTurn = max(plague_turn - gc.getGame().getGameTurn(), 0)
            aHelp.append('瘟疫   ' + str(i + 1) + ' ' + global_plaguenamelist[i] + '      开始于回合: ' + str(plague_turn) + '   剩余回合:  ' + str(iGameTurn))

    # 勒索国家金币的信息
    if (PYTHON_SCREEN_VICTORY_TIPS_12):
        aHelp.append(' ')
        aHelp.append('可勒索金币数量排名')
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive()):
                iPlayer = iCiv
                human = utils.getHumanID()
                cantrade = gc.getPlayer(iPlayer).canTradeNetworkWith(human)
                a = gc.AI_considerOfferThreshold(human, iPlayer)  # 3是中国
                b = gc.getPlayer(iPlayer).AI_maxGoldTrade(human)
                c = min(a, b)
                if cantrade and c > 0:
                    civname = gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                    aHelp.append(civname + ':' + str(c))

        pass

    # 科技交易信息
    if (PYTHON_SCREEN_VICTORY_TIPS_13):
        aHelp.append(' ')
        aHelp.append('AI可卖科技列表：')
        for iCiv in range(iNumPlayers):
            iPlayer = iCiv
            human = utils.getHumanID()
            if (gc.getPlayer(iCiv).isAlive() and iCiv is not human):
                for iTech in range(xml.iNumTechs):
                    cantrade = gc.getPlayer(iPlayer).canTradeNetworkWith(human)
                    buyplayer = human
                    sellplayer = iPlayer
                    AIhastech = gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isHasTech(iTech)
                    Humanhastech = gc.getTeam(gc.getPlayer(human).getTeam()).isHasTech(iTech)
                    if (AIhastech and not Humanhastech):
                        techvalue = getTechValue(buyplayer, iTech, sellplayer)
                        if techvalue > 0:
                            civname = gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                            techname = utils.getTechNameCn(iTech)
                            cantradetext = ''
                            bcantradetech = canTradeTech(buyplayer, iTech, sellplayer)
                            if (not cantrade or not bcantradetech):
                                cantradetext = '[目前无法交易]'
                            aHelp.append(civname + ':     ' + techname + '(' + str(techvalue) + ')' + cantradetext)

        aHelp.append(' ')
        aHelp.append('人类可卖科技列表：')
        for iCiv in range(iNumPlayers):
            iPlayer = iCiv
            human = utils.getHumanID()
            if (gc.getPlayer(iCiv).isAlive() and iCiv is not human):
                for iTech in range(xml.iNumTechs):
                    cantrade = gc.getPlayer(iPlayer).canTradeNetworkWith(human)
                    buyplayer = iPlayer
                    sellplayer = human
                    AIhastech = gc.getTeam(gc.getPlayer(iPlayer).getTeam()).isHasTech(iTech)
                    Humanhastech = gc.getTeam(gc.getPlayer(human).getTeam()).isHasTech(iTech)
                    if (not AIhastech and Humanhastech):
                        techvalue = getTechValue(buyplayer, iTech, sellplayer)
                        if techvalue > 0:
                            civname = gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                            techname = utils.getTechNameCn(iTech)
                            cantradetext = ''
                            bcantradetech = canTradeTech(buyplayer, iTech, sellplayer)

                            bTradeWorth = False
                            iAImaxMoney = gc.getPlayer(buyplayer).AI_maxGoldTrade(utils.getHumanID())
                            iMinPercent = PYTHON_TECHTRADE_VALUE_MIN_PERCENT
                            iThreshold = techvalue * iMinPercent / 100
                            if (iAImaxMoney >= iThreshold):
                                bTradeWorth = True

                            if (not cantrade or not bcantradetech or not bTradeWorth):
                                cantradetext = '[目前无法交易]'
                                # aHelp.append(civname + ':     ' + techname + '(' + str(techvalue) + ')' + cantradetext)
                            else:
                                txt = '%s:    %s  :  %d (%d' % (civname, techname, techvalue, iAImaxMoney * 100 / techvalue) + '%)'
                                aHelp.append(txt)
                                # aHelp.append(civname + ':     ' + techname+'('+str(techvalue)+')' + cantradetext)

        pass

    # 4.金币信息
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_04 > 0):
        aHelp.append(' ')
        techlist = []
        valuelist = []
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive()):
                iGold = gc.getPlayer(iCiv).getGold()
                iGoldPerTurn = gc.getPlayer(iCiv).AI_maxGoldPerTurnTrade(gc.getGame().getActivePlayer())
                # iTechValue = gc.getPlayer(iCiv).getEconomyHistory(gc.getGame().getGameTurn()-1)
                iTechValue = iGold + iGoldPerTurn * 10
                valuelist.append(iTechValue)
                techlist.append([iCiv, iTechValue])
            pass
        AveragePoint = 1
        if (len(valuelist) > 0 and sum(valuelist) > 0):
            AveragePoint = sum(valuelist) / len(valuelist)
        aHelp.append('全球国库排名')

        techlist.sort(key=lambda x: -x[1])
        for i in range(len(techlist)):
            if (i < xml.PYTHON_SCREEN_VICTORY_TIPS_04):
                iCiv = techlist[i][0]
                iTechValue = techlist[i][1]
                civname = gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                if (isDecline(iCiv)):
                    civname = civname + '[F]'

                rank_percent = iTechValue * 100 / AveragePoint

                iGold = gc.getPlayer(iCiv).getGold()
                iGoldPerTurn = gc.getPlayer(iCiv).AI_maxGoldPerTurnTrade(gc.getGame().getActivePlayer())
                txt2 = str(iGold) + '(' + str(iGoldPerTurn) + ')'

                txt = ' RANK (' + str(i + 1) + ') : ' + civname + '             ' + str(txt2) + '  (' + str(rank_percent) + '%)' + '              '
                aHelp.append(txt)

    # 5.军事实力
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_05 > 0):
        aHelp.append(' ')
        techlist = []
        valuelist = []
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive()):
                iTechValue = gc.getPlayer(iCiv).getPowerHistory(gc.getGame().getGameTurn() - 1)
                valuelist.append(iTechValue)
                techlist.append([iCiv, iTechValue])
            pass
        AveragePoint = 1
        if (len(valuelist) > 0 and sum(valuelist) > 0):
            AveragePoint = sum(valuelist) / len(valuelist)
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_ARMYRANK", ()))

        techlist.sort(key=lambda x: -x[1])
        for i in range(len(techlist)):
            if (i < xml.PYTHON_SCREEN_VICTORY_TIPS_05):
                iCiv = techlist[i][0]
                iTechValue = techlist[i][1]
                civname = gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                if (isDecline(iCiv)):
                    civname = civname + '[F]'

                rank_percent = iTechValue * 100 / AveragePoint
                aHelp.append(' RANK (' + str(i + 1) + ') : ' + civname + '             with ' + str(iTechValue) + '  (' + str(rank_percent) + '%)')

    # 5.文化实力
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_05 > 0):
        aHelp.append(' ')
        techlist = []
        valuelist = []
        for iCiv in range(iNumPlayers):
            if (gc.getPlayer(iCiv).isAlive()):
                iTechValue = gc.getPlayer(iCiv).getCultureHistory(gc.getGame().getGameTurn() - 1)
                valuelist.append(iTechValue)
                techlist.append([iCiv, iTechValue])
            pass
        AveragePoint = 1
        if (len(valuelist) > 0 and sum(valuelist) > 0):
            AveragePoint = sum(valuelist) / len(valuelist)
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CULTURERANK", ()))

        techlist.sort(key=lambda x: -x[1])
        for i in range(len(techlist)):
            if (i < xml.PYTHON_SCREEN_VICTORY_TIPS_05):
                iCiv = techlist[i][0]
                iTechValue = techlist[i][1]
                civname = gc.getPlayer(iCiv).getCivilizationShortDescription(0)
                if (isDecline(iCiv)):
                    civname = civname + '[F]'

                rank_percent = iTechValue * 100 / AveragePoint
                aHelp.append(' RANK (' + str(i + 1) + ') : ' + civname + '             with ' + str(iTechValue) + '  (' + str(rank_percent) + '%)')

    # 6 世界最大城市排名
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_06 > 0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_POP", ()))
        lCities = calculateTopCities_population()
        i_num_city = 0
        for iCity in lCities:
            if (i_num_city < xml.PYTHON_SCREEN_VICTORY_TIPS_06):
                i_num_city += 1
                civname = iCity[0].getName() + '  [' + str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0)) + ']'
                iValue = iCity[1]
                rank_percent = 100
                aHelp.append(' RANK (' + str(i_num_city) + ') : ' + civname + '             with ' + str(iValue) + ' ')
        pass

    # 7.世界文化最高城市排名
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_07 > 0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_CUL", ()))
        lCities = calculateTopCities_culture()
        i_num_city = 0
        for iCity in lCities:
            if (i_num_city < xml.PYTHON_SCREEN_VICTORY_TIPS_07):
                i_num_city += 1
                civname = iCity[0].getName() + '  [' + str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0)) + ']'
                iValue = iCity[1]
                rank_percent = 100
                aHelp.append(' RANK (' + str(i_num_city) + ') : ' + civname + '             with ' + str(iValue) + ' ')
        pass

    # 8.世界工业产量最高城市排名
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_08 > 0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_PRO", ()))
        lCities = calculateTopCities_production()
        i_num_city = 0
        for iCity in lCities:
            if (i_num_city < xml.PYTHON_SCREEN_VICTORY_TIPS_08):
                i_num_city += 1
                civname = iCity[0].getName() + '  [' + str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0)) + ']'
                iValue = iCity[1]
                rank_percent = 100
                aHelp.append(' RANK (' + str(i_num_city) + ') : ' + civname + '             with ' + str(iValue) + ' ')
        pass

    # 9.世界商业产出最高城市排名
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_09 > 0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_COM", ()))
        lCities = calculateTopCities_COMMERCE()
        i_num_city = 0
        for iCity in lCities:
            if (i_num_city < xml.PYTHON_SCREEN_VICTORY_TIPS_09):
                i_num_city += 1
                civname = iCity[0].getName() + '  [' + str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0)) + ']'
                iValue = iCity[1]
                rank_percent = 100
                aHelp.append(' RANK (' + str(i_num_city) + ') : ' + civname + '             with ' + str(iValue) + ' ')
        pass

    # 10.世界食物产出最高城市排名
    if (xml.PYTHON_SCREEN_VICTORY_TIPS_10 > 0):
        aHelp.append(' ')
        aHelp.append(localText.getText("TXT_KEY_VICTORY_TIPS_IN_SCREEN_CITY_RANK_FOOD", ()))
        lCities = calculateTopCities_FOOD()
        i_num_city = 0
        for iCity in lCities:
            if (i_num_city < xml.PYTHON_SCREEN_VICTORY_TIPS_10):
                i_num_city += 1
                civname = iCity[0].getName() + '  [' + str(gc.getPlayer(iCity[0].getOwner()).getCivilizationShortDescription(0)) + ']'
                iValue = iCity[1]
                rank_percent = 100
                aHelp.append(' RANK (' + str(i_num_city) + ') : ' + civname + '             with ' + str(iValue) + ' ')
        pass

    return aHelp
