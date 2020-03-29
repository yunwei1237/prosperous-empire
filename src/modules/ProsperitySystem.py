# -*- coding: utf-8 -*-
from header_dialogs import *
from module_scripts import *

'''
    繁荣度功能（星期为单位）
    1.基础增加2点繁荣
    2.有庄园再增加3点繁荣
    2.有磨坊再增加5点繁荣
    2.有了望塔再增加1点繁荣
    2.有学校再增加2点繁荣
    2.有驿站再增加1点繁荣
    2.有监狱再增加1点繁荣
    4.城镇拥有工厂时增加7点繁荣
    
    
    被洗劫后不增加繁荣

'''


## 繁荣度多久更新一次（24*7）（游戏中的单位：小时）
prosperity_update_interval = 24 * 7

## 每一次更新必然增加的繁荣度
center_base_prosperity = 2

'''
    庄园繁荣度加成
'''
center_has_manor_prosperity= 3 #village
'''
    磨坊繁荣度加成
'''
center_has_mill_prosperity= 5 #village
'''
    了望塔繁荣度加成
'''
center_has_watch_tower_prosperity= 1 #village
'''
    学校繁荣度加成
'''
center_has_school_prosperity= 2 #village
'''
    驿站繁荣度加成
'''
center_has_messenger_post_prosperity= 1 #town, castle, village
'''
    监狱繁荣度加成
'''
center_has_prisoner_tower_prosperity= 1 #town, castle

'''
    工厂繁荣度加成
'''
center_player_enterprise_prosperity = 7
## 以下内容非游戏程序员不要修改

## 【slot】

## party slot


## 【args】

## 巡逻队类型
spt_patrol             = 7


prosperitySystem = {
    "name":"ProsperitySystem",
    "enable":True,
    "dependentOn":["PartyBaseScripts"],
    "simple_triggers":{
        "append":[
            ##
            (prosperity_update_interval, [
                (display_message,"@prisperity init"),
                (call_script, "script_update_prisperity_for_all_center"),
            ]),
        ],
    },
    "scripts":{
        "append":[
            ## 巡逻队的核心功能，驱动巡逻队运行的代码
            ("update_prisperity_for_all_center",[
                ## 领地巡逻队
                (try_for_range,":center_no",centers_begin,centers_end),
                    (this_or_next|party_slot_eq,":center_no",slot_party_type,spt_town),
                    (this_or_next|party_slot_eq,":center_no",slot_party_type,spt_castle),
                    (party_slot_eq,":center_no",slot_party_type,spt_village),

                    ## 城堡没有被围攻
                    (this_or_next|party_slot_eq, ":center_no", slot_center_is_besieged_by, -1),
                    ## 村庄是正常状态
                    (party_slot_eq,":center_no",slot_village_state,svs_normal),

                    (assign,":prosperity",center_base_prosperity),
                    ## 庄园加成
                    (try_begin),
                        (party_slot_eq,":center_no",slot_center_has_manor,1),
                        (val_add,":prosperity",center_has_manor_prosperity),
                    (try_end),
                    ## 磨坊加成
                    (try_begin),
                        (party_slot_eq,":center_no", slot_center_has_fish_pond, 1),
                        (val_add,":prosperity",center_has_mill_prosperity),
                    (try_end),
                    ## 了望塔加成
                    (try_begin),
                        (party_slot_eq,":center_no",slot_center_has_watch_tower,1),
                        (val_add,":prosperity",center_has_watch_tower_prosperity),
                    (try_end),
                    ## 学校加成
                    (try_begin),
                        (party_slot_eq, ":center_no", slot_center_has_school, 1),
                        (val_add, ":prosperity", center_has_school_prosperity),
                    (try_end),
                    ## 驿站加成
                    (try_begin),
                        (party_slot_eq, ":center_no", slot_center_has_messenger_post, 1),
                        (val_add, ":prosperity", center_has_messenger_post_prosperity),
                    (try_end),
                    ## 监狱加成
                    (try_begin),
                        (party_slot_eq, ":center_no", slot_center_has_prisoner_tower, 1),
                        (val_add, ":prosperity", center_has_prisoner_tower_prosperity),
                    (try_end),
                    ## 玩家工厂加成
                    (try_begin),
                        (party_slot_eq, ":center_no", slot_center_player_enterprise, 1),
                        (val_add, ":prosperity", center_player_enterprise_prosperity),
                    (try_end),

                    (party_get_slot,":center_prosperity",":center_no",slot_town_prosperity),
                    (val_add,":center_prosperity",":prosperity"),
                    (party_set_slot,":center_no",slot_town_prosperity,":center_prosperity"),

                    (assign,reg1,":prosperity"),
                    (str_store_party_name_link,s1,":center_no"),
                    (display_message,"@{s1} 增 加 {reg1} 点 繁 荣 度"),
                (try_end),
                ]),
        ],
    }
}