import sys

reload(sys)
sys.setdefaultencoding('utf-8')


PY_BALANCE_MAX_RESERACH_PUNISH=1        #<!--mediv01 新增，科技领先时的科研惩罚最大比例，数值为1-9，数字越大领先时科研惩罚越大 9为默认模式-->
PY_BALANCE_MAX_RESERACH_BONUS=25        #<!--mediv01 新增，科技落后时的科研提升最大比例，数值为25-100，数字越小落后时科研提升越大 50为默认模式-->


PY_PLAGUE_KILL_PEOPLE=0                 #<!--mediv01 新增，瘟疫能否杀死军队  1为默认模式-->
PY_PLAGUE_HUMAN_NO_INFECT=1             #<!--mediv01 新增，人类玩家不会触发瘟疫  0为默认模式-->
PY_PLAGUE_POPE_NO_INFECT=1             #<!--mediv01 新增，教皇国不会成为瘟疫起点，可以有助于瘟疫快速扩散  0为默认模式-->


PY_UNIT_CAN_BE_FLIP=0                   #<!--mediv01 新增，能否翻转军队  1为默认模式-->
PY_RISEANDFALL_HUMAN_NO_REBEL=0         #<!--mediv01 新增，人类控制的文明不会有文明复活  0为默认模式-->


PY_Orthodoxy_CAN_TRIGGLER_REFORM=0      #<!--mediv01 新增，东正教也可以出发宗教改革  0为默认模式-->




PY_STABILITY_HUMAN_NO_COLLAPSE=0        #<!--mediv01 新增，人类玩家不会崩溃 0为默认模式-->
PY_tStabilityPenalty_ENABLE=1             #<!--mediv01 新增，允许自定义核心地块、历史地块对所有玩家的稳定度加成  0为默认模式-->
PY_tStabilityPenalty = ( -2, -1, 0, 1, 2 )     # province type: unstable, border, potential, historic, core    默认是 ( -5, -2, 0, 0, 0 )


PY_STABILITY_BONOUS_FOR_H1 = 60   #<!--mediv01 新增，一档难度对人类玩家稳定度的加成 6为默认模式-->  #mediv01 曾经是6
PY_STABILITY_BONOUS_FOR_H2 = 2   #<!--mediv01 新增，一档难度对人类玩家稳定度的加成 2为默认模式-->  #mediv01 曾经是2


# 开启信息提示系统
PYTHON_SCREEN_VICTORY_TIPS = 1

# 基本信息提示
PYTHON_SCREEN_VICTORY_TIPS_00 = 1

# 部落村庄信息
PYTHON_SCREEN_VICTORY_TIPS_11 = 1

# 科技信息
PYTHON_SCREEN_VICTORY_TIPS_04 = 1

# 军事实力
PYTHON_SCREEN_VICTORY_TIPS_05 = 10

# 6 世界最大城市排名
PYTHON_SCREEN_VICTORY_TIPS_06 = 10

# 7.世界文化最高城市排名
PYTHON_SCREEN_VICTORY_TIPS_07 = 10

# 8.世界工业产量最高城市排名
PYTHON_SCREEN_VICTORY_TIPS_08 = 10

# 9.世界商业产出最高城市排名
PYTHON_SCREEN_VICTORY_TIPS_09 = 10

# 10.世界食物产出最高城市排名
PYTHON_SCREEN_VICTORY_TIPS_10 = 10



PYTHON_USE_LOG = 1





































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