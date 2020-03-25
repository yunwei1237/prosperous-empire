# -*- coding: utf-8 -*-
from module_game_menus import game_menus
from module_scripts import *

## config

## 最终 = 200 * 7（1400） + 1000（最大税收）
village_rent_increase_per_day = 200
## 最终 = 400 * 7（2800） + 2000（最大税收）
castle_rent_increase_per_day = 400
## 最终 = 800 * 7（5600） + 2000（最大税收）
town_rent_increase_per_day = 800

## 每天更新（24）
center_tax_inscrease_interval = 24

## 领主自动收税时间(7天收一次，和玩家一样)
lord_auto_collect_tax_interval = 24 * 7



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
            (center_tax_inscrease_interval,[
                (try_for_range,":center_no",centers_begin,centers_end),
                    (party_get_slot,":rents",":center_no",slot_center_accumulated_rents),
                    (try_begin),
                        (party_slot_eq,":center_no",slot_party_type,spt_village),
                        (val_add,":rents",village_rent_increase_per_day),
                    (else_try),
                        (party_slot_eq,":center_no",slot_party_type,spt_castle),
                        (val_add,":rents",castle_rent_increase_per_day),
                    (else_try),
                        (party_slot_eq,":center_no",slot_party_type,spt_town),
                        (val_add,":rents",town_rent_increase_per_day),
                    (try_end),
                    (party_set_slot,":center_no",slot_center_accumulated_rents,":rents"),

                    # (str_store_party_name,s1,":center_no"),
                    # (assign,reg1,":rents"),
                    # (display_message,"@update {s1} 's rents {reg1}"),
                (try_end),
            ]),
            ## 领主收税
            (lord_auto_collect_tax_interval,[
                (try_for_range,":center_no",centers_begin,centers_end),
                    (party_get_slot,":lord",":center_no",slot_town_lord),
                    ## 如果领地有主人
                    (ge,":lord",0),
                    (party_get_slot,":rents",":center_no",slot_center_accumulated_rents),

                    ## 计算领主的租金(80%)
                    (store_mul,":lord_rents",":rents",80),
                    (val_div,":lord_rents",100),

                    ## 设置领主的财富
                    (troop_get_slot,":wealth",":lord",slot_troop_wealth),
                    (val_add,":wealth",":lord_rents"),
                    (troop_set_slot,":lord",slot_troop_wealth,":wealth"),

                    ## 计算领主的租金(20%)
                    (store_mul, ":center_rents", ":rents", 20),
                    (val_div, ":center_rents", 100),

                    ##领地的财富(用于村庄建设或巡逻队维护等等)
                    (party_get_slot,":town_wealth",":center_no",slot_town_wealth),
                    (val_add,":town_wealth",":center_rents"),
                    (party_set_slot,":center_no",slot_town_wealth,":town_wealth"),

                    ## 清空租金
                    (party_set_slot,":center_no",slot_center_accumulated_rents,0),

                    # (str_store_party_name,s1,":center_no"),
                    # (str_store_troop_name,s2,":lord"),
                    # (assign,reg1,":rents"),
                    # (assign,reg2,":lord_rents"),
                    # (assign,reg3,":center_rents"),
                    # (display_message,"@{s2} at {s1} get rents {reg1},add wealth is {reg2}，center add wealth is {reg3}"),
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
                "insertBefore":[
                    {
                        "sign":"village_center",
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
               "mno_troops_manage|管 理 村 民。"
            ]
        }
    }
}