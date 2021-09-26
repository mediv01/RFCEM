from CvPythonExtensions import *


gc = CyGlobalContext()
localText = CyTranslator()

def getTurn():
    return gc.getGame().getGameTurn()


def getYear():
    return gc.getGame().getGameTurnYear()


def getTurnForYear(iGameturn):
    return gc.getGame().getTurnYear(iGameturn)


def PlotToStr(tPlot):
    return '(' + str(tPlot[0]) + ', ' + str(tPlot[1]) + ')'

'''
# 会报错 MAP感觉有些问题
def getProvinceName11111(iProvinceIdOrPlot):
    import RFCEMapUtil
    provinceMapDefault = -1
    if (isinstance(iProvinceIdOrPlot, CyPlot)):
        iProvince = RFCEMapUtil.RFCEMapManager().getProvinceId(iProvinceIdOrPlot)
    else:
        iProvince = iProvinceIdOrPlot
    if (iProvince != provinceMapDefault):
        return localText.getText(("TXT_KEY_PROVINCE_NAME_%i" % iProvince), ())
    return ""

def GetProvinceName11111(tPlot):
    import RFCEMapUtil
    txt = ''
    if getTurn()>=1:
        iProvince = RFCEMapUtil.RFCEMapManager().getProvinceId(tPlot)
        txt =localText.getText( ("TXT_KEY_PROVINCE_NAME_%i" %iProvince),())
    return txt

    # return RFCEMapUtil.RFCEMapManager().getProvinceName(tPlot)

'''

global_plaguenamelist = [
    '查士丁尼大瘟疫',
    '黑死病第一次大流行',
    '黑死病第二次大流行',
    '伦敦大瘟疫',
    '马赛大瘟疫',
]



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
