# -*- coding: utf-8 -*-
from header_dialogs import *
from module_scripts import *

'''
    巡逻队功能

    每48（由patrol_update_interval决定）小时会更新巡逻队（补充士兵，添加经验，贩卖俘虏）
    此巡逻队只为据点生成，包括，首都（6队，每队至少80人），城镇（4队，每队至少80人），城堡（2队，每队至少60人），和村庄（1队，每队至少40人）.

    人数超过限制和金钱（据点的钱）不够时就不会再补充士兵，如果超过是不限制的。
    队数如果少于限制数量，就会创建以补足数量。
    士兵每天都会有经验加成
    俘虏贩卖金币会保存到据点

'''


## 常量，供策划使用

## 首都巡逻队数量
capital_town_patrol_max_num = 6
## 城镇巡逻队数量
town_patrol_max_num = 4
## 城堡巡逻队数量
castle_patrol_max_num = 2
## 村庄巡逻队数量
village_patrol_max_num = 1

## 城镇巡逻队最少人数（如果数量不够，会陆续补充至此数量，如果数量超出，不会解雇）
town_patrol_min_size = 80
## 城堡巡逻队最少人数
castle_patrol_min_size = 60
## 村庄巡逻队最少人数
village_patrol_min_size = 40

## 首都巡逻队强度（强度越大，士兵等级越高）
capital_town_patrol_strength = 8
## 城镇巡逻队强度
town_patrol_strength = 6
## 城堡巡逻队强度
castle_patrol_strength = 4
## 村庄巡逻队强度
village_patrol_strength = 2


## 巡逻队多久更新一次（游戏中的单位：小时）
patrol_update_interval = 48

## 巡逻队初次创建时的经验
patrol_init_party_xp= 2500

## 巡逻队每天晚上每点强度的经验（每晚经验 = strength * patrol_every_day_per_strength_xp）
patrol_every_day_per_strength_xp= 100

## 每次升级士兵的花费
patrol_update_cost_money = 100



## 以下内容非游戏程序员不要修改

## 【slot】

## party slot

## 用于保存巡逻队的数量
slot_party_patrol_num     = 400
## 用于保存巡逻的据点
slot_party_protect_center = 401

## 【args】

## 巡逻队类型
spt_patrol             = 7


