# -*- coding: utf-8 -*-

from module_scripts import *
from modules.AgricultureSystem_header import *

from modules.HeroCollection_header import *


## 村庄，养殖，种植，开采系统

## 所有的功能都是与村长进行对话来完成系统的功能


## 以下内容非程序员不要修改

## 小麦，橄榄，枣，亚麻,葡萄，卷心菜，

argricultureConfig = [
    {
        "name":"plant",
        "name_cns":"种 植",
        "kinds":[
            {
                "item":"itm_grain",
                "create_money":200,
                "cost_per_season":50,
                "output_max_num_per_season":100,
                "output_min_num_per_season":30,
                "time_per_season":24*7,
            },
            {
                "item":"itm_cabbages",
                "create_money":250,
                "cost_per_season":55,
                "output_max_num_per_season":120,
                "output_min_num_per_season":30,
                "time_per_season":24*4,
            }
        ],
    },
    {
        "name":"breed",
        "name_cns":"养 殖",
        "kinds":[
            {
                "item":"itm_honey",
                "create_money":500,
                "cost_per_season":100,
                "output_max_num_per_season":200,
                "output_min_num_per_season":120,
                "time_per_season":24*7*4,
            },
            {
                "item":"itm_cattle_meat",
                "create_money":1000,
                "cost_per_season":80,
                "output_max_num_per_season":500,
                "output_min_num_per_season":280,
                "time_per_season":24*7*3,
            }
        ],
    }
]

## header
systemTroops =  createSysteTroop(argricultureConfig)
## constans



## slot
## 每一种类型分配一个slot保存土地数量
slot_center_argriculture_system_begin = 415


## 是否自动出售
slot_player_argriculture_auto_sell = 175
## args




agricultureSystem = {
    "name":"agricultureSystem",
    "enable":False,
    "troops":{
        "append":systemTroops,
    },
    "simple_triggers":{
        "append":[
            (24,[
                (call_script,"script_update_argriculture_system"),
            ]),
        ],
    },
    "triggers":{
        "append":[
            ## 初始化农业系统
            (0,0,ti_once,[],[
                (call_script,"script_init_argriculture_system"),
            ])
        ],
    },
    "scripts":{
        "append":[
            ("init_argriculture_system",
                 ## 初始化
                 initSystemTroop(argricultureConfig)
             ),
            ## 每小时更新一次
            ("update_argriculture_system",[
                (try_for_range,":center_no",centers_begin,centers_end),

                (party_slot_eq,":center_no",slot_party_type,spt_village),
                    (store_add,"kind_begin",system_kind_begin,1),
                    (try_for_range,":kind","kind_begin",system_kind_end),
                        (store_sub,":offset",":kind",system_kind_begin),
                        (val_add,":offset",1),
                        (store_add,":slot_no",slot_center_argriculture_system_begin,":offset"),
                        (party_get_slot,":num",":center_no",":slot_no"),
                        (gt,":num",0),
                        (troop_get_slot,":max",":kind",sk_output_max_num_per_season_index),
                        (troop_get_slot,":min",":kind",sk_output_min_num_per_season_index),
                        ## 产量
                        (store_random_in_range,":output_amount",":min",":max"),
                        ## 由于繁荣度而产生的额外产量
                        (party_get_slot,":prosperity",":center_no",slot_town_prosperity),
                        (store_mul,":additional_output",":max",":prosperity"),
                        ## 减少额外产出比率
                        (val_div,":additional_output",100 * 2),

                        (val_add,":output_amount",":additional_output"),

                        ## 限制最大数量
                        (val_min,":output_amount",":max"),
                        (troop_get_slot,":item_no",":kind",sk_item_index),

                        ##
                        (str_store_party_name,s1,":center_no"),
                        (str_store_item_name,s2,":item_no"),
                        (assign,reg1,":output_amount"),

                        (try_begin),
                            (player_slot_eq,slot_player_argriculture_auto_sell,1),
                            (store_item_value,":price",":item_no"),
                            (store_mul,":total",":price",":output_amount"),
                            ## 交易技能额外收入
                            (store_skill_level,":trade","trp_player",skl_trade),
                            (store_mul,":additional_money",":total",":trade"),
                            (val_div,":additional_money",10),
                            (val_add,":total",":additional_money"),
                            (call_script,"script_troop_add_gold","trp_player",":total"),

                            (display_message,"str_sell_s1_output_reg1_s2"),
                        (else_try),
                            (troop_add_item,"trp_player",":item_no",":output_amount"),

                            (display_message,"str_get_s1_output_reg1_s2"),
                        (try_end)
                    (try_end),
                (try_end),
            ]),
        ],
    },
    "strings":{
        "append":mergeList(parseStrings(argricultureConfig),
                           [
                               ("get_s1_output_reg1_s2","get {s1} output {reg1} {s2}")
                               ("sell_s1_output_reg1_s2","sell {s1} output {reg1} {s2}")
                           ]),
    },
    "internationals":{
        "cns":{
            "game_strings":mergeList(parseCnsGameStrings(argricultureConfig),
                                     [
                                         "str_at_s1_output_reg1_s2|在{s1}出产{s2}个{reg1}"
                                     ]),
        }
    }
}