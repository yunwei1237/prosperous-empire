# -*- coding: utf-8 -*-
from module_game_menus import game_menus
from module_scripts import *

'''

    据点税收增强，
    原游戏中，税收太少，导致军队士兵一直都很孱弱，没有办法和玩家进行交战，以至于玩家50个士兵可以对战200个领主士兵，
    主要原因是领主没有钱进行军队的升级和维护
    
    对于玩家来说，租金太少，没有办法对建筑进行升级和维护军队
'''

## 每天更新（24）
center_tax_inscrease_interval = 24

## 最终 = 200 * 7（1400） + 1000（最大税收）
village_rent_increase_per_day = 200
## 最终 = 400 * 7（2800） + 2000（最大税收）
castle_rent_increase_per_day = 400
## 最终 = 800 * 7（5600） + 2000（最大税收）
town_rent_increase_per_day = 800


villageMange = {
    "name":"villageMange",
    "enable":True,
    "simple_triggers":{
        "append":[
            ## 增加税收
            (center_tax_inscrease_interval,[
                (try_for_range,":center_no",centers_begin,centers_end),
                    (party_get_slot,":rents",":center_no",slot_center_accumulated_rents),
                    (try_begin),
                        (party_slot_eq,":center_no",slot_party_type,spt_village),
                        (val_add,":rents",village_rent_increase_per_day),
                    (else_try),
                        (party_slot_eq,":center_no",slot_party_type,spt_castle),
                        (val_add,":rents",castle_rent_increase_per_day),
                    (else_try),
                        (party_slot_eq,":center_no",slot_party_type,spt_town),
                        (val_add,":rents",town_rent_increase_per_day),
                    (try_end),
                    (party_set_slot,":center_no",slot_center_accumulated_rents,":rents"),

                    # (str_store_party_name,s1,":center_no"),
                    # (assign,reg1,":rents"),
                    # (display_message,"@update {s1} 's rents {reg1}"),
                (try_end),
            ]),
        ],
    },
}