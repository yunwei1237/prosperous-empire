###################################################
# header_parties.py
# This file contains declarations for parties
# DO NOT EDIT THIS FILE!
###################################################


from header_common import *

#
#pf_min_strength(x)

pf_icon_mask                 = 0x000000ff
pf_disabled                  = 0x00000100
pf_is_ship                   = 0x00000200
pf_is_static                 = 0x00000400

pf_label_small               = 0x00000000
pf_label_medium              = 0x00001000
pf_label_large               = 0x00002000

pf_always_visible            = 0x00004000
pf_default_behavior          = 0x00010000
pf_auto_remove_in_town       = 0x00020000
pf_quest_party               = 0x00040000
pf_no_label                  = 0x00080000
pf_limit_members             = 0x00100000
pf_hide_defenders            = 0x00200000
pf_show_faction              = 0x00400000
#pf_is_hidden                = 0x01000000 #used in the engine, do not overwrite this flag
pf_dont_attack_civilians     = 0x02000000
pf_civilian                  = 0x04000000


pf_carry_goods_bits    = 48
pf_carry_gold_bits     = 56
pf_carry_gold_multiplier = 20
pf_carry_goods_mask    = 0x00ff000000000000
pf_carry_gold_mask     = 0xff00000000000000

def carries_goods(x):
  return (((bignum | x) << pf_carry_goods_bits) & pf_carry_goods_mask)
def carries_gold(x):
  if (x > 10000): x =10000
  if (x < 0): x = 0
  return ((big_num | (x / pf_carry_gold_multiplier)) << pf_carry_gold_bits) & pf_carry_gold_mask

pmf_is_prisoner = 0x0001

no_faction = -1

## 永远不会移动
ai_bhvr_hold            = 0
## 移动到一个据点或队伍
ai_bhvr_travel_to_party = 1
## 巡逻一个地点
ai_bhvr_patrol_location = 2
## 巡逻一个据点或队伍
ai_bhvr_patrol_party    = 3
## 跟踪一个据点或队伍
ai_bhvr_track_party     = 4 #deprecated, use the alias ai_bhvr_attack_party instead.
## 攻击一个据点或队伍
ai_bhvr_attack_party    = 4
## 逃避一个队伍的攻击
ai_bhvr_avoid_party     = 5
## 移动到一个地点
ai_bhvr_travel_to_point = 6
## 越过一个据点或队伍
ai_bhvr_negotiate_party = 7
## 在城镇中坚守
ai_bhvr_in_town         = 8
## 移动到船上
ai_bhvr_travel_to_ship  = 9
## 护送队伍
ai_bhvr_escort_party    = 10
## 被队伍带领（牛群）
ai_bhvr_driven_by_party = 11

#experience constants
player_loot_share = 10
hero_loot_share = 3


#personality modifiers:
# courage 8 means neutral
courage_4  = 0x0004
courage_5  = 0x0005
courage_6  = 0x0006
courage_7  = 0x0007
courage_8  = 0x0008
courage_9  = 0x0009
courage_10 = 0x000A
courage_11 = 0x000B
courage_12 = 0x000C
courage_13 = 0x000D
courage_14 = 0x000E
courage_15 = 0x000F

aggressiveness_0  = 0x0000
aggressiveness_1  = 0x0010
aggressiveness_2  = 0x0020
aggressiveness_3  = 0x0030
aggressiveness_4  = 0x0040
aggressiveness_5  = 0x0050
aggressiveness_6  = 0x0060
aggressiveness_7  = 0x0070
aggressiveness_8  = 0x0080
aggressiveness_9  = 0x0090
aggressiveness_10 = 0x00A0
aggressiveness_11 = 0x00B0
aggressiveness_12 = 0x00C0
aggressiveness_13 = 0x00D0
aggressiveness_14 = 0x00E0
aggressiveness_15 = 0x00F0

banditness        = 0x0100

soldier_personality = aggressiveness_8 | courage_9
merchant_personality = aggressiveness_0 | courage_7
escorted_merchant_personality = aggressiveness_0 | courage_11
bandit_personality   = aggressiveness_3 | courage_8 | banditness


