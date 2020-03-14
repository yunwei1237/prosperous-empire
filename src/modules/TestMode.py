# -*- coding: utf-8 -*-

from header_game_menus import *
from header_mission_templates import *
from module_mission_templates import *

testMode = {
    "name":"testMode",
    "enable":True,
    "mission_templates":{
        "create_mission_templates":[
            (
                "my_lead_charge", mtf_battle_mode | mtf_synch_inventory, charge,
                "You lead your men to battle.",
                [
                    (1, mtef_defenders | mtef_team_0, 0, aif_start_alarmed, 12, []),
                    (0, mtef_defenders | mtef_team_0, 0, aif_start_alarmed, 0, []),
                    (4, mtef_attackers | mtef_team_1, 0, aif_start_alarmed, 12, []),
                    (4, mtef_attackers | mtef_team_1, 0, aif_start_alarmed, 0, []),
                ],
                [
                    (ti_on_agent_spawn, 0, 0, [],
                     [
                         (store_trigger_param_1, ":agent_no"),
                         (call_script, "script_agent_reassign_team", ":agent_no"),

                         (assign, ":initial_courage_score", 5000),

                         (agent_get_troop_id, ":troop_id", ":agent_no"),
                         (store_character_level, ":troop_level", ":troop_id"),
                         (val_mul, ":troop_level", 35),
                         (val_add, ":initial_courage_score", ":troop_level"),  # average : 20 * 35 = 700

                         (store_random_in_range, ":randomized_addition_courage", 0, 3000),  # average : 1500
                         (val_add, ":initial_courage_score", ":randomized_addition_courage"),

                         (agent_get_party_id, ":agent_party", ":agent_no"),
                         (party_get_morale, ":cur_morale", ":agent_party"),

                         (store_sub, ":morale_effect_on_courage", ":cur_morale", 70),
                         (val_mul, ":morale_effect_on_courage", 30),  # this can effect morale with -2100..900
                         (val_add, ":initial_courage_score", ":morale_effect_on_courage"),

                         # average = 5000 + 700 + 1500 = 7200; min : 5700, max : 8700
                         # morale effect = min : -2100(party morale is 0), average : 0(party morale is 70), max : 900(party morale is 100)
                         # min starting : 3600, max starting  : 9600, average starting : 7200
                         (agent_set_slot, ":agent_no", slot_agent_courage_score, ":initial_courage_score"),
                     ]),

                    common_battle_init_banner,

                    (ti_on_agent_killed_or_wounded, 0, 0, [],
                     [
                         (store_trigger_param_1, ":dead_agent_no"),
                         (store_trigger_param_2, ":killer_agent_no"),
                         (store_trigger_param_3, ":is_wounded"),

                         (try_begin),
                         (ge, ":dead_agent_no", 0),
                         (neg | agent_is_ally, ":dead_agent_no"),
                         (agent_is_human, ":dead_agent_no"),
                         (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
                         ##          (str_store_troop_name, s6, ":dead_agent_troop_id"),
                         ##          (assign, reg0, ":dead_agent_no"),
                         ##          (assign, reg1, ":killer_agent_no"),
                         ##          (assign, reg2, ":is_wounded"),
                         ##          (agent_get_team, reg3, ":dead_agent_no"),
                         # (display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"),
                         (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1),
                         # addition_to_p_total_enemy_casualties
                         (eq, ":is_wounded", 1),
                         (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1),
                         (try_end),

                         (call_script, "script_apply_death_effect_on_courage_scores", ":dead_agent_no",
                          ":killer_agent_no"),
                     ]),

                    common_battle_tab_press,

                    (ti_question_answered, 0, 0, [],
                     [(store_trigger_param_1, ":answer"),
                      (eq, ":answer", 0),
                      (assign, "$pin_player_fallen", 0),
                      (try_begin),
                      (store_mission_timer_a, ":elapsed_time"),
                      (gt, ":elapsed_time", 20),
                      (str_store_string, s5, "str_retreat"),
                      (call_script, "script_simulate_retreat", 10, 20, 1),
                      (try_end),
                      (call_script, "script_count_mission_casualties_from_agents"),
                      (finish_mission, 0), ]),

                    (ti_before_mission_start, 0, 0, [],
                     [
                         (team_set_relation, 0, 2, 1),
                         (team_set_relation, 1, 3, 1),
                         (call_script, "script_place_player_banner_near_inventory_bms"),

                         (party_clear, "p_routed_enemies"),

                         (assign, "$g_latest_order_1", 1),
                         (assign, "$g_latest_order_2", 1),
                         (assign, "$g_latest_order_3", 1),
                         (assign, "$g_latest_order_4", 1),
                     ]),

                    (0, 0, ti_once, [], [(assign, "$g_battle_won", 0),
                                         (assign, "$defender_reinforcement_stage", 0),
                                         (assign, "$attacker_reinforcement_stage", 0),
                                         (call_script, "script_place_player_banner_near_inventory"),
                                         (call_script, "script_combat_music_set_situation_with_culture"),
                                         (assign, "$g_defender_reinforcement_limit", 2),
                                         ]),

                    common_music_situation_update,
                    common_battle_check_friendly_kills,

                    (1, 0, 5, [

                        # new (25.11.09) starts (sdsd = TODO : make a similar code to also helping ally encounters)
                        # count all total (not dead) enemy soldiers (in battle area + not currently placed in battle area)
                        (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
                        (assign, ":total_enemy_soldiers", reg0),

                        # decrease number of agents already in battle area to find all number of reinforcement enemies
                        (assign, ":enemy_soldiers_in_battle_area", 0),
                        (try_for_agents, ":cur_agent"),
                        (agent_is_human, ":cur_agent"),
                        (agent_get_party_id, ":agent_party", ":cur_agent"),
                        (try_begin),
                        (neq, ":agent_party", "p_main_party"),
                        (neg | agent_is_ally, ":cur_agent"),
                        (val_add, ":enemy_soldiers_in_battle_area", 1),
                        (try_end),
                        (try_end),
                        (store_sub, ":total_enemy_reinforcements", ":total_enemy_soldiers",
                         ":enemy_soldiers_in_battle_area"),

                        (try_begin),
                        (lt, ":total_enemy_reinforcements", 15),
                        (ge, "$defender_reinforcement_stage", 2),
                        (eq, "$defender_reinforcement_limit_increased", 0),
                        (val_add, "$g_defender_reinforcement_limit", 1),
                        (assign, "$defender_reinforcement_limit_increased", 1),
                        (try_end),
                        # new (25.11.09) ends

                        (lt, "$defender_reinforcement_stage", "$g_defender_reinforcement_limit"),
                        (store_mission_timer_a, ":mission_time"),
                        (ge, ":mission_time", 10),
                        (store_normalized_team_count, ":num_defenders", 0),
                        (lt, ":num_defenders", 6)],
                     [(add_reinforcements_to_entry, 0, 7), (assign, "$defender_reinforcement_limit_increased", 0),
                      (val_add, "$defender_reinforcement_stage", 1)]),

                    (1, 0, 5, [(lt, "$attacker_reinforcement_stage", 2),
                               (store_mission_timer_a, ":mission_time"),
                               (ge, ":mission_time", 10),
                               (store_normalized_team_count, ":num_attackers", 1),
                               (lt, ":num_attackers", 6)],
                     [(add_reinforcements_to_entry, 3, 7), (val_add, "$attacker_reinforcement_stage", 1)]),

                    ##common_battle_check_victory_condition,
                    ##common_battle_victory_display,

                    (1, 4, ti_once, [(main_hero_fallen)],
                     [
                         (assign, "$pin_player_fallen", 1),
                         (str_store_string, s5, "str_retreat"),
                         (call_script, "script_simulate_retreat", 10, 20, 1),
                         (assign, "$g_battle_result", -1),
                         (set_mission_result, -1),
                         (call_script, "script_count_mission_casualties_from_agents"),
                         (finish_mission, 0)]),

                    common_battle_inventory,

                    # AI Triggers
                    (0, 0, ti_once, [
                        (store_mission_timer_a, ":mission_time"), (ge, ":mission_time", 2),
                    ],
                     [(call_script, "script_select_battle_tactic"),
                      (call_script, "script_battle_tactic_init"),
                      # (call_script, "script_battle_calculate_initial_powers"), #deciding run away method changed and that line is erased
                      ]),

                    (3, 0, 0, [
                        (call_script, "script_apply_effect_of_other_people_on_courage_scores"),
                    ], []),  # calculating and applying effect of people on others courage scores

                    (3, 0, 0, [
                        (try_for_agents, ":agent_no"),
                        (agent_is_human, ":agent_no"),
                        (agent_is_alive, ":agent_no"),
                        (store_mission_timer_a, ":mission_time"),
                        (ge, ":mission_time", 3),
                        (call_script, "script_decide_run_away_or_not", ":agent_no", ":mission_time"),
                        (try_end),
                    ], []),  # controlling courage score and if needed deciding to run away for each agent

                    (5, 0, 0, [
                        (store_mission_timer_a, ":mission_time"),

                        (ge, ":mission_time", 3),

                        (call_script, "script_battle_tactic_apply"),
                    ], []),  # applying battle tactic

                    common_battle_order_panel,
                    common_battle_order_panel_tick,

                ],
            ),
        ],
    },
    "game_menus":{
        "create_game_menus":[
            ("just_test_menu",menu_text_color(0xFF000000)|mnf_disable_all_keys,
                "this just a test menu.",
                "none",
                [],
                [
                  ("go_back",[],"Go back",
                   [
                     (change_screen_quit),
                   ]),
                ]
              ),
        ],
        "add_game_menu_options":{
            "start_game_0":{
                "after":{
                    "continue":[
                        ("test_alley",[],"TEST 【alley】",
                         [
                            (call_script,"script_start_test_palyer"),
                        ]),
                        ("test_map",[],"TEST 【map】",
                         [
                             (troop_set_name,"trp_player","@test"),
                             (party_set_name,"p_main_party","@test"),

                            (troop_add_item, "trp_player", "itm_saddle_horse", 0),
                            (troop_add_item, "trp_player", "itm_courser", 0),
                            (troop_add_item, "trp_player", "itm_courtly_outfit", 0),
                            (troop_add_item, "trp_player", "itm_heraldic_mail_with_tabard", 0),
                            (troop_add_item, "trp_player", "itm_red_gambeson", 0),
                            (troop_add_item, "trp_player", "itm_sword_medieval_c", 0),
                            (troop_add_item, "trp_player", "itm_tab_shield_kite_cav_b", 0),
                            (troop_add_item, "trp_player", "itm_light_lance", 0),

                             (troop_raise_skill,"trp_player",skl_riding,10),

                             (try_for_range,":npc","trp_npc1","trp_npc16"),
                                (call_script,"script_recruit_troop_as_companion",":npc"),
                                (troop_raise_skill,":npc",skl_persuasion,1),
                             (try_end),
                             (troop_add_gold,"trp_player",100000),
                             #(party_relocate_near_party,"p_town_1","p_main_party"),
                             (party_relocate_near_party,"p_main_party","p_town_2",3),
                             (change_screen_map),
                        ]),
                    ],
                },
                # "before":{
                #     "continue":[
                #         ("test_begin",[],"TEST begin",
                #          [
                #             (call_script,"script_start_test_palyer"),
                #         ]),
                #     ],
                # },

            },
            "just_test_menu":{
                "replace":{
                    "go_back":[
                        ("test_info",[],"TEST info",
                         [
                            (call_script,"script_start_test_palyer"),
                        ]),
                    ],
                },
            }
        },
    },
    "scripts":[
        ("start_test_palyer",[
            (troop_add_item, "trp_player", "itm_saddle_horse", 0),
            (troop_add_item, "trp_player", "itm_courser", 0),
            (troop_add_item, "trp_player", "itm_courtly_outfit", 0),
            (troop_add_item, "trp_player", "itm_heraldic_mail_with_tabard", 0),
            (troop_add_item, "trp_player", "itm_red_gambeson", 0),
            (troop_add_item, "trp_player", "itm_sword_medieval_c", 0),
            (troop_add_item, "trp_player", "itm_tab_shield_kite_cav_b", 0),
            (troop_add_item, "trp_player", "itm_light_lance", 0),


            (set_party_battle_mode),
            (troop_equip_items,"trp_player"),
            (jump_to_scene, "scn_random_scene_plain"),
            (set_jump_mission,"mst_my_lead_charge"),
            (set_visitor,0,"trp_player"),
            (set_visitor,0,"trp_swadian_knight"),
            (set_visitors, 4, "trp_looter", 10),
            (set_visitors, 4, "trp_bandit", 10),

            (change_screen_mission),
        ]),
    ],
    "internationals":{
        "cns":{
            "game_menus":[
                "mno_test_alley|测 试 【 武 道 场 】",
                "mno_test_map|测 试 【 大 地 图 】",
            ]
        }
    }
}