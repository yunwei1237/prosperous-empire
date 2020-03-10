# -*- coding: utf-8 -*-

from module_scripts import *


'''

patrol party
'''

## constans
capital_town_patrol_max_num = 6
town_patrol_max_num = 4
castle_patrol_max_num = 2
village_patrol_max_num = 1

town_patrol_min_size = 80
castle_patrol_min_size = 60
village_patrol_min_size = 40

capital_town_patrol_strength = 8
town_patrol_strength = 6
castle_patrol_strength = 4
village_patrol_strength = 2

## party slot
slot_party_patrol_num     = 400
slot_party_protect_center = 401

'''
    巡逻队
'''
spt_patrol             = 7

patrolParty = {
    "name":"patrol party",
    "strings":[{
        "s5_s_patrol_party":"{s5}'s patrol Party",
    }],
    "map_trigger":[
        (24,[
            (call_script,"script_update_patrol_partys_for_all"),
        ]),
    ],
    "scripts":[
        ("get_prisoner_prices",
         [
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
        ("update_center_wealth",
         [
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
        ("create_patrol_party",
         [
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
              (call_script, "script_cf_reinforce_party", ":new_party"),
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
                (this_or_next|party_slot_eq,":center_no",slot_party_type,spt_village),

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
            (try_end),
            (try_end),
            ## 维护巡逻队
            ## 1.处理俘虏（本国招降，它国贩卖）
            ## 2.补充士兵(不会一次补足)
            ## 3.升级士兵
            (try_for_parties,":party_no"),
                (party_slot_eq,":party_no",slot_party_type,spt_patrol),
                ## 【处理俘虏】
                (party_get_num_prisoners,":pri_size",":party_no"),
                (try_begin),
                (gt,":pri_size",0),
                (party_get_slot,":troop_faction",":party_no",slot_center_original_faction),
                (party_get_num_prisoner_stacks,":stack",":party_no"),
                (assign,":total_price",0),
                (try_for_range_backwards,":index",0,":stack"),
                    (party_stack_get_troop_id,":troop",":index"),
                    (store_faction_of_party,":troop_faction",":troop"),
                    ## 本栏中俘虏的个数
                    (party_stack_get_size,":cur_stack_size",":index"),
                    (try_begin),
                        ## 本国招募
                        (party_slot_eq,":party_no",slot_center_original_faction,":troop_faction"),
                        ## 添加同伴
                        (party_add_members,":party_no",":troop",":cur_stack_size"),
                    (else_try),
                        ## 它国贩卖
                        (call_script,"script_get_prisoner_prices",":troop",":cur_stack_size"),
                        (assign,":pri_price",reg0),
                        (val_add,":total_price",":pri_price"),
                    (try_end),
                    ## 移除俘虏
                    (party_remove_prisoners,":party_no",":troop",":cur_stack_size"),
                (try_end),
                (try_begin),
                    (gt,":total_price",0),
                    (call_script,"script_update_center_wealth",":center_no",":total_price",1),
                (try_end),
                ## 【补充士兵】
                (assign,":need_size",0),
                (assign,":times",0),
                (party_get_num_companions,":cur_size",":party_no"),
                ## 获得巡逻的据点
                (party_get_slot, ":center_no",slot_party_protect_center, ":party_no"),
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
                    (lt,":cur_size",":need_size"),
                    (call_script, "script_update_center_wealth", ":center_no",500,-1),
                    (call_script, "script_cf_reinforce_party", ":party_no"),
                    ## 【升级士兵】
                    (store_mul,":xp",":times",100),
                    (party_upgrade_with_xp, ":party_no", ":xp", 0),
                (try_end),
            (try_end),
        ])
    ],
}