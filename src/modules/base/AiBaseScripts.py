# -*- coding: utf-8 -*-

## 用于编写一些ai方面的功能
from header_operations import *
from header_parties import *
from module_constants import *

aiBaseScripts={
    "name":"AiBaseScripts",
    "enable":True,
    "scripts":{
        "append":[
            ## 移动到某个据点
            ("set_party_ai_go_to_center",[
                (store_script_param_1,":party"),
                (store_script_param_2,":center"),
                (party_set_slot, ":party", slot_party_ai_state, spai_trading_with_town),
                (party_set_slot, ":party", slot_party_ai_object, ":center"),
                (party_set_ai_behavior, ":party", ai_bhvr_travel_to_party),
                (party_set_ai_object, ":party", ":center"),
            ]),
            ## 巡逻某个据点
            ("set_party_ai_patrol_center",[
                (store_script_param,":party",1),
                (store_script_param,":town",2),
                (store_script_param,":radius",3),

                (try_begin),
                    (le,":radius",0),
                    (assign,":radius",20),
                (try_end),

                (party_set_slot, ":party", slot_party_ai_state, spai_patrolling_around_center),
                (party_set_slot, ":party", slot_party_ai_object, ":town"),
                (party_set_ai_behavior, ":party", ai_bhvr_patrol_party),
                (party_set_ai_object, ":party", ":town"),
                (party_set_ai_patrol_radius,":party",":radius")
            ]),
        ],
    }
}