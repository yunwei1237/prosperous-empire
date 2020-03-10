# -*- coding: utf-8 -*-

## constants


## slot
## 职责，同伴在队伍的职责
from header_common import *
from header_dialogs import *
from header_operations import *
from header_skills import *
from module_constants import *

slot_party_team_duty = 405



## args

adjutant_least_int_level = 10 ##　智力10以上才能做副官


## slot_party_team_duty args
sptd_none = 0 ##　无职位
sptd_adjutant         = 1 ## 副官 整理部队，管理任命职责人员（军备，后勤，军医等等）
sptd_armament         = 2 ## 军备（囤积箭矢，保存战利品）
sptd_chef             = 3 ## 厨师（基础士气，管理食物，自动购买）
sptd_accountant       = 4 ## 会计（保存金币，战败后几乎不丢失钱财）
sptd_adviser          = 5 ## 谋士（提供各种建议）
sptd_military_surgeon = 6 ## 军医（减少死亡，恢复体力）
sptd_veterinarian     = 7 ## 兽医（减少死亡，战场恢复体力，治愈马匹）
sptd_siege_division   = 8 ## 攻城师（加快攻城建筑）
sptd_coach            = 9 ## 教练（增加经验）

partyManage={
    "name":"partyManage",
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
        ###### [任命军备官]【物品管理】
        [anyone | plyr, "adjutant_team_talk", [
            ## 查找并取消任命
            (party_get_num_companion_stacks,":companions_stack","p_main_party"),
            (try_for_range,":i_stack",":companions_stack"),
                (party_stack_get_troop_id,":troop",":i_stack"),
                (party_slot_eq,":troop",slot_party_team_duty,sptd_armament),
                (party_set_slot,":troop",slot_party_team_duty,sptd_none),
            (try_end),
        ],"I want to dismiss a armament", "close_window", []],
        [anyone | plyr, "adjutant_team_talk", [],"I want to appoint a armament", "adjutant_appoint_armament_talk", []],
        [anyone, "adjutant_appoint_armament_talk", [], "Who do you appoint ?", "adjutant_appoint_armament_talk_choice", []],
        ## 不选择的选项（玩家点击失误时，取消的选项）
        [anyone | plyr, "adjutant_appoint_armament_talk_choice", [], "none", "close_window", []],
        ## 给玩家一个列表，供玩家选择
        [anyone | plyr | repeat_for_troops, "adjutant_appoint_armament_talk_choice", [
            (store_repeat_object,":troop"),
            ## 是否在玩家队伍中
            (troop_slot_eq, ":troop", slot_troop_occupation, slto_player_companion),
            ## 保存队员名称
            (str_store_troop_name,s1,":troop"),
            ## 保存队员技能等级
            (store_skill_level,reg1,":troop",skl_inventory_management),
            ## 技能等级至少为1
            (gt,reg1,0),
        ], "{s1} (inventory management {reg1})", "close_window", [
            (party_set_slot,"$g_talk_troop",slot_party_team_duty,sptd_armament),
        ]],

        ###### [任命厨师长]【武器掌握】
        [anyone | plyr, "adjutant_team_talk", [
            ## 查找并取消任命
            (party_get_num_companion_stacks,":companions_stack","p_main_party"),
            (try_for_range,":i_stack",":companions_stack"),
                (party_stack_get_troop_id,":troop",":i_stack"),
                (party_slot_eq,":troop",slot_party_team_duty,sptd_chef),
                (party_set_slot,":troop",slot_party_team_duty,sptd_none),
            (try_end),
        ],"I want to dismiss a chef", "close_window", []],
        [anyone | plyr, "adjutant_team_talk", [], "I want to appoint a chef", "adjutant_appoint_chef_talk", []],
        [anyone, "adjutant_appoint_chef_talk", [], "Who do you appoint ?", "adjutant_appoint_chef_talk_choice",[]],
        ## 不选择的选项（玩家点击失误时，取消的选项）
        [anyone | plyr, "adjutant_appoint_chef_talk_choice", [], "none", "close_window", []],
        ## 给玩家一个列表，供玩家选择
        [anyone | plyr | repeat_for_troops, "adjutant_appoint_chef_talk_choice", [
            (store_repeat_object, ":troop"),
            ## 是否在玩家队伍中
            (troop_slot_eq, ":troop", slot_troop_occupation, slto_player_companion),
            ## 保存队员名称
            (str_store_troop_name, s1, ":troop"),
            ## 保存队员技能等级
            (store_skill_level, reg1, ":troop", skl_weapon_master),
            ## 技能等级至少为1
            (gt,reg1,0),
        ], "{s1} (inventory management {reg1})", "close_window", [
             (party_set_slot, "$g_talk_troop", slot_party_team_duty, sptd_chef),
         ]],

        ###### [任命会计]【交易】
        [anyone | plyr, "adjutant_team_talk", [
            ## 查找并取消任命
            (party_get_num_companion_stacks,":companions_stack","p_main_party"),
            (try_for_range,":i_stack",":companions_stack"),
                (party_stack_get_troop_id,":troop",":i_stack"),
                (party_slot_eq,":troop",slot_party_team_duty,sptd_accountant),
                (party_set_slot,":troop",slot_party_team_duty,sptd_none),
            (try_end),
        ],"I want to dismiss a chef", "close_window", []],
        [anyone | plyr, "adjutant_team_talk", [], "I want to appoint a accountant", "adjutant_appoint_accountant_talk", []],
        [anyone, "adjutant_appoint_accountant_talk", [], "Who do you appoint ?", "adjutant_appoint_accountant_talk_choice",[]],
        ## 不选择的选项（玩家点击失误时，取消的选项）
        [anyone | plyr, "adjutant_appoint_accountant_talk_choice", [], "none", "close_window", []],
        ## 给玩家一个列表，供玩家选择
        [anyone | plyr | repeat_for_troops, "adjutant_appoint_accountant_talk_choice", [
            (store_repeat_object, ":troop"),
            ## 是否在玩家队伍中
            (troop_slot_eq, ":troop", slot_troop_occupation, slto_player_companion),
            ## 保存队员名称
            (str_store_troop_name, s1, ":troop"),
            ## 保存队员技能等级
            (store_skill_level, reg1, ":troop", skl_trade),
            ## 技能等级至少为1
            (gt,reg1,0),
        ], "{s1} (inventory management {reg1})", "close_window", [
             (party_set_slot, "$g_talk_troop", slot_party_team_duty, sptd_accountant),
         ]],

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

        ###### [任命军医]【手术，急救，疗伤，任何一项】
        [anyone | plyr, "adjutant_team_talk", [
            ## 查找并取消任命
            (party_get_num_companion_stacks, ":companions_stack", "p_main_party"),
            (try_for_range, ":i_stack", ":companions_stack"),
            (party_stack_get_troop_id, ":troop", ":i_stack"),
            (party_slot_eq, ":troop", slot_party_team_duty, sptd_military_surgeon),
            (party_set_slot, ":troop", slot_party_team_duty, sptd_none),
            (try_end),
        ], "I want to dismiss a military surgeon", "close_window", []],
        [anyone | plyr, "adjutant_team_talk", [], "I want to appoint a military surgeon", "adjutant_appoint_military_surgeon_talk",
         []],
        [anyone, "adjutant_appoint_military_surgeon_talk", [], "Who do you appoint ?",
         "adjutant_appoint_military_surgeon_talk_choice", []],
        ## 不选择的选项（玩家点击失误时，取消的选项）
        [anyone | plyr, "adjutant_appoint_military_surgeon_talk_choice", [], "none", "close_window", []],
        ## 给玩家一个列表，供玩家选择
        [anyone | plyr | repeat_for_troops, "adjutant_appoint_military_surgeon_talk_choice", [
            (store_repeat_object, ":troop"),
            ## 是否在玩家队伍中
            (troop_slot_eq, ":troop", slot_troop_occupation, slto_player_companion),
            ## 保存队员名称
            (str_store_troop_name, s1, ":troop"),
            ## 保存队员技能等级
            (store_skill_level, reg1, ":troop", skl_surgery), ## 手术
            (store_skill_level, reg2, ":troop", skl_first_aid), ## 急救
            (store_skill_level, reg3, ":troop", skl_wound_treatment), ## 疗伤
            ## 技能等级至少为1
            (this_or_next|gt,reg1,0),
            (this_or_next|gt,reg2,0),
            (gt,reg3,0),
        ], "{s1} (surgery {reg1},first aid {reg2},wound treatment {reg3})", "close_window", [
             (party_set_slot, "$g_talk_troop", slot_party_team_duty, sptd_military_surgeon),
         ]],
        ### 【副官功能】=============================================================================================
    ],
    "scripts":[

    ],
}



