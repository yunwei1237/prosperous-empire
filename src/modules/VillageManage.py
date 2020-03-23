# -*- coding: utf-8 -*-
from module_game_menus import game_menus
from module_scripts import *

from modules.HeroCollection_header import *


## 村庄，养殖，种植，开采系统

## 所有的功能都是与村长进行对话来完成系统的功能


## 以下内容非程序员不要修改

## constans



## slot

## args




villageMange = {
    "name":"villageMange",
    "enable":True,
    "simple_triggers":{
        "append":[

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