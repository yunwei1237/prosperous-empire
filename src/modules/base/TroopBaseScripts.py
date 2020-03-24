# -*- coding: utf-8 -*-

## 包含一些对阵营常用的操作
from header_operations import *
from header_parties import *
from header_skills import skl_trainer
from module_constants import *



## args
from modules.HeroCollection_header import mergeList

## 姓氏
first = [u"陈",u"李",u"黄",u"张",u"梁",u"林",u"刘",u"吴",u"罗",u"杨",u"诸 葛",u"司 马"]
## 名字
second = [u"宛",u"丘",u"形",u"采",u"用",u"其",u"利",u"器",u"用",u"以",u"木",u"德",u"玄 策",u"大 目"]


def parseFirstStrings(chars):
    list = []
    for index in range(len(chars)):
        list.append((u"first_name_{}".format(index).encode('utf-8'),u"{}".format(chars[index]).encode('utf-8')))
    list.append(("first_name_end","end"))
    return list

def parseSecondStrings(chars):
    list = []
    for index in range(len(chars)):
        list.append((u"second_name_{}".format(index).encode('utf-8'),u"{}".format(chars[index]).encode('utf-8')))
    list.append(("second_name_end","end"))
    return list

def parseCnsFirstStrings(chars):
    list = []
    for index in range(len(chars)):
        list.append(u"str_first_name_{}|{}".format(index,chars[index]).encode('utf-8'))
    return list

def parseCnsSecondStrings(chars):
    list = []
    for index in range(len(chars)):
        list.append(u"str_second_name_{}|{}".format(index,chars[index]).encode('utf-8'))
    return list

first_begin = "str_first_name_0"
first_end = "str_first_name_end"

second_begin = "str_second_name_0"
second_end = "str_second_name_end"



## slot
slot_troop_first_name = 177
slot_troop_second_name = 178

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

            ("set_random_name",[
                (store_script_param_1,":troop"),
                (store_random_in_range,":first",first_begin,first_end),
                (store_random_in_range,":second",second_begin,second_end),
                (troop_set_slot,":troop",slot_troop_first_name,":first"),
                (troop_set_slot,":troop",slot_troop_second_name,":second"),
                (str_store_string,s1,":first"),
                (str_store_string,s2,":second"),
                (troop_set_name,":troop","str_s1_s2_name"),
            ]),
            ("get_random_first_name",[
                (store_random_in_range,":first",first_begin,first_end),
                (assign,reg0,":first"),
            ]),
            ("get_random_second_name", [
                (store_random_in_range, ":second", second_begin, second_end),
                (assign,reg0,":second"),
            ]),

            ("set_name_for_son", [
                (store_script_param_1, ":father"),
                (store_script_param_2, ":son"),
                (troop_get_slot,":first_name",":father",slot_troop_first_name),
                (call_script,"script_get_random_second_name"),
                (assign,":second_name",reg0),

                (troop_set_slot,":son",slot_troop_first_name,":first_name"),
                (troop_set_slot,":son",slot_troop_second_name,":second_name"),

                (str_store_string, s1, ":first_name"),
                (str_store_string, s2, ":second_name"),
                (troop_set_name, ":son", "str_s1_s2_name"),

                (troop_set_slot, ":son", slot_troop_father, ":father"),
            ]),

            ("set_age_in_range",[
                (store_script_param,":troop",1),
                (store_script_param,":min_age",2),
                (store_script_param,":max_age",3),
                (store_random_in_range, ":age", ":min_age", ":max_age"),
                (call_script, "script_init_troop_age", ":father", ":age"),
            ]),
            ("set_son_age",[
                (store_script_param,":father",1),
                (store_script_param,":son",2),
                (troop_get_slot,":father_age",":father",slot_troop_age),
                (store_random_in_range,":father_age_in_son_birth",20,30),
                (store_sub,":son_age",":father_age",":father_age_in_son_birth"),
                (call_script, "script_init_troop_age", ":father", ":age"),
            ]),
            ("troop_clear_items",[
                (store_script_param,":troop",1),
                (troop_get_inventory_capacity, ":inv_size", ":troop"),
                (try_for_range, ":i_slot", 0, ":inv_size"),
                    (troop_get_inventory_slot, ":item_id", ":troop", ":i_slot"),
                    (ge, ":item_id", 0),
                    (troop_remove_item,":troop",":item_id"),
                (try_end),
            ]),
            ("get_troop_all_items",[
                (store_script_param,":target_troop",1),
                (store_script_param,":source_troop",2),
                (call_script,"script_troop_clear_items",":target_troop"),

                (troop_get_inventory_capacity, ":inv_size", ":source_troop"),
                (try_for_range, ":i_slot", 0, ":inv_size"),
                    (troop_get_inventory_slot, ":item_id", ":source_troop", ":i_slot"),
                    (ge, ":item_id", 0),
                    (troop_add_item,":target_troop",":item_id"),
                (try_end),
            ]),
            ("get_troop_all_wealth",[
                (store_script_param,":target_troop",1),
                (store_script_param,":source_troop",2),
                (troop_get_slot,":wealth",":source_troop",slot_troop_wealth),
                (troop_get_slot,":renown",":source_troop",slot_troop_renown),
                (troop_get_slot,":father",":source_troop",slot_troop_father),
                (troop_get_slot,":mother",":source_troop",slot_troop_mother),
                (troop_get_slot,":spouse",":source_troop",slot_troop_spouse),
                (troop_get_slot,":guardian",":source_troop",slot_troop_guardian),
                (troop_get_slot,":betrothed",":source_troop",slot_troop_betrothed),

                (troop_set_slot,":target_troop",slot_troop_wealth,":wealth"),
                (troop_set_slot,":target_troop",slot_troop_renown,":renown"),
                (troop_set_slot,":target_troop",slot_troop_father,":father"),
                (troop_set_slot,":target_troop",slot_troop_mother,":mother"),
                (troop_set_slot,":target_troop",slot_troop_spouse,":spouse"),
                (troop_set_slot,":target_troop",slot_troop_guardian,":guardian"),
                (troop_set_slot,":target_troop",slot_troop_betrothed,":betrothed"),

                (call_script, "script_update_troop_notes",":target_troop"),
            ]),
        ],
    },
    "strings":{
        "append":mergeList(
            parseFirstStrings(first),
            parseSecondStrings(second),
            [
                ("s5_leave_home","{s5} leave home"),
                ("s5_go_home","{s5} go home"),
                ("s1_s2_name","{s1} {s2}"),
            ],
        ),
    },

    "internationals":{
        "cns":{
            "game_strings":mergeList(
                parseCnsFirstStrings(first),
                parseCnsSecondStrings(second),
                [
                    "str_s5_leave_home|{s5}出 门 了",
                    "str_s5_go_home|{s5}回 家 了",
                    "str_s1_s2_name|{s1}{s2}",
                ]
            ),
        }
    }
}


##print parseCnsFirstStrings(first)