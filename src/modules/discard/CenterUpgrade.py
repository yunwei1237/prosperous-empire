

## 据点根据繁荣度可以升级

## 当前遇到以下几个问题

## 1.游戏本身是以区间来进行城镇数据（价格等等）更新，如果新的城镇加入该区间会导致自动更新,如果城镇设置为不可用，
# 那会导致操作城镇时没有判断城镇是否可用的条件时，会导致-1作为城镇id，以至于游戏会出现大量红色错误信息，游戏更新数据出错
## 如果不存放到区间，不会出错这个错误，但是如果希望城镇数据能够自动更新时，就会比较困难，因为它不在系统数据更新的区间，
# 如果把数据更新的代码再写一遍，代码量会比较大，甚至一些对话都要重新写一遍，或者加上新城镇的判断
##


## 设想：每一个据点都是城镇，没有城堡和村庄，可以通过设置party的slot来改变城镇的图标和内部结构(仍然逃不开区间带来的问题，哈哈)

##

# -*- coding: utf-8 -*-

from module_scripts import *

from modules.lord.HeroCollection_header import *



## 以下内容非程序员不要修改

## constans


## slot

slot_party_center_upgrade_status = 410

## args

spcus_center_town = 1
spcus_center_castle = 2
spcus_center_village = 3



centerUpgrade = {
    "name":"centerUpgrade",
    "enable":False,
    "parties":
        {
            "append":mergeList([],[],[]),
        },
    "scenes":
        {
            "append": mergeList([], [], []),
        },
    "troops":
        {
            "insertAfter":[{
                "sign":"relative_of_merchants_end",
                "data":[

                ],
            }],
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
            ## 只会被使用一次
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