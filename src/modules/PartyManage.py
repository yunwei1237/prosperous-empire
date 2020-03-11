# -*- coding: utf-8 -*-

## constants


## slot
## 职责，同伴在队伍的职责
from header_common import *
from header_dialogs import *
from header_mission_templates import af_override_horse, mtef_visitor_source
from header_operations import *
from header_skills import *
from module_constants import *
from header_triggers import *

slot_party_team_duty = 405



## args

adjutant_least_int_level = 10 ##　智力10以上才能做副官


## slot_party_team_duty args
sptd_none = 0 ##　无职位
sptd_adjutant         = 1 ## 副官 整理部队，管理任命职责人员（军备，后勤，军医等等）
sptd_adviser          = 2 ## 谋士（提供各种建议）
sptd_armament         = 3 ## 军备（囤积箭矢，保存战利品）
sptd_chef             = 4 ## 厨师（基础士气，管理食物，自动购买）
sptd_accountant       = 5 ## 会计（保存金币，战败后几乎不丢失钱财）
sptd_military_surgeon = 6 ## 军医（减少死亡，恢复体力）
sptd_veterinarian     = 7 ## 兽医（减少死亡，战场恢复体力，治愈马匹）
sptd_siege_division   = 8 ## 攻城师（加快攻城建筑）
sptd_coach            = 9 ## 教练（增加经验）

sptd_end            = 10 ## 职位结束标识

partyManage={
    "name":"partyManage",
    "strings":{
        "sptd_none":"none",
        "sptd_adjutant":"adjutant",
        "sptd_adviser":"adviser",
        "sptd_armament":"armament",
        "sptd_chef":"chef",
        "sptd_accountant":"accountant",
        "sptd_military_surgeon":"military surgeon",
        "sptd_veterinarian":"veterinarian",
        "sptd_siege_division":"siege division",
        "sptd_coach":"coach",
    },
    "dialogs":[
        ### 【副官功能】=============================================================================================
        [anyone | plyr, "member_talk", [],"I want to appoint you as my adjutant.", "adjutant_appoint_talk", [
            ## 职位空缺
            (assign,":be_done",0),
            ## 对话人当前的职位
            (assign,":cur_duty"),
            (party_get_num_companions,":companions","p_main_party"),
            (try_for_range,":company",0,":companions"),
                (party_stack_get_troop_id,":troop",":company"),
                (troop_is_hero,":troop"),
                (try_begin),
                    ## 如果当前兵种是正在说话人的，就获得他的职位
                    (eq,"$g_talk_troop",":troop"),
                    (party_get_slot,":cur_duty",slot_party_team_duty),
                (try_end),
                (party_slot_eq,":troop",slot_party_team_duty,sptd_adjutant),
                (val_add,":be_done",1),
            (try_end),
            (store_attribute_level,":int_level",sf_base_att_int),
            ## 是否有人在做副官
            (assign,reg1,":be_done"),
            ## 当前npc的职责
            (assign,reg2,":cur_duty"),
            ## 当前npc的智力
            (assign,reg3,":int_level"),
        ]],
        ## 可以接受这个职位（1.该职位空缺 2.智力大于10　３.没有有做其它工作）
        [anyone, "adjutant_appoint_talk", [
            ## 等于0代表没有任何坐这个职位
            (eq,reg1,0),
            ## 没有做其它工作
            (eq,reg2,sptd_none),
            ## 智力大于10
            (ge,reg3,adjutant_least_int_level),
        ],"I'm honored to take this job", "close_window", [
            (party_set_slot,"$g_talk_troop",slot_party_team_duty,sptd_adjutant),
        ]],
        ## 不能接受1，智力小于10
        [anyone, "adjutant_appoint_talk", [
            ## 等于0代表没有任何坐这个职位
            (eq, reg1, 0),
            ## 没有做其它工作
            (eq, reg2, sptd_none),
            ## 智力小于10
            (lt, reg3, adjutant_least_int_level),
        ],"I'm sorry I can't do the job", "close_window", []],
        ## 不能接受2，该职位已经有人在做
        [anyone, "adjutant_appoint_talk", [
            ## 已经有人做了
            (gt, reg1, 0),
            ## 没有做其它工作
            (eq, reg2, sptd_none),
            ## 智力大于10
            (ge, reg3, adjutant_least_int_level),
        ],"Someone in our army has already done the work", "close_window", []],
        ## 不能接受3，当前已经有工作
        [anyone, "adjutant_appoint_talk", [
            ## 等于0代表没有任何坐这个职位
            (eq, reg1, 0),
            ## 已经有职责了
            (gt, reg2, sptd_none),
            ## 智力大于10
            (ge, reg3, adjutant_least_int_level),
        ], "I already have a very important job", "close_window", []],
        ## 副官职责
        ###### 进入副官对话
        [anyone | plyr, "member_talk", [
            (party_slot_eq,"$g_talk_troop",slot_party_team_duty,sptd_adjutant),
        ],"Let me talk about the army", "adjutant_team_talk", []],
        ###### [军队整理]
        [anyone | plyr, "adjutant_team_talk", [],"Please help me organize the team.", "adjutant_sort_team_talk", []],
        [anyone, "adjutant_sort_team_talk", [], "As you wish", "close_window", []],

        ###### [任命谋士]【智力10以上和说服力】（可以任命多个）
        [anyone | plyr, "adjutant_team_talk", [

        ],"I want to dismiss a adviser", "adjutant_appoint_adviser_talk_choice", [
            ## 解雇
            (assign,reg1,0),]],
        [anyone | plyr, "adjutant_team_talk", [], "I want to appoint a adviser", "adjutant_appoint_adviser_talk", [
            ## 任命
            (assign, reg1, 1),
        ]],
        [anyone, "adjutant_appoint_adviser_talk", [], "Who do you appoint ?", "adjutant_appoint_adviser_talk_choice",[]],
        ## 不选择的选项（玩家点击失误时，取消的选项）
        [anyone | plyr, "adjutant_appoint_adviser_talk_choice", [], "none", "close_window",[]],
        ## 给玩家一个列表，供玩家选择
        [anyone | plyr | repeat_for_troops, "adjutant_appoint_adviser_talk_choice", [
            (store_repeat_object, ":troop"),
            ## 是否在玩家队伍中
            (troop_slot_eq, ":troop", slot_troop_occupation, slto_player_companion),
            ## 保存队员名称
            (str_store_troop_name, s1, ":troop"),
            ## 保存队员技能等级
            (store_skill_level, reg1, ":troop", skl_persuasion),
            ## 技能等级至少为1
            (gt,reg1,0),
            ## 保存队员属性等级
            (store_attribute_level, reg2, ":troop", sf_base_att_int),
            (ge,reg2,10)
        ], "{s1} (persuasion {reg1})", "close_window", [
            (try_begin),
                (eq,reg1,1),
                (party_set_slot, "$g_talk_troop", slot_party_team_duty, sptd_adviser),
            (else_try),
                (party_set_slot, "$g_talk_troop", slot_party_team_duty, sptd_none),
            (try_end),
         ]],

        ### 任命（非副官和谋士的其它所有职位）
        ###### [任命军医]【手术，急救，疗伤，任何一项】
        [anyone | plyr | repeat_for_100, "adjutant_team_talk", [
            (store_repeat_object,":duty_no"),
            ## 确保不是副官和谋士
            (is_between,sptd_armament,sptd_end),
            ## 查找当前职位的人员
            (assign,":staff",-1),
            (party_get_num_companion_stacks, ":companions_stack", "p_main_party"),
            (try_for_range, ":i_stack", ":companions_stack"),
                (party_stack_get_troop_id, ":troop", ":i_stack"),
                (party_slot_eq, ":troop", slot_party_team_duty, reg1),
                (assign,":staff",":troop"),
            (try_end),
            ## 如果职员不为空
            (gt,":staff",0),
            ## 计算出职位的字符串编号
            (store_add,":str_no","str_sptd_none",":duty_no"),
            (str_store_string,s1,":str_no"),
            ## 计算出职位的字符串编号
            (assign,reg1,":duty_no"),
            (assign,reg2,":staff"),
            ## 给玩家显示下要解雇的名称，方便玩家判断
            (str_store_troop_name,s2,reg2),
        ], "I want to dismiss {s1} ({s2})", "adjutant_dismiss_talk", []],
        ## 提示玩家要解雇的人员
        [anyone, "adjutant_dismiss_talk", [
            (str_store_troop_name,s1,reg2),
        ], "I will inform {s1}", "close_window",[
            (party_set_slot, reg2, slot_party_team_duty, sptd_none),
        ]],
        ## 招募人员
        [anyone | plyr | repeat_for_100, "adjutant_team_talk", [
            (store_repeat_object,":duty_no"),
            ## 确保不是副官和谋士
            (is_between,sptd_armament,sptd_end),
            ## 查找当前职位的人员
            (assign,":staff",-1),
            (party_get_num_companion_stacks, ":companions_stack", "p_main_party"),
            (try_for_range, ":i_stack", ":companions_stack"),
                (party_stack_get_troop_id, ":troop", ":i_stack"),
                (party_slot_eq, ":troop", slot_party_team_duty, reg1),
                (assign,":staff",":troop"),
            (try_end),
            ## 如果职员为空才能再次招募和解雇完全相反
            (le,":staff",0),
            ## 计算出职位的字符串编号
            (store_add,":str_no","str_sptd_none",":duty_no"),
            (str_store_string,s1,":str_no"),
            ## 获得职位编号
            (assign,reg10,":duty_no"),
        ], "I want to appoint a {s1}", "adjutant_appoint_military_surgeon_talk",[]],
        ## 提示玩家进入选择职位的列表
        [anyone, "adjutant_appoint_military_surgeon_talk", [], "Who do you appoint ?",
         "adjutant_appoint_military_surgeon_talk_choice", []],
        ## 不选择的选项（玩家点击失误时，取消的选项）
        [anyone | plyr, "adjutant_appoint_military_surgeon_talk_choice", [], "none", "close_window", []],
        ## 给玩家一个列表，供玩家选择
        [anyone | plyr | repeat_for_troops, "adjutant_appoint_military_surgeon_talk_choice", [
            (store_repeat_object, ":troop"),
            ## 是否在玩家队伍中
            (troop_slot_eq, ":troop", slot_troop_occupation, slto_player_companion),
            ## 不同职位的条件判断(是否符合当前职位)
            (assign,":is_fit",0),
            ## 保存不同职业的描述信息
            (str_clear,s2),
            (try_begin),
                ## 军备官
                (eq,reg10,sptd_armament),
                ## 保存队员技能等级
                (store_skill_level, reg1, ":troop", skl_inventory_management),
                ## 技能等级至少为1
                (gt, reg1, 0),
                (assign,":is_fit",1),
                (assign,s2,"@inventory management:{reg1}"),
            (else_try),
                ## 厨师官
                (eq, reg10, sptd_chef),
                ## 保存队员技能等级
                (store_skill_level, reg1, ":troop", skl_weapon_master),
                ## 技能等级至少为1
                (gt, reg1, 0),
                (assign, ":is_fit", 1),
                (assign,s2,"@weapon master:{reg1}"),
            (else_try),
                ## 会计官
                (eq, reg10, sptd_accountant),
                ## 保存队员技能等级
                (store_skill_level, reg1, ":troop", skl_trade),
                ## 技能等级至少为1
                (gt, reg1, 0),
                (assign, ":is_fit", 1),
                (assign,s2,"@trade:{reg1}"),
            (else_try),
                ## 军医官
                (this_or_next|eq, reg10, sptd_military_surgeon),
                ## 兽医官
                (eq, reg10, sptd_veterinarian),
                ## 保存队员技能等级
                (store_skill_level, reg1, ":troop", skl_surgery),  ## 手术
                (store_skill_level, reg2, ":troop", skl_first_aid),  ## 急救
                (store_skill_level, reg3, ":troop", skl_wound_treatment),  ## 疗伤
                ## 技能等级至少为1
                (this_or_next | gt, reg1, 0),
                (this_or_next | gt, reg2, 0),
                (gt, reg3, 0),
                (assign, ":is_fit", 1),
                (try_begin),
                    (gt,reg1,0),
                    (str_store_string,s2,"@surgery:{reg1} "),
                (else_try),
                    (gt,reg2,0),
                    (str_store_string,s2,"@first aid:{reg2} "),
                (else_try),
                    (gt, reg3, 0),
                    (str_store_string, s2, "@wound treatment:{reg3} "),
                (try_end),
            (else_try),
                ## 攻城师
                (eq, reg10, sptd_siege_division),
                ## 保存队员技能等级
                (store_skill_level, reg1, ":troop", skl_engineer),  ## 工程学
                ## 技能等级至少为1
                (gt, reg1, 0),
                (assign, ":is_fit", 1),
                (assign,s2,"@engineer:{reg1}"),
            (else_try),
                ## 教练
                (eq, reg10, sptd_coach),
                ## 保存队员技能等级
                (store_skill_level, reg1, ":troop", skl_trainer),  ## 教练
                ## 技能等级至少为1
                (gt, reg1, 0),
                (assign, ":is_fit", 1),
                (assign, s2, "@trainer:{reg1}"),
            (try_end),
            ## 如果符合任何一个条件
            (eq,":is_fit",1),
            ## 保存队员名称
            (str_store_troop_name, s1, ":troop"),
            (assign,reg1,":troop"),
        ], "{s1} ({s2})", "close_window", [
             ## reg1 玩家选择的人员编号
             ## reg10 代表职位的编号，也就是以sptd_开头的变量
             (party_set_slot, reg1, slot_party_team_duty, reg10),
         ]],
        ### 【副官功能】=============================================================================================
    ],
    "scripts":[

        ## 更新人物的财产
        ("update_troop_wealth",
         [
             (store_script_param_1, ":troop"),
             (store_script_param_2, ":value"),
             ## 0:失去钱 1：获得钱
             (store_script_param, ":type",3),
             (troop_get_slot,":wealth",":troop",slot_troop_wealth),
             (try_begin),
                (gt,":type",0),
                (val_add,":wealth",":value"),
                (troop_add_gold, ":troop", ":value"),
             (else_try),
                (val_sub,":wealth",":value"),
                (troop_remove_gold, ":troop", ":value"),
             (try_end),
             (troop_set_slot,":troop",slot_troop_wealth,":wealth"),
             (play_sound, "snd_money_received"),
         ]),
        ## 军备官功能

        ## 收集和使用箭矢
        ("collect_or_use_arrows",[
            (store_script_param_1,":nums"),
            (store_script_param_2,":collect_or_use"),
            (assign,reg1,":nums"),
            (try_begin),
                (gt,":collect_or_use",0),
                (val_add,"$g_player_arrows",":nums"),
            (call_script,"script_update_troop_wealth","trp_player",),
                (display_message,"@buy arrows {reg1}."),
            (else_try),
                (val_sub,"$g_player_arrows",":nums"),
                (display_message,"@use arrows {reg1}."),
            (try_end),
        ]),
    ],
    "simple_triggers":[
        ## 每24小时购买一次箭矢
        (24,[
            (party_is_in_any_town,"p_main_party"),
            (assign,":has_armament",0),
            (party_stack_get_size,":stack","p_main_party"),
            (try_for_range,":i_stack",0,":stack"),
            (party_stack_get_troop_id,":troop",":i_stack"),
            (troop_is_hero,":troop"),
            (party_slot_eq,":troop",slot_party_team_duty,sptd_armament),
            (assign,":has_armament",1),
            (try_end),
            ## 如果有军备官
            (eq,":has_armament",1),
            ## 购买箭矢(每次500支，每支1金币)
            (call_script,"script_collect_or_use_arrows",500,1),
        ]),
    ],
    "mission_templates":{
        ## 创建新的战斗模板
        "create_mission_templates":[
            ("party_test",0,-1,"test mt",[],[]),
        ],
        ## 为战斗模板添加出生源信息
        "add_mission_template_spawns":{
            ## 为lead_charge战斗模板添加触发器，[]中是一个触发器列表
            "lead_charge":[
                (31,mtef_visitor_source,af_override_horse,0,1,[]),
            ]
        },
        ## 为战斗模板添加触发器
        "add_mission_template_triggers":{
            ## 为lead_charge战斗模板添加触发器，[]中是一个触发器列表
            "lead_charge":[
                (0.1, 0, ti_once, [(map_free,0)], [(dialog_box,"str_tutorial_map1")]),
            ]
        },
    },
}

  