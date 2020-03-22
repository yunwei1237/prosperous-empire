# -*- coding: utf-8 -*-

from module_scripts import *

from modules.HeroCollection_header import *



hero_size = 50


has_one_children_probability = 80

has_two_children_probability = 40

hero_party_init_xp = 2500


hero_party_init_strength = 5

hero_party_update_interval = 12

hero_party_min_count = 35


## 以下内容非程序员不要修改

## constans

hero_begin = "trp_hero_1"
hero_end = "trp_hero_end"



## slot

## 英雄出生在哪个国家（招兵时会使用他出生的国家兵种）
slot_troop_from_faction = 175
slot_troop_last_patroll_center = 176

heroCollection = {
    "name":"HeroCollection",
    "enable":True,
    "dependentOn":["PatrolParty"],
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
                    (troop_set_slot,":cur_troop",slot_troop_from_faction,":faction"),
                    (troop_get_slot,":faction",":cur_troop",slot_troop_from_faction),
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
            ("hero_party_add_members",[
                (store_script_param_1,":troop_no"),
                (store_script_param_2,":strength_val"),

                (troop_get_slot,":party",":troop_no",slot_troop_leaded_party),
                ## 获得低级阵营模板
                (troop_get_slot,":faction",":troop_no",slot_troop_from_faction),
                (store_random_in_range,":pt_no",0,100),
                (try_begin),
                    (le,":pt_no",70),
                    (faction_get_slot,":pt_temp",":faction",slot_faction_reinforcements_a),
                (else_try),
                    (le,":pt_no",90),
                    (faction_get_slot,":pt_temp",":faction",slot_faction_reinforcements_b),
                (else_try),
                    (le,":pt_no",95),
                    (faction_get_slot,":pt_temp",":faction",slot_faction_reinforcements_c),
                (try_end),
                (try_for_range, ":unused", 0, ":strength_val"),
                    (party_add_template,":party",":pt_temp"),
                (try_end),
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
                (set_spawn_radius, 2),
                (troop_get_slot,":center_no",":troop_no",slot_troop_home),
                #(spawn_around_party, ":center_no", "pt_kingdom_hero_party"),

                (spawn_around_party, "p_main_party", "pt_kingdom_hero_party"),
                (assign, ":new_party", reg0),

                (party_set_faction, ":new_party", ":party_faction"),

                (party_set_flags, ":new_party", pf_default_behavior, 0),
                (troop_set_slot,":troop_no",slot_troop_leaded_party,":new_party"),
                (str_store_troop_name,s5,":troop_no"),
                (party_set_name, ":new_party", "str_s5_s_party"),
                ## 添加英雄
                (party_add_leader,":new_party",":troop_no"),
                ## 增加士兵
                (call_script,"script_hero_party_add_members",":troop_no",":strength_val"),
                ## 增加经验
                (store_mul,":xp_addition_for_centers",":strength_val", hero_party_init_xp),
                (party_upgrade_with_xp, ":new_party", ":xp_addition_for_centers", 0),
                (assign, reg0, ":new_party"),
              ]),
            ## 获得一个阵营全部的据点
            ("get_all_center_arr_of_faction",[
                (store_script_param_1,":faction"),
                (assign,":size",0),
                (assign,":index",0),
                (try_for_range,":center",centers_begin,centers_end),
                    (this_or_next|party_slot_eq,":center",slot_party_type,spt_town),
                    (this_or_next|party_slot_eq,":center",slot_party_type,spt_castle),
                    (party_slot_eq,":center",slot_party_type,spt_village),
                    (store_faction_of_party,":party_faction",":center"),
                    (eq,":party_faction",":faction"),
                    #(store_sub,":offset",":center",centers_begin),
                    ## 跳过0下标，下标为0的位置用于存放据点的个数
                    (val_add,":index",1),
                    (party_set_slot,"p_temp_party",":index",":center"),
                    (val_add,":size",1),
                (try_end),
                (party_set_slot,"p_temp_party",0,":size"),
            ]),
            ## 获得指定地点最近的据点
            ("get_center_close_the_center",[
                (store_script_param_1,":center"),
                (store_script_param_2,":not_want_center"),

                (assign,":min",99999999),
                (assign,":close_center",":center"),
                (try_for_range,":center_no",centers_begin,centers_end),
                    (store_distance_to_party_from_party,":distance",":center_no",":center"),
                    (le,":min",":distance"),
                    (neq,":center_no",":not_want_center"),
                    (assign,":min",":distance"),
                    (assign,":close_center",":center_no"),
                (try_end),
                (assign,reg0,":close_center"),
            ]),
            ## 更新英雄的状态，定时更新
            ("update_hero_collection_status",[
                ## 创建队伍
                (try_for_range,":cur_troop",hero_begin,hero_end),
                    (troop_get_slot,":party",":cur_troop",slot_troop_leaded_party),
                    (try_begin),
                        ## 队伍无效后（被击败）
                        (lt,":party",0),
                        ## 出生在家乡附近
                        (call_script,"script_create_party_common",":cur_troop",hero_party_init_strength,"fac_commoners"),
                        (assign,":party",reg0),
                        (str_store_party_name_link,s1,":party"),
                        (troop_get_slot,":center_no",":cur_troop",slot_troop_home),
                        (str_store_party_name_link,s2,":center_no"),
                        (display_message,"@party({s1}) is create at {s2}"),
                    (try_end),
                    #(troop_get_slot,":faction",":cur_troop",slot_troop_from_faction),
                    #(str_store_faction_name,s2,":faction"),
                    #(display_message,"@faction name is {s2}"),
                    ## 更新ai 就是巡逻英雄的国家，不会去其它国家巡逻，边界不考虑，可能会跨越边界
                    # (call_script,"script_get_all_center_arr_of_faction",":faction"),
                    # (party_get_slot,":size","p_temp_party",0),
                    # (str_store_faction_name,s10,":faction"),
                    # (try_for_range,":center_index",0,":size"),
                    #     (val_add,":center_index",1),
                    #     (str_store_party_name_link,s11,":center_index"),
                    #     (display_message,"@faction({s10}) 's center({s11})"),
                    # (try_end),
                    # (store_random_in_range,":center_index",0,":size"),
                    # ## 跳过0索引
                    # (val_add,":center_index",1),
                    # (party_get_slot,":center","p_temp_party",":center_index"),
                    (troop_get_slot,":home_center",":cur_troop",slot_troop_home),
                    (troop_get_slot,":last_center",":cur_troop",slot_troop_last_patroll_center),
                    (call_script,"script_get_center_close_the_center",":home_center",":last_center"),
                    (assign,":new_center",reg0),
                    (troop_set_slot,":cur_troop",slot_troop_last_patroll_center,":new_center"),
                    (str_store_troop_name,s1,":cur_troop"),
                    (str_store_party_name,s3,":new_center"),
                    (display_message,"@party({s1}) patroll cennter({s3})"),

                    (call_script, "script_party_set_ai_state", ":party",  spai_patrolling_around_center, ":center"),


                    ## 每一点统御增加一点军事强度
                    (store_troop_count_companions,":party_size",":party"),
                    (try_begin),
                        (lt,hero_party_min_count),
                        (store_skill_level,":leadership",":cur_troop",skl_leadership),
                        (assign,":strength",":leadership"),
                        (call_script, "script_hero_party_add_members", ":cur_troop", ":strength"),
                        (display_message,"@hero count update"),
                    (try_end),
                    (str_store_troop_name,s4,":cur_troop"),
                    (display_message,"@hero({s4}) status update end"),
                (try_end),
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