from Mediv01_Utils import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

########################################## <!-- 科研惩罚相关 -->######################################################

# <!--mediv01 新增，科技领先时的科研惩罚最大比例，数值为1-9，科研惩罚为25%-1000%，数字越大领先时科研惩罚越大 9为默认模式（科研惩罚最高1000%）-->
PY_BALANCE_MAX_RESERACH_PUNISH = 1

# <!--mediv01 新增，科技落后时的科研提升最大比例，数值为25-100，数字越小落后时科研提升越大 50为默认模式-->
PY_BALANCE_MAX_RESERACH_BONUS = 25



########################################## <!-- 瘟疫相关 -->######################################################

# <!--mediv01 新增，瘟疫能否杀死军队 1为瘟疫能杀死军队  1为默认模式  -->
PY_PLAGUE_KILL_PEOPLE = 1

# <!--mediv01 新增，1为人类玩家不会触发瘟疫  0为默认模式-->
PY_PLAGUE_HUMAN_NO_INFECT = 1

# <!--mediv01 新增，1为教皇国不会成为瘟疫起点，可以有助于瘟疫快速扩散  0为默认模式-->
PY_PLAGUE_POPE_NO_INFECT = 1




########################################## <!-- 兴衰相关 -->######################################################
# <!--mediv01 新增，玩家的城市不会被新出生的文明翻转  0为可以被翻转  0为默认模式-->
PY_HUMAN_CANNOT_BE_FLIP = 1

# <!--mediv01 新增，新出生的文明能否在翻转区内能否翻转军队 1为可以翻转  1为默认模式-->
PY_UNIT_CAN_BE_FLIP = 0

# <!--mediv01 新增，人类控制的文明，在稳定度较低时，不会被文明复活影响  0为默认模式-->
PY_RISEANDFALL_HUMAN_NO_REBEL = 1

# <!--mediv01 新增，人类控制的文明，在独立城邦检查时，不会被独立城邦反抗  0为默认模式-->
PY_BARBS_HUMAN_NO_REBEL = 1

# <!--mediv01 新增，东正教也可以出发宗教改革  0为默认模式-->
PY_Orthodoxy_CAN_TRIGGLER_REFORM = 0




########################################## <!-- 十字军相关 -->######################################################


# <!--mediv01 新增，人类玩家军队参加十字军后，原有单位不会消失  0为默认模式-->
PY_CRUSADES_HUMAN_UNIT_NOT_LEAVE = 1

# <!--mediv01 新增，人类玩家军队参加十字军后，参战单位不会返回  0为默认模式-->
PY_CRUSADES_HUMAN_UNIT_NOT_RETURN = 1

# <!--mediv01 新增，人类玩家总是十字军的领袖 0为默认模式-->
PY_CRUSADES_HUMAN_ALWAYS_LEADER= 1


# <!--mediv01 新增，统计天主教最富裕的文明排除教皇国 0为默认模式-->
PY_CRUSADES_RICHEST_CIV_NOT_INCLUDE_POPE = 1


# <!--mediv01 新增，人类玩家总是可以贿赂十字军 0为默认模式-->
PY_CRUSADES_HUMAN_ALWAYS_BRIBE_CRUSADE= 1


########################################## <!-- 稳定度相关 -->######################################################

# <!--mediv01 新增，人类玩家不会崩溃 0为默认模式-->
PY_STABILITY_HUMAN_NO_COLLAPSE = 1

# <!--mediv01 新增，允许自定义核心地块、历史地块对所有玩家的稳定度加成  0为默认模式-->
PY_tStabilityPenalty_ENABLE = 1
# province type: unstable, border, potential, historic, core    默认是 ( -5, -2, 0, 0, 0 )
PY_tStabilityPenalty = (-2, -1, 0, 1, 2)
#PY_tStabilityPenalty = (2, 1, 0, 1, 2)


# <!--mediv01 新增，一档难度对人类玩家稳定度的加成 6为默认模式-->  #mediv01 曾经是6
PY_STABILITY_BONOUS_FOR_H1 = 60

# <!--mediv01 新增，二档难度对人类玩家稳定度的加成 2为默认模式-->  #mediv01 曾经是2
PY_STABILITY_BONOUS_FOR_H2 = 2

