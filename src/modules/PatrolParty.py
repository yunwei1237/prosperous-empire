# -*- coding: utf-8 -*-

from module_scripts import *


## constans

## 巡逻队数量（固定）
capital_town_patrol_max_num = 6
town_patrol_max_num = 4
castle_patrol_max_num = 2
village_patrol_max_num = 1

## 巡逻队人数（至少）
town_patrol_min_size = 80
castle_patrol_min_size = 60
village_patrol_min_size = 40

## 巡逻队军事强度
capital_town_patrol_strength = 8
town_patrol_strength = 6
castle_patrol_strength = 4
village_patrol_strength = 2

## party slot
slot_party_patrol_num     = 400
slot_party_protect_center = 401


## args
'''
    巡逻队
'''
spt_patrol             = 7

'''
    巡逻队功能
    
    每24小时会更新巡逻队（补充士兵，添加经验，贩卖俘虏）
    此巡逻队只为据点生成，包括，首都（6队，每队至少80人），城镇（4队，每队至少80人），城堡（2队，每队至少60人），和村庄（1队，每队至少40人）.
    
    人数超过限制和金钱（据点的钱）不够时就不会再补充士兵，如果超过是不限制的。
    队数如果少于限制数量，就会创建以补足数量。
    士兵每天都会有经验加成
    俘虏贩卖金币会保存到据点
    
'''
patrolParty = {
    "name":"PatrolParty",
    "enable":True,
    "strings":{
        "append":[
            ("s5_s_patrol_party","{s5}'s patrol Party"),
        ],
    },
    "simple_triggers":{
        "append":[
            (6, [

                ## todo 统计被打败的队伍,从slot中减去
                ##(display_message, "@start exec script_update_patrol_partys_for_all"),
                (call_script, "script_update_patrol_partys_for_all"),
            ]),

            (1, [
                ## 转变阵营的据点的巡逻队也要转换阵营(1个小时检测一次)
                ## 如果能够在阵营转换时就检测应该效果最好（但是可能需要修改系统代码）
                (call_script, "script_update_all_patrol_party_faction"),
                ## 统计被打败的队伍,从slot中减去
            ]),
            (1,[
                (try_for_parties,":party"),
                    (party_is_active,":party"),
                    (party_slot_eq,":party",slot_party_type,spt_patrol),
                    (party_slot_eq,":party",slot_party_protect_center,"p_town_3"),
                    (assign,reg1,":party"),
                    (display_message,"@p_town_3 party id: {reg1}"),
                    (party_get_num_companions,reg2,":party"),
                    (display_message,"@p_town_3 party size: {reg2}"),
                (try_end),
            ]),
            (6,[
                (display_message,"@center patrol begin update size"),
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
                    (display_message,"@center({s1}) patrol size({reg1}) update"),
                (try_end),
            ]),
        ],
    },
    "scripts":{
        "append":[
            ("reinforce_party",[
                 (store_script_param_1, ":party_no"),

                 (store_faction_of_party, ":party_faction", ":party_no"),
                 (party_get_slot, ":party_type", ":party_no", slot_party_type),

                 # Rebellion changes begin:
                 (try_begin),
                 (eq, ":party_type", spt_kingdom_hero_party),
                 (party_stack_get_troop_id, ":leader", ":party_no"),
                 (troop_get_slot, ":party_faction", ":leader", slot_troop_original_faction),
                 (try_end),
                 # Rebellion changes end

                 (try_begin),
                 (eq, ":party_faction", "fac_player_supporters_faction"),
                 (party_get_slot, ":town_lord", ":party_no", slot_town_lord),
                 (try_begin),
                 (gt, ":town_lord", 0),
                 (troop_get_slot, ":party_faction", ":town_lord", slot_troop_original_faction),
                 (else_try),
                 (party_get_slot, ":party_faction", ":party_no", slot_center_original_faction),
                 (try_end),
                 (try_end),

                 (faction_get_slot, ":party_template_a", ":party_faction", slot_faction_reinforcements_a),
                 (faction_get_slot, ":party_template_b", ":party_faction", slot_faction_reinforcements_b),
                 (faction_get_slot, ":party_template_c", ":party_faction", slot_faction_reinforcements_c),

                 (assign, ":party_template", 0),
                 (store_random_in_range, ":rand", 0, 100),
                 (try_begin),
                 (this_or_next | eq, ":party_type", spt_town),
                 (eq, ":party_type", spt_castle),  # CASTLE OR TOWN
                 (try_begin),
                 (lt, ":rand", 65),
                 (assign, ":party_template", ":party_template_a"),
                 (else_try),
                 (assign, ":party_template", ":party_template_b"),
                 (try_end),
                 (else_try),
                 (this_or_next|eq, ":party_type", spt_kingdom_hero_party),
                 (eq, ":party_type", spt_patrol),
                 (try_begin),
                 (lt, ":rand", 50),
                 (assign, ":party_template", ":party_template_a"),
                 (else_try),
                 (lt, ":rand", 75),
                 (assign, ":party_template", ":party_template_b"),
                 (else_try),
                 (assign, ":party_template", ":party_template_c"),
                 (try_end),
                 (else_try),
                 (try_end),

                 (try_begin),
                 (gt, ":party_template", 0),
                 (party_add_template, ":party_no", ":party_template"),
                 (try_end),
             ]),
            ("get_prisoner_prices",[
                 (store_script_param_1, ":troop_id"),
                 (store_script_param_2, ":size"),
                 (store_character_level, ":troop_level", ":troop_id"),
                 (assign, ":ransom_amount", ":troop_level"),
                 (val_add, ":ransom_amount", 10),
                 (val_mul, ":ransom_amount", ":ransom_amount"),
                 (val_div, ":ransom_amount", 6),
                 (val_mul,":ransom_amount",":size"),
                 (assign, reg0, ":ransom_amount"),
             ]),
            ("update_center_wealth",[
                 (store_script_param_1, ":center_no"),
                 (store_script_param_2, ":value"),
                 ## 0:失去钱 1：获得钱
                 (store_script_param, ":type",3),

                 (troop_get_slot,":wealth",":center_no",slot_town_wealth),
                 (try_begin),
                     (gt,":type",0),
                     (val_add,":wealth",":value"),
                 (else_try),
                    (val_sub,":wealth",":value"),
                 (try_end),
                 (troop_set_slot,":center_no",slot_town_wealth,":wealth"),
             ]),
            ("create_patrol_party",[
                (store_script_param, ":center_no", 1),
                (store_script_param, ":strength_val", 2),

                 (store_faction_of_party,":party_faction",":center_no"),
                (set_spawn_radius, 10),
                (spawn_around_party, ":center_no", "pt_kingdom_hero_party"),
                (assign, ":new_party", reg0),

                (party_set_faction, ":new_party", ":party_faction"),
                ##(party_set_slot, ":new_party", slot_party_home_center, ":center_no"),

                (party_set_slot, ":new_party", slot_party_type, spt_patrol),
                (party_set_slot, ":new_party", slot_party_ai_state, spai_patrolling_around_center),
                (party_set_slot, ":new_party", slot_party_ai_object, ":center_no"),
                (party_set_ai_behavior, ":new_party", ai_bhvr_patrol_party),
                (party_set_ai_object, ":new_party", ":center_no"),
                (party_set_flags, ":new_party", pf_default_behavior, 0),
                (party_set_slot, ":new_party", slot_party_protect_center, ":center_no"),
                (str_store_party_name,s5,":center_no"),
                (party_set_name, ":new_party", "str_s5_s_patrol_party"),
                ## 增加士兵
                (try_for_range, ":unused", 0, ":strength_val"),
                  (call_script, "script_reinforce_party", ":new_party"),
                (try_end),
                ## 增加经验
                (store_mul,":xp_addition_for_centers",":strength_val",2500),
                (party_upgrade_with_xp, ":new_party", ":xp_addition_for_centers", 0),
                (assign, reg0, ":new_party"),
                (try_end),
              ]),
            ("update_patrol_partys_for_all",[
                ## 领地巡逻队
                (try_for_range,":center_no",centers_begin,centers_end),
                    (this_or_next|party_slot_eq,":center_no",slot_party_type,spt_town),
                    (this_or_next|party_slot_eq,":center_no",slot_party_type,spt_castle),
                    (party_slot_eq,":center_no",slot_party_type,spt_village),

                    ## 排除玩家领地（玩家巡逻队需要玩家自己创建）
                    (neg|party_slot_eq,":center_no",slot_town_lord,"trp_player"),

                    ## 计算需要创建的部队数量和每个巡逻队的军事强度
                    (assign,":need_create_party_num",0),
                    (assign,":strength",0),
                    (party_get_slot,":center_patrol_num",":center_no",slot_party_patrol_num),
                    (try_begin),
                        (party_slot_eq,":center_no",slot_party_type,spt_town),
                        (try_begin),
                            (party_get_slot,":leader",":center_no",slot_town_lord),
                            (is_between,":leader",kings_begin,kings_end),
                            (store_sub,":need_create_party_num",capital_town_patrol_max_num,":center_patrol_num"),
                            (assign,":strength",capital_town_patrol_strength),
                        (else_try),
                            (store_sub,":need_create_party_num",town_patrol_max_num,":center_patrol_num"),
                            (assign,":strength",town_patrol_strength),
                        (try_end),
                    (else_try),
                        (party_slot_eq,":center_no",slot_party_type,spt_castle),
                        (store_sub,":need_create_party_num",castle_patrol_max_num,":center_patrol_num"),
                        (assign,":strength",castle_patrol_strength),
                    (else_try),
                        (store_sub,":need_create_party_num",village_patrol_max_num,":center_patrol_num"),
                        (assign,":strength",village_patrol_strength),
                    (try_end),
                    (try_for_range,":i",0,":need_create_party_num"),
                        ## 在指定地方创建巡逻队
                        (call_script,"script_create_patrol_party", ":center_no", ":strength"),
                        (str_store_party_name,s1,":center_no"),
                        (display_message,"@create :{s1} patrol party"),
                        ## 更新创建的队数量，以免重复创建
                        (val_add,":center_patrol_num",1),
                        (party_set_slot,":center_no",slot_party_patrol_num,":center_patrol_num"),
                    (try_end),
                (try_end),
                ## 维护巡逻队
                ## 1.处理俘虏（本国招降，它国贩卖）
                ## 2.补充士兵(不会一次补足)
                ## 3.升级士兵
                (try_for_parties,":party_no"),
                    (party_slot_eq,":party_no",slot_party_type,spt_patrol),
                    ##(party_is_active,":party_no"),
                    ## 【处理俘虏】
                    (party_get_num_prisoners,":pri_size",":party_no"),
                    (try_begin),
                        (gt,":pri_size",0),
                        (store_faction_of_party,":party_faction",":party_no"),
                        (party_get_num_prisoner_stacks,":stack",":party_no"),
                        (assign,":total_price",0),
                        (try_for_range_backwards,":index",0,":stack"),
                            (party_prisoner_stack_get_troop_id,":troop",":party_no",":index"),
                            (store_faction_of_troop,":troop_faction",":troop"),
                            ## 本栏中俘虏的个数
                            (party_prisoner_stack_get_size,":cur_stack_size",":party_no",":index"),
                            (try_begin),
                                (str_store_faction_name,s1,":party_faction"),
                                (str_store_faction_name,s2,":troop_faction"),
                                (str_store_troop_name,s3,":troop"),
                                #(display_message,"@party faction name ({s1})     troop faction name ({s2} troop:{s3})"),
                                ## 本国招募
                                (eq,":party_faction",":troop_faction"),
                                ## 添加同伴
                                (party_add_members,":party_no",":troop",":cur_stack_size"),
                                (str_store_party_name,s1,":party_no"),
                                (str_store_troop_name,s2,":troop"),
                                (assign,reg1,":cur_stack_size"),
                                #(display_message,"@do add troops({reg1}):{s1}"),
                            (else_try),
                                ## 它国贩卖
                                (call_script,"script_get_prisoner_prices",":troop",":cur_stack_size"),
                                (assign,":pri_price",reg0),
                                (val_add,":total_price",":pri_price"),
                            (try_end),
                            ## 移除俘虏
                            (party_remove_prisoners,":party_no",":troop",":cur_stack_size"),
                            (str_store_party_name,s1,":party_no"),
                            #(display_message,"@do remove prisoners:{s1}"),
                        (try_end),
                    (try_end),

                    (try_begin),
                        (gt,":total_price",0),
                        (call_script,"script_update_center_wealth",":center_no",":total_price",1),
                        (str_store_party_name,s1,":party_no"),
                        (assign,reg1,":total_price"),
                        #(display_message,"@add money({reg1}) :{s1}"),
                    (try_end),

                    ## 【补充士兵】
                    (assign,":need_size",0),
                    (assign,":times",0),
                    (party_get_num_companions,":cur_size",":party_no"),
                    ## 获得巡逻的据点
                    (party_get_slot, ":center_no",":party_no",slot_party_protect_center),
                    (try_begin),
                        (party_slot_eq,":center_no",slot_party_type,spt_town),
                        (store_sub,":need_size",town_patrol_min_size,":cur_size"),
                        (assign,":times",town_patrol_strength),
                    (else_try),
                        (party_slot_eq,":center_no",slot_party_type,spt_castle),
                        (store_sub,":need_size",castle_patrol_min_size,":cur_size"),
                        (assign,":times",castle_patrol_strength),
                    (else_try),
                        (party_slot_eq,":center_no",slot_party_type,spt_village),
                        (store_sub,":need_size",village_patrol_min_size,":cur_size"),
                        (assign,":times",village_patrol_strength),
                    (try_end),
                    (try_begin),
                        (assign,reg2,":need_size"),
                        #(display_message,"@need size {reg2}"),
                        (gt,":need_size",0),
                        #(party_slot_ge,":center_no",slot_town_wealth,500),
                        (call_script, "script_update_center_wealth", ":center_no",500,-1),
                        (call_script, "script_reinforce_party", ":party_no"),
                        (str_store_party_name,s1,":party_no"),
                        #(display_message,"@add party:{s1}"),
                    (try_end),
                    ## 【升级士兵】
                    (store_mul,":xp",":times",100),
                    (party_upgrade_with_xp, ":party_no", ":xp", 0),
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
            ## 统计被打败的队伍,从slot中减去
            # ("",[
            #
            # ]),
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