# -*- coding: utf-8 -*-
from ID_parties import *
from ID_troops import *
from header_dialogs import *
from module_scripts import *

from modules.lord.HeroCollection_header import *




## 英雄数量
from modules.base.TroopBaseScripts import *

hero_size = 50


## 生一个小孩的可能性
has_one_children_probability = 30


## 生两个小孩的可能性
has_two_children_probability = 5


## 初始军事强度
hero_party_init_strength = 5


## 多久更新一次英雄部队
hero_party_update_interval = 12


## 英雄士兵数量小于时，就开始招募
hero_party_min_count = 35

## 英雄加入玩家队伍需要的关系值
hero_join_player_party_relation = 25

## 村民每次交易货款
farmer_trade_money = 500

## 商人每次交易货款
merchant_trade_money = 1000


## 英雄图标
hero_leader_map_icon = "icon_peasant"
hero_farmer_map_icon = "icon_village_a"
hero_looter_map_icon = "icon_axeman"
hero_merchant_map_icon = "icon_mule"
hero_soldier_map_icon = "icon_vaegir_knight"
hero_lord_map_icon = "icon_gray_knight"
hero_king_map_icon = "icon_gray_knight"

## 以下内容非程序员不要修改

## constans

hero_begin = "trp_hero_1"
hero_end = "trp_hero_end"

## slot

## 英雄状态
slot_troop_hero_status = getTroopSlotNo("slot_troop_hero_status")

## 作为领军（没有目标和理想）
## AI:
# 基本：巡逻家乡附近并与劫匪作战，靠战利品，物品，俘虏过生活（支付队伍工资）
## 贫穷时（财富为0时）：性格比较好的会变成农民，性格不好的会变成劫匪
## 富有时（财富为5000时）：有军事和好战性格时大机率会选择成为士兵，没有此性格时，会选择作为商人
##
sths_is_leader      = 0
## 在做农民
## AI:
# 基本：带领农民与城镇进行交易，靠货物生活
## 富有时，会变成领军
sths_is_farmer      = 1
## 在做不法之徒
## AI:带领劫匪攻击农民，玩家，商队，领主，国王,靠战利品，物品，俘虏生活
##
sths_is_outlaws      = 2
## 在做商人
## AI:带领商队，来回于城镇之间，靠货物生活，招募俘虏（支付队伍工资）
sths_is_merchant    = 3
## 在做士兵（在玩家或领主队伍中）
## AI:
## 1.服务玩家时：加入玩家队伍，与玩家并肩作战
## 2.服务领主和国王时：独自领军，并跟随领主或国王
## 3.服务领地时：巡逻领地，并与劫匪和敌国作战
## 声望高时，会做被国王封为领主
##　
sths_is_soldier     = 4
## 在做一个国家的领主
## AI:独自领军，保护自己的土地，招募英雄为随从，跟随元帅与敌军战斗，作为元帅时，率领领主大军作战，（支付队伍工资）
## 当声望高时，拥有特殊性格（贪婪的）时，会选择独立，创建一个全新政权
sths_is_lord        = 5
## 在做国王
## AI:独自领军，保护自己的土地，与敌国作战，招募英雄为领主或招募英雄为随从，作为元帅时，率领领主大军作战，（支付队伍工资）

sths_is_king        = 6

sths_end            = 7


hero_status_begin = sths_is_leader
hero_status_end = sths_end


outlaws_spawn_point_begin = p_steppe_bandit_spawn_point
outlaws_spawn_point_end = p_desert_bandit_spawn_point + 1

## 英雄出生在哪个国家（招兵时会使用他出生的国家兵种）
slot_troop_from_faction = getTroopSlotNo("slot_troop_from_faction")


## 英雄服务的目标队伍
## 士兵：服务的领主
## 劫匪：巢穴
slot_troop_service_target = getTroopSlotNo("slot_troop_service_target")


