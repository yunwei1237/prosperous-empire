# -*- coding: utf-8 -*-
from ID_troops import *
from header_dialogs import *
from header_game_menus import *
from module_mission_templates import *

testMode = {
    "name":"testMode",
    "enable":True,
    "mission_templates":{
        "append":[
            ("my_alley_fight", mtf_battle_mode, charge,
                "Alley fight",
                [
                    (0, mtef_team_0 | mtef_use_exact_number, 0, aif_start_alarmed, 100, []),
                    (1, mtef_visitor_source | mtef_team_1, 0, aif_start_alarmed, 200, []),
                    (2, mtef_visitor_source | mtef_team_1, 0, aif_start_alarmed, 200, []),
                    (3, mtef_visitor_source | mtef_team_1, 0, aif_start_alarmed, 200, []),
                ],
                [
                    common_battle_init_banner,

                    common_inventory_not_available,

                    (ti_on_agent_spawn, 0, 0, [],
                     [
                         (store_trigger_param_1, ":agent_no"),
                         (get_player_agent_no, ":player_agent"),
                         (neq, ":agent_no", ":player_agent"),
                         (assign, "$g_main_attacker_agent", ":agent_no"),
                         (agent_ai_set_aggressiveness, ":agent_no", 199),

                         (try_begin),
                         (agent_get_troop_id, ":troop_no", ":agent_no"),
                         (is_between, ":troop_no", "trp_swadian_merchant", "trp_startup_merchants_end"),
                         (agent_set_team, ":agent_no", 7),
                         (team_set_relation, 0, 7, 0),
                         (try_end),
                     ]),

                    (0, 0, 0,
                     [
                         (eq, "$talked_with_merchant", 0),
                     ],
                     [
                         (get_player_agent_no, ":player_agent"),
                         (agent_get_position, pos0, ":player_agent"),

                         (try_for_agents, ":agent_no"),
                             (agent_get_troop_id, ":troop_no", ":agent_no"),
                             (is_between, ":troop_no", "trp_swadian_merchant", "trp_startup_merchants_end"),
                             (agent_set_scripted_destination, ":agent_no", pos0),
                             (agent_get_position, pos1, ":agent_no"),
                             (get_distance_between_positions, ":dist", pos0, pos1),
                             (le, ":dist", 200),
                             (assign, "$talk_context", tc_back_alley),
                             (start_mission_conversation, ":troop_no"),
                         (try_end),
                     ]),

                    (1, 0, 0, [],
                     [
                         (get_player_agent_no, ":player_agent"),
                         (ge, "$g_main_attacker_agent", 0),
                         (ge, ":player_agent", 0),
                         (agent_is_active, "$g_main_attacker_agent"),
                         (agent_is_active, ":player_agent"),
                         (agent_get_position, pos0, ":player_agent"),
                         (agent_get_position, pos1, "$g_main_attacker_agent"),
                         (get_distance_between_positions, ":dist", pos0, pos1),
                         (ge, ":dist", 5),
                         (agent_set_scripted_destination, "$g_main_attacker_agent", pos0),
                     ]),

                    (ti_tab_pressed, 0, 0, [],
                     [
                         (finish_mission),
                     ]),

                    (0, 0, 0, [],
                     [
                         (key_is_down,key_c),
                         (display_message, "str_cannot_leave_now"),
                     ]),

                    (0, 0, ti_once, [],
                     [
                         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
                         (set_party_battle_mode),
                     ]),

                    (0, 0, ti_once,
                     [
                         (neg | main_hero_fallen),
                         (num_active_teams_le, 1),
                     ],
                     [
                         (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),

                         (try_begin),
                         (eq, ":starting_town_faction", "fac_kingdom_1"),
                         (assign, ":troop_of_merchant", "trp_swadian_merchant"),
                         (else_try),
                         (eq, ":starting_town_faction", "fac_kingdom_2"),
                         (assign, ":troop_of_merchant", "trp_vaegir_merchant"),
                         (else_try),
                         (eq, ":starting_town_faction", "fac_kingdom_3"),
                         (assign, ":troop_of_merchant", "trp_khergit_merchant"),
                         (else_try),
                         (eq, ":starting_town_faction", "fac_kingdom_4"),
                         (assign, ":troop_of_merchant", "trp_nord_merchant"),
                         (else_try),
                         (eq, ":starting_town_faction", "fac_kingdom_5"),
                         (assign, ":troop_of_merchant", "trp_rhodok_merchant"),
                         (else_try),
                         (eq, ":starting_town_faction", "fac_kingdom_6"),
                         (assign, ":troop_of_merchant", "trp_sarranid_merchant"),
                         (try_end),

                         (add_visitors_to_current_scene, 3, ":troop_of_merchant", 1, 0),
                     ]),

                    (1, 0, ti_once,
                     [
                         (eq, "$talked_with_merchant", 1),
                     ],
                     [
                         (try_begin),
                         (main_hero_fallen),
                         (assign, "$g_killed_first_bandit", 0),
                         (else_try),
                         (assign, "$g_killed_first_bandit", 1),
                         (try_end),

                         (finish_mission),
                         (assign, "$g_main_attacker_agent", 0),
                         (assign, "$talked_with_merchant", 1),

                         (assign, "$current_startup_quest_phase", 1),

                         (change_screen_return),
                         (set_trigger_result, 1),

                         (get_player_agent_no, ":player_agent"),
                         (store_agent_hit_points, ":hit_points", ":player_agent"),

                         (try_begin),
                         (lt, ":hit_points", 90),
                         (agent_set_hit_points, ":player_agent", 90),
                         (try_end),
                     ]),

                    (1, 3, ti_once,
                     [
                         (main_hero_fallen),
                     ],
                     [
                         (try_begin),
                         (main_hero_fallen),
                         (assign, "$g_killed_first_bandit", 0),
                         (else_try),
                         (assign, "$g_killed_first_bandit", 1),
                         (try_end),

                         (finish_mission),
                         (assign, "$g_main_attacker_agent", 0),
                         (assign, "$talked_with_merchant", 1),

                         (assign, "$current_startup_quest_phase", 1),

                         (change_screen_return),
                         (set_trigger_result, 1),

                         (get_player_agent_no, ":player_agent"),
                         (store_agent_hit_points, ":hit_points", ":player_agent"),

                         (try_begin),
                         (lt, ":hit_points", 90),
                         (agent_set_hit_points, ":player_agent", 90),
                         (try_end),
                     ]),
            ]),
            ("my_town_center", 0, -1,
                "Default town visit",
                [(0, mtef_scene_source | mtef_team_0, af_override_horse, 0, 1, pilgrim_disguise),
                 (1, mtef_scene_source | mtef_team_0, 0, 0, 1, []),
                 (2, mtef_scene_source | mtef_team_0, af_override_horse, 0, 1, pilgrim_disguise),
                 (3, mtef_scene_source | mtef_team_0, af_override_horse, 0, 1, pilgrim_disguise),
                 (4, mtef_scene_source | mtef_team_0, af_override_horse, 0, 1, pilgrim_disguise),
                 (5, mtef_scene_source | mtef_team_0, af_override_horse, 0, 1, pilgrim_disguise),
                 (6, mtef_scene_source | mtef_team_0, af_override_horse, 0, 1, pilgrim_disguise),
                 (7, mtef_scene_source | mtef_team_0, af_override_horse, 0, 1, pilgrim_disguise),
                 (8, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (9, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (10, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (11, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (12, mtef_visitor_source, af_override_horse, 0, 1, []), (13, mtef_visitor_source, 0, 0, 1, []),
                 (14, mtef_scene_source, 0, 0, 1, []), (15, mtef_scene_source, 0, 0, 1, []),
                 (16, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (17, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (18, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (19, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (20, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (21, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (22, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (23, mtef_visitor_source, af_override_horse, 0, 1, []),  # guard
                 (24, mtef_visitor_source, af_override_horse, 0, 1, []),  # guard
                 (25, mtef_visitor_source, af_override_horse, 0, 1, []),  # guard
                 (26, mtef_visitor_source, af_override_horse, 0, 1, []),  # guard
                 (27, mtef_visitor_source, af_override_horse, 0, 1, []),  # guard
                 (28, mtef_visitor_source, af_override_horse, 0, 1, []),  # guard
                 (29, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (30, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (31, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (32, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (33, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (34, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (35, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (36, mtef_visitor_source, af_override_horse, 0, 1, []),  # town walker point
                 (37, mtef_visitor_source, af_override_horse, 0, 1, []),  # town walker point
                 (38, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (39, mtef_visitor_source, af_override_horse, 0, 1, []),
                 (40, mtef_visitor_source | mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
                 # in towns, can be used for guard reinforcements
                 (41, mtef_visitor_source | mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
                 # in towns, can be used for guard reinforcements
                 (42, mtef_visitor_source | mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
                 # in towns, can be used for guard reinforcements
                 (43, mtef_visitor_source | mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
                 # in towns, can be used for guard reinforcements
                 (44, mtef_visitor_source | mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
                 (45, mtef_visitor_source | mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
                 (46, mtef_visitor_source | mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
                 (47, mtef_visitor_source | mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
                 ],
                [
                    (ti_on_agent_spawn, 0, 0, [],
                     [
                         (store_trigger_param_1, ":agent_no"),
                         (call_script, "script_init_town_agent", ":agent_no"),
                         (try_begin),
                         (this_or_next | eq, "$talk_context", tc_escape),
                         (eq, "$talk_context", tc_prison_break),
                         (agent_get_troop_id, ":troop_no", ":agent_no"),
                         (troop_slot_eq, ":troop_no", slot_troop_will_join_prison_break, 1),
                         (agent_set_team, ":agent_no", 0),
                         (agent_ai_set_aggressiveness, ":agent_no", 5),
                         (troop_set_slot, ":troop_no", slot_troop_will_join_prison_break, 0),
                         (try_begin),
                         (troop_slot_eq, ":troop_no", slot_troop_mission_participation, mp_prison_break_stand_back),
                         (agent_get_position, pos1, ":agent_no"),
                         (agent_set_scripted_destination, ":agent_no", pos1),
                         (try_end),
                         (try_end),
                     ]),

                    (ti_before_mission_start, 0, 0, [],
                     [
                         (assign, "$g_main_attacker_agent", 0),
                     ]),

                    (1, 0, ti_once,
                     [],
                     [
                         (try_begin),
                         (eq, "$g_mt_mode", tcm_default),
                         (store_current_scene, ":cur_scene"),
                         (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
                         (try_end),
                         (call_script, "script_init_town_walker_agents"),
                         (try_begin),
                         (eq, "$sneaked_into_town", 1),
                         (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
                         (else_try),
                         (call_script, "script_music_set_situation_with_culture", mtf_sit_town),
                         (try_end),
                     ]),

                    (ti_before_mission_start, 0, 0,
                     [],
                     [
                         (call_script, "script_change_banners_and_chest")
                     ]),

                    (ti_inventory_key_pressed, 0, 0,
                     [
                         (try_begin),
                         (eq, "$g_mt_mode", tcm_default),
                         (set_trigger_result, 1),
                         (else_try),
                         (eq, "$g_mt_mode", tcm_disguised),
                         (display_message, "str_cant_use_inventory_disguised"),
                         (else_try),
                         (display_message, "str_cant_use_inventory_now"),
                         (try_end),
                     ],
                     []),

                    (ti_tab_pressed, 0, 0,
                     [
                         (try_begin),
                         (this_or_next | eq, "$talk_context", tc_escape),
                         (eq, "$talk_context", tc_prison_break),
                         (display_message, "str_cannot_leave_now"),
                         (else_try),
                         (this_or_next | eq, "$g_mt_mode", tcm_default),
                         (eq, "$g_mt_mode", tcm_disguised),
                         (mission_enable_talk),
                         (set_trigger_result, 1),
                         (else_try),
                         (display_message, "str_cannot_leave_now"),
                         (try_end),
                     ],
                     []),

                    (ti_on_leave_area, 0, 0,
                     [
                         (try_begin),
                         (eq, "$g_defending_against_siege", 0),
                         (assign, "$g_leave_town", 1),
                         (try_end),
                     ],
                     [
                         (try_begin),
                         (eq, "$talk_context", tc_escape),
                         (call_script, "script_deduct_casualties_from_garrison"),
                         (jump_to_menu, "mnu_sneak_into_town_caught_dispersed_guards"),
                         (try_end),

                         (mission_enable_talk),
                     ]),

                    (0, 0, ti_once,
                     [],
                     [
                         (party_slot_eq, "$current_town", slot_party_type, spt_town),
                         (call_script, "script_town_init_doors", 0),
                         (try_begin),
                         (eq, "$town_nighttime", 0),
                         (play_sound, "snd_town_ambiance", sf_looping),
                         (try_end),
                     ]),

                    (3, 0, 0,
                     [
                         (call_script, "script_tick_town_walkers")
                     ],
                     []),

                    (2, 0, 0,
                     [
                         (call_script, "script_center_ambiance_sounds")
                     ],
                     []),

                    # JAILBREAK TRIGGERS
                    # Civilians get out of the way
                    (1, 0, 0,
                     [
                         (this_or_next | eq, "$talk_context", tc_prison_break),
                         (eq, "$talk_context", tc_escape),
                     ],
                     [
                         # (agent_get_team, ":prisoner_agent", 0),
                         (call_script, "script_neutral_behavior_in_fight"),
                         (mission_disable_talk),
                     ]),

                    # The game begins with the town alerted
                    (1, 0, ti_once,
                     [
                         # If I set this to 1, 0, ti_once, then the prisoner spawns twice
                         (eq, "$talk_context", tc_escape),
                     ],
                     [
                         (get_player_agent_no, ":player_agent"),
                         (assign, reg6, ":player_agent"),
                         (call_script, "script_activate_town_guard"),

                         (get_player_agent_no, ":player_agent"),
                         (agent_get_position, pos4, ":player_agent"),

                         (try_for_range, ":prisoner", active_npcs_begin, kingdom_ladies_end),
                         (troop_slot_ge, ":prisoner", slot_troop_mission_participation, mp_prison_break_fight),

                         (str_store_troop_name, s4, ":prisoner"),
                         (display_message, "str_s4_joins_prison_break"),

                         (store_current_scene, ":cur_scene"),  # this might be a better option?
                         (modify_visitors_at_site, ":cur_scene"),

                         # <entry_no>,<troop_id>,<number_of_troops>, <team_no>, <group_no>),
                         # team no and group no are used in multiplayer mode only. default team in entry is used in single player mode
                         (store_current_scene, ":cur_scene"),
                         (modify_visitors_at_site, ":cur_scene"),
                         (add_visitors_to_current_scene, 24, ":prisoner", 1, 0, 0),
                         (troop_set_slot, ":prisoner", slot_troop_will_join_prison_break, 1),
                         (try_end),
                     ]),

                    (3, 0, 0,
                     [
                         (main_hero_fallen, 0),
                     ],
                     [
                         (try_begin),
                         (this_or_next | eq, "$talk_context", tc_prison_break),
                         (eq, "$talk_context", tc_escape),

                         (call_script, "script_deduct_casualties_from_garrison"),
                         (jump_to_menu, "mnu_captivity_start_castle_defeat"),

                         (assign, ":end_cond", kingdom_ladies_end),
                         (try_for_range, ":prisoner", active_npcs_begin, ":end_cond"),
                         (troop_set_slot, ":prisoner", slot_troop_mission_participation, 0),  # new
                         (try_end),

                         (mission_enable_talk),
                         (finish_mission, 0),
                         (else_try),
                         (set_trigger_result, 1),
                         (try_end),
                     ]),

                    (3, 0, 0,
                     [
                         (eq, "$talk_context", tc_escape),
                         (neg | main_hero_fallen, 0),
                         (store_mission_timer_a, ":time"),
                         (ge, ":time", 10),

                         (all_enemies_defeated),  # 1 is default enemy team for in-town battles
                     ],
                     [
                         (call_script, "script_deduct_casualties_from_garrison"),
                         (try_for_agents, ":agent"),
                         (agent_get_troop_id, ":troop", ":agent"),
                         (troop_slot_ge, ":troop", slot_troop_mission_participation, mp_prison_break_fight),
                         (try_begin),
                         (agent_is_alive, ":agent"),
                         (troop_set_slot, ":troop", slot_troop_mission_participation, mp_prison_break_escaped),
                         (else_try),
                         (troop_set_slot, ":troop", slot_troop_mission_participation, mp_prison_break_caught),
                         (try_end),
                         (try_end),
                         (jump_to_menu, "mnu_sneak_into_town_caught_ran_away"),

                         (mission_enable_talk),
                         (finish_mission, 0)
                     ]),

                    (ti_on_agent_killed_or_wounded, 0, 0, [],
                     [
                         (store_trigger_param_1, ":dead_agent_no"),
                         (store_trigger_param_2, ":killer_agent_no"),
                         # (store_trigger_param_3, ":is_wounded"),

                         (agent_get_troop_id, ":dead_agent_troop_no", ":dead_agent_no"),
                         (agent_get_troop_id, ":killer_agent_troop_no", ":killer_agent_no"),

                         (try_begin),
                         (this_or_next | eq, ":dead_agent_troop_no", "trp_swadian_prison_guard"),
                         (this_or_next | eq, ":dead_agent_troop_no", "trp_vaegir_prison_guard"),
                         (this_or_next | eq, ":dead_agent_troop_no", "trp_khergit_prison_guard"),
                         (this_or_next | eq, ":dead_agent_troop_no", "trp_nord_prison_guard"),
                         (this_or_next | eq, ":dead_agent_troop_no", "trp_rhodok_prison_guard"),
                         (eq, ":dead_agent_troop_no", "trp_sarranid_prison_guard"),

                         (eq, ":killer_agent_troop_no", "trp_player"),

                         (display_message, "@You got keys of dungeon."),
                         (try_end),
                     ]),
                    (0,0,0,[],[
                        (key_clicked,key_o),
                        (assign,"$talk_context", tc_town_talk),
                        (display_message,"@p is clicked !"),
                    ]),
                ]),
        ]
    },
    "game_menus":{
            "append":[
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
            "children":{
                "start_game_0>#5":{
                    "insertAfter":[
                        {
                            "sign":"continue",
                            "data":[
                                ("test_alley",[],"TEST 【alley】",
                                 [
                                     (call_script,"script_create_battle_for_player","p_town_1",slot_town_alley,20,20),
                                 ]),

                                 ("test_arena",[],"TEST 【arena】",
                                 [
                                     (call_script,"script_create_battle_for_player","p_town_1",slot_town_arena,20,20),
                                 ]),

                                ("test_tavern",[],"TEST 【tavern】",
                                 [
                                     (call_script,"script_create_battle_for_player","p_town_1",slot_town_tavern,20,20),
                                 ]),

                                ("test_prison",[],"TEST 【prison】",
                                 [
                                     (call_script,"script_create_battle_for_player","p_town_1",slot_town_prison,20,20),
                                 ]),
                                ("test_castle",[],"TEST 【castle】",
                                 [
                                     (call_script,"script_create_battle_for_player","p_town_1",slot_town_castle,20,20),
                                 ]),

                                ("test_center",[],"TEST 【center】",
                                 [
                                     (call_script,"script_create_battle_for_player","p_town_1",slot_town_center,20,20),
                                 ]),

                                ("test_plain",[],"TEST 【plain】",
                                 [
                                     (call_script,"script_create_battle_for_player","scn_random_scene_plain",-1,20,20),
                                ]),

                                ("test_zendar",[],"TEST 【zendar】",
                                 [
                                    (set_visitor, 0, "trp_player"),
                                    (set_jump_mission, "mt_my_town_center"),
                                    (jump_to_scene, "scn_zendar_center"),
                                    (change_screen_mission),

                                ]),
                                ("test_map",[],"TEST 【map】",
                                 [
                                     (troop_set_name,"trp_player","@test"),                                                                                              (party_set_name,"p_main_party","@test"),

                                    (troop_add_item, "trp_player", "itm_saddle_horse", 0),
                                    (troop_add_item, "trp_player", "itm_courser", 0),
                                    (troop_add_item, "trp_player", "itm_courtly_outfit", 0),
                                    (troop_add_item, "trp_player", "itm_heraldic_mail_with_tabard", 0),
                                    (troop_add_item, "trp_player", "itm_red_gambeson", 0),
                                    (troop_add_item, "trp_player", "itm_sword_medieval_c", 0),
                                    (troop_add_item, "trp_player", "itm_tab_shield_kite_cav_b", 0),
                                    (troop_add_item, "trp_player", "itm_light_lance", 0),

                                     (troop_raise_skill,"trp_player",skl_riding,10),
                                     (troop_raise_skill,"trp_player",skl_leadership,10),

                                     # (try_for_range,":npc","trp_npc1","trp_npc16"),
                                     #    (call_script,"script_recruit_troop_as_companion",":npc"),
                                     #    (troop_raise_skill,":npc",skl_persuasion,1),
                                     # (try_end),

                                     (party_add_members,"p_main_party","trp_swadian_knight",200),
                                     (troop_add_gold,"trp_player",100000),
                                     (troop_add_items,"trp_player","itm_dried_meat",10),

                                     #(party_relocate_near_party,"p_town_1","p_main_party"),
                                     (party_relocate_near_party,"p_main_party","p_town_3",3),
                                     (change_screen_map),
                                ]),
                            ],
                        },
                    ],
                },
            },
    },
    "scripts":{
        "append":[
            ("create_battle_for_player",[
                (store_script_param_1,":center"),
                (store_script_param_2,":place"),
                (store_script_param,":companies_nums",3),
                (store_script_param,":enemies_nums",4),

                #(party_get_slot, ":scene_no", "p_town_1", slot_town_alley),
                (try_begin),
                    (gt,":place",0),
                    (party_get_slot, ":scene_no", ":center", ":place"),
                (else_try),
                    (assign, ":scene_no", ":center"),
                (try_end),


                (modify_visitors_at_site, ":scene_no"),

                (reset_visitors),
                (set_visitor, 0, "trp_player"),

                (party_add_members,"p_main_party","trp_swadian_knight",":companies_nums"),

                (troop_add_item, "trp_player", "itm_saddle_horse", 0),
                (troop_add_item, "trp_player", "itm_courser", 0),
                (troop_add_item, "trp_player", "itm_courtly_outfit", 0),
                (troop_add_item, "trp_player", "itm_heraldic_mail_with_tabard", 0),
                (troop_add_item, "trp_player", "itm_red_gambeson", 0),
                (troop_add_item, "trp_player", "itm_sword_medieval_c", 0),
                (troop_add_item, "trp_player", "itm_tab_shield_kite_cav_b", 0),
                (troop_add_item, "trp_player", "itm_light_lance", 0),
                (troop_raise_skill,"trp_player",skl_riding,10),
                (troop_equip_items,"trp_player"),


                (val_mul,":enemies_nums",3),
                (set_visitors, 2, "trp_bandit",":enemies_nums"),

                (set_jump_mission, "mt_my_alley_fight"),
                (jump_to_scene, ":scene_no"),
                (change_screen_mission),
            ]),
        ]
    },
    "internationals":{
        "cns":{
            "game_menus":[
                "mno_test_alley|测 试 【 街 道 】",
                "mno_test_map|测 试 【 大 地 图 】",
                "mno_test_arena|测 试 【 竞 技 场 】",
                "mno_test_tavern|测 试 【 酒 馆 】",
                "mno_test_prison|测 试 【 监 狱 】",
                "mno_test_castle|测 试 【 大 厅 】",
                "mno_test_center|测 试 【 地 形 】",
                "mno_test_zendar|测 试 【 禅 达 】",
            ]
        }
    },
    "dialogs":{
        "insertBefore":[
            {
                "sign":"start:Surrender_or_die@:battle_reason_stated[1,3,4]",
                "data":[
                    [trp_constable_hareck, "start", [], "are you ok ?", "constable_hareck_hi",[]],
                    [anyone | plyr, "constable_hareck_hi", [], "yes , I'm ok !", "close_window", []],
                ]
            }
        ]
    }
}