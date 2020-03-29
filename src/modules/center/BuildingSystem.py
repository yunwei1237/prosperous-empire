# -*- coding: utf-8 -*-
from header_dialogs import *
from module_scripts import *

'''
    建筑功能
    游戏开始时，为所有据点随机生成建筑

'''

'''
    庄园建造机率
'''
center_has_manor_possibility= 30 #village
'''
    磨坊建造机率
'''
center_has_mill_possibility= 90 #village
'''
    了望塔建造机率
'''
center_has_watch_tower_possibility= 80 #village
'''
    学校繁建造机率
'''
center_has_school_possibility= 10 #village
'''
    驿站建造机率
'''
center_has_messenger_post_possibility= 80 #town, castle, village
'''
    监狱建造机率
'''
center_has_prisoner_tower_possibility= 20 #town, castle


buildingSystem = {
    "name":"BuildingSystem",
    "enable":True,
    "triggers":{
        "append":[
            ## 游戏开始时执行
            (0,0,ti_once,[],[
                (call_script, "script_init_building_when_game_start"),
            ]),
        ],
    },
    "scripts":{
        "append":[
            ## 巡逻队的核心功能，驱动巡逻队运行的代码
            ("init_building_when_game_start",[
                ## 领地巡逻队
                (try_for_range,":center_no",centers_begin,centers_end),
                    (this_or_next|party_slot_eq,":center_no",slot_party_type,spt_town),
                    (this_or_next|party_slot_eq,":center_no",slot_party_type,spt_castle),
                    (party_slot_eq,":center_no",slot_party_type,spt_village),

                    #(str_store_party_name_link,s1,":center_no"),

                    ## 庄园建造
                    (store_random_in_range,":build_possibility",1,101),
                    (try_begin),
                        (le,":build_possibility",center_has_manor_possibility),
                        (party_set_slot,":center_no",slot_center_has_manor,1),
                        #(display_message,"@{s1} 建 造 庄 园"),
                    (try_end),
                    ## 磨坊建造
                    (store_random_in_range,":build_possibility",1,101),
                    (try_begin),
                        (le,":build_possibility",center_has_mill_possibility),
                        (party_set_slot,":center_no", slot_center_has_fish_pond, 1),
                        #(display_message,"@{s1} 建 造 磨 坊"),
                    (try_end),
                    ## 了望塔建造
                    (store_random_in_range,":build_possibility",1,101),
                    (try_begin),
                        (le,":build_possibility",center_has_watch_tower_possibility),
                        (party_set_slot,":center_no",slot_center_has_watch_tower,1),
                        #(display_message,"@{s1} 建 造 了 望 塔"),
                    (try_end),
                    ## 学校建造
                    (store_random_in_range,":build_possibility",1,101),
                    (try_begin),
                        (le,":build_possibility",center_has_school_possibility),
                        (party_set_slot, ":center_no", slot_center_has_school, 1),
                        #(display_message,"@{s1} 建 造 学 校"),
                    (try_end),
                    ## 驿站建造
                    (store_random_in_range,":build_possibility",1,101),
                    (try_begin),
                        (le,":build_possibility",center_has_messenger_post_possibility),
                        (party_set_slot, ":center_no", slot_center_has_messenger_post, 1),
                        #(display_message,"@{s1} 建 造 驿 站"),
                    (try_end),
                    ## 监狱建造
                    (store_random_in_range,":build_possibility",1,101),
                    (try_begin),
                        (le,":build_possibility",center_has_prisoner_tower_possibility),
                        (party_set_slot, ":center_no", slot_center_has_prisoner_tower, 1),
                        #(display_message,"@{s1} 建 造 监 狱"),
                    (try_end),
                (try_end),
            ]),
        ],
    }
}