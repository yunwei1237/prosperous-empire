# -*- coding: utf-8 -*-
from module_game_menus import game_menus
from module_scripts import *


## 最终 = 200 * 7（1400） + 1000（最大税收）
village_rent_increase_per_day = 200
## 最终 = 400 * 7（2800） + 2000（最大税收）
castle_rent_increase_per_day = 400
## 最终 = 800 * 7（5600） + 2000（最大税收）
town_rent_increase_per_day = 800

## 以下内容非程序员不要修改

## constans



## slot

## args




villageMange = {
    "name":"villageMange",
    "enable":True,
    "simple_triggers":{
        "append":[
            ## 增加税收
            (24,[
                (try_for_range,":center_no",centers_begin,centers_end),
                    (party_get_slot,":rents",":center_no",slot_center_accumulated_rents),
                    (try_begin),
                        (party_slot_eq,":center_no",slot_party_type,spt_town),
                        (val_add,":rents",village_rent_increase_per_day),
                    (else_try),
                        (party_slot_eq,":center_no",slot_party_type,spt_town),
                        (val_add,":rents",castle_rent_increase_per_day),
                    (else_try),
                        (party_slot_eq,":center_no",slot_party_type,spt_town),
                        (val_add,":rents",town_rent_increase_per_day),
                    (try_end),
                (party_set_slot,":center_no",slot_center_accumulated_rents,":rents"),
                (try_end),
            ]),
        ],
    },
    "scripts":{
        "append":[
        ],
    },
    "game_menus":{
        "children":{
            "village>#5":{
                "insertAfter":[
                    {
                        "sign":"village_manage",
                        "data":[
                            ("troops_manage",[
                                #(party_slot_eq, "$current_town", slot_town_lord, "trp_player")
                            ],"Manage this village' troops.",
                            [
                               (change_screen_exchange_members,1),
                            ]),
                        ],
                    }
                ],
            },
        }
    },
    "internationals":{
        "cns":{
            "game_menus":[
               "mno_troops_manage|管 理 村 民"
            ]
        }
    }
}