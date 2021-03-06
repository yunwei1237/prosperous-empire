# -*- coding: utf-8 -*-

## 包含一些对阵营常用的操作
from header_operations import *
from header_parties import *
from header_skills import *
from module_constants import *



## args
from modules.lord.HeroCollection_header import mergeList

## 姓氏
first = [u"陈",u"李",u"黄",u"张",u"朱",u"梁",u"林",u"刘",u"马",u"白",u"吴",u"曹",u"蔡",u"车",u"谭",u"罗",u"杨",u"诸 葛",u"司 马",u"南 宫",u"太 史",u"公 良",u"公 孙",u"公 良",u"百 里"]
## 名字
second = [u"宛",u"丘",u"形",u"采",u"用",u"其",u"利",u"器",u"用",u"桐",u"平",u"桃",u"山",u"明",u"月",u"朋",u"峰",u"峦",u"清",u"浮",u"桥",u"杰",u"贡",u"英",u"弄",u"三",u"武",u"言",u"玄 策",u"大 目",u"三 刀"]


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
                (call_script, "script_init_troop_age", ":troop", ":age"),
            ]),
            ("set_son_age",[
                (store_script_param,":father",1),
                (store_script_param,":son",2),
                (troop_get_slot,":father_age",":father",slot_troop_age),
                (store_random_in_range,":father_age_in_son_birth",20,30),
                (store_sub,":age",":father_age",":father_age_in_son_birth"),
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

                (store_faction_of_troop,":faction",":source_troop"),
                (try_begin),
                    (faction_slot_eq,":faction",slot_faction_leader,":source_troop"),
                    (faction_set_slot,":faction",slot_faction_leader,":target_troop"),
                (try_end),

                (call_script, "script_update_troop_notes",":target_troop"),
            ]),
            ("player_cosplay_anyone",[
                (store_script_param,":troop",1),

                (str_store_troop_name,s5,":troop"),
                (display_message,"@cosplay {s5}"),

                (troop_set_name,"trp_player",s5),
                (party_set_name,"p_main_party","str_s5_s_party"),

                (store_faction_of_troop,":faction",":troop"),
                (call_script,"script_player_join_faction",":faction"),

                (assign, "$player_has_homage", 1),

                (call_script,"script_get_center_of_lord",":troop","p_town_1"),
                (assign,":center",reg0),

                (call_script,"script_get_troop_all_items","trp_player",":troop"),

                (troop_equip_items,"trp_player"),
                (call_script,"script_get_troop_all_wealth","trp_player",":troop"),
                (call_script,"script_get_loard_all_centers","trp_player",":troop"),
                (troop_get_slot,":party",":troop",slot_troop_leaded_party),
                (call_script,"script_add_party_as_companions","p_main_party",":party",-1),
                (party_relocate_near_party,"p_main_party",":center",3),
            ]),
            ## 获得领主的军事强度
            ("get_lord_strength",[
                (store_script_param_1,":leader"),
                (assign,":strength",0),
                (try_begin),
                    (ge,":leader"),
                    ## 战术加成
                    (store_skill_level,":tactics",skl_tactics,":leader"),
                    (store_mul,":tactics_strength",":tactics",2),
                    (val_add,":strength",":tactics_strength"),
                    ## 教练加成
                    (store_skill_level,":trainer",skl_trainer,":leader"),
                    (store_mul,":trainer_strength",":trainer",2),
                    (val_add,":strength",":trainer_strength"),
                    ## 性格加成
                    (this_or_next|troop_slot_eq,":leader",slot_lord_reputation_type,lrep_martial),
                    (troop_slot_eq,":leader",slot_lord_reputation_type,lrep_quarrelsome),
                    (val_add,":strength",3),
                    ## 性格缺陷
                    (troop_slot_eq,":leader",slot_lord_reputation_type,lrep_custodian),
                    (val_sub,":strength",3),
                (try_end),
                (assign,reg0,":strength"),
            ]),
            ## 更新领主财富
            ("update_lord_wealth",[
                 (store_script_param_1, ":lord_no"),
                 (store_script_param_2, ":value"),
                 ## 0:失去钱 1：获得钱
                 (store_script_param, ":type",3),

                 (troop_get_slot,":wealth",":lord_no",slot_troop_wealth),
                 (try_begin),
                     (gt,":type",0),
                     (val_add,":wealth",":value"),
                 (else_try),
                    (val_sub,":wealth",":value"),
                 (try_end),
                 (troop_set_slot,":lord_no",slot_troop_wealth,":wealth"),
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