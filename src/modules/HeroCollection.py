# -*- coding: utf-8 -*-
from header_dialogs import *
from module_scripts import *

from modules.HeroCollection_header import *




## 英雄数量
from modules.base.TroopBaseScripts import *

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

## 英雄加入玩家队伍需要的关系值
hero_join_player_party_relation = 25


## 以下内容非程序员不要修改

## constans

hero_begin = "trp_hero_1"
hero_end = "trp_hero_end"

## slot

## 英雄状态
slot_troop_hero_status = 175

sths_normal           = 1
sths_in_player_party = 2


## 英雄出生在哪个国家（招兵时会使用他出生的国家兵种）
slot_troop_from_faction = 176

## 英雄上一次巡逻的据点
slot_troop_last_patroll_center = 177




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
                #(display_message,"@heros is init"),
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
                    (call_script,"script_set_random_name",":cur_troop"),
                    ## 状态
                    (troop_set_slot,":cur_troop",slot_troop_hero_status,sths_normal),
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

                    # (str_store_troop_name_link,s1,":cur_troop"),
                    # (str_store_faction_name_link,s2,":faction"),
                    # (str_store_party_name_link,s3,":center"),
                    # (display_message,"@hero({s1})'faction is {s2},home is {s3}"),
                (try_end),
                ## 初始化人员关系（只设置，父亲，儿子，没有庞大家族）
                (try_for_range,":cur_index",hero_begin,hero_end),
                    #(store_add,":father","trp_hero_1",":cur_index"),
                    (assign,":father",":cur_index"),
                    ## 年龄
                    (call_script,"script_set_age_in_range",":father",45,60),
                    ## 随机生成长子(80%机率)
                    (store_random_in_range,":isSun",1,101),
                    (try_begin),
                        (le,":isSun",has_one_children_probability),
                        (store_add,":son",":cur_index",1),
                        ## 儿子年龄
                        (call_script,"script_set_son_age",":father",":son"),
                        ## 儿子的名字
                        (call_script,"script_set_name_for_son",":father",":son"),

                        # (str_store_troop_name_link,s10,":father"),
                        # (str_store_troop_name_link,s20,":son"),
                        # (display_message,"@{s10} has a first children({s20})"),
                    (try_end),
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
                        (troop_slot_eq,":cur_troop",slot_troop_hero_status,sths_normal),
                        ## 出生在家乡附近
                        (call_script,"script_create_party",":cur_troop",":home",fac_commoners,-1,-1,"icon_gray_knight",-1),
                        #(call_script,"script_create_party",":cur_troop","p_main_party",hero_default_faction,-1,-1,"icon_gray_knight",-1),
                        (assign,":party",reg0),
                        ## 增加士兵
                        (troop_get_slot, ":faction", ":cur_troop", slot_troop_from_faction),
                        (call_script,"script_party_add_members",":party",":faction",hero_party_init_strength,60,40),
                        ## 增加经验
                        (call_script,"script_party_add_xp_and_upgrade",":party",hero_party_init_strength,20),
                        ## 设置ai
                        (call_script,"script_party_change_ai_state",":party",ai_bhvr_patrol_party,":home",5),
                        # (str_store_party_name_link,s1,":party"),
                        # (str_store_party_name_link,s2,":home"),
                        # (display_message,"@party({s1}) is create at {s2}"),
                    (try_end),

                    (ge,":party",0),
                    (troop_get_slot,":last_center",":cur_troop",slot_troop_last_patroll_center),
                    (call_script,"script_get_center_close_the_center",":home",":last_center"),
                    (assign,":new_center",reg0),
                    (troop_set_slot,":cur_troop",slot_troop_last_patroll_center,":new_center"),

                    # (str_store_troop_name,s1,":cur_troop"),
                    # (str_store_party_name,s3,":new_center"),
                    # (display_message,"@party({s1}) patroll cennter({s3})"),

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
                    # (str_store_troop_name,s4,":cur_troop"),
                    # (display_message,"@hero({s4}) status update end"),
                (try_end),
            ]),
        ],
    },
    "dialogs":{
        "insertBefore":[{
            "sign":"start:Yes___sire_my_lady__@:lord_start[1,3,4]",
            "data":[
                [anyone ,"start", [
					(is_between,"$g_talk_troop",hero_begin, hero_end),
                ],"Yes, {sire/my lady}?", "hero_start",[]],

                [anyone|plyr ,"hero_start", [],"Would you like to follow me?", "hire_hero_talk",[]],

                [anyone ,"hire_hero_talk", [
                    # (call_script,"script_troop_get_player_relation","$g_talk_troop"),
                    # (ge,reg0,hero_join_player_party_relation),
                ],"I'm glad to be part of your team", "close_window",[
                    (call_script,"script_add_party_with_hero_as_companions","p_main_party","$g_talk_troop_party"),
                    (troop_set_slot,"$g_talk_troop", slot_troop_hero_status, sths_in_player_party),

                    (eq, "$talk_context", tc_party_encounter),
                    (assign, "$g_leave_encounter", 1)
                ]],

                [anyone ,"hire_hero_talk", [],"I'm not familiar with you", "close_window",[]],

                [anyone|plyr ,"hero_start", [],"no thing!", "close_window",[
                    (eq, "$talk_context", tc_party_encounter),
                    (assign, "$g_leave_encounter", 1)
                ]],
            ]
        },],
    },
    "internationals":{
        "cns":{
            "dialogs":[
                "dlga_start:hero_start|你 好, {先 生/女 士}, 有 什 么 事 情 吗 ？",
                "dlga_hero_start:hire_hero_talk|你 想 跟 着 我 吗 ？",
                "dlga_hire_hero_talk:close_window|我 很 高 兴 能 够 成 为 你 队 伍 的 一 员 。",
                "dlga_hire_hero_talk:close_window.1|我 还 不 熟 悉 你 的 为 人 。",
                "dlga_hero_start:close_window|没 事",
            ]
        }
    }
}