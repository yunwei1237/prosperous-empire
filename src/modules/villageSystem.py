# -*- coding: utf-8 -*-

from module_scripts import *

from modules.HeroCollection_header import *


## 村庄，养殖，种植，开采系统

## 所有的功能都是与村长进行对话来完成系统的功能


## 以下内容非程序员不要修改

## constans



## slot
slot_party_village_system = 415
## args




centerUpgrade = {
    "name":"centerUpgrade",
    "enable":False,
    "parties":
        {
            "append":mergeList([],[],[]),
        },
    "simple_triggers":{
        "append":[
            (1,[
                (call_script,"script_update_hero_collection_status"),
            ]),
        ],
    },
    "triggers":{
        "append":[
            ## 游戏开始时就初始化英雄信息(只更新一次)
            (0,0,ti_once,[],[
                (call_script,"script_init_hero_collection"),
            ]),
        ],
    },
    "scripts":{
        "append":[
            ("init_all_center_info",[
                (call_script, "script_update_all_notes"),
            ]),

            ("center_update_status",[
                (store_script_param_1,":center"),
                (store_script_param_2,":isUpgrade"),
            ]),
        ],
    },
    # "internationals":{
    #     "cns":{
    #         "game_strings":[
    #             # "str_s5_s_patrol_party|{s5}的 巡 逻 队",
    #         ]
    #     }
    # }
}