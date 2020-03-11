
# -*- coding: utf-8 -*-

from header_common import find_object


# if(find_object("spr","village_fire_big") < 0):
#     raise RuntimeError("aaaaa")


# from process_import_modules import *
# #
# # preprocessString()

# xx = lambda x:x*2
#
# print xx(8)
from header_troops import *
from import_modules import *
from module_troops import *




# def repeatTroop(size,troop):
#     '''
#         将兵种重复多少个
#     :param start: 开始的编号
#     :param end: 结束的编号(不包含)
#     :param troop: 兵种模板
#     :return:
#     '''
#     return repeatTroop(0,size,troop)

# for troop in repeatTroop(12,18,["npc{}","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_boots,itm_knife],
#    str_8|agi_7|int_12|cha_7|level(3),wp(60),knows_tracker_npc|
#    knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
#    0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],):
#     print troop


# troops = repeatTroop(12,18,["npc{}","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_boots,itm_knife],
#    str_8|agi_7|int_12|cha_7|level(3),wp(60),knows_tracker_npc|
#    knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
#    0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],)
#
#
# for i in mergeList([0,1,2,3],[18,22,44],troops):
#     print i



for i in repeatRandomTroop(18):
    print i



