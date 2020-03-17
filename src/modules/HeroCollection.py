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
    "enable":False,
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
            # Respawn hero party after kingdom hero is released from captivity.
            (48,
             [
                (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
                    (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),

                    (str_store_troop_name, s1, ":troop_no"),

                    (neg | troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
                    (neg | troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),

                    (store_troop_faction, ":cur_faction", ":troop_no"),
                    (try_begin),
                        (eq, ":cur_faction", "fac_outlaws"),  # Do nothing
                    (else_try),
                         (try_begin),
                             (eq, "$cheat_mode", 2),
                             (str_store_troop_name, s4, ":troop_no"),
                             (display_message, "str_debug__attempting_to_spawn_s4"),
                         (try_end),

                         (call_script, "script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege",
                          ":cur_faction", ":troop_no"),  # Can fail
                         (assign, ":center_no", reg0),

                         (try_begin),
                             (eq, "$cheat_mode", 2),
                             (str_store_party_name, s7, ":center_no"),
                             (str_store_troop_name, s0, ":troop_no"),
                             (display_message, "str_debug__s0_is_spawning_around_party__s7"),
                         (try_end),

                         (call_script, "script_create_kingdom_hero_party", ":troop_no", ":center_no"),

                         (try_begin),
                             (eq, "$g_there_is_no_avaliable_centers", 0),
                             (party_attach_to_party, "$pout_party", ":center_no"),
                         (try_end),

                         # new
                         # (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                         # (call_script, "script_npc_decision_checklist_party_ai", ":troop_no"), #This handles AI for both marshal and other parties
                         # (call_script, "script_party_set_ai_state", ":party_no", reg0, reg1),
                         # new end

                         (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                         (call_script, "script_party_set_ai_state", ":party_no", spai_holding_center, ":center_no"),

                    (else_try),
                         (neg | faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
                         (try_begin),
                             (is_between, ":troop_no", kings_begin, kings_end),
                             (troop_set_slot, ":troop_no", slot_troop_change_to_faction, "fac_commoners"),
                         (else_try),
                             (store_random_in_range, ":random_no", 0, 100),
                             (lt, ":random_no", 10),
                             (call_script, "script_cf_get_random_active_faction_except_player_faction_and_faction", ":cur_faction"),
                             (troop_set_slot, ":troop_no", slot_troop_change_to_faction, reg0),
                         (try_end),
                    (try_end),
                (try_end),
             ]),
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