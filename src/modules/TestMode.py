from header_game_menus import *
from header_mission_templates import *
from module_mission_templates import *

testMode = {
    "name":"testMode",
    "enable":True,
    "mission_templates":{
        "create_mission_templates":[
            (
                "test_alley_fight", mtf_battle_mode, charge,
                "test alley fight",
                [
                    (0, mtef_team_0 | mtef_use_exact_number, af_override_horse, aif_start_alarmed, 20, []),
                    (3, mtef_visitor_source | mtef_team_1, af_override_horse, aif_start_alarmed, 20, []),
                ],
                [
                    common_battle_init_banner,
                    common_inventory_not_available,
                ],
            )
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
        "add_game_menus":{
            "start_game_0":{
                "after":{
                    "continue":[
                        ("test_alley",[],"TEST 【alley】",
                         [
                            (call_script,"script_start_test_palyer"),
                        ]),
                    ],
                },
                "before":{
                    "continue":[
                        ("test_begin",[],"TEST begin",
                         [
                            (call_script,"script_start_test_palyer"),
                        ]),
                    ],
                },
                "replace":{
                    "test_begin":[
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

            (set_visitor,0,"trp_player"),
            (set_visitors,0,"trp_swadian_knight",1),
            (set_visitors, 3, "trp_looter", 10),
            (set_visitors, 3, "trp_bandit", 10),
            (set_party_battle_mode),
            (set_jump_mission,"mst_test_alley_fight"),
        ]),
    ],
}