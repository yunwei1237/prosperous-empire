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
                "my_alley_fight", mtf_battle_mode, charge,
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
                             (troop_raise_skill,"trp_player",skl_leadership,10),

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

                        ]),
                    ],
                },
            }
        },
    },
    "scripts":[
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
    ],
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
            ]
        }
    }
}