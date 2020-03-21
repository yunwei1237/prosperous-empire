# -*- coding: utf-8 -*-
from header_common import *
from header_operations import *

# '''
#     功能大概如下：
#     1.出城游玩（非战争期间）
#     2.打击劫匪
#     3.被俘虏交赎金（玩家）
# '''
from module_constants import *




lady_party_min_count = 35

ladiesGoOut={
    "name":"LadiesGoOut",
    "dependentOn":["PartyBaseScripts"],
    "simple_triggers":{
        "append":[
            (12,[
                (call_script,"script_ladies_go_out"),
            ]),
        ],
    },
    "scripts":{
        "append":[
            ("ladies_go_out",[
                (try_for_range,":lady_no",kingdom_ladies_begin,kingdom_ladies_end),
                    ## 获领导的队伍
                    (troop_get_slot, ":lead_party", ":lady_no", slot_troop_leaded_party),
                    ## 是否有交战
                    (store_faction_of_party,":faction",":lady_no"),
                    (call_script,"script_get_num_of_enemy_state",":faction"),
                    (try_begin),
                        ## 非战争时期
                        (eq,reg0,0),
                        (troop_get_slot,":home",":lady_no",slot_troop_home),
                        (try_begin),
                            (lt,":lead_party",":home",),
                            ## 创建部队(-1代表使用默认值)
                            (call_script,"script_create_party",":lady_no",-1,-1,-1,-1,-1,-1),
                            ## 增加士兵
                            (call_script,"script_party_add_members",reg0,-1,3),
                            ## 增加经验
                            (call_script,"script_party_add_xp_and_upgrade",reg0,10,100),
                            ## 设置ai
                            (call_script, "script_party_set_ai_state", reg0,  spai_patrolling_around_center, ":home"),
                        (else_try),
                            (party_get_num_companions,":size",":lead_party"),
                            (lt,":size",lady_party_min_count),
                            ## 增加士兵
                            (call_script,"script_party_add_members",":lead_party",-1,3),
                            ## 增加经验
                            (call_script,"script_party_add_xp_and_upgrade",":lead_party",10,100),
                        (try_end),
                    (else_try),
                        ## 有战争时,不会出外游玩
                        (ge,":lead_party",0),
                        (remove_party,":lead_party"),
                        (troop_set_slot,":lady_no",slot_troop_leaded_party,-1),
                    (try_end),
                (try_end),
            ]),
        ],
    },
}