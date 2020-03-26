# -*- coding: utf-8 -*-
from header_operations import *
from modules.HeroCollection_header import repeatArcher1


def parseStrings(config):
    result = []
    for sysCfg in config:
        result.append(("system_" + sysCfg.get("name"),sysCfg.get("name")))
    return result

def parseCnsGameStrings(config):
    result = []
    for sysCfg in config:
        result.append(("str_system_{}|{}".format(sysCfg.get("name"),sysCfg.get("name_cns"))))
    return result


## 每一个系统的种类信息，就使用一个兵种来进行保存，第0位保存个数，其它保存输出物品类型
## 0:本系统个数

##
def createSysteTroop(config):
    result = []
    result.append(repeatArcher1(1, "system_begin")[0])
    for sysCfg in config:
        result.append(repeatArcher1(1,"system_" + sysCfg.get("name"))[0])
    result.append(repeatArcher1(1, "system_end")[0])

    for sysCfg in config:
        result.append(repeatArcher1(1,"system_{}_" + sysCfg.get("name"))[0])
    result.append(repeatArcher1(1, "system_end")[0])

    return result


system_begin = "trp_system_begin"
system_end = "trp_system_end"

system_kind_begin = "trp_system_kind_begin"
system_kind_end = "trp_system_kind_end"

def createSysteTroop(config):
    result = []

    result.append(repeatArcher1(1, "system_begin")[0])
    for sysCfg in config:
        result.append(repeatArcher1(1, "system_" + sysCfg.get("name"))[0])
    result.append(repeatArcher1(1, "system_end")[0])

    result.append(repeatArcher1(1, "system_kind_begin")[0])
    for sysCfg in config:
        systemName = sysCfg.get("name")
        kindList = sysCfg.get("kinds");
        size = len(kindList)
        for i in range(size):
            kindCfg = kindList[i]
            item = kindCfg.get("item")
            result.append(repeatArcher1(1, "system_"+systemName+"_" + item)[0])
    result.append(repeatArcher1(1, "system_kind_end")[0])
    return result


sk_item_index = 0
sk_create_money_index = 1
sk_cost_per_season_index = 2
sk_output_max_num_per_season_index = 3
sk_output_min_num_per_season_index = 4
sk_time_per_season_index = 5

def initSystemTroop(config):
    result = []
    for sysCfg in config:
        systemName = sysCfg.get("name")
        system_troop_id = "trp_system_{}".format(systemName)
        kindList = sysCfg.get("kinds");
        size = len(kindList)
        for i in range(size):
            kindCfg = kindList[i]
            item = kindCfg.get("item")
            system_kind_troop_id = "trp_system_{}_{}".format(systemName,item)
            result.append((troop_set_slot,system_troop_id,i,system_kind_troop_id))
            result.append((troop_set_slot,system_kind_troop_id,sk_item_index,kindCfg.get("item"))),
            result.append((troop_set_slot,system_kind_troop_id,sk_create_money_index,kindCfg.get("create_money"))),
            result.append((troop_set_slot,system_kind_troop_id,sk_cost_per_season_index,kindCfg.get("cost_per_season"))),
            result.append((troop_set_slot,system_kind_troop_id,sk_output_max_num_per_season_index,kindCfg.get("output_max_num_per_season"))),
            result.append((troop_set_slot,system_kind_troop_id,sk_output_min_num_per_season_index,kindCfg.get("output_min_num_per_season"))),
            result.append((troop_set_slot,system_kind_troop_id,sk_time_per_season_index,kindCfg.get("time_per_season"))),
    return result



