
from header_operations import *
from module_scripts import *


'''

patrol party
'''



## constans

capital_town_patrol_max_num = 6
town_patrol_max_num = 4
castle_patrol_max_num = 2
village_patrol_max_num = 1

capital_town_patrol_strength = 8
town_patrol_strength = 6
castle_patrol_strength = 4
village_patrol_strength = 2

slot_party_patrol_num = 400

patrolParty = {
    "name":"patrol party",
    "constans":["slot_party_patrol_num = 400"],
    "scripts":[
        ("create_patrol_party",
         [
            (store_script_param, ":center_no", 1),
            (store_script_param, ":strength_val", 2),
            (store_faction_of_party, ":faction_no", ":center_no"),
             (faction_get_slot,":party_temp_id",":faction_no",slot_troop_party_template)
            (try_begin),
            (is_between, ":town_no", towns_begin, towns_end),
            (set_spawn_radius, 0),
            (spawn_around_party, ":village_no", "pt_village_farmers"),
            (assign, ":new_party", reg0),

            (party_set_faction, ":new_party", ":party_faction"),
            (party_set_slot, ":new_party", slot_party_home_center, ":village_no"),
            (party_set_slot, ":new_party", slot_party_last_traded_center, ":village_no"),

            (party_set_slot, ":new_party", slot_party_type, spt_village_farmer),
            (party_set_slot, ":new_party", slot_party_ai_state, spai_trading_with_town),
            (party_set_slot, ":new_party", slot_party_ai_object, ":town_no"),
            (party_set_ai_behavior, ":new_party", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":new_party", ":town_no"),
            (party_set_flags, ":new_party", pf_default_behavior, 0),
            (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
            (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
            (store_add, ":cur_good_price_slot", ":cur_goods", ":item_to_price_slot"),
            (party_get_slot, ":cur_village_price", ":village_no", ":cur_good_price_slot"),
            (party_set_slot, ":new_party", ":cur_good_price_slot", ":cur_village_price"),
            (try_end),
            (assign, reg0, ":new_party"),
            (try_end),

          ]),
        ("update_patrol_partys_for_all",[
            (try_for_range,"center_no",centers_begin,centers_end),
                (this_or_next|party_slot_eq,"center_no",slot_party_type,spt_town),
                (this_or_next|party_slot_eq,"center_no",slot_party_type,spt_castle),
                (this_or_next|party_slot_eq,"center_no",slot_party_type,spt_village),

                (assign,":need_create_party_num",0),
                (party_get_slot,":center_patrol_num","center_no",slot_party_patrol_num),
                (try_begin),
                    (party_slot_eq,":center_no",slot_party_type,spt_town),
                    (try_begin),
                        (party_get_slot,":leader",":center_no",slot_town_lord),
                        (is_between,":leader",kings_begin,kings_end),
                        (store_sub,":need_create_party_num",capital_town_patrol_max_num,":center_patrol_num"),
                    (else_try),
                        (store_sub,":need_create_party_num",town_patrol_max_num,":center_patrol_num"),
                    (try_end),
                (else_try),
                    (party_slot_eq,":center_no",slot_party_type,spt_castle),
                    (store_sub,":need_create_party_num",castle_patrol_max_num,":center_patrol_num"),
                (else_try)
                    (store_sub,":need_create_party_num",village_patrol_max_num,":center_patrol_num"),
                (try_end),
                (call_script,"script_cf_create_kingdom_party", ":faction_no", ":party_type"),
            (try_end),
        ])
    ],

}