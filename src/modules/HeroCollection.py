# -*- coding: utf-8 -*-

from module_scripts import *

from modules.HeroCollection_header import *




## 英雄数量
hero_size = 50


## 生一个小孩的可能性
has_one_children_probability = 30


## 生两个小孩的可能性
has_two_children_probability = 5


## 初始军事强度
hero_party_init_strength = 5


## 多久更新一次英雄部队
hero_party_update_interval = 12


## 英雄士兵数量小于时，就开始招募
hero_party_min_count = 35


## 默认阵营（赏金猎人）
hero_default_faction = fac_manhunters


## 以下内容非程序员不要修改

## constans

hero_begin = "trp_hero_1"
hero_end = "trp_hero_end"

## slot

## 英雄出生在哪个国家（招兵时会使用他出生的国家兵种）
slot_troop_from_faction = 175

## 英雄上一次巡逻的据点
slot_troop_last_patroll_center = 176


slot_troop_first_name = 177
slot_troop_second_name = 178

heroCollection = {
    "name":"HeroCollection",
    "enable":True,
    "dependentOn":["PartyBaseScripts","TroopBaseScripts"],
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
                ## 初始化人员信息
                (try_for_range,":cur_troop",hero_begin,hero_end),
                    ## 姓名
                    (call_script,"script_get_random_first_name"),
                    (str_store_string,s1,s0),
                    (troop_set_slot,":cur_troop",slot_troop_first_name,s1),
                    (call_script,"script_get_random_second_name"),
                    (str_store_string,s2,s0),
                    (troop_set_slot,":cur_troop",slot_troop_second_name,s2),
                    (troop_set_name, ":cur_troop", "str_s1_s2_name"),
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
                    (troop_set_slot,":cur_troop",slot_troop_from_faction,":faction"),
                    ## 阵营(平民阵营)
                    (troop_set_faction,":cur_troop",hero_default_faction),

                    (str_store_troop_name_link,s1,":cur_troop"),
                    (str_store_faction_name_link,s2,":faction"),
                    (str_store_party_name_link,s3,":center"),
                    (display_message,"@hero({s1})'faction is {s2},home is {s3}"),
                (try_end),
                ## 初始化人员关系（只设置，父亲，儿子，兄弟，没有庞大家族）
                (try_for_range,":cur_index",0,hero_size),
                    (store_add,":father","trp_hero_1",":cur_index"),
                    ## 年龄
                    (store_random_in_range, ":age", 36, 60),
                    (call_script, "script_init_troop_age", ":father", ":age"),

                    ## 获得姓氏
                    (troop_get_slot,":father_first_name",":father",slot_troop_first_name),
                (assign,reg1,":father_first_name"),
                (str_store_string,s1,":father_first_name"),
                (display_message,"@father's first name is {s1}(reg:{reg1})"),
                    ## 随机生成老大(80%机率)
                    (store_random_in_range,":isSun",1,101),
                    (try_begin),
                        (le,":isSun",has_one_children_probability),
                        (val_add,":cur_index",1),
                        (store_add,":son_one","trp_hero_1",":cur_index"),
                        (store_random_in_range, ":age", 25, 60),
                        #(call_script, "script_init_troop_age", ":son_one", ":age"),

                        (call_script,"script_get_random_second_name"),
                        (str_store_string,s2,s0),

                        #(str_store_string,s1,":father_first_name"),
                        (troop_set_slot, ":son_one", slot_troop_first_name, s1),
                        (troop_set_slot,":son_one",slot_troop_second_name,s2),

                        (troop_set_name, ":son_one", "str_s1_s2_name"),

                        (troop_set_slot, ":son_one", slot_troop_father, ":father"),

                        (str_store_troop_name_link,s10,":father"),
                        (str_store_troop_name_link,s20,":son_one"),
                        (display_message,"@{s10} has a first children({s20})"),
                    (try_end),
                    ## 随机生成老二（40%机率）
                    # (store_random_in_range,":isSun",1,101),
                    # (try_begin),
                    #     (le,":isSun",has_two_children_probability),
                    #     (val_add,":cur_index",1),
                    #     (store_add,":son_two","trp_hero_1",":cur_index"),
                    #     (store_random_in_range, ":age", 25, 60),
                    #     (call_script, "script_init_troop_age", ":son_two", ":age"),
                    #
                    #     (call_script,"script_get_random_second_name"),
                    #     (str_store_string,s2,s0),
                    #     (troop_set_slot,":son_two",slot_troop_first_name,s1),
                    #     (troop_set_slot,":son_two",slot_troop_second_name,s2),
                    #     (troop_set_name, ":son_two", "str_s1_s2_name"),
                    #
                    #     (troop_set_slot, ":son_two", slot_troop_father, ":father"),
                    #
                    #     (str_store_troop_name_link, s10, ":father"),
                    #     (str_store_troop_name_link, s20, ":son_one"),
                    #     (display_message, "@{s10} has a second children({s20})"),
                    # (try_end),
                (try_end),
                ## 更新所有英雄的信息
                (call_script, "script_update_all_notes"),
            ]),
            ## 更新英雄的状态，定时更新
            ("update_hero_collection_status",[
                ## 创建队伍
                (try_for_range,":cur_troop",hero_begin,hero_end),
                    (troop_get_slot,":party",":cur_troop",slot_troop_leaded_party),
                    (troop_get_slot,":home",":cur_troop",slot_troop_home),
                    (try_begin),
                        ## 队伍无效后（被击败）
                        (le,":party",0),
                        ## 出生在家乡附近
                        #(call_script,"script_create_party",":cur_troop",":home",fac_commoners,-1,-1,"icon_gray_knight",-1),
                        (call_script,"script_create_party",":cur_troop","p_main_party",hero_default_faction,-1,-1,"icon_gray_knight",-1),
                        (assign,":party",reg0),
                        ## 增加士兵
                        (troop_get_slot, ":faction", ":cur_troop", slot_troop_from_faction),
                        (call_script,"script_party_add_members",":party",":faction",hero_party_init_strength,60,40),
                        ## 增加经验
                        (call_script,"script_party_add_xp_and_upgrade",":party",hero_party_init_strength,20),
                        ## 设置ai
                        (call_script,"script_party_change_ai_state",":party",ai_bhvr_patrol_party,":home",5),
                        (str_store_party_name_link,s1,":party"),
                        (str_store_party_name_link,s2,":home"),
                        (display_message,"@party({s1}) is create at {s2}"),
                    (try_end),
                    (troop_get_slot,":last_center",":cur_troop",slot_troop_last_patroll_center),
                    (call_script,"script_get_center_close_the_center",":home",":last_center"),
                    (assign,":new_center",reg0),
                    (troop_set_slot,":cur_troop",slot_troop_last_patroll_center,":new_center"),
                    (str_store_troop_name,s1,":cur_troop"),
                    (str_store_party_name,s3,":new_center"),
                    (display_message,"@party({s1}) patroll cennter({s3})"),

                    (call_script,"script_party_change_ai_state",":party",ai_bhvr_patrol_party,":new_center",5),

                    (store_troop_count_companions,":party_size",":party"),
                    (try_begin),
                        (lt,hero_party_min_count),
                        ## 每一点统御增加一点军事强度
                        (store_skill_level,":leadership",":cur_troop",skl_leadership),
                        (assign,":strength",":leadership"),
                        (call_script,"script_party_add_members",":party",-1,":strength",60,40),
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