# -*- coding: utf-8 -*-

from module_scripts import *

from modules.HeroCollection_header import *



hero_size = 50


has_one_children_probability = 80

has_two_children_probability = 40

hero_party_init_xp = 2500


hero_party_init_strength = 2

hero_party_update_interval = 4


## 以下内容非程序员不要修改

## constans

hero_begin = "trp_hero_1"
hero_end = "trp_hero_end"


heroCollection = {
    "name":"HeroCollection",
    "enable":True,
    "troops":
        {
            "insertBefore":[
                {
                    "sign":"heroes_end",
                    "data":mergeList(repeatRandomTroop(hero_size,"hero_{}"),repeatArcher1(1,"hero_end")),
                }
            ]
        },
    "simple_triggers":{
        "append":[
            (hero_party_update_interval,[
                #(call_script,"script_init_hero_collection"),
                (call_script,"script_update_hero_collection_status"),
            ]),
        ],
    },
    "triggers":{
        "append":[
            ## 游戏开始时就初始化英雄信息(只更新一次)
            (0,0,ti_once,[],[
                (display_message,"@heros is init"),
                (call_script,"script_init_hero_collection"),
            ]),
        ],
    },
    "scripts":{
        "append":[
            ## 只会被使用一次
            ("init_hero_collection",[
                (display_message,"@heros is init begin"),
                ## 初始化人员信息
                (try_for_range,":cur_troop",hero_begin,hero_end),
                    (str_store_troop_name_link,s1,":cur_troop"),
                    (display_message,"@hero({s1}) is init start"),
                    ## 职业
                    (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
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
                    (str_store_faction_name,s1,":faction"),
                    (display_message,"@hero faction is {s1}"),
                    (troop_set_slot,":cur_troop",slot_troop_original_faction,":faction"),
                    (troop_get_slot,":faction",":cur_troop",slot_troop_original_faction),
                    (str_store_faction_name,s2,":faction"),
                    (display_message,"@hero faction is {s2}    2222222222"),
                    (troop_set_note_available,":cur_troop",1),
                    ## 阵营(平民阵营)
                    (troop_set_faction,":cur_troop","fac_commoners"),
                    (str_store_troop_name_link,s1,":cur_troop"),
                    (display_message,"@hero({s1}) is init over"),
                (try_end),
                ## 初始化人员关系（只设置，父亲，儿子，兄弟，没有庞大家族）
                (try_for_range,":cur_index",0,hero_size),
                    (store_add,":father","trp_hero_1",":cur_index"),
                    ## 年龄
                    (store_random_in_range, ":age", 36, 60),
                    (call_script, "script_init_troop_age", ":father", ":age"),
                    ## 随机生成老大(80%机率)
                    (store_random_in_range,":isSun",1,101),
                    (try_begin),
                        (ge,":isSun",has_one_children_probability),
                        (val_add,":cur_index",1),
                        (store_add,":son_one","trp_hero_1",":cur_index"),
                        (store_random_in_range, ":age", 25, 60),
                        (call_script, "script_init_troop_age", ":son_one", ":age"),
                        (troop_set_slot, ":son_one", slot_troop_father, ":father"),
                        (display_message,"@childre one"),
                    (try_end),
                    ## 随机生成老二（40%机率）
                    (store_random_in_range,":isSun",1,101),
                    (try_begin),
                        (ge,":isSun",has_two_children_probability),
                        (val_add,":cur_index",1),
                        (store_add,":son_two","trp_hero_1",":cur_index"),
                        (store_random_in_range, ":age", 25, 60),
                        (call_script, "script_init_troop_age", ":son_two", ":age"),
                        (troop_set_slot, ":son_two", slot_troop_father, ":father"),
                        (display_message,"@childre two"),
                    (try_end),
                (try_end),
                ## 更新所有英雄的信息
                (call_script, "script_update_all_notes"),

                (display_message,"@heros is init end"),
            ]),
            ## 创建部队通用方法
            ("create_party_common",[
                (store_script_param, ":troop_no", 1),
                (store_script_param, ":strength_val", 2),
                (store_script_param, ":faction_no", 3),
                (try_begin),
                    (lt,":faction_no",0),
                    (store_faction_of_party,":party_faction",":troop_no"),
                (try_end),
                (set_spawn_radius, 10),
                (troop_get_slot,":center_no",":troop_no",slot_troop_home),
                (spawn_around_party, ":center_no", "pt_kingdom_hero_party"),
                (assign, ":new_party", reg0),

                (party_set_faction, ":new_party", ":party_faction"),

                (party_set_flags, ":new_party", pf_default_behavior, 0),
                (troop_set_slot,":troop_no",slot_troop_leaded_party,":new_party"),
                (str_store_troop_name,s5,":troop_no"),
                (party_set_name, ":new_party", "str_s5_s_party"),
                ## 增加士兵
                (try_for_range, ":unused", 0, ":strength_val"),
                  (call_script, "script_reinforce_party", ":new_party"),
                (try_end),
                ## 增加经验
                (store_mul,":xp_addition_for_centers",":strength_val", hero_party_init_xp),
                (party_upgrade_with_xp, ":new_party", ":xp_addition_for_centers", 0),
                (assign, reg0, ":new_party"),
              ]),
            ## 获得一个阵营全部的据点
            ("get_all_center_arr_of_faction",[
                (store_script_param_1,":faction"),
                (assign,":size",0),
                (try_for_range,":center",centers_begin,centers_end),
                    (store_faction_of_party,":party_faction",":center"),
                    (eq,":party_faction",":faction"),
                    (store_sub,":offset",":center",centers_begin),
                    ## 跳过0下标，下标为0的位置用于存放据点的个数
                    (val_add,":offset",1),
                    (party_set_slot,"p_temp_party",":offset",":center"),
                    (val_add,":size",1),
                (try_end),
                (party_set_slot,"p_temp_party",0,":size"),
            ]),
            ## 更新英雄的状态，定时更新
            ("update_hero_collection_status",[
                ## 创建队伍
                (display_message,"@hero status update begin"),
                (try_for_range,":cur_troop",hero_begin,hero_end),
                    (assign, reg1, ":cur_troop"),
                    (display_message, "@troop id {reg1}"),
                    (troop_get_slot,":party",":cur_troop",slot_troop_leaded_party),
                    (assign,reg1,":party"),
                    (display_message,"@party id {reg1}"),
                    (try_begin),
                        ## 队伍无效后（被击败）
                        (le,":party",0),
                        ## 出生在家乡附近
                        (call_script,"script_create_party_common",":cur_troop",hero_party_init_strength,"fac_commoners"),
                        (assign,":party",reg0),
                        (str_store_party_name_link,s1,":party"),
                        (display_message,"@party({s1}) is create"),
                    (try_end),
                    (troop_get_slot,":faction",":cur_troop",slot_troop_original_faction),
                    (str_store_faction_name,s2,":faction"),
                    (display_message,"faction name is {s2}"),
                    ## 更新ai 就是巡逻英雄的国家，不会去其它国家巡逻，边界不考虑，可能会跨越边界
                    (call_script,"script_get_all_center_arr_of_faction",":faction"),
                    (party_get_slot,":size","p_temp_party",0),
                    (store_random_in_range,":center_index",0,":size"),
                    ## 跳过0索引
                    (val_add,":center_index",1),
                    (party_get_slot,":center","p_temp_party",":center_index"),
                    (call_script, "script_party_set_ai_state", ":party",  spai_patrolling_around_center, ":center"),

                    ## 每一点统御增加一点军事强度
                    (store_skill_level,":leadership",":cur_troop",skl_leadership),
                    (assign,":strength",":leadership"),
                    (try_for_range,":unused",0,":strength"),
                        (call_script, "script_reinforce_party", ":party"),
                    (try_end),

                    (display_message,"@hero status update"),
                (try_end),
                (display_message,"@hero status update end"),
            ]),
        ],
    },
    # "internationals":{
    #     "cns":{
    #         "game_strings":[
    #             # "str_s5_s_patrol_party|{s5}的 巡 逻 队",
    #         ]
    #     }
    # }
}