patrolParty = {
    "name":"PatrolParty",
    "enable":True,
    "dependentOn":["PartyBaseScripts"],
    "strings":{
        "append":[
            ("s5_s_patrol_party","{s5}'s patrol Party"),
        ],
    },
    "triggers":{
        "append":[
            ## 游戏开始时就创建循环队
            (0,0,ti_once,[],[
                (call_script, "script_update_patrol_partys_for_all"),
            ]),
        ],
    },
    "simple_triggers":{
        "append":[
            ## 定期创建和维护巡逻队
            (patrol_update_interval, [
                (call_script, "script_update_patrol_partys_for_all"),
            ]),
            ## 在据点变更领主时，巡逻队也相应变更阵营
            (1, [
                ## 转变阵营的据点的巡逻队也要转换阵营(1个小时检测一次)
                ## 如果能够在阵营转换时就检测应该效果最好（但是可能需要修改系统代码）
                (call_script, "script_update_all_patrol_party_faction"),
                ## 统计被打败的队伍,从slot中减去
            ]),
            ## 显示一个城镇巡逻队的信息(用于测试巡逻队是否正常刷出)
            # (1,[
            #     (display_message,"@---------------------------"),
            #     (try_for_parties,":party"),
            #         (party_is_active,":party"),
            #         (party_slot_eq,":party",slot_party_type,spt_patrol),
            #         (party_slot_eq,":party",slot_party_protect_center,"p_town_3"),
            #         (assign,reg1,":party"),
            #         ##(display_message,"@p_town_3 party id: {reg1}"),
            #         (party_get_num_companions,reg2,":party"),
            #         (display_message,"@p_town_3 id:{reg1} party size: {reg2}"),
            #     (try_end),
            #     (display_message,"@---------------------------"),
            # ]),
            ## 每6小时统计一次每一个据点巡逻队的数量，便于巡逻队被击败后及时创建
            ## ## 统计被打败的队伍,从slot中减去
            (6,[
                #(display_message,"@center patrol begin update size"),
                ## 初始化所有城镇的数量
                (try_for_parties,":center_no"),
                    (this_or_next | party_slot_eq, ":center_no", slot_party_type, spt_town),
                    (this_or_next | party_slot_eq, ":center_no", slot_party_type, spt_castle),
                    (party_slot_eq, ":center_no", slot_party_type, spt_village),
                    (party_set_slot,":center_no",slot_party_patrol_num,0),
                (try_end),

                ## 统计据点巡逻队数量
                (try_for_parties, ":party"),
                    (party_is_active,":party"),
                    (party_slot_eq, ":party", slot_party_type, spt_patrol),
                    (party_get_slot,":center",":party",slot_party_protect_center),
                    (party_get_slot,":num",":center",slot_party_patrol_num),
                    (val_add,":num",1),
                    (party_set_slot,":center",slot_party_patrol_num,":num"),
                    (str_store_party_name,s1,":center"),
                    (assign,reg1,":num"),
                    #(display_message,"@center({s1}) patrol size({reg1}) update"),
                (try_end),
            ]),

            (6,[
                (call_script, "script_give_center_to_lord", "p_town_16", "trp_player", 1),
            ]),
        ],
    },
    "scripts":{
        "append":[
            ## 获得巡逻队的军事强度
            ("get_patrol_center_strength",[
                (store_script_param_1,":center_no"),
                (assign,":strength",0),
                (try_begin),
                    (party_slot_eq, ":center_no", slot_party_type, spt_town),
                    (try_begin),
                        (party_get_slot, ":leader", ":center_no", slot_town_lord),
                        (is_between, ":leader", kings_begin, kings_end),
                        (assign, ":strength", capital_town_patrol_strength),
                    (else_try),
                        (assign, ":strength", town_patrol_strength),
                    (try_end),
                (else_try),
                    (party_slot_eq, ":center_no", slot_party_type, spt_castle),
                    (assign, ":strength", castle_patrol_strength),
                (else_try),
                    (assign, ":strength", village_patrol_strength),
                (try_end),
                (assign,reg0,":strength"),
            ]),
            ## 获得巡逻队需要创建的数量
            ("get_patrol_center_need_create_num",[
                (store_script_param_1,":center_no"),
                (assign,":need_create_party_num",0),

                (party_get_slot,":center_patrol_num",":center_no",slot_party_patrol_num),
                (try_begin),
                    (party_slot_eq, ":center_no", slot_party_type, spt_town),
                    (try_begin),
                        (party_get_slot, ":leader", ":center_no", slot_town_lord),
                        (is_between, ":leader", kings_begin, kings_end),
                        (store_sub, ":need_create_party_num", capital_town_patrol_max_num, ":center_patrol_num"),
                    (else_try),
                        (store_sub, ":need_create_party_num", town_patrol_max_num, ":center_patrol_num"),
                    (try_end),
                (else_try),
                    (party_slot_eq, ":center_no", slot_party_type, spt_castle),
                    (store_sub, ":need_create_party_num", castle_patrol_max_num, ":center_patrol_num"),
                (else_try),
                    (store_sub, ":need_create_party_num", village_patrol_max_num, ":center_patrol_num"),
                (try_end),
                (assign,reg1,":need_create_party_num"),
            ]),
            ## 获得巡逻队需要招募的士兵数量
            ("get_patrol_party_need_size",[
                (store_script_param_1,":party_no"),
                (assign,":need_size",0),
                (party_get_num_companions,":cur_size",":party_no"),
                ## 获得巡逻的据点
                (party_get_slot, ":center_no",":party_no",slot_party_protect_center),
                (try_begin),
                    (party_slot_eq,":center_no",slot_party_type,spt_town),
                    (store_sub,":need_size",town_patrol_min_size,":cur_size"),
                (else_try),
                    (party_slot_eq,":center_no",slot_party_type,spt_castle),
                    (store_sub,":need_size",castle_patrol_min_size,":cur_size"),
                (else_try),
                    (party_slot_eq,":center_no",slot_party_type,spt_village),
                    (store_sub,":need_size",village_patrol_min_size,":cur_size"),
                (try_end),
                (assign,reg0,":need_size"),
            ]),

            ## 巡逻队的核心功能，驱动巡逻队运行的代码
            ("update_patrol_partys_for_all",[
                ## 领地巡逻队
                (try_for_range,":center_no",centers_begin,centers_end),
                    (this_or_next|party_slot_eq,":center_no",slot_party_type,spt_town),
                    (this_or_next|party_slot_eq,":center_no",slot_party_type,spt_castle),
                    (party_slot_eq,":center_no",slot_party_type,spt_village),
                    ## 排除玩家领地（玩家巡逻队需要玩家自己创建）
                    (neg|party_slot_eq,":center_no",slot_town_lord,"trp_player"),

                    ## 计算每个巡逻队的军事强度
                    (call_script,"script_get_patrol_center_strength",":center_no"),
                    (assign,":strength",reg0),
                    ## 计算需要创建的部队数量
                    (call_script,"script_get_patrol_center_need_create_num",":center_no"),
                    (assign,":need_create_party_num",reg1),
                    (try_for_range,":unused",0,":need_create_party_num"),
                        ## 在指定地方创建巡逻队
                        (call_script,"script_create_party",-1,":center_no",-1,-1,"str_s5_s_patrol_party",spt_patrol,"icon_khergit_horseman_b",-1),
                        (assign,":party",reg0),
                        ## 设置巡逻据点
                        (party_set_slot, ":party",slot_party_protect_center,":center_no"),
                        ## 增加士兵
                        (call_script,"script_party_add_members",":party",-1,":strength",30,50),
                        ## 增加经验
                        (call_script,"script_party_add_xp_and_upgrade",":party",":strength",50),
                        ## 设置ai
                        ##(call_script, "script_party_set_ai_state", ":lady_party",  spai_patrolling_around_center, ":home"),
                        (call_script,"script_party_change_ai_state",":party",ai_bhvr_patrol_party,":center_no",5),

                        #(str_store_party_name,s1,":center_no"),
                        #(display_message,"@create :{s1} patrol party"),
                        ## 更新创建的队数量，以免重复创建
                        (party_get_slot,":center_patrol_num",":center_no",slot_party_patrol_num),
                        (val_add,":center_patrol_num",1),
                        (party_set_slot,":center_no",slot_party_patrol_num,":center_patrol_num"),
                    (try_end),
                (try_end),
                ## 维护巡逻队
                ## 1.处理俘虏（本国招降，它国贩卖）
                ## 2.补充士兵(不会一次补足)
                ## 3.升级士兵
                (try_for_parties,":party_no"),
                    (ge,":party_no",0),
                    (party_slot_eq,":party_no",slot_party_type,spt_patrol),
                    ## 【处理俘虏】,招募本国，它国售卖
                    (call_script,"script_party_handle_prisoners",":party_no",0),
                    ## 【补充士兵】
                    ## 获得巡逻的据点
                    (party_get_slot, ":center_no",":party_no",slot_party_protect_center),
                    ## 获得需要招募的数量
                    (call_script,"script_get_patrol_party_need_size",":party_no"),
                    (assign,":need_size",reg0),
                    (try_begin),
                        (gt,":need_size",0),
                        (party_slot_ge,":center_no",slot_town_wealth,patrol_update_cost_money),
                        ## 花钱招募
                        (call_script, "script_update_center_wealth", ":center_no",patrol_update_cost_money,-1),
                        ## 增加士兵
                        (call_script,"script_party_add_members",":party",-1,":strength",30,50),
                        #(str_store_party_name,s1,":party_no"),
                        #(display_message,"@add party:{s1}"),
                    (try_end),
                    ## 【升级士兵】
                    ## 获得巡逻据点的军事强度
                    (call_script,"script_get_patrol_center_strength",":center_no"),
                    (assign,":strength",reg0),
                    ## 增加经验
                    (call_script,"script_party_add_xp_and_upgrade",":party_no",":strength",50),
                (try_end),
            ]),
            ## 转变阵营的据点的巡逻队也要转换阵营
            ("update_all_patrol_party_faction",[
                (try_for_parties,":party_no"),
                    (party_slot_eq,":party_no",slot_party_type,spt_patrol),
                    (party_get_slot,":center_no",":party_no",slot_party_protect_center),
                    (store_faction_of_party,":center_faction",":center_no"),
                    (party_set_faction, ":party_no", ":center_faction"),
                (try_end),
            ]),
        ],
    },
    "dialogs":{
        "replace":[
            {
                "sign":"party_encounter_hostile_defender:Surrender_or_die@:party_encounter_hostile_ultimatum_surrender[1,3,4]",
                "data":[
                    [anyone|plyr,"party_encounter_hostile_defender", [],
                       "Surrender or die!", "party_encounter_hostile_ultimatum_surrender", [
                         #(display_message,"@Surrender or die!"),
                         (try_begin),
                            #(str_store_party_name,s1,"p_main_party"),
                            (assign,":party","$g_encountered_party"),
                            #(str_store_party_name,s2,":party"),
                            (store_faction_of_party,":faction",":party"),
                            #(str_store_faction_name,s3,":faction"),
                            #(display_message,"@player({s1}) is attack party({s2}) of faction({s3})."),
                            (call_script, "script_change_player_relation_with_faction_ex", ":faction", -1),
                         (try_end),
                       ]
                    ],
                ],
            },
        ],
    },
    "internationals":{
        "cns":{
            "game_strings":[
                "str_s5_s_patrol_party|{s5}的 巡 逻 队",
            ]
        }
    }
}