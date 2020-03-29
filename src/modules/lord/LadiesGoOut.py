# -*- coding: utf-8 -*-
from header_common import *
from header_operations import *

# '''
#     功能大概如下：
#     1.出城游玩（非战争期间）
#     2.打击劫匪
#     3.被俘虏交赎金（玩家）
# '''
from header_parties import ai_bhvr_patrol_party
from module_constants import *



'''

    女主出游：在没有战争时期，女主们会组织一小队人游山玩水。
'''

## 女士队伍小于人时开始招募士兵
lady_party_min_count = 17

## 敌国数量小于多少时才出来(等于0时代表没有任何战争时才出来游玩)
lady_can_go_out_enemy_state_num = 0

## 出游更新时间
lady_go_out_update_time = 12


ladiesGoOut={
    "name":"LadiesGoOut",
    "dependentOn":["PartyBaseScripts","FactionBaseScripts"],
    "simple_triggers":{
        "append":[
            (lady_go_out_update_time,[
                (call_script,"script_ladies_go_out"),
            ]),
        ],
    },
    "scripts":{
        "append":[
            ("ladies_go_out",[
                (display_message,"@ladies go out start"),
                (try_for_range,":lady_no",kingdom_ladies_begin,kingdom_ladies_end),
                    ## 获领导的队伍
                    (troop_get_slot, ":lead_party", ":lady_no", slot_troop_leaded_party),
                    ## 是否有交战
                    (store_faction_of_troop,":faction",":lady_no"),
                    ## 必须是当前活跃阵营
                    (is_between,":faction",kingdoms_begin,kingdoms_end),
                    (call_script,"script_get_num_of_enemy_state",":faction"),
                    (assign,":enemy_state_num",reg0),
                    (try_begin),
                        ## 非战争时期
                        (le,":enemy_state_num",lady_can_go_out_enemy_state_num),
                        #(troop_get_slot,":home",":lady_no",slot_troop_home),
                        (troop_get_slot,":home",":lady_no",slot_troop_cur_center),
                        # (str_store_troop_name,s1,":lady_no"),
                        # (str_store_party_name,s2,":home"),
                        # (display_message,"@lady({s1})'home is {s2}"),
                        # (assign,reg1,":lead_party"),
                        # (display_message,"@lead_party id is {reg1}"),
                        (try_begin),
                            (le,":lead_party",0),
                            ## 创建部队(-1代表使用默认值)
                            (call_script,"script_create_party",":lady_no",":home",-1,-1,-1,"icon_woman_b",-1),
                            (assign,":lady_party",reg0),
                            ## 增加士兵
                            (call_script,"script_party_add_members",":lady_party",-1,5,0,10),
                            ## 增加经验
                            (call_script,"script_party_add_xp_and_upgrade",":lady_party",20,100),
                            ## 设置ai
                            ##(call_script, "script_party_set_ai_state", ":lady_party",  spai_patrolling_around_center, ":home"),
                            (call_script,"script_party_change_ai_state",":lady_party",ai_bhvr_patrol_party,":home",5),
                            # (str_store_party_name,s1,":lady_party"),
                            # (display_message,"@lady party({s1}) be created"),
                            (call_script,"script_troop_leave_home",":lady_no"),
                        (else_try),
                            (party_get_num_companions,":size",":lead_party"),
                            (lt,":size",lady_party_min_count),
                            ## 增加士兵
                            (call_script,"script_party_add_members",":lead_party",-1,1,0,10),
                            ## 增加经验
                            (call_script,"script_party_add_xp_and_upgrade",":lead_party",3,100),
                            (str_store_party_name,s1,":lead_party"),
                            (display_message,"@lady party({s1}) is update"),
                        (try_end),
                    (else_try),
                        # 有战争时,不会出外游玩
                        (gt,":lead_party",0),
                        (str_store_party_name,s1,":lead_party"),
                        (display_message,"@lady party({s1}) is go home"),
                        (remove_party,":lead_party"),
                        (troop_set_slot,":lady_no",slot_troop_leaded_party,-1),
                        (call_script,"script_troop_go_home",":lady_no"),
                    (try_end),
                (try_end),
            ]),
        ],
    },
}