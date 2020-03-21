# -*- coding: utf-8 -*-

## 包含一些对队伍常用的操作
from header_operations import *
from header_parties import *
from header_skills import skl_trainer
from module_constants import *



## args


per_strength_xp = 100


partyBaseScripts={
    "name":"PartyBaseScripts",
    "enable":True,
    "scripts":{
        "append":[
            ## 创建部队通用方法
            ("create_party",[
                (store_script_param, ":leader_no", 1),
                (store_script_param, ":center_no", 2),
                (store_script_param, ":faction_no", 3),
                (store_script_param, ":spawn_radius", 4),
                (store_script_param, ":party_name", 5),

                (try_begin),
                    (lt,":center_no",0),
                    (assign,":center_no","p_main_party"),
                (try_end),

                (try_begin),
                    (lt,":faction_no",0),
                    (store_faction_of_party,":faction_no",":leader_no"),
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
                (str_store_string,s6,":party_name"),
                (try_begin),
                    (ge,":leader_no",0),
                    ## 设置领导的队伍
                    (troop_set_slot,":leader_no",slot_troop_leaded_party,":new_party"),
                    ## 添加领导者
                    (party_add_leader,":new_party",":leader_no"),
                    ## 设置队伍名称为领导者队伍
                    (str_store_troop_name,s5,":leader_no"),
                    (str_store_string,s6,"str_s5_s_party"),
                (try_end),
                ## 设置队伍名称
                (party_set_name, ":new_party", s6),
                (assign, reg0, ":new_party"),
              ]),

            ("party_add_members", [
                (store_script_param_1, ":party_no"),
                (store_script_param_2, ":faction_no"),
                (store_script_param, ":strength",3),
                ## 初级士兵概率（值最大为100）
                (store_script_param, ":primary_probability",4),
                ## 中级士兵概率（值最大为100）
                (store_script_param, ":intermediate_probability",5),
                ## 高级士兵概念（高级 = 100 - 初级 - 中级）
                #(store_script_param, ":advanced_probability",6),

                (try_begin),
                    (lt,":faction_no",0),
                    (store_faction_of_party,":faction_no",":party_no"),
                (try_end),

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
                (try_for_range, ":unused", 0, ":strength"),
                    (party_add_template, ":party_no", ":pt_temp"),
                (try_end),
            ]),
            ("party_add_xp_and_upgrade",[
                (store_script_param_1, ":party_no"),
                (store_script_param_2, ":strength"),
                (store_script_param, ":special_arms_probability",3),

                ## 计算军事强度(同伴有教练技能时会增加经验)
                (party_get_num_companion_stacks,":stack",":party_no"),
                (try_for_range,":stack_index",0,":stack"),
                    (party_stack_get_troop_id,":troop_no",":party_no",":stack_index"),
                    (troop_is_hero,":troop_no"),
                    (store_skill_level,":trainer_level",":troop_no",skl_trainer),
                    (val_add,":strength",":trainer_level"),
                (try_end),
                (store_mul, ":total_xp", ":strength_val", per_strength_xp),

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
            ]),
        ],
    }
}