# -*- coding: utf-8 -*-

from module_scripts import *

from modules.HeroCollection_header import *
## constans

hero_begin = "trp_hero_1"
hero_end = "trp_hero_end"

## slot

## args
spt_hero             = 21

'''

    
'''


heroCollection = {
    "name":"HeroCollection",
    "enable":True,
    "troops":{
        "insertBefore":{
            "sign":"heroes_end",
            "data":mergeList(repeatRandomTroop(51,"hero_{}"),repeatArcher1(1,"hero_end")),
        }
    },
    "strings":{
        "append":[
            # ("s5_s_patrol_party","{s5}'s patrol Party"),
        ],
    },
    "simple_triggers":{
        "append":[
            # (6, []),
        ],
    },
    "scripts":{
        "append":[
            ## 只会被使用一次
            ("init_hero_collection",[
                ## 初始化人员信息
                (try_for_range,":cur_troop",hero_begin,hero_end),
                    (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
                    ## 年龄
                    (store_random_in_range, ":age", 18, 60),
                    (troop_set_slot, ":cur_troop", slot_troop_age, ":age"),
                    (call_script, "script_init_troop_age", ":cur_troop", ":age"),
                    ## 性格 (直接使用系统领主性格)
                    (store_random_in_range,":reputation",lrep_none,lrep_conventional),
                    (troop_set_slot,":cur_troop",slot_lord_reputation_type,":reputation"),
                    ## 财富
                    (store_random_in_range,":wealth",200,10000),
                    (troop_set_slot,":cur_troop",slot_troop_wealth,":wealth"),
                    ## 声望
                    (store_random_in_range,":renown",20,300),
                    (troop_set_slot,":cur_troop",slot_troop_renown,":renown"),
                    ## 家乡
                    (store_random_in_range,":center",centers_begin,centers_end),
                    (troop_set_slot,":cur_troop",slot_troop_home,":center"),
                    (store_faction_of_party,":faction",":center"),
                    (troop_set_slot,":cur_troop",slot_troop_original_faction,":faction"),
                (try_end),
                ## 初始化人员关系（只设置，父亲，儿子，兄弟，没有庞大家族）
                (try_for_range,":cur_troop",hero_begin,hero_end),
                    (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
                    (store_random_in_range, ":age", 18, 60),
                    (troop_set_slot, ":cur_troop", slot_troop_age, ":age"),
                    (call_script, "script_init_troop_age", ":cur_troop", ":age"),
                (try_end),
            ]),
        ],
    },
    "internationals":{
        "cns":{
            "game_strings":[
                # "str_s5_s_patrol_party|{s5}的 巡 逻 队",
            ]
        }
    }
}