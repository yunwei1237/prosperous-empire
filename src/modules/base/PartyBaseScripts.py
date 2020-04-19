# -*- coding: utf-8 -*-

## 包含一些对队伍常用的操作
from header_operations import *
from header_parties import *
from header_skills import skl_trainer
from module_constants import *







## slot
## 用于保存巡逻的据点
from smart_module_slot import getPartySlotNo

slot_party_protect_center = getPartySlotNo("slot_party_protect_center")


## args
## 巡逻队类型
spt_patrol             = 7

## args


per_strength_xp = 100


partyBaseScripts={
    "name":"PartyBaseScripts",
    "enable":True,
    "scripts":{
        "append":[
            ## 创建部队通用方法
            ("create_party",[
                ## 领导者
                (store_script_param, ":leader_no", 1),
                ## 创建在哪个地区附近
                (store_script_param, ":center_no", 2),
                ## 队伍阵营，优先使用领导者阵营，其次才会使用据点阵营，否则就是平民阵营
                (store_script_param, ":faction_no", 3),
                ## 范围
                (store_script_param, ":spawn_radius", 4),
                ## 队伍名称id（优先使用队伍领导者名称，其实使用据点名称，最后使用国家名称)
                (store_script_param, ":party_name", 5),
                ## 队伍类型
                (store_script_param, ":party_type", 6),
                ## 图标
                (store_script_param, ":map_icon", 7),
                ## 旗帜
                (store_script_param, ":map_banner", 8),

                (try_begin),
                    (lt,":center_no",0),
                    (assign,":center_no","p_main_party"),
                (try_end),

                (try_begin),
                    (lt,":faction_no",0),
                    (try_begin),
                        (ge,":leader_no",0),
                        (store_faction_of_troop,":faction_no",":leader_no"),
                    (else_try),
                        (ge,":center_no",0),
                        (store_faction_of_party,":faction_no",":center_no"),
                    (else_try),
                        (assign,":faction_no","fac_commoners"),
                    (try_end),
                (try_end),

                (try_begin),
                    (lt,":spawn_radius",0),
                    (assign,":spawn_radius",3),
                (try_end),

                (set_spawn_radius, ":spawn_radius"),
                (spawn_around_party, ":center_no", "pt_kingdom_hero_party"),
                (assign, ":new_party", reg0),
                ## 设置阵营
                (party_set_faction, ":new_party", ":faction_no"),
                (party_set_flags, ":new_party", pf_default_behavior, 0),

                (try_begin),
                    (ge,":leader_no",0),
                    ## 设置领导的队伍
                    (troop_set_slot,":leader_no",slot_troop_leaded_party,":new_party"),
                    ## 添加领导者
                    (party_add_leader,":new_party",":leader_no"),
                (try_end),

                (try_begin),
                    (ge,":leader_no",0),
                    (str_store_troop_name,s5,":leader_no"),
                (else_try),
                    (ge,":center_no",0),
                    (str_store_party_name,s5,":center_no"),
                (else_try),
                    (ge,":faction_no",0),
                    (str_store_faction_name,s5,":faction_no"),
                (try_end),

                ## 设置队伍名称
                (try_begin),
                (ge,":party_name",0),
                    (party_set_name, ":new_party", ":party_name"),
                (else_try),
                    (party_set_name, ":new_party", "str_s5_s_party"),
                (try_end),

                (try_begin),
                    (ge,":party_type",0),
                    (party_set_slot,":new_party",slot_party_type,":party_type"),
                (try_end),

                ## 设置指定外观
                (try_begin),
                    (ge,":map_icon",0),
                    (party_set_icon,":new_party",":map_icon"),
                (try_end),

                ## 设置指定旗帜
                (try_begin),
                    (ge,":map_banner",0),
                    (party_set_banner_icon,":new_party",":map_banner"),
                (try_end),
                (assign, reg0, ":new_party"),
              ]),

            ("party_add_members", [
                (store_script_param, ":party_no",1),
                (store_script_param, ":faction_no",2),
                ## 军事强度
                (store_script_param, ":strength",3),
                ## 队伍模板，
                ## -1,使用阵营士兵模板
                ## 指定模板时，使用指定模板添加士兵
                (store_script_param, ":party_template", 4),
                ## 初级士兵概率（值最大为100）
                (store_script_param, ":primary_probability",5),
                ## 中级士兵概率（值最大为100）
                (store_script_param, ":intermediate_probability",6),
                ## 高级士兵概念（高级 = 100 - 初级 - 中级）
                #(store_script_param, ":advanced_probability",6),

                (try_begin),
                    (lt,":faction_no",0),
                    (store_faction_of_party,":faction_no",":party_no"),
                (try_end),

                (try_begin),
                    (le,":strength",0),
                    (assign,":strength",1),
                (try_end),

                ## 处理模板
                (try_begin),
                    ## 默认模板时，使用阵营士兵模板
                    (lt,":party_template",0),
                    ## 计算中级士兵的概率
                    (val_add,":intermediate_probability",":primary_probability"),
                    ## 根据概率获得阵营模板
                    (store_random_in_range, ":pt_no", 0, 100),
                    (try_begin),
                        (le, ":pt_no", ":primary_probability"),
                        (faction_get_slot, ":pt_temp", ":faction_no", slot_faction_reinforcements_a),
                    (else_try),
                        (le, ":pt_no", ":intermediate_probability"),
                        (faction_get_slot, ":pt_temp", ":faction_no", slot_faction_reinforcements_b),
                    (else_try),
                        (faction_get_slot, ":pt_temp", ":faction_no", slot_faction_reinforcements_c),
                    (try_end),
                (else_try),
                    ## 使用指定模板
                    (assign,":pt_temp",":party_template"),
                (try_end),
                ## 根据模板生成士兵
                (try_for_range, ":unused", 0, ":strength"),
                    (party_add_template, ":party_no", ":pt_temp"),
                (try_end),
            ]),
            ("party_add_xp_and_upgrade",[
                (store_script_param, ":party_no",1),
                (store_script_param, ":strength",2),
                (store_script_param, ":special_arms_probability",3),

                (try_begin),
                    (gt,":strength",0),
                    ## 计算军事强度(同伴有教练技能时会增加经验)
                    (party_get_num_companion_stacks,":stack",":party_no"),
                    (try_for_range,":stack_index",0,":stack"),
                        (party_stack_get_troop_id,":troop_no",":party_no",":stack_index"),
                        (troop_is_hero,":troop_no"),
                        (store_skill_level,":trainer_level",":troop_no",skl_trainer),
                        (val_add,":strength",":trainer_level"),
                    (try_end),
                    (store_mul, ":total_xp", ":strength", per_strength_xp),

                    ## 根据特殊兵种概率来升级更加强壮的士兵，如果没有指定概率就是随机升级
                    (try_begin),
                        (gt,":special_arms_probability",0),
                        (store_random_in_range,":pro",0,100),
                        (try_begin),
                            (le,":special_arms_probability",":pro"),
                            (party_upgrade_with_xp, ":party_no", ":total_xp", 1),
                        (else_try),
                            (party_upgrade_with_xp, ":party_no", ":total_xp", 2),
                        (try_end),
                    (else_try),
                        (party_upgrade_with_xp, ":party_no", ":total_xp", 0),
                    (try_end),
                (try_end),
            ]),
            ("party_change_ai_state",[
                (store_script_param,":party",1),
                (store_script_param,":behavior",2),
                (store_script_param,":target",3),
                (store_script_param,":patrol_radius",3),

                (try_begin),
                    (le,":patrol_radius",0),
                    (assign,":patrol_radius",3),
                (try_end),

                # (party_set_slot, ":party", slot_party_ai_state, spai_patrolling_around_center),
                # (party_set_slot, ":party", slot_party_ai_object, ":target"),
                (party_set_ai_behavior, ":party", ":behavior"),
                (party_set_ai_object, ":party", ":target"),
                (party_set_ai_patrol_radius, ":party", ":patrol_radius"),
            ]),
            ## 计算俘虏价格
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
            ## 更新据点财富
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
            ("party_handle_prisoners",[
                ## 需要处理俘虏的队伍
                (store_script_param_1,":party_no"),
                ## 是否会招募俘虏  -1，全部售卖 0:招募本国士兵 1：招募全部士兵
                (store_script_param_2,":recruit"),
                (party_get_num_prisoners,":pri_size",":party_no"),
                ## 有俘虏才进行处理
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
                        ## 全部售卖
                        (eq,":recruit",-1),
                        (call_script, "script_get_prisoner_prices", ":troop", ":cur_stack_size"),
                        (assign, ":pri_price", reg0),
                        (val_add, ":total_price", ":pri_price"),
                        #(display_message,"@出售全部士兵"),
                    (else_try),
                        ## 本国招募，它国售卖
                        (eq, ":recruit", 0),
                        (try_begin),
                            (str_store_faction_name,s1,":party_faction"),
                            (str_store_faction_name,s2,":troop_faction"),
                            (str_store_troop_name,s3,":troop"),
                            #(display_message,"@party faction name ({s1})     troop faction name ({s2} troop:{s3})"),
                            ## 本国招募
                            (eq,":party_faction",":troop_faction"),
                            ## 添加同伴
                            (party_add_members,":party_no",":troop",":cur_stack_size"),
                            # (str_store_party_name,s1,":party_no"),
                            # (str_store_troop_name,s2,":troop"),
                            # (assign,reg1,":cur_stack_size"),
                            #(display_message,"@do add troops({reg1}):{s1}"),
                            #(display_message,"@招募本国士兵"),
                        (else_try),
                            ## 它国贩卖
                            (call_script,"script_get_prisoner_prices",":troop",":cur_stack_size"),
                            (assign,":pri_price",reg0),
                            (val_add,":total_price",":pri_price"),
                            #(display_message,"@售卖它国部分士兵"),
                        (try_end),
                    (else_try),
                        ## 全部招募
                        (party_add_members, ":party_no", ":troop", ":cur_stack_size"),
                        #(display_message,"@招募全部士兵"),
                    (try_end),
                    ## 将处理后的俘虏从俘虏栏中移除
                    (party_remove_prisoners,":party_no",":troop",":cur_stack_size"),
                    #(str_store_party_name,s1,":party_no"),
                    #(display_message,"@do remove prisoners:{s1}"),

                (try_end),
                (gt,":total_price",0),
                (party_stack_get_troop_id,":leader",":party_no",0),
                (try_begin),
                    (ge,":leader",0),
                    (call_script, "script_update_lord_wealth", ":leader", ":total_price", 1),
                (else_try),
                    (party_slot_eq,":party_no",slot_party_type,spt_patrol),
                    (party_get_slot,":center",":party_no",slot_party_protect_center),
                    (call_script,"script_update_center_wealth",":center",":total_price",1),
                (else_try),
                    (store_faction_of_party,":faction",":party_no"),
                    (faction_get_slot,":king",":faction",slot_faction_leader),
                    (call_script, "script_update_lord_wealth", ":king", ":total_price", 1),
                (try_end),
            ]),
            ## 获得指定队伍附近指定类型的队伍
            ("get_the_nearby_center",[
                ## 当前队伍
                (store_script_param_1,":cur_party"),
                ## 最近队伍的类型(如：附近的村庄（spt_village），附近的城堡（spt_castle），附近的城镇（spt_town）)
                (store_script_param_2,":party_type"),
                (assign,":min",99999999),
                (assign,":close_center",":cur_party"),
                (try_for_range,":center_no",centers_begin,centers_end),
                    ## 过滤指定类型
                    (party_slot_eq,":center_no",slot_party_type,":party_type"),
                    ## 获得据点之间的距离
                    (store_distance_to_party_from_party,":distance",":center_no",":cur_party"),
                    (le,":distance",":min"),
                    (assign,":min",":distance"),
                    (assign,":close_center",":center_no"),
                (try_end),
                (assign,reg0,":close_center"),
            ]),
            ## 获得一个阵营全部的据点
            ("get_all_center_arr_of_faction", [
                (store_script_param_1, ":faction"),
                (assign, ":size", 0),
                (assign, ":index", 0),
                (try_for_range, ":center", centers_begin, centers_end),
                (this_or_next | party_slot_eq, ":center", slot_party_type, spt_town),
                (this_or_next | party_slot_eq, ":center", slot_party_type, spt_castle),
                (party_slot_eq, ":center", slot_party_type, spt_village),
                (store_faction_of_party, ":party_faction", ":center"),
                (eq, ":party_faction", ":faction"),
                # (store_sub,":offset",":center",centers_begin),
                ## 跳过0下标，下标为0的位置用于存放据点的个数
                (val_add, ":index", 1),
                (party_set_slot, "p_temp_party", ":index", ":center"),
                (val_add, ":size", 1),
                (try_end),
                (party_set_slot, "p_temp_party", 0, ":size"),
            ]),
            ("add_party_as_companions",
                [
                  (store_script_param, ":target_party",1), #Target Party_id
                  (store_script_param, ":source_party",2), #Source Party_id
                  ## 英雄是否也加入： -1代表只加入士兵，大于等于0代表英雄加入
                  (store_script_param, ":include_hero",3), #Source Party_id
                  (party_get_num_companion_stacks, ":num_stacks",":source_party"),
                  (try_for_range, ":stack_no", 0, ":num_stacks"),
                    (party_stack_get_troop_id, ":stack_troop",":source_party",":stack_no"),
                    (assign,":hero_can_join",0),
                    (try_begin),
                        (troop_is_hero,":stack_troop"),
                        (ge,":include_hero",0),
                        (assign,":hero_can_join",1),
                    (try_end),
                    ## 非英雄
                    (this_or_next|neg|troop_is_hero,":stack_troop"),
                    ## 或者 是英雄，也允许英雄加入
                    (eq,":hero_can_join",1),
                    (party_stack_get_size, ":stack_size",":source_party",":stack_no"),
                    (party_add_members, ":target_party", ":stack_troop", ":stack_size"),

                    (party_stack_get_num_wounded, ":num_wounded", ":source_party", ":stack_no"),
                    (party_wound_members, ":target_party", ":stack_troop", ":num_wounded"),

                    (str_store_troop_name,s6,":stack_troop"),
                    (try_begin),
                        (troop_is_hero,":stack_troop"),
                        (display_message, "@{s6} has joined your party."),
                    (else_try),
                        (assign,reg1,":stack_size"),
                        (display_message, "@{reg1} {s6} join your party."),
                    (try_end),
                  (try_end),
                  (remove_party,":source_party"),
              ]),

            ("get_loard_all_centers",[
                (store_script_param_1,":target_troop"),
                (store_script_param_2,":source_troop"),
                (try_for_range,":center",centers_begin,centers_end),
                    (party_slot_eq,":center",slot_town_lord,":source_troop"),
                    (call_script,"script_give_center_to_lord",":center",":target_troop",1),
                (try_end),
            ]),
            ("get_center_of_lord",[
                (store_script_param_1,":lord"),
                (store_script_param_2,":default_center"),
                (assign,":town",":default_center"),
                (assign,":castle",":default_center"),
                (assign,":village",":default_center"),
                (try_for_range,":center",centers_begin,castles_end),
                    (party_slot_eq,":center",slot_town_lord,":lord"),
                    (try_begin),
                        (party_slot_eq,":center",slot_party_type,spt_town),
                        (assign,":town",":center"),
                    (else_try),
                        (party_slot_eq,":center",slot_party_type,spt_castle),
                        (assign,":castle",":center"),
                    (else_try),
                        (party_slot_eq,":center",slot_party_type,spt_village),
                        (assign,":village",":center"),
                    (try_end),
                (try_end),

                (try_begin),
                    (ge,":town",0),
                    (assign,reg0,":town"),
                (else_try),
                    (ge, ":castle", 0),
                    (assign, reg0, ":castle"),
                (else_try),
                    (ge, ":village", 0),
                    (assign, reg0, ":village"),
                (try_end),
            ]),
            ("get_party_max_skill",[
                (store_script_param_1,":party_no"),
                (store_script_param_2,":skill_id"),
                (assign,":max_level",0),
                (party_get_num_companion_stacks,":stacks",":party_no"),
                (try_for_range,":stack_i",0,":stacks"),
                    (party_stack_get_troop_id,":troop_no",":party_no",":stack_i"),
                    (troop_is_hero,":troop_no"),
                    (store_skill_level,":skill_level",":troop_no",":skill_id"),
                    (gt,":skill_level",":max_level"),
                    (assign,":max_level",":skill_level"),
                (try_end),
                (assign,reg0,":max_level"),
            ]),
        ],
    },
    "internationals":{
        "cns":{
            "game_strings":
                [
                    "str_s5_leave_home|{s5}出 门 了",
                    "str_s5_go_home|{s5}回 家 了",
                    "str_s1_s2_name|{s1}{s2}",
                ],
            "quick_strings":[
                "qstr_{reg1}_{s6}_join_your|{reg1} 个 {s6} 加 入 到 你 的 了 队 伍。",
            ],
        }
    }
}