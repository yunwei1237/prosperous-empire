# -*- coding: utf-8 -*-
from module_game_menus import game_menus
from module_scripts import *


'''
    领主收租功能
    
    领主会像玩家一样进行收租，用于军队建设，也会保存一些给城镇或村庄，用于基础维修
    
    如果据点没有主人，就会一直保存租金，直到有领主上任
'''

## 领主自动收税时间(7天收一次，和玩家一样)
lord_auto_collect_tax_interval = 24 * 7


## 村庄保留租金的比例 20%（用于村庄建设）
village_retain_ratio = 20


## 领主保留租金的比例 80%（用于军队招募和升级）
lord_retain_ratio = 100 - village_retain_ratio


lordCollectionRents = {
    "name":"LordCollectionRents",
    "enable":True,
    "simple_triggers":{
        "append":[
            ## 领主收税
            (lord_auto_collect_tax_interval,[
                (try_for_range,":center_no",centers_begin,centers_end),
                    (party_get_slot,":lord",":center_no",slot_town_lord),
                    ## 如果领地有主人
                    (ge,":lord",0),
                    (party_get_slot,":rents",":center_no",slot_center_accumulated_rents),

                    ## 计算领主的租金(80%)
                    (store_mul,":lord_rents",":rents",lord_retain_ratio),
                    (val_div,":lord_rents",100),

                    ## 设置领主的财富
                    (troop_get_slot,":wealth",":lord",slot_troop_wealth),
                    (val_add,":wealth",":lord_rents"),
                    (troop_set_slot,":lord",slot_troop_wealth,":wealth"),

                    ## 计算领主的租金(20%)
                    (store_mul, ":center_rents", ":rents", village_retain_ratio),
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
}