heroCollection = {
    "name":"HeroCollection",
    "enable":True,
    "dependentOn":["PartyBaseScripts","TroopBaseScripts","AiBaseScripts"],
    "troops":
        {
            "insertBefore":[
                {
                    "sign":"heroes_end",
                    "data":mergeList(repeatRandomTroop(hero_size,"hero_{}"),repeatArcher1(1,"hero_end")),
                }
            ]
        },
    "party_templates":{
        "append":[
            ("hero_leader_party", "{!}hero_leader_party", 0, 0, fac_commoners, 0, [(trp_watchman,5,10),(trp_caravan_guard,1,5),(trp_mercenary_crossbowman,1,5),(trp_hired_blade,1,2),(trp_mercenary_horseman,2,5),(trp_mercenary_cavalry,1,2)]),
        ],
    },
    "simple_triggers":{
        "append":[
            ## 村民和商人的思想
            (2,[
                (try_for_range,":hero",hero_begin,hero_end),
                    (call_script,"script_display_troop_info",":hero"),
                    (call_script,"script_trade_party_ai_update",":hero"),
                (try_end),
            ]),
        ],
    },
    "triggers":{
        "append":[
            ## 游戏开始时就初始化英雄信息(只更新一次)
            (0,0,ti_once,[],[
                #(display_message,"@heros is init"),
                (call_script,"script_init_hero_collection"),
            ]),
        ],
    },
    "scripts":{
        "append":[
            ## 只会被使用一次
            ("init_hero_collection",[
                ## 初始化人员信息
                (try_for_range,":troop",hero_begin,hero_end),
                    ## 姓名
                    (call_script,"script_set_random_name",":troop"),
                    ## 生活状态(随机职业,不包含国王)
                    (store_random_in_range,":hero_status",hero_status_begin,hero_status_end - 1),
                    (troop_set_slot,":troop", slot_troop_hero_status, ":hero_status"),
                    ## 职业
                    (troop_set_slot, ":troop", slot_troop_occupation, slto_kingdom_hero),
                    ## 性格 (直接使用系统领主性格)
                    (store_random_in_range,":reputation",lrep_none,lrep_conventional),
                    (troop_set_slot,":troop",slot_lord_reputation_type,":reputation"),
                    ## 财富
                    (store_random_in_range,":wealth",200,2000),
                    (troop_set_slot,":troop",slot_troop_wealth,":wealth"),
                    ## 声望
                    (store_random_in_range,":renown",20,100),
                    (troop_set_slot,":troop",slot_troop_renown,":renown"),


                    ## 家乡和阵营
                    (try_begin),
                        (troop_slot_eq,":troop",slot_troop_hero_status,sths_is_leader),
                        (store_random_in_range,":hometown",centers_begin,centers_end),
                        (assign,":cur_faction","fac_commoners"),
                    (else_try),
                        (this_or_next|troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_farmer),
                        (this_or_next|troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_merchant),
                        (this_or_next|troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_soldier),
                        (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_lord),
                        (try_begin),
                            (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_farmer),
                            (store_random_in_range,":hometown",villages_begin,villages_end),
                        (else_try),
                            (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_merchant),
                            (store_random_in_range,":hometown",towns_begin,towns_end),
                        (else_try),
                            (store_random_in_range,":hometown",centers_begin,centers_begin),
                        (try_end),
                        (store_faction_of_party,":from_faction",":hometown"),
                        (assign,":cur_faction",":from_faction"),
                    (else_try),
                        (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_outlaws),
                        (assign,":cur_faction","fac_outlaws"),
                    (try_end),

                    ## 家乡
                    (troop_set_slot,":troop",slot_troop_home,":hometown"),
                    ## 出生时的阵营（用于招兵）
                    (store_faction_of_party,":from_faction",":hometown"),
                    (troop_set_slot,":troop",slot_troop_from_faction,":from_faction"),
                    ## 当前加入的阵营
                    (troop_set_faction, ":troop", ":cur_faction"),
                    ## 服务对象
                    (call_script,"script_get_service_target",":troop"),
                    (assign,":service_target",reg0),
                    (troop_set_slot, ":troop", slot_troop_service_target, ":service_target"),
                    # (str_store_troop_name_link,s1,":troop"),
                    # (str_store_faction_name_link,s2,":faction"),
                    # (str_store_party_name_link,s3,":center"),
                    # (display_message,"@hero({s1})'faction is {s2},home is {s3}"),

                (try_end),
                ## 初始化人员关系（只设置，父亲，儿子，没有庞大家族）
                (assign,":next",0),
                (try_for_range,":unused",0,hero_size),
                    ## 索引不能超出范围
                    (lt,":next",hero_size),
                    ## 计算出要处理的英雄编号
                    (store_add,":hero",hero_begin,":next"),
                    ## 将index指向下个要处理的编号
                    (val_add,":next",1),
                    (assign,":father",":hero"),
                    ## 年龄
                    (call_script,"script_set_age_in_range",":father",45,60),
                    ## 随机生成长子(80%机率)
                    (store_random_in_range,":isSun",1,101),
                    (try_begin),
                        (le,":isSun",has_one_children_probability),
                        (assign,":son",":next"),
                        (val_add,":next",1),
                        ## 儿子年龄
                        (call_script,"script_set_son_age",":father",":son"),
                        ## 儿子的名字
                        (call_script,"script_set_name_for_son",":father",":son"),

                        # (str_store_troop_name_link,s10,":father"),
                        # (str_store_troop_name_link,s20,":son"),
                        # (display_message,"@{s10} has a first children({s20})"),
                    (try_end),
                (try_end),
                ## 更新所有英雄的信息
                (call_script, "script_update_all_notes"),
            ]),
            ## 更新英雄的状态，定时更新
            ("create_hero_party",[
                ## 队伍领导者
                (store_script_param,":troop",1),
                ## 在哪个据点创建
                (store_script_param,":center",2),
                ## 队伍出现在据点附近的距离
                (store_script_param,":radius",3),
                (troop_get_slot,":party",":troop",slot_troop_leaded_party),
                ## 队伍无效后（被击败）,需要创建队伍
                (lt,":party",0),

                ## 部队创建时的参数准备
                (assign,":init_xp",hero_party_init_strength),
                (try_begin),
                    (this_or_next | troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_king),
                    (this_or_next | troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_soldier),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_lord),
                    ## -1 代表使用国家特有兵种
                    (assign,":party_template",-1),
                (else_try),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_leader),
                    (assign,":party_template","pt_hero_leader_party"),
                (else_try),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_merchant),
                    (assign,":party_template","pt_kingdom_caravan_party"),
                (else_try),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_farmer),
                    (assign,":party_template","pt_village_farmers"),
                (else_try),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_outlaws),
                    (troop_get_slot, ":spawn_point",":troop", slot_troop_service_target),
                    (try_begin),
                        (eq,":spawn_point",p_steppe_bandit_spawn_point),
                        (assign,":party_template","pt_steppe_bandits"),
                    (else_try),
                        (eq,":spawn_point",p_taiga_bandit_spawn_point),
                        (assign,":party_template","pt_taiga_bandits"),
                    (else_try),
                        (eq,":spawn_point",p_mountain_bandit_spawn_point),
                        (assign,":party_template","pt_mountain_bandits"),
                    (else_try),
                        (eq,":spawn_point",p_forest_bandit_spawn_point),
                        (assign,":party_template","pt_forest_bandits"),
                    (else_try),
                        (eq,":spawn_point",p_sea_raider_spawn_point_1),
                        (assign,":party_template","pt_sea_raiders"),
                    (else_try),
                        (eq,":spawn_point",p_desert_bandit_spawn_point),
                        (assign,":party_template","pt_desert_bandits"),
                    (try_end),
                    ## 不法之徒不升级士兵
                    (assign,":init_xp",0),
                (try_end),
                ## 获得队伍图标
                (call_script,"script_get_hero_map_icon",":troop"),
                (assign,":map_icon",reg0),
                ## 阵营
                (store_faction_of_troop,":faction",":troop"),
                ## 创建队伍
                (call_script,"script_create_party",":troop",":center", ":faction", ":radius", -1, spt_kingdom_hero_party, ":map_icon", -1),
                (assign,":party",reg0),
                ## 增加士兵
                (troop_get_slot, ":faction", ":troop", slot_troop_from_faction),
                (call_script,"script_party_add_members",":party",":faction",hero_party_init_strength,":party_template",60,40),
                ## 增加经验
                (call_script,"script_party_add_xp_and_upgrade",":party",hero_party_init_strength,20),
                # (str_store_party_name_link,s1,":party"),
                # (str_store_party_name_link,s2,":home"),
                # (display_message,"@party({s1}) is create at {s2}"),
            ]),
            ("get_hero_map_icon",[
                (store_script_param_1,":troop"),
                (try_begin),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_leader),
                    (assign,":map_icon",hero_leader_map_icon),
                (else_try),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_farmer),
                    (assign,":map_icon",hero_farmer_map_icon),
                (else_try),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_outlaws),
                    (assign,":map_icon",hero_looter_map_icon),
                (else_try),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_merchant),
                    (assign,":map_icon",hero_merchant_map_icon),
                (else_try),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_soldier),
                    (assign,":map_icon",hero_soldier_map_icon),
                (else_try),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_lord),
                    (assign,":map_icon",hero_lord_map_icon),
                (else_try),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_king),
                    (assign,":map_icon",hero_king_map_icon),
                (try_end),
                (assign,reg0,":map_icon"),
            ]),
            ## 服务对象策略：
            # 士兵，家乡领主>城堡或城镇领主>国王
            # 劫匪：巢穴
            ("get_service_target",[
                (store_script_param_1,":troop"),
                (troop_get_slot,":hometown",":troop",slot_troop_home),
                (assign,":service_target",-1),
                (try_begin),
                    ## 服务于家乡的领主（或国王）
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_soldier),
                    (try_begin),
                        ## 家乡是城镇或城堡时
                        (this_or_next|is_between, ":hometown", towns_begin, towns_end),
                        (is_between, ":hometown", castles_begin, castles_end),
                        (try_begin),
                            (party_get_slot, ":lord", ":hometown", slot_town_lord),
                            ## 服务于家乡的领主
                            (gt, ":lord", 0),
                            (assign,":service_target",":lord"),
                        (else_try),
                            ## 家乡没有领主时，服务于国王
                            (store_faction_of_party,":faction",":hometown"),
                            (faction_get_slot,":king",":faction",slot_faction_leader),
                            (assign,":service_target",":king"),
                        (try_end),
                    (else_try),
                        ## 家乡是村庄
                        (is_between, ":hometown", villages_begin, villages_end),
                        (try_begin),
                            (party_get_slot, ":lord", ":hometown", slot_town_lord),
                            ## 服务于村庄的领主
                            (gt, ":lord", 0),
                            (assign,":service_target",":lord"),
                        (else_try),
                            ## 村庄没有领主时，服务于城堡或城镇的领主
                            (party_get_slot,":up_center",":hometown",slot_village_bound_center),
                            (party_get_slot,":lord",":up_center",slot_town_lord),
                            (gt, ":lord", 0),
                            (assign,":service_target",":lord"),
                        (else_try),
                            ## 城堡或城镇没有领主时，服务于国王
                            (store_faction_of_party,":faction",":hometown"),
                            (faction_get_slot,":king",":faction",slot_faction_leader),
                            (assign,":service_target",":king"),
                        (try_end),
                    (try_end),
                (else_try),
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_outlaws),
                    (store_random_in_range,":spawn_point",outlaws_spawn_point_begin,outlaws_spawn_point_end),
                    (assign,":service_target",":spawn_point"),
                (try_end),
                (assign,reg0,":service_target"),
            ]),
            ## 交易队伍ai【核心ai之一】
            ("trade_party_ai_update",[
                (store_script_param_1,":troop"),
                (this_or_next | troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_farmer),
                (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_merchant),
                ## 获得英雄领导的队伍
                (troop_get_slot,":party",":troop",slot_troop_leaded_party),
                ## 获得英雄的家（城堡或者村庄）
                (troop_get_slot,":home",":troop",slot_troop_home),
                ## 创建队伍（如果领导的队伍被打败了，或者队伍第一次出现地图）
                (try_begin),
                    ## 队伍没有创建时（或被打败）,创建队伍
                    (le,":party",0),
                    ## 创建队伍
                    (call_script,"script_create_hero_party",":troop",":home",0),
                    (assign,":party",reg0),
                (try_end),
                ## 获得英雄当前所在的地点
                (party_get_cur_town,":cur_center",":party"),

                ## 获得村民或商人要交易的城市
                (assign,":trade_town",-1),
                ## 获得英雄即将交易城市
                (try_begin),
                    ## 村民的话，就去市里做交易
                    (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_farmer),
                    (party_get_slot,":trade_town",":home",slot_village_bound_center),
                (else_try),
                    ## 商人的话
                    (try_begin),
                        ## 如果家乡是村庄，就去市里交易
                        (is_between,":home",villages_begin,villages_end),
                        (party_get_slot,":trade_town",":home",slot_village_bound_center),
                    (else_try),
                        ## 否则，就去附近的城镇交易
                        (call_script,"script_get_the_nearby_center",":home",spt_town),
                        (assign,":trade_town",reg0),
                    (try_end),
                (try_end),

                (try_begin),
                    ## 英雄是否在家
                    (eq,":cur_center",":home"),
                    ## 英雄没有被俘虏
                    (troop_slot_eq,":troop",slot_troop_prisoner_of_party,-1),
                    ## 从家出发，去市里卖货
                    (call_script,"script_set_party_ai_go_to_center",":party",":trade_town"),
                    (display_message,"@hero go to trade town"),
                (else_try),
                    ## 英雄在交易的城市里
                    (this_or_next|eq,":cur_center",":trade_town"),
                    ## 交易城市没有被围攻
                    (party_slot_eq,":trade_town",slot_center_is_besieged_by,-1),
                    ## 开始回家
                    (call_script,"script_set_party_ai_go_to_center",":party",":home"),
                    ## 收货钱
                    (try_begin),
                        (troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_farmer),
                        (call_script,"script_update_lord_wealth",":troop",farmer_trade_money,1),
                    (else_try),
                        (call_script,"script_update_lord_wealth",":troop",merchant_trade_money,1),
                    (try_end),
                    (display_message,"@hero go to home"),
                (try_end),

                # (str_store_troop_name,s1,":troop"),
                # (display_message,"@{s1} is update over"),
            ]),
            ## 战斗队伍ai【核心ai之二】
            ("war_party_ai_update", [
                (store_script_param_1,":troop"),
                (troop_get_slot,":party",":troop",slot_troop_leaded_party),
                (troop_get_slot,":service_target",":troop",slot_troop_service_target),
                (party_get_num_companions,":companions_size",":party"),
                (try_begin),
                    (this_or_next | troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_leader),
                    (this_or_next | troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_outlaws),
                    (call_script,"script_party_set_ai_state",":party",spai_patrolling_around_center,":service_target"),
                (else_try),
                    (this_or_next | troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_soldier),
                    (call_script,"script_party_set_ai_state",":party",spai_accompanying_army,":service_target"),
                (else_try),
                    (this_or_next | troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_lord),
                    (this_or_next | troop_slot_eq, ":troop", slot_troop_hero_status, sths_is_king),

                    (store_faction_of_troop,":faction",":troop"),
                    (faction_get_slot,":marshall",":faction",slot_faction_marshall),
                    (store_relation,":marshall_relation",":troop",":marshall"),
                    (troop_get_slot,":service_target",":marshall",slot_troop_leaded_party),
                    (faction_get_slot,":faction_ai",":faction",slot_faction_ai_state),
                    (try_begin),
                        ## 集结军队，
                        (eq,":faction_ai",sfai_gathering_army),
                        ## 士兵数量大于30个
                        (ge, ":companions_size", 30),
                        ## 与元帅的关系不为负
                        (ge, ":marshall_relation", 0),
                        ## 服务对象正常
                        (gt, ":service_target", 0),
                        (call_script, "script_party_set_ai_state", ":party", spai_accompanying_army, ":service_target"),
                    (else_try),

                    (try_end),
                (try_end),
            ]),
        ],
    },
    "dialogs":{
        "insertBefore":[{
            "sign":"start:Yes___sire_my_lady__@:lord_start[1,3,4]",
            "data":[
                [anyone ,"start", [
					(is_between,"$g_talk_troop",hero_begin, hero_end),
                ],"Yes, {sire/my lady}?", "hero_start",[]],

                [anyone|plyr ,"hero_start", [],"Would you like to follow me?", "hire_hero_talk",[]],

                [anyone ,"hire_hero_talk", [
                    # (call_script,"script_troop_get_player_relation","$g_talk_troop"),
                    # (ge,reg0,hero_join_player_party_relation),
                ],"I'm glad to be part of your team", "close_window",[
                    (call_script,"script_add_party_as_companions","p_main_party","$g_talk_troop_party",1),
                    (troop_set_slot,"$g_talk_troop", slot_troop_hero_status, sths_is_soldier),

                    (eq, "$talk_context", tc_party_encounter),
                    (assign, "$g_leave_encounter", 1)
                ]],

                [anyone ,"hire_hero_talk", [],"I'm not familiar with you", "close_window",[]],

                [anyone|plyr ,"hero_start", [],"no thing!", "close_window",[
                    (eq, "$talk_context", tc_party_encounter),
                    (assign, "$g_leave_encounter", 1)
                ]],
            ]
        },],
    },
    "internationals":{
        "cns":{
            "dialogs":[
                "dlga_start:hero_start|你 好, {先 生/女 士}, 有 什 么 事 情 吗 ？",
                "dlga_hero_start:hire_hero_talk|你 想 跟 着 我 吗 ？",
                "dlga_hire_hero_talk:close_window|我 很 高 兴 能 够 成 为 你 队 伍 的 一 员 。",
                "dlga_hire_hero_talk:close_window.1|我 还 不 熟 悉 你 的 为 人 。",
                "dlga_hero_start:close_window|没 事",
            ]
        }
    }
}