# <!--mediv01 新增，不允许弹出城市建议弹窗   0为默认模式-->  #mediv01 曾经是2
PY_DONNOT_USE_CITY_ADVICE = 1


########################################## <!-- ScreenTip提示系统相关 -->######################################################


# <!-- 1为显示高级信息提示系统的总开关      0为默认模式 mediv01 -->
PYTHON_SCREEN_VICTORY_TIPS = 1

# <!-- 1为显示基本信息提示      0为默认模式 mediv01 -->
PYTHON_SCREEN_VICTORY_TIPS_00 = 1

# <!-- 1为显示部落村庄信息     0为默认模式 mediv01 -->
PYTHON_SCREEN_VICTORY_TIPS_11 = 1

# <!-- 1为显示十字军提醒信息     0为默认模式 mediv01 -->
PYTHON_SCREEN_VICTORY_TIPS_02 = 1

# <!-- 1为显示可以勒索国家的提醒   0为默认模式 mediv01 -->
PYTHON_SCREEN_VICTORY_TIPS_12 = 1

# 可以交易科技的提醒
PYTHON_SCREEN_VICTORY_TIPS_13 = 1

# 瘟疫提醒提醒
PYTHON_SCREEN_VICTORY_TIPS_03 = 1

# 科技排名信息提醒
PYTHON_SCREEN_VICTORY_TIPS_04 = 10

# 军事实力排名提醒
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



########################################## <!-- 日志系统相关 -->######################################################



# <!-- 1为打开日志功能 此选项为日志功能的总开关   0为默认模式 mediv01 -->
PYTHON_USE_LOG = 1

# <!-- 1为记录INFO的日志 0为默认模式 mediv01 -->
PYTHON_LOG_ON_INFO = 1

# <!-- 1为记录野蛮人入侵的日志 0为默认模式 mediv01 -->
PYTHON_LOG_ON_BARB = 1

# <!-- 1为记录独立城邦的日志 0为默认模式 mediv01 -->
PYTHON_LOG_ON_INDEPENDENT = 1

# <!-- 1为记录国家诞生灭亡的日志 0为默认模式 mediv01 -->
PYTHON_LOG_ON_RISK_AND_FALL = 1

# <!-- 1为记录瘟疫传播的日志 0为默认模式 mediv01 -->
PYTHON_LOG_ON_PLAGUE = 1

# <!-- 1为记录奇观建成日志 0为默认模式 mediv01 -->
PYTHON_LOG_ON_WONDER = 1

# <!-- 1为记录十字军相关信息日志 0为默认模式 mediv01 -->
PYTHON_LOG_ON_CRUSADE = 1

########################################## <!-- 积分榜系统相关 -->######################################################


# 积分榜上显示独立城邦
PYTHON_SHOW_MINOR_CITY_ON_SCREEN = 1


# 积分榜上显示的国名更具体
PYTHON_SCRREN_SHOW_CIVNAME_WITH_FIXNAME = 1

# 积分榜上显示玩家的金币数和回合金
PYTHON_SHOW_CIV_MONEY_ON_PANNEL = 1


# 积分榜上超过多少金币就会高亮显示
PYTHON_SHOW_CIV_MONEY_HIGHLIGHT_LEVEL1 = 500
PYTHON_SHOW_CIV_MONEY_HIGHLIGHT_LEVEL2 = 1000


# 积分榜上超过多少回合金就会高亮显示
PYTHON_SHOW_CIV_MONEY_PERTURN_HIGHLIGHT_LEVEL1 = 5
PYTHON_SHOW_CIV_MONEY_PERTURN_HIGHLIGHT_LEVEL2 = 10


# 积分榜上可以永远看到其他玩家的科研进度
PYTHON_CAN_SEE_OTHER_PLAYER_TECH_INFO = 1

# 开启积分榜科技交易提示功能
PYTHON_CAN_USE_TECHTRADE_VALUE_ALERT = 1

#   <!--  大于0的数字为显示可交易科技最低价值的阈值，95代表95%，0为默认模式  mediv01 2021年8月版本 -->
PYTHON_TECHTRADE_VALUE_MIN_PERCENT = 80


