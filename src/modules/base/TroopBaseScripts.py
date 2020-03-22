# -*- coding: utf-8 -*-

## 包含一些对阵营常用的操作
from header_operations import *
from header_parties import *
from header_skills import skl_trainer
from module_constants import *



## args


troopBaseScripts={
    "name":"TroopBaseScripts",
    "enable":True,
    "scripts":{
        "append":[
            ## 出门
            ("troop_leave_home",[
                (store_script_param, ":troop", 1),
                (troop_get_slot,":home",":troop",slot_troop_cur_center),
                (party_get_slot, ":home_castle", ":home", slot_town_castle),
                (remove_troop_from_site, ":troop",":home_castle"),
                (display_message,"str_s5_leave_home"),
              ]),
            ## 回家
            ("troop_go_home",[
                (store_script_param, ":troop", 1),
                (troop_get_slot,":home",":troop",slot_troop_cur_center),
                (party_get_slot, ":home_castle", ":home", slot_town_castle),
                (modify_visitors_at_site, ":troop",":home_castle"),
                (display_message,"str_s5_go_home"),
              ]),
        ],
    },
    "strings":{
        "append":[
            ("s5_leave_home","{s5} leave home"),
            ("s5_go_home","{s5} go home"),
        ],
    },

    "internationals":{
        "cns":{
            "game_strings":[
                "str_s5_leave_home|{s5}出 门 了",
                "str_s5_go_home|{s5}回 家 了",
            ]
        }
    }
}