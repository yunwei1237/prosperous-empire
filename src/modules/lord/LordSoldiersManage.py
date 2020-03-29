# -*- coding: utf-8 -*-
from module_game_menus import game_menus
from module_scripts import *


'''
    领主军队管理功能
    
    领主会对军队进行相应的管理
    当没有国家交战时，会全部出售俘虏
    当有少量国家交战时，会出售它国俘虏，并招募本国俘虏
    当有大量国家交战时，会招募全部俘虏
    也就是不交战时，钱最重要，交战时士兵最重要
    
    时间越长，领主的士兵等级会越高，战斗力也越强
    
    ，该功能只针对以下性格的领主：
    1.军事的
    2.好战的
    3.和善的
    4.正直的
    5.冷酷的（坏人也有比较厉害的）
    6.善良的
    
    【重点】：招募和升级都是需要钱的，没有钱，就不会招募和升级！！！！
    
    
    注：如果全部都对军事做管理，那玩家将很大机率打不过任何一个领主
'''

## 领主自动维护士兵时间24 * 1(1天)
lord_auto_collect_tax_interval = 4

## 每次招募士兵花费
lord_recruit_soldiers_cost = 1500

## 每次更新士兵花费
lord_update_soldiers_cost = 700

lordSoldiersManage = {
    "name":"LordSoldiersManage",
    "enable":True,
    # "triggers":{
    #     "append":[
    #         ## 测试处理俘虏功能
    #         (0,0,ti_once,[],[
    #             (try_for_range,":lord_no",lords_begin,lords_end),
    #                 (troop_get_slot,":party",":lord_no",slot_troop_leaded_party),
    #                 (ge,":party",0),
    #                 (party_add_prisoners,":party","trp_swadian_knight",5),
    #                 (party_add_prisoners,":party","trp_vaegir_knight",5),
    #                 (party_add_prisoners,":party","trp_khergit_lancer",5),
    #                 (party_add_prisoners,":party","trp_nord_champion",5),
    #                 (party_add_prisoners,":party","trp_rhodok_sharpshooter",5),
    #                 (party_add_prisoners,":party","trp_sarranid_mamluke",5),
    #             (try_end),
    #         ]),
    #     ],
    # },
    "simple_triggers":{
        "append":[
            ## 领主军队维护
            (lord_auto_collect_tax_interval,[
                (try_for_range,":lord_no",lords_begin,lords_end),
                    (this_or_next|troop_slot_eq,":lord_no",slot_lord_reputation_type,lrep_martial),
                    (this_or_next|troop_slot_eq,":lord_no",slot_lord_reputation_type,lrep_goodnatured),
                    (this_or_next|troop_slot_eq,":lord_no",slot_lord_reputation_type,lrep_upstanding),
                    (this_or_next|troop_slot_eq,":lord_no",slot_lord_reputation_type,lrep_benefactor),
                    (this_or_next|troop_slot_eq,":lord_no",slot_lord_reputation_type,lrep_selfrighteous),
                    (troop_slot_eq,":lord_no",slot_lord_reputation_type,lrep_quarrelsome),

                    (troop_get_slot,":party",":lord_no",slot_troop_leaded_party),
                    (gt,":party",0),

                    ## 军队士兵数量
                    (party_get_num_companions,":party_size",":party"),

                    ## 理想士兵数量
                    (call_script,"script_party_get_ideal_size",":party"),
                    (assign,":ideal_size",reg0),

                    ## 需要补充的士兵数量
                    (store_sub,":need_add",":ideal_size",":party_size"),

                    # (str_store_troop_name_link, s1, ":lord_no"),
                    # (assign,reg1,":need_add"),
                    # (display_message,"@{s1} 需 要 补 充 的 士 兵 数 量 为 : {reg1}"),
                    # (troop_get_slot,":wealth",":lord_no",slot_troop_wealth),
                    # (assign,reg1,":wealth"),
                    # (display_message,"@{s1} 财 富 为 {reg1}(处 理 俘 虏 前)"),

                    (party_get_num_prisoners,":prisoners_num",":party"),
                    (try_begin),
                        ## 如果有俘虏就处理
                        (gt,":prisoners_num",0),
                        ## 根据当前国情进行俘虏处理
                        (store_faction_of_troop, ":faction", ":lord_no"),
                        (call_script, "script_get_num_of_enemy_state", ":faction"),
                        (assign, ":enemy_state_num", reg0),
                        (try_begin),
                            ## 没有有任何国家交战
                            (eq, ":enemy_state_num", 0),
                            ## 不需要补充士兵
                            (le,":need_add",0),
                            ## 俘虏全部出售
                            (assign, ":handle", -1),
                            #(display_message,"@{s1} 出 售 全 部 俘 虏"),
                        (else_try),
                            ## 交战国家较少
                            (le, ":enemy_state_num", 2),
                            ## 不需要补充士兵
                            (le,":need_add",0),
                            ## 本国招募，它国出售
                            (assign, ":handle", 0),
                            #(display_message,"@{s1} 招 募 部 分 俘 虏"),
                        (else_try),
                            ## 交战国家较多
                            ## 全部招募
                            (assign, ":handle", 1),
                            #(display_message,"@{s1} 招 募 全 部 俘 虏"),
                        (try_end),
                        ## 【处理俘虏】
                        (call_script, "script_party_handle_prisoners", ":party", ":handle"),
                    (try_end),

                    ## 重新计算军队士兵数量
                    (party_get_num_companions,":party_size",":party"),
                    ## 军事强度
                    (call_script,"script_get_lord_strength",":lord_no"),
                    (assign,":strength",reg0),

                    ## 需要补充的士兵数量
                    (store_sub,":need_add",":ideal_size",":party_size"),

                    # (str_store_troop_name_link, s1, ":lord_no"),
                    # (assign,reg1,":need_add"),
                    # (display_message,"@{s1} 需 要 补 充 的 士 兵 数 量 为 : {reg1}"),
                    # (troop_get_slot,":wealth",":lord_no",slot_troop_wealth),
                    # (assign,reg1,":wealth"),
                    # (str_store_troop_name_link,s1,":lord_no"),
                    # (display_message,"@{s1} 财 富 为 {reg1} ( 招 募 士 兵 前 )"),
                    ## 士兵补充
                    (try_begin),
                        ## 士兵需要补充
                        (lt, ":party_size", ":ideal_size"),
                        ## 钱足够
                        (troop_slot_ge,":lord_no",slot_troop_wealth,lord_recruit_soldiers_cost),
                        ## 增加士兵
                        (call_script, "script_party_add_members", ":party", -1, ":strength", 30, 50),
                        ## 减少钱财
                        (call_script,"script_update_lord_wealth",":lord_no",lord_recruit_soldiers_cost,-1),

                        # (str_store_troop_name_link, s1, ":lord_no"),
                        # (display_message,"@{s1} 补 充 士 兵"),
                        # (troop_get_slot,":wealth",":lord_no",slot_troop_wealth),
                        # (assign,reg1,":wealth"),
                        # (str_store_troop_name_link,s1,":lord_no"),
                        # (display_message,"@{s1} 财 富 为 {reg1}(招 募 士 兵 后)"),
                    (try_end),

                    ## 增加经验
                    (try_begin),
                        ## 钱足够
                        (troop_slot_ge, ":lord_no", slot_troop_wealth, lord_update_soldiers_cost),
                        ## 减少钱财
                        (call_script,"script_update_lord_wealth",":lord_no",lord_update_soldiers_cost,-1),
                        (call_script,"script_party_add_xp_and_upgrade",":party",":strength",70),

                        # (str_store_troop_name_link, s1, ":lord_no"),
                        # (display_message,"@{s1} 升 级 士 兵"),
                        # (troop_get_slot,":wealth",":lord_no",slot_troop_wealth),
                        # (assign,reg1,":wealth"),
                        # (str_store_troop_name_link,s1,":lord_no"),
                        # (display_message,"@{s1} 财 富 为 {reg1}(升 级 士 兵 后)"),
                    (try_end),
                    #(display_message,"@----------------------------------------------------------------------------------"),
                (try_end),
            ]),
        ],
    },
}