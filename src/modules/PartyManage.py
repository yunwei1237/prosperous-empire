# -*- coding: utf-8 -*-

## constants


## slot
## 职责，同伴在队伍的职责
from header_dialogs import *
from header_mission_templates import *
from header_operations import *
from header_skills import *
from header_triggers import *
from module_constants import *

slot_party_team_duty = 405



## args

adjutant_least_int_level = 10 ##　智力10以上才能做副官

adviser_least_int_level = 12 ## 智力12以上才能做谋士
## 无命令
player_command_none = -1
## 解雇
player_command_dismiss = 0

## 任命
player_command_appoint = 1


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
    "enable":True,
    "strings":{
        "append":[
            ("sptd_none","none"),
            ("sptd_adjutant","adjutant"),
            ("sptd_adviser","adviser"),
            ("sptd_armament","armament"),
            ("sptd_chef","chef"),
            ("sptd_accountant","accountant"),
            ("sptd_military_surgeon","military surgeon"),
            ("sptd_veterinarian","veterinarian"),
            ("sptd_siege_division","siege division"),
            ("sptd_coach","coach"),
            ("doctor_skill_info","surgery:{reg1},first aid:{reg2},wound treatment:{reg3}"),
        ],
    },
    "dialogs":{
        "append":[
### 【副官功能】=============================================================================================
            [anyone | plyr, "member_talk", [

                (str_store_troop_name,s3,"$g_talk_troop"),
                (try_begin),
                    (gt,"$g_player_adjutant",0),
                    (str_store_troop_name,s1,"$g_player_adjutant"),
                    (display_message, "@队 伍 副 官 : {s1}"),
                (try_end),

                (party_get_slot, ":duty", "$g_talk_troop", slot_party_team_duty),
                (val_add, ":duty", "str_sptd_none"),
                (str_store_string, s2, ":duty"),
                (display_message, "@{s3} 的 职 业 : {s2}"),

                (store_attribute_level,reg1,"$g_talk_troop",sf_base_att_int),
                (display_message, "@{s3} 的 智 力 : {reg1}"),

                ## 如果已经是了，就不显示任命对话框
                (neg|party_slot_eq,"$g_talk_troop",slot_party_team_duty,sptd_adjutant),
            ],"I want to appoint you as my adjutant(int {reg1}).", "adjutant_appoint_talk", []],

            ## 解除副官
            [anyone | plyr, "member_talk", [
                ## 如果已经是了，就不显示任命对话框
                (party_slot_eq,"$g_talk_troop",slot_party_team_duty,sptd_adjutant),
            ],"I want to dismiss you", "adjutant_dismiss_talk", []],

            [anyone, "adjutant_dismiss_talk", [],"ok", "member_talk", [
                ## 任命副官
                (party_set_slot,"$g_talk_troop",slot_party_team_duty,sptd_none),
                ## 记录副官信息
                (assign,"$g_player_adjutant",0),
            ]],

            ## 可以接受这个职位（1.该职位空缺 2.智力大于10　３.没有有做其它工作）
            [anyone, "adjutant_appoint_talk", [
                ## 职位空缺
                (le,"$g_player_adjutant",0),
                ## 当前人物空闲
                (party_slot_eq,"$g_talk_troop",slot_party_team_duty,sptd_none),
                ## 智力大于10
                (store_attribute_level,":int_level","$g_talk_troop",sf_base_att_int),
                (ge,":int_level",adjutant_least_int_level),
            ],"I'm honored to take this job", "member_talk", [
                ## 任命副官
                (party_set_slot,"$g_talk_troop",slot_party_team_duty,sptd_adjutant),
                ## 记录副官信息
                (assign,"$g_player_adjutant","$g_talk_troop"),
            ]],
            ## 不能接受1，智力小于10
            [anyone, "adjutant_appoint_talk", [
                (store_attribute_level, ":int_level", "$g_talk_troop", sf_base_att_int),
                ## 智力大于10
                (lt, ":int_level", adjutant_least_int_level),
                (assign,reg1,adjutant_least_int_level),
                (str_store_string,s1,"@int last {reg1}"),
            ],"I'm sorry I can't do the job({s1})", "member_talk", []],
            ## 不能接受2，该职位已经有人在做
            [anyone, "adjutant_appoint_talk", [
                ## 职位空缺
                (gt, "$g_player_adjutant", 0),
                (str_store_troop_name,s1,"$g_player_adjutant"),
            ],"Someone in our army has already done the work({s1})", "member_talk", []],
            ## 不能接受3，当前已经有工作
            [anyone, "adjutant_appoint_talk", [
                ## 当前人物空闲
                (party_get_slot,":duty","$g_talk_troop",slot_party_team_duty),
                (gt,":duty",sptd_none),
                (val_add,":duty","str_sptd_none"),
                (str_store_string,s1,":duty"),
            ], "I already have a very important job({s1})", "member_talk", []],
            ## 副官职责


            ###### 进入副官对话
            [anyone | plyr, "member_talk", [
                (party_slot_eq,"$g_talk_troop",slot_party_team_duty,sptd_adjutant),
            ],"Let me talk about the army", "adjutant_team_into_talk", []],
            [anyone, "adjutant_team_into_talk", [],"is ok ?", "adjutant_team_talk", []],
            ###### [军队整理]
            [anyone | plyr, "adjutant_team_talk", [],"Please help me organize the team.", "adjutant_sort_team_talk", []],
            [anyone, "adjutant_sort_team_talk", [], "As you wish", "adjutant_team_into_talk", []],

            ###### [任命谋士]【智力10以上和说服力】（可以任命多个）
            [anyone | plyr, "adjutant_team_talk", [
                (assign,reg1,adviser_least_int_level),
                (str_store_string,s1,"@int last {reg1}"),
            ],"I want to dismiss a adviser ({s1})", "adjutant_appoint_adviser_into_talk_choice", [
                ## 解雇
                (assign,"$g_player_command",player_command_dismiss),
            ]],
            [anyone | plyr, "adjutant_team_talk", [], "I want to appoint a adviser", "adjutant_appoint_adviser_into_talk_choice", [
                ## 任命
                (assign, "$g_player_command", player_command_appoint),
            ]],

            [anyone, "adjutant_appoint_adviser_into_talk_choice", [], "Who do you appoint ?", "adjutant_appoint_adviser_talk_choice",[]],

            ## 不选择的选项（玩家点击失误时，取消的选项）
            [anyone | plyr, "adjutant_appoint_adviser_talk_choice", [], "none", "adjutant_team_into_talk", []],

            ## 给玩家一个列表，供玩家选择
            [anyone | plyr | repeat_for_troops, "adjutant_appoint_adviser_talk_choice", [
                (store_repeat_object, ":troop"),
                ## 是否在玩家队伍中
                (troop_slot_eq, ":troop", slot_troop_occupation, slto_player_companion),
                ## 保存队员名称
                (str_store_troop_name, s1, ":troop"),

                ## 保存队员技能等级
                (store_skill_level, reg10, skl_persuasion, ":troop"),
                ## 保存队员属性等级
                (store_attribute_level, reg20, ":troop", sf_base_att_int),

                (assign,":continue",0),
                (try_begin),
                    (eq,"$g_player_command",player_command_appoint),
                    ## 技能等级至少为1
                    (ge, reg10, 1),
                    (ge, reg20, adviser_least_int_level),
                    (party_slot_eq, ":troop", slot_party_team_duty, sptd_none),
                    (assign,":continue",1),
                (else_try),
                    (eq,"$g_player_command",player_command_dismiss),
                    (party_slot_eq, ":troop", slot_party_team_duty, sptd_adviser),
                    (assign,":continue",1),
                (try_end),
                (eq,":continue",1),
            ], "{s1} (persuasion {reg10}  int {reg20})", "adjutant_appoint_adviser_into_talk_choice", [
                (store_repeat_object, ":troop"),
                (str_store_troop_name,s2,":troop"),
                (try_begin),
                    (eq,"$g_player_command",player_command_appoint),
                    (display_message,"@任 命 {s2}"),
                    (party_set_slot, ":troop", slot_party_team_duty, sptd_adviser),
                (else_try),
                    (display_message,"@解 雇 {s2}"),
                    (party_set_slot, ":troop", slot_party_team_duty, sptd_none),
                (try_end),

                #(assign,"$g_player_command",player_command_none),
             ]],


            ###### 询问计策
            [anyone | plyr, "member_talk", [
                (party_slot_eq,"$g_talk_troop",slot_party_team_duty,sptd_adviser),
            ],"Do you have any good ideas", "adviser_team_good_idea_talk", []],
            ## 好的
            [anyone, "adviser_team_good_idea_talk", [],"no yet", "member_talk", []],


            ###### 解雇职员
            [anyone | plyr, "adjutant_team_talk", [], "I want to dismiss a clerk", "adjutant_team_dismiss_clerk_talk", []],
            ## 好的
            [anyone, "adjutant_team_dismiss_clerk_talk", [], "What staff would you like to appoint?", "adjutant_team_dismiss_clerk_talk_choice", []],

            [anyone | plyr, "adjutant_team_dismiss_clerk_talk_choice", [], "forget it", "adjutant_team_dissmiss_clerk_talk_choice_none",[]],

            [anyone | plyr, "adjutant_team_dissmiss_clerk_talk_choice_none", [], "ok", "adjutant_team_talk",[]],

            [anyone | plyr | repeat_for_troops, "adjutant_team_dismiss_clerk_talk_choice", [
                (store_repeat_object,":troop"),
                ## 是否在玩家队伍中
                (troop_slot_eq, ":troop", slot_troop_occupation, slto_player_companion),
                (party_get_slot,":duty_no",":troop",slot_party_team_duty),
                ## 确定任职
                (neq,":duty_no",sptd_none),
                ## 确保不是副官和谋士
                (is_between,":duty_no",sptd_armament,sptd_end),
                ## 保存队员名称
                (str_store_troop_name, s1, ":troop"),
                # ## 查找当前职位的人员
                # ## 计算出职位的字符串编号
                (store_add,":str_no","str_sptd_none",":duty_no"),
                (str_store_string,s2,":str_no"),
            ], "I want to dismiss {s1} ({s2})", "adjutant_team_dismiss_clerk_talk", [
                (store_repeat_object,":troop"),

                ## 保存队员名称
                (str_store_troop_name, s1, ":troop"),
                # ## 查找当前职位的人员
                # ## 计算出职位的字符串编号
                (party_get_slot,":duty_no",":troop",slot_party_team_duty),
                (store_add, ":str_no", "str_sptd_none", ":duty_no"),
                (str_store_string, s2, ":str_no"),
                (display_message,"@解 雇 {s1}({s2})"),

                ## 解雇
                (party_set_slot,":troop",slot_party_team_duty,sptd_none),

            ]],

            ###### 招募职员
            [anyone | plyr, "adjutant_team_talk", [], "I want to appoint a clerk", "adjutant_team_appoint_clerk_talk", []],
            ## 好的
            [anyone, "adjutant_team_appoint_clerk_talk", [], "What staff would you like to appoint?", "adjutant_team_appoint_clerk_talk_choice", []],

            [anyone | plyr, "adjutant_team_appoint_clerk_talk_choice", [], "forget it", "adjutant_team_appoint_clerk_talk_choice_none",[]],
            [anyone | plyr, "adjutant_team_appoint_clerk_talk_choice_none", [], "ok", "adjutant_team_talk",[]],

            ## 招募人员
            [anyone | plyr | repeat_for_100, "adjutant_team_appoint_clerk_talk_choice", [
                (store_repeat_object,":duty_no"),
                ## 确保不是副官和谋士
                (is_between,":duty_no",sptd_armament,sptd_end),
                ## 查找当前职位的人员
                (assign,":staff",-1),
                (party_get_num_companion_stacks, ":companions_stack", "p_main_party"),
                (try_for_range, ":i_stack",0,":companions_stack"),
                    (party_stack_get_troop_id, ":troop","p_main_party", ":i_stack"),
                    (troop_is_hero,":troop"),
                    (str_store_troop_name,s2,":troop"),
                    (display_message,"@troop name is: {s2}"),
                    (party_slot_eq, ":troop", slot_party_team_duty, ":duty_no"),
                    (display_message,"@staff troop name is: {s2}"),
                    (assign,":staff",":troop"),
                (try_end),
                (assign,reg1,":staff"),
                (display_message,"@staff {reg1}"),
                ## 如果职员为空才能再次招募和解雇完全相反
                (le,":staff",0),
                ## 计算出职位的字符串编号
                (store_add,":str_no","str_sptd_none",":duty_no"),
                (str_store_string,s1,":str_no"),

            ], "I want to appoint a {s1}", "adjutant_appoint_clerk_talk",[
                (store_repeat_object,":duty_no"),
                ## 获得职位编号
                (assign,reg10,":duty_no"),
            ]],
            ## 提示玩家进入选择职位的列表
            [anyone, "adjutant_appoint_clerk_talk", [], "Who do you appoint ?","adjutant_appoint_clerk_talk_choice", []],
            ## 不选择的选项（玩家点击失误时，取消的选项）
            [anyone | plyr, "adjutant_appoint_clerk_talk_choice", [], "none", "adjutant_appoint_clerk_talk_choice_none", []],
            [anyone, "adjutant_appoint_clerk_talk_choice_none", [], "ok", "adjutant_team_appoint_clerk_talk_choice", []],
            ## 给玩家一个列表，供玩家选择
            [anyone | plyr | repeat_for_troops, "adjutant_appoint_clerk_talk_choice", [
                (store_repeat_object, ":troop"),
                ## 必须是没有职位
                (party_slot_eq,":troop",slot_party_team_duty,sptd_none),
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
                    (store_skill_level, reg1, skl_inventory_management, ":troop"),
                    ## 技能等级至少为1
                    (gt, reg1, 0),
                    (assign,":is_fit",1),
                    (str_store_string,s2,"@inventory:{reg1}"),
                (else_try),
                    ## 厨师官
                    (eq, reg10, sptd_chef),
                    ## 保存队员技能等级
                    (store_skill_level, reg1, skl_weapon_master, ":troop"),
                    ## 技能等级至少为1
                    (gt, reg1, 0),
                    (assign, ":is_fit", 1),
                    (str_store_string,s2,"@weapon master:{reg1}"),
                (else_try),
                    ## 会计官
                    (eq, reg10, sptd_accountant),
                    ## 保存队员技能等级
                    (store_skill_level, reg1, skl_trade, ":troop"),
                    ## 技能等级至少为1
                    (gt, reg1, 0),
                    (assign, ":is_fit", 1),
                    (str_store_string,s2,"@trade:{reg1}"),
                (else_try),
                    ## 军医官
                    (this_or_next|eq, reg10, sptd_military_surgeon),
                    ## 兽医官
                    (eq, reg10, sptd_veterinarian),
                    ## 保存队员技能等级
                    (store_skill_level, reg1, skl_surgery, ":troop"),  ## 手术
                    (store_skill_level, reg2, skl_first_aid, ":troop"),  ## 急救
                    (store_skill_level, reg3, skl_wound_treatment, ":troop"),  ## 疗伤
                    ## 技能等级至少为1
                    (this_or_next | gt, reg1, 0),
                    (this_or_next | gt, reg2, 0),
                    (gt, reg3, 0),
                    (assign, ":is_fit", 1),
                    # (try_begin),
                    #     (gt,reg1,0),
                    #     (str_store_string,s2,"@surgery:{reg1}"),
                    # (else_try),
                    #     (gt,reg2,0),
                    #     (str_store_string,s2,"@first aid:{reg2}"),
                    # (else_try),
                    #     (gt, reg3, 0),
                    #     (str_store_string, s2, "@wound treatment:{reg3}"),
                    # (try_end),
                    (str_store_string, s2, "str_doctor_skill_info"),
                (else_try),
                    ## 攻城师
                    (eq, reg10, sptd_siege_division),
                    ## 保存队员技能等级
                    (store_skill_level, reg1, skl_engineer, ":troop"),  ## 工程学
                    ## 技能等级至少为1
                    (gt, reg1, 0),
                    (assign, ":is_fit", 1),
                    (str_store_string,s2,"@engineer:{reg1}"),
                (else_try),
                    ## 教练
                    (eq, reg10, sptd_coach),
                    ## 保存队员技能等级
                    (store_skill_level, reg1, skl_trainer, ":troop"),  ## 教练
                    ## 技能等级至少为1
                    (gt, reg1, 0),
                    (assign, ":is_fit", 1),
                    (str_store_string, s2, "@trainer:{reg1}"),
                (try_end),
                ## 如果符合任何一个条件
                (eq,":is_fit",1),
                ## 保存队员名称
                (str_store_troop_name, s1, ":troop"),
                (assign,reg1,":troop"),
            ], "{s1} ({s2})", "adjutant_team_appoint_clerk_talk", [
                 ## reg1 玩家选择的人员编号
                 ## reg10 代表职位的编号，也就是以sptd_开头的变量
                (store_repeat_object, ":troop"),

                (str_store_troop_name,s5,":troop"),

                (store_add, ":str_no", "str_sptd_none", reg10),
                (str_store_string, s6, ":str_no"),

                (display_message,"@任 命 {s5} 为 {s6}"),

                 (party_set_slot, ":troop", slot_party_team_duty, reg10),
             ]],
            ## 【副官功能】=============================================================================================

            ###### 没什么事
            [anyone | plyr, "adjutant_team_talk", [],"is nothing", "adjutant_team_nothing_talk", []],
            ## 好的
            [anyone | plyr, "adjutant_team_nothing_talk", [],"ok", "member_talk", []],
      ],
    },
    "scripts":{
        "append":[
            ## 更新人物的财产
            ("update_troop_wealth", [
                (store_script_param_1, ":troop"),
                (store_script_param_2, ":value"),
                ## 0:失去钱 1：获得钱
                (store_script_param, ":type", 3),
                (troop_get_slot, ":wealth", ":troop", slot_troop_wealth),
                (try_begin),
                (gt, ":type", 0),
                (val_add, ":wealth", ":value"),
                (troop_add_gold, ":troop", ":value"),
                (else_try),
                (val_sub, ":wealth", ":value"),
                (troop_remove_gold, ":troop", ":value"),
                (try_end),
                (troop_set_slot, ":troop", slot_troop_wealth, ":wealth"),
                (play_sound, "snd_money_received"),
            ]),
            ## 军备官功能
            ## 收集和使用箭矢
            ("collect_or_use_arrows", [
                (store_script_param_1, ":nums"),
                (store_script_param_2, ":collect_or_use"),
                (assign, reg1, ":nums"),
                (try_begin),
                (gt, ":collect_or_use", 0),
                (val_add, "$g_player_arrows", ":nums"),
                (call_script, "script_update_troop_wealth", "trp_player",),
                (display_message, "@buy arrows {reg1}."),
                (else_try),
                (val_sub, "$g_player_arrows", ":nums"),
                (display_message, "@use arrows {reg1}."),
                (try_end),
            ]),
        ],
    },
    "simple_triggers":{
        "append":[
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
    },
    "mission_templates":{
        "append":[
            ("party_test",0,-1,"test mt",[],[]),
        ],
        "children":{
            "lead_charge>#4":{
                "append":[
                    (31,mtef_visitor_source,af_override_horse,0,1,[]),
                ],
            },
            "lead_charge>#5":{
                "append":[
                    (0.1, 0, ti_once, [(map_free,0)], [(dialog_box,"str_tutorial_map1")]),
                ],
            }
        },
    },
    "internationals":{
        "cns":{
            "game_strings":[
                "str_sptd_none|无 职 位",
                "str_sptd_adjutant|副 官",
                "str_sptd_adviser|谋 士",
                "str_sptd_armament|军 需 官",
                "str_sptd_chef|厨 师 长",
                "str_sptd_accountant|会 计 员",
                "str_sptd_military_surgeon|军 医 官",
                "str_sptd_veterinarian|兽 医 官",
                "str_sptd_siege_division|攻 城 官",
                "str_sptd_coach|教 练",
                "str_doctor_skill_info|手 术 :{reg1},急 救 :{reg2},疗 伤 :{reg3}",
            ],
            "dialogs":[
                "dlga_member_talk:adjutant_appoint_talk|我 想 要 任 命 你 为 我 的 副 官 ( 智 力 : {reg1} )",
                "dlga_member_talk:adjutant_dismiss_talk|我 不 需 要 你 做 副 官 了",
                "dlga_member_talk:adjutant_team_into_talk|让 我 们 来 讨 论 下 军 队 的 事 务",

                "dlga_adjutant_team_into_talk:adjutant_team_talk|好 的 , 老 大",

                "dlga_adjutant_appoint_talk:member_talk|我 很 荣 幸 能 够 做 这 个 工 作",
                "dlga_adjutant_appoint_talk:member_talk.1|我 不 能 胜 任 这 个 工 作 ({s1})",
                "dlga_adjutant_appoint_talk:member_talk.2|已 经 有 人 在 做 这 个 工 作 了 ({s1})",
                "dlga_adjutant_appoint_talk:member_talk.3|我 已 经 有 一 个 很 重 要 的 工 作 了 ({s1})",

                "dlga_adjutant_dismiss_talk:member_talk|好 的 ， 老 大",

                "dlga_adjutant_team_talk:adjutant_sort_team_talk|请 帮 我 整 理 下 军 队",
                "dlga_adjutant_team_talk:adjutant_sort_team_talk.1|算 了 吧",
                "dlga_adjutant_sort_team_talk:adjutant_team_into_talk|如 你 所 愿",


                "dlga_adjutant_team_talk:adjutant_appoint_adviser_into_talk_choice|我 想 解 雇 一 个 谋 士",
                "dlga_adjutant_team_talk:adjutant_appoint_adviser_into_talk_choice.1|我 想 任 命 一 个 谋 士 (说 服 力 最 少 1,{s1})",
                "dlga_adjutant_team_talk:adjutant_team_nothing_talk|没 事",

                "dlga_adjutant_team_nothing_talk:member_talk|好 的",

                "dlga_adjutant_appoint_adviser_talk_choice:adjutant_team_into_talk|不 用 了",
                "dlga_adjutant_appoint_adviser_talk_choice:adjutant_appoint_adviser_into_talk_choice|{s1} (说 服 力 : {reg10} 智 力 : {reg20})",
                "dlga_adjutant_appoint_adviser_into_talk_choice:adjutant_appoint_adviser_talk_choice|您 想 指 定 谁 ？",

                "dlga_member_talk:adviser_team_good_idea_talk|你 有 什 么 好 想 法 吗 ?",
                "dlga_adviser_team_good_idea_talk:member_talk|还 没 有 !",




                "dlga_adjutant_team_talk:adjutant_team_dismiss_clerk_talk|我 想 要 解 雇 一 个 职 员",
                "dlga_adjutant_team_dismiss_clerk_talk:adjutant_team_dismiss_clerk_talk_choice|你 想 要 解 雇 哪 一 个 职 员 ?",

                "dlga_adjutant_team_dismiss_clerk_talk_choice:adjutant_team_dissmiss_clerk_talk_choice_none|算 了",
                "dlga_adjutant_team_dissmiss_clerk_talk_choice_none:adjutant_team_talk|好 的",
                "dlga_adjutant_team_dismiss_clerk_talk_choice:adjutant_team_dismiss_clerk_talk|我 想 要 解 雇 {s1} ({s2})",

                "dlga_adjutant_team_talk:adjutant_team_appoint_clerk_talk|我 想 要 任 命 一 个 职 员",
                "dlga_adjutant_team_appoint_clerk_talk:adjutant_team_appoint_clerk_talk_choice|你 想 任 命 哪 种 职 员 ?",

                "dlga_adjutant_team_appoint_clerk_talk_choice:adjutant_team_appoint_clerk_talk_choice_none|算 了",
                "dlga_adjutant_team_appoint_clerk_talk_choice_none:adjutant_team_talk|好 的",
                "dlga_adjutant_team_appoint_clerk_talk_choice:adjutant_appoint_clerk_talk|我 想 要 任 命 一 个 {s1}",

                "dlga_adjutant_appoint_clerk_talk:adjutant_appoint_clerk_talk_choice|你 想 任 命 谁 ?",

                ##"dlga_adjutant_appoint_clerk_talk_choice:adjutant_appoint_clerk_talk_choice|我 想 要 任 命 {s1}",

                "dlga_adjutant_appoint_clerk_talk_choice:adjutant_appoint_clerk_talk_choice_none|算 了",
                "dlga_adjutant_appoint_clerk_talk_choice_none:adjutant_team_appoint_clerk_talk_choice|好 的",
            ],
            "quick_strings":[
                #"qstr_surgery:{reg1}|手 术 :{reg1}",
                "qstr_trainer:{reg1}|教 练 :{reg1}",
                "qstr_inventory:{reg1}|物 品 管 理 :{reg1}", ##
                "qstr_weapon_master:{reg1}|武 器 管 理 :{reg1}",
                "qstr_trade:{reg1}|交 易 :{reg1}",
                #"qstr_first_aid:{reg2}|急 救 :{reg2}",
                #"qstr_wound_treatment:{reg3}|疗 伤 :{reg3}",
                "qstr_engineer:{reg1}|工 程 师 :{reg1}",
                "qstr_trainer:{reg1}|教 练 :{reg1}",
                "qstr_int_last_{reg1}|智 力 最 少 {reg1}",
            ],
        }
    },
}