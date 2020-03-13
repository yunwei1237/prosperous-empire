# -*- coding: utf-8 -*-
from ID_items import *
from ID_quests import *
from ID_factions import *
##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

########################################################
##  ITEM SLOTS             #############################物品slot
########################################################

slot_item_is_checked               = 0  ###物品已经检查slot，用于检查物品栏
slot_item_food_bonus               = 1  ###食物士气奖励
slot_item_book_reading_progress    = 2  ###书籍阅读进度
slot_item_book_read                = 3  ###书籍阅读
slot_item_intelligence_requirement = 4  ###物品情报需求

slot_item_amount_available         = 7  ###物品供应量

###消费者在镇上一个好的需求，在抽象的测量单位。更为重要的项目（即，如谷物）价格较高
slot_item_urban_demand             = 11 #consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
###在农村的消费需求，在抽象的测量单位
slot_item_rural_demand             = 12 #consumer demand in villages, measured in abstract units
###在农村的消费需求，在抽象的测量单位
slot_item_desert_demand            = 13 #consumer demand in villages, measured in abstract units

slot_item_production_slot          = 14   ###物品生产slot
slot_item_production_string        = 15   ###物品生产字符串

###物品绑好的价格。 例如，武器和金属装甲工具，衬垫布，皮革，皮革制品，等
slot_item_tied_to_good_price       = 20 #ie, weapons and metal armor to tools, padded to cloth, leather to leatherwork, etc

###物品数量坐标
slot_item_num_positions            = 22
###物品坐标开始
slot_item_positions_begin          = 23 #reserve around 5 slots after this ###保护区大约5 slot之后


slot_item_multiplayer_faction_price_multipliers_begin = 30 #reserve around 10 slots after this ###保护区大约10 slot之后

slot_item_primary_raw_material    		= 50
slot_item_is_raw_material_only_for      = 51
slot_item_input_number                  = 52 #ie, how many items of inputs consumed per run
###物品基本价格
slot_item_base_price                    = 53 #taken from module_items
#slot_item_production_site			    = 54 #a string replaced with function - Armagan
slot_item_output_per_run                = 55 #number of items produced per run
slot_item_overhead_per_run              = 56 #labor and overhead per run
slot_item_secondary_raw_material        = 57 #in this case, the amount used is only one
slot_item_enterprise_building_cost      = 58 #enterprise building cost


slot_item_multiplayer_item_class   = 60 #temporary, can be moved to higher values
slot_item_multiplayer_availability_linked_list_begin = 61 #temporary, can be moved to higher values


########################################################
##  AGENT SLOTS            #############################agent slot
########################################################

slot_agent_target_entry_point     = 0   ###入口点触发（和下面的重复？）
slot_agent_target_x_pos           = 1   ###x坐标触发
slot_agent_target_y_pos           = 2   ###y坐标触发
slot_agent_is_alive_before_retreat= 3   ###撤退之前活着
slot_agent_is_in_scripted_mode    = 4   ###剧本模式
slot_agent_is_not_reinforcement   = 5   ###agent不是援军
slot_agent_tournament_point       = 6   ###竞技场点
slot_agent_arena_team_set         = 7   ###设置agent竞技场组别
slot_agent_spawn_entry_point      = 8   ###agent刷兵点
slot_agent_target_prop_instance   = 9   ###道具实例触发
slot_agent_map_overlay_id         = 10  ###agent地图贴图id
slot_agent_target_entry_point     = 11  ###入口点触发（和上面的重复？）
slot_agent_initial_ally_power     = 12  ###最初友军力量
slot_agent_initial_enemy_power    = 13  ###最初敌人力量
slot_agent_enemy_threat           = 14  ###敌人的威胁
slot_agent_is_running_away        = 15  ###agent在逃跑
slot_agent_courage_score          = 16  ###agent勇气评分
slot_agent_is_respawn_as_bot      = 17  ###agent重生为BOT
slot_agent_cur_animation          = 18  ###agent当前动画
slot_agent_next_action_time       = 19  ###agent下次事件时间
slot_agent_state                  = 20  ###agent状态
slot_agent_in_duel_with           = 21  ###agent决斗和
slot_agent_duel_start_time        = 22  ###agent决斗开始时间

slot_agent_walker_occupation      = 25  ###散步的人的职业


    
########################################################
##  FACTION SLOTS          #############################国家slot
########################################################
###国家ai状态
slot_faction_ai_state                   = 4
###国家ai对象
slot_faction_ai_object                  = 5
###国家ai根据，目前未使用的，可以链接到从决策表生成的字符串
slot_faction_ai_rationale               = 6 #Currently unused, can be linked to strings generated from decision checklists


###国家元帅
slot_faction_marshall                   = 8
###国家ai进攻最大的追随者
slot_faction_ai_offensive_max_followers = 9

###国家文化
slot_faction_culture                    = 10
###国家国王
slot_faction_leader                     = 11

###国家临时slot
slot_faction_temp_slot                  = 12

##slot_faction_vassal_of            = 11
###国家旗帜
slot_faction_banner                     = 15

###国家军队数目
slot_faction_number_of_parties    = 20
###国家状态
slot_faction_state                = 21

###王国叛军
slot_faction_adjective            = 22


###国家玩家警报
slot_faction_player_alarm         		= 30
###国家上次雇佣提议时间
slot_faction_last_mercenary_offer_time 	= 31
###国家承认玩家
slot_faction_recognized_player    		= 32

#overriding troop info for factions in quick start mode.###压倒一切的队伍信息在快速启动模式的国家。
slot_faction_quick_battle_tier_1_infantry      = 41 ###国家快速战斗步兵兵种树1
slot_faction_quick_battle_tier_2_infantry      = 42 ###国家快速战斗步兵兵种树2
slot_faction_quick_battle_tier_1_archer        = 43 ###国家快速战斗弓箭手兵种树1
slot_faction_quick_battle_tier_2_archer        = 44 ###国家快速战斗弓箭手兵种树2
slot_faction_quick_battle_tier_1_cavalry       = 45 ###国家快速战斗骑兵兵种树1
slot_faction_quick_battle_tier_2_cavalry       = 46 ###国家快速战斗骑兵兵种树2

slot_faction_tier_1_troop         = 41 ###国家兵种树1
slot_faction_tier_2_troop         = 42 ###国家兵种树2
slot_faction_tier_3_troop         = 43 ###国家兵种树3
slot_faction_tier_4_troop         = 44 ###国家兵种树4
slot_faction_tier_5_troop         = 45 ###国家兵种树5

###阵营逃兵
slot_faction_deserter_troop       = 48
###阵营警卫
slot_faction_guard_troop          = 49
###阵营传令兵
slot_faction_messenger_troop      = 50
###阵营监狱守卫
slot_faction_prison_guard_troop   = 51
###阵营城堡守卫
slot_faction_castle_guard_troop   = 52

###城镇散步男性
slot_faction_town_walker_male_troop      = 53
###城镇散步女性
slot_faction_town_walker_female_troop    = 54
###村庄散步男性
slot_faction_village_walker_male_troop   = 55
###村庄散步女性
slot_faction_village_walker_female_troop = 56
###城镇男性间谍
slot_faction_town_spy_male_troop         = 57
###城镇女性间谍
slot_faction_town_spy_female_troop       = 58

###国家造反概率
slot_faction_has_rebellion_chance = 60

###国家不稳定，最后一次测量
slot_faction_instability          = 61 #last time measured


#UNIMPLEMENTED FEATURE ISSUES
slot_faction_war_damage_inflicted_when_marshal_appointed = 62 #Probably deprecate###可能废弃
slot_faction_war_damage_suffered_when_marshal_appointed  = 63 #Probably deprecate###可能废弃

###国家政治问题
slot_faction_political_issue 							 = 64 #Center or marshal appointment
###国家政治问题时间
slot_faction_political_issue_time 						 = 65 #Now is used


#Rebellion changes
#slot_faction_rebellion_target                     = 65
#slot_faction_inactive_leader_location         = 66
#slot_faction_support_base                     = 67
#Rebellion changes



#slot_faction_deserter_party_template       = 62

slot_faction_reinforcements_a        = 77 ###国家刷兵模版a
slot_faction_reinforcements_b        = 78 ###国家刷兵模版b
slot_faction_reinforcements_c        = 79 ###国家刷兵模版c

slot_faction_num_armies              = 80 ###国家军队数
slot_faction_num_castles             = 81 ###国家城堡数量
slot_faction_num_towns               = 82 ###国家城镇数量

slot_faction_last_attacked_center    = 85 ###国家最后进攻的中心
slot_faction_last_attacked_hours     = 86 ###国家最后进攻的时间
slot_faction_last_safe_hours         = 87 ###国家最后安全的时间

slot_faction_num_routed_agents       = 90 ###国家agent路易数量

#useful for competitive consumption ####用于竞争性消费
slot_faction_biggest_feast_score      = 91
slot_faction_biggest_feast_time       = 92
slot_faction_biggest_feast_host       = 93


#Faction AI states ###国家AI状态
###国家最后宴会结果。当宴会开始——这需要被废弃
slot_faction_last_feast_concluded       = 94 #Set when a feast starts -- this needs to be deprecated
###国家最后宴会开始时间。
slot_faction_last_feast_start_time      = 94 #this is a bit confusing

###国家AI最后进攻时间
slot_faction_ai_last_offensive_time 	= 95 #Set when an offensive concludes
###国家AI最后进攻结果
slot_faction_last_offensive_concluded 	= 95 #Set when an offensive concludes

###国家AI最后重置时间。最后一次，派有违约或盛宴——这决定领主不满的运动。在faction_ai脚本
slot_faction_ai_last_rest_time      	= 96 #the last time that the faction has had default or feast AI -- this determines lords' dissatisfaction with the campaign. Set during faction_ai script
###国家AI当前状态起点
slot_faction_ai_current_state_started   = 97 #

###国家AI最后决定性的事件。电脑的防守、宣言或战争。
slot_faction_ai_last_decisive_event     = 98 #capture a fortress or declaration of war

###玩家国家troop的士气
slot_faction_morale_of_player_troops    = 99

#diplomacy
slot_faction_truce_days_with_factions_begin 			= 120
slot_faction_provocation_days_with_factions_begin 		= 130
slot_faction_war_damage_inflicted_on_factions_begin 	= 140
slot_faction_sum_advice_about_factions_begin 			= 150

#revolts -- notes for self
#type 1 -- minor revolt, aimed at negotiating change without changing the ruler
#type 2 -- alternate ruler revolt (ie, pretender, chinese dynastic revolt -- keep the same polity but switch the ruler)
	#subtype -- pretender (keeps the same dynasty)
	#"mandate of heaven" -- same basic rules, but a different dynasty
	#alternate/religious
	#alternate/political
#type 3 -- separatist revolt
	# reGonalist/dynastic (based around an alternate ruling house
	# regionalist/republican
	# messianic (ie, Canudos)
	
########################################################
##  PARTY SLOTS            #############################队伍slot
########################################################
###队伍类型 
slot_party_type                = 0  #spt_caravan, spt_town, spt_castle

###队伍撤退标签
slot_party_retreat_flag        = 2
###队伍忽视玩家
slot_party_ignore_player_until = 3
###队伍ai状态
slot_party_ai_state            = 4
###队伍ai对象
slot_party_ai_object           = 5
###队伍ai根据，当前未使用，但可以用于保存一个字符串解释领主的思考
slot_party_ai_rationale        = 6 #Currently unused, but can be used to save a string explaining the lord's thinking

#slot_town_belongs_to_kingdom   = 6
###城镇领主
slot_town_lord                 = 7
###队伍ai
slot_party_ai_substate         = 8
###玩家夺走城镇
slot_town_claimed_by_player    = 9

###玩家赶牛
slot_cattle_driven_by_player = slot_town_lord #hack

###城镇大街
slot_town_center        = 10
###城镇城堡
slot_town_castle        = 11
###城镇监狱
slot_town_prison        = 12
###城镇酒馆
slot_town_tavern        = 13
###城镇商店
slot_town_store         = 14
###城镇竞技场
slot_town_arena         = 16
###城镇小巷
slot_town_alley         = 17
###城镇城墙
slot_town_walls         = 18
###中心文化
slot_center_culture     = 19

###城镇酒馆老板
slot_town_tavernkeeper  = 20
###城镇武器老板
slot_town_weaponsmith   = 21
###城镇铠甲老板
slot_town_armorer       = 22
###城镇杂货老板
slot_town_merchant      = 23
###城镇马匹老板
slot_town_horse_merchant= 24
###城镇镇长、村庄村长
slot_town_elder         = 25
###中心玩家关系
slot_center_player_relation = 26

###围困中心的攻城塔
slot_center_siege_with_belfry = 27
###中心上一次接受的troop
slot_center_last_taken_by_troop = 28

# party will follow this party if set:
slot_party_commander_party = 30 #default -1   #Deprecate###废弃
###队伍跟随玩家
slot_party_following_player    = 31
###队伍跟随玩家时间限制
slot_party_follow_player_until_time = 32
###队伍不要跟随玩家时间限制
slot_party_dont_follow_player_until_time = 33

###村庄搜查
slot_village_raided_by        = 34
###村庄状态 svs_normal正常 svs_being_raided开始搜查 svs_looted掠夺 svs_recovering恢复 svs_deserted无人居住
slot_village_state            = 35 #svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted
###劫掠前进
slot_village_raid_progress    = 36
###恢复前进
slot_village_recover_progress = 37
###村庄增加冒烟
slot_village_smoke_added      = 38

###村庄滋生强盗
slot_village_infested_by_bandits   = 39

###中心上次访问的领主
slot_center_last_visited_by_lord   = 41

###中心上次玩家警报小时
slot_center_last_player_alarm_hour = 42

###村庄玩家不能偷牛
slot_village_player_can_not_steal_cattle = 46

###中心累积税金
slot_center_accumulated_rents      = 47 #collected automatically by NPC lords NPC领主的自动收集
###中心累积关税
slot_center_accumulated_tariffs    = 48 #collected automatically by NPC lords NPC领主的自动收集
###城镇城堡财富
slot_town_wealth        = 49 #total amount of accumulated wealth in the center, pays for the garrison
###城镇繁荣度
slot_town_prosperity    = 50 #affects the amount of wealth generated
###城镇玩家几率、胜率
slot_town_player_odds   = 51


###队伍上次支付收费时间
slot_party_last_toll_paid_hours = 52
###城镇城堡食物储藏量
slot_party_food_store           = 53 #used for sieges
###村庄被围
slot_center_is_besieged_by      = 54 #used for sieges
###上次发现的敌人
slot_center_last_spotted_enemy  = 55

slot_party_cached_strength        = 56  ###队伍缓存强度
slot_party_nearby_friend_strength = 57  ###队伍附近朋友强度
slot_party_nearby_enemy_strength  = 58  ###队伍附近敌军强度
slot_party_follower_strength      = 59  ###队伍跟随强度

slot_town_reinforcement_party_template = 60 ###城镇援军队伍模版
slot_center_original_faction           = 61 ###中心原始国家
slot_center_ex_faction                 = 62 ###中心之外国家

###队伍跟随我
slot_party_follow_me                   = 63
###中心围攻开始时间
slot_center_siege_begin_hours          = 64 #used for sieges
###中心围攻难度
slot_center_siege_hardness             = 65

slot_center_sortie_strength            = 66 ###中心突围强度
slot_center_sortie_enemy_strength      = 67 ###中心突围敌军强度

slot_party_last_in_combat              = 68 #used for AI ###队伍上次战斗的时间
slot_party_last_in_home_center         = 69 #used for AI ###队伍上次在城镇家里的时间
slot_party_leader_last_courted         = 70 #used for AI ###队伍领袖上次追求的时间
slot_party_last_in_any_center          = 71 #used for AI ###队伍上次在任何城镇的时间



slot_castle_exterior    = slot_town_center ###城堡外部=城镇中心

#slot_town_rebellion_contact   = 76
#trs_not_yet_approached  = 0
#trs_approached_before   = 1
#trs_approached_recently = 2


########################## slot_troop_kingsupport_argument ###npc支持国家争论的参数
argument_none         = 0
###索赔
argument_claim        = 1 #deprecate for legal      ###藐视法律
###法律
argument_legal        = 1

###尺度
argument_ruler        = 2 #deprecate for commons    ###反对为下议院
###下议院
argument_commons      = 2

###效益
argument_benefit      = 3 #deprecate for reward     ###反对奖励
###奖励
argument_reward       = 3 

###胜利
argument_victory      = 4
###上议院
argument_lords        = 5
###对抗
argument_rivalries    = 6 #new - needs to be added  ###需要增加

slot_town_village_product = 76

slot_town_rebellion_readiness = 77
#(readiness can be a negative number if the rebellion has been defeated)

slot_town_arena_melee_mission_tpl = 78
slot_town_arena_torny_mission_tpl = 79
slot_town_arena_melee_1_num_teams = 80
slot_town_arena_melee_1_team_size = 81
slot_town_arena_melee_2_num_teams = 82
slot_town_arena_melee_2_team_size = 83
slot_town_arena_melee_3_num_teams = 84
slot_town_arena_melee_3_team_size = 85
slot_town_arena_melee_cur_tier    = 86
##slot_town_arena_template	  = 87

slot_center_npc_volunteer_troop_type   = 90
slot_center_npc_volunteer_troop_amount = 91
slot_center_mercenary_troop_type  = 90
slot_center_mercenary_troop_amount= 91
slot_center_volunteer_troop_type  = 92
slot_center_volunteer_troop_amount= 93

#slot_center_companion_candidate   = 94
slot_center_ransom_broker         = 95
slot_center_tavern_traveler       = 96
slot_center_traveler_info_faction = 97
slot_center_tavern_bookseller     = 98
slot_center_tavern_minstrel       = 99

###队伍掠夺数量slot
num_party_loot_slots    = 5
###队伍下次掠夺物品slot
slot_party_next_looted_item_slot  = 109
slot_party_looted_item_1          = 110
slot_party_looted_item_2          = 111
slot_party_looted_item_3          = 112
slot_party_looted_item_4          = 113
slot_party_looted_item_5          = 114
slot_party_looted_item_1_modifier = 115
slot_party_looted_item_2_modifier = 116
slot_party_looted_item_3_modifier = 117
slot_party_looted_item_4_modifier = 118
slot_party_looted_item_5_modifier = 119

slot_village_bound_center         = 120   ###村庄归属于那个城镇城堡
slot_village_market_town          = 121   ###村庄城镇市场
slot_village_farmer_party         = 122   ###村庄民兵队伍
slot_party_home_center            = 123   ###队伍的家是那座中心   #Only use with caravans and villagers ###只有商队和村民使用

###中心当前建造
slot_center_current_improvement   = 124
###中心建造结束时间
slot_center_improvement_end_hour  = 125

###队伍上次和中心贸易
slot_party_last_traded_center     = 126 



slot_center_has_manor            = 130 #village###庄园
slot_center_has_fish_pond        = 131 #village###鱼塘、磨坊
slot_center_has_watch_tower      = 132 #village###了望塔
slot_center_has_school           = 133 #village###学校
slot_center_has_messenger_post   = 134 #town, castle, village###驿站
slot_center_has_prisoner_tower   = 135 #town, castle###监狱

village_improvements_begin = slot_center_has_manor
village_improvements_end          = 135

walled_center_improvements_begin = slot_center_has_messenger_post
walled_center_improvements_end               = 136

###城镇玩家工厂
slot_center_player_enterprise     				  = 137 #noted with the item produced
slot_center_player_enterprise_production_order    = 138
slot_center_player_enterprise_consumption_order   = 139 #not used
###城镇玩家工厂建造时间
slot_center_player_enterprise_days_until_complete = 139 #Used instead

slot_center_player_enterprise_balance             = 140 #not used
slot_center_player_enterprise_input_price         = 141 #not used
slot_center_player_enterprise_output_price        = 142 #not used



slot_center_has_bandits                        = 155  ###中心有土匪
slot_town_has_tournament                       = 156  ###城镇有锦标赛
slot_town_tournament_max_teams                 = 157  ###城镇锦标赛最大组
slot_town_tournament_max_team_size             = 158  ###城镇锦标赛最大组大小

slot_center_faction_when_oath_renounced        = 159


###########################城镇散步的市民
slot_center_walker_0_troop                   = 160
slot_center_walker_1_troop                   = 161
slot_center_walker_2_troop                   = 162
slot_center_walker_3_troop                   = 163
slot_center_walker_4_troop                   = 164
slot_center_walker_5_troop                   = 165
slot_center_walker_6_troop                   = 166
slot_center_walker_7_troop                   = 167
slot_center_walker_8_troop                   = 168
slot_center_walker_9_troop                   = 169

slot_center_walker_0_dna                     = 170
slot_center_walker_1_dna                     = 171
slot_center_walker_2_dna                     = 172
slot_center_walker_3_dna                     = 173
slot_center_walker_4_dna                     = 174
slot_center_walker_5_dna                     = 175
slot_center_walker_6_dna                     = 176
slot_center_walker_7_dna                     = 177
slot_center_walker_8_dna                     = 178
slot_center_walker_9_dna                     = 179

slot_center_walker_0_type                    = 180
slot_center_walker_1_type                    = 181
slot_center_walker_2_type                    = 182
slot_center_walker_3_type                    = 183
slot_center_walker_4_type                    = 184
slot_center_walker_5_type                    = 185
slot_center_walker_6_type                    = 186
slot_center_walker_7_type                    = 187
slot_center_walker_8_type                    = 188
slot_center_walker_9_type                    = 189

###################城镇贸易路线
slot_town_trade_route_1           = 190
slot_town_trade_route_2           = 191
slot_town_trade_route_3           = 192
slot_town_trade_route_4           = 193
slot_town_trade_route_5           = 194
slot_town_trade_route_6           = 195
slot_town_trade_route_7           = 196
slot_town_trade_route_8           = 197
slot_town_trade_route_9           = 198
slot_town_trade_route_10          = 199
slot_town_trade_route_11          = 200
slot_town_trade_route_12          = 201
slot_town_trade_route_13          = 202
slot_town_trade_route_14          = 203
slot_town_trade_route_15          = 204

slot_town_trade_routes_begin = slot_town_trade_route_1
slot_town_trade_routes_end = slot_town_trade_route_15 + 1

###交易商品数 = 补给品 - 香料
num_trade_goods = itm_siege_supply - itm_spice
slot_town_trade_good_productions_begin       = 500 #a harmless number, until it can be deprecated

#These affect production but in some cases also demand, so it is perhaps easier to itemize them than to have separate 

###村庄牛数量
slot_village_number_of_cattle   = 205
###风干肉，奶酪，隐藏，黄油，
slot_center_head_cattle         = 205 #dried meat, cheese, hides, butter
###中心羊数量。香肠，羊毛
slot_center_head_sheep			= 206 #sausages, wool
###中心马数量。马可以用于跟踪贸易项目但不出售
slot_center_head_horses		 	= 207 #horses can be a trade item used in tracking but which are never offered for sale

###中心牧场亩数。放牧牛羊的牧场面积，如果该值为牛、羊的数量高，增长更快
slot_center_acres_pasture       = 208 #pasture area for grazing of cattles and sheeps, if this value is high then number of cattles and sheeps increase faster


###生产来源开始
slot_production_sources_begin = 209

slot_center_acres_grain			= 209 #grain            ###农场（粮食）
slot_center_acres_olives        = 210 #olives       ###橄榄园（橄榄）
slot_center_acres_vineyard		= 211 #fruit          ###葡萄园（葡萄）
slot_center_acres_flax          = 212 #flax         ###亚麻园（亚麻）
slot_center_acres_dates			= 213 #dates

slot_center_fishing_fleet		= 214 #smoked fish      ###捕鱼船队（熏鱼）
slot_center_salt_pans		    = 215 #salt             ###盐田（盐）

slot_center_apiaries       		= 216 #honey          ###养蜂场（蜂蜜）
slot_center_silk_farms			= 217 #silk             ###丝绸场（丝绸）
slot_center_kirmiz_farms		= 218 #dyes             ###染料场（染料）

slot_center_iron_deposits       = 219 #iron         ###铁矿床（铁器）
slot_center_fur_traps			= 220 #furs               ###毛皮陷阱（毛皮）

slot_center_mills				= 221 #bread                ###磨坊（面包）
slot_center_breweries			= 222 #ale                ###啤酒厂（啤酒）
slot_center_wine_presses		= 223 #wine             ###酿酒厂（葡萄酒）
slot_center_olive_presses		= 224 #oil              ###橄榄机（橄榄油）

slot_center_linen_looms			= 225 #linen            ###亚麻织机（亚麻）
slot_center_silk_looms          = 226 #velvet       ###丝织机（天鹅绒）
slot_center_wool_looms          = 227 #wool cloth   ###毛织机

slot_center_pottery_kilns		= 228 #pottery          ###陶窑（陶器）
slot_center_smithies			= 229 #tools              ###铁匠铺（工具）
slot_center_tanneries			= 230 #leatherwork        ###制革厂（皮革）
#naval stores - uses timber, pitch, and linen###海军商店-使用木材，沥青，和亚麻布
slot_center_shipyards			= 231                     ###船坞

slot_center_household_gardens   = 232 #cabbages     ###家庭花园(卷心菜)

###生产来源结束
slot_production_sources_end = 233

#all spice comes overland to Tulga ###所有的香料来陆路Tulga 图鲁加
#all dyes come by sea to Jelkala  ###所有的染料是由海上来jelkala 杰卡拉

#chicken and pork are perishable and non-tradeable, and based on grain production
###鸡肉和猪肉是易逝性和不可交易的，基于粮食生产
#timber and pitch if we ever have a shipbuilding industry ###木材和沥青的如果我们有造船业
#limestone and timber for mortar, if we allow building ###石灰石和木材砂浆，如果我们允许建设

slot_town_last_nearby_fire_time                         = 240 ###城镇城堡上次附近村庄着火时间

#slot_town_trade_good_prices_begin            = slot_town_trade_good_productions_begin + num_trade_goods + 1
###队伍下命令的troop
slot_party_following_orders_of_troop        = 244
###队伍命令类型
slot_party_orders_type				        = 245
###队伍命令目标
slot_party_orders_object				    = 246
###队伍命令时间
slot_party_orders_time				    	= 247

slot_party_temp_slot_1			            = 248 #right now used only within a single script, merchant_road_info_to_s42, to denote closed roads. Now also used in comparative scripts
slot_party_under_player_suggestion			= 249 #move this up a bit
slot_town_trade_good_prices_begin 			= 250

slot_center_last_reconnoitered_by_faction_time 				= 350
#slot_center_last_reconnoitered_by_faction_cached_strength 	= 360
#slot_center_last_reconnoitered_by_faction_friend_strength 	= 370




#slot_party_type values
##spt_caravan            = 1  ###商队
spt_castle             = 2    ###城堡
spt_town               = 3    ###城镇
spt_village            = 4    ###村庄
##spt_forager            = 5  ###抢劫者
##spt_war_party          = 6  ###
##spt_patrol             = 7  ###巡逻队、侦察队
##spt_messenger          = 8  ###信使
##spt_raider             = 9  ###袭击者、侵入者
##spt_scout              = 10 ###侦察
spt_kingdom_caravan    = 11   ###王国商队
##spt_prisoner_train     = 12 ###囚犯队
spt_kingdom_hero_party = 13   ###王国领主军队
##spt_merchant_caravan   = 14 ###商人商队
spt_village_farmer     = 15   ###村庄农民、农场主
spt_ship               = 16   ###船
spt_cattle_herd        = 17   ###牛群
spt_bandit_lair       = 18    ###强盗巢穴
#spt_deserter           = 20  ###逃兵

kingdom_party_types_begin = spt_kingdom_caravan
kingdom_party_types_end = spt_kingdom_hero_party + 1


#slot_faction_state values ###slot_faction_state 阵营国家状态的值

sfs_active                     = 0 ###活跃的
sfs_defeated                   = 1 ###打败的
sfs_inactive                   = 2 ###不活跃的
sfs_inactive_rebellion         = 3 ###不活跃的叛乱
sfs_beginning_rebellion        = 4 ###开始叛乱


#slot_faction_ai_state values ###slot_faction_ai_state阵营国家ai状态的值
###默认
sfai_default                   		 = 0 #also defending
###聚会军队
sfai_gathering_army            		 = 1
###攻击中心
sfai_attacking_center          		 = 2
###袭击村庄
sfai_raiding_village           		 = 3
###攻击敌人军队
sfai_attacking_enemy_army      		 = 4
###攻击敌人中心周围
sfai_attacking_enemies_around_center = 5
###宴会，可宴，婚礼，或重大赛事
sfai_feast             		 		 = 6 #can be feast, wedding, or major tournament

#Social events are a generic aristocratic gathering. Tournaments take place if they are in a town, and hunts take place if they are at a castle.
###社会事件是一个通用的贵族聚会。比赛发生，如果他们是在一个小镇，找出发生如果他们在一个城堡。

#Weddings will take place at social events between betrothed couples if they have been engaged for at least a month, if the lady's guardian is the town lord, and if both bride and groom are present
###婚礼将在订婚的社会事件如果他们订婚已经至少一个月，如果女士的监护人是该镇的主，如果新郎新娘都是存在的



#Rebellion system changes begin ###制度变迁开始反抗
sfai_nascent_rebellion          = 7
#Rebellion system changes end


#slot_party_ai_state values ###slot_party_ai_state队伍AI状态的值
###未定义的
spai_undefined                  = -1
###围攻中心
spai_besieging_center           = 1
###中心附近巡逻
spai_patrolling_around_center   = 4
###袭击中心周围、掠夺村庄
spai_raiding_around_center      = 5
##spai_raiding_village            = 6
###坚守中心
spai_holding_center             = 7
##spai_helping_town_against_siege = 9
###袭击军队
spai_engaging_army              = 10
###伴随军队
spai_accompanying_army          = 11
###保护军队
spai_screening_army             = 12
###城镇贸易
spai_trading_with_town          = 13
###从中心撤退逃跑
spai_retreating_to_center       = 14
##spai_trading_within_kingdom     = 15
###访问村庄
spai_visiting_village           = 16 #same thing, I think. Recruiting differs from holding because NPC parties don't actually enter villages ###同样的事情，我想。招聘与控股因为NPC当事人没有真正进入村庄


#slot_village_state values ###slot_village_state村庄状态的值
###正常的
svs_normal                      = 0
###被搜查
svs_being_raided                = 1
###掠夺
svs_looted                      = 2
###回收
svs_recovering                  = 3
###废弃的
svs_deserted                    = 4
###围困
svs_under_siege                 = 5

#$g_player_icon_state values 玩家icon状态
pis_normal                      = 0   ###正常
pis_camping                     = 1   ###扎营
pis_ship                        = 2   ###船


########################################################
##  SCENE SLOTS            #############################场景slot
########################################################

slot_scene_visited              = 0   ###场景访问
slot_scene_belfry_props_begin   = 10  ###场景攻城塔道具开始



########################################################
##  TROOP SLOTS            #############################troop slot
########################################################
#slot_troop_role         = 0  # 10=Kingdom Lord ###troop地位

###troop职业 0自由 1商人
slot_troop_occupation          = 2  # 0 = free, 1 = merchant
#slot_troop_duty               = 3  # Kingdom duty, 0 = free ###troop职务
#slot_troop_homage_type         = 45  ###troop效忠顺从类型
#homage_mercenary =             = 1 #Player is on a temporary contract ###玩家在一个临时合同
#homage_official =              = 2 #Player has a royal appointment ###玩家有一个皇家任命
#homage_feudal   =              = 3 #


###troop状态
slot_troop_state               = 3  
###最后交谈时间
slot_troop_last_talk_time      = 4
###我也用这个求爱的状态——可能成为累赘
slot_troop_met                 = 5 #i also use this for the courtship state -- may become cumbersome
###troop求爱进展 2表示钦佩 3同意婚姻 4结束关系
slot_troop_courtship_state     = 5 #2 professed admiration, 3 agreed to seek a marriage, 4 ended relationship

###troop队伍模版
slot_troop_party_template      = 6
###troop王国阶层
#slot_troop_kingdom_rank        = 7

###troop声望
slot_troop_renown              = 7

###troop是囚犯
##slot_troop_is_prisoner         = 8  # important for heroes only 只能是重要的英雄
###队伍troop囚犯
slot_troop_prisoner_of_party   = 8  # important for heroes only 只能是重要的英雄
#slot_troop_is_player_companion = 9  # important for heroes only:::USE  slot_troop_occupation = slto_player_companion

###troop目前事件
slot_troop_present_at_event    = 9

###troop领导的队伍，只能用于领主，当领主被俘虏，则此slot赋值为-1，表示不能带任何兵
slot_troop_leaded_party         = 10 # important for kingdom heroes only
###troop财产，只能用于领主
slot_troop_wealth               = 11 # important for kingdom heroes only
###troop当前所在城市中心 npc在酒馆刷新用（非王国英雄）
slot_troop_cur_center           = 12 # important for royal family members only (non-kingdom heroes)

###troop场景道具旗帜，只有领主和玩家有
slot_troop_banner_scene_prop    = 13 # important for kingdom heroes and player only

###troop原始阵营
slot_troop_original_faction     = 14 # for pretenders
#slot_troop_loyalty              = 15 #deprecated - this is now derived from other figures###废弃
slot_troop_player_order_state   = 16 #Deprecated###废弃
slot_troop_player_order_object  = 17 #Deprecated###废弃

#troop_player order state are all deprecated in favor of party_order_state. This has two reasons -- 1) to reset AI if the party is eliminated, and 2) to allow the player at a later date to give orders to leaderless parties, if we want that


#Post 0907 changes begin
###troop年龄
slot_troop_age                 =  18
###troop年龄外貌
slot_troop_age_appearance      =  19

#Post 0907 changes end

slot_troop_does_not_give_quest = 20
slot_troop_player_debt         = 21
###troop与玩家好感
slot_troop_player_relation     = 22
#slot_troop_player_favor        = 23
slot_troop_last_quest          = 24
slot_troop_last_quest_betrayed = 25
slot_troop_last_persuasion_time= 26 ###troop上次说服时间
slot_troop_last_comment_time   = 27
slot_troop_spawned_before      = 28

#Post 0907 changes begin
slot_troop_last_comment_slot   = 29
#Post 0907 changes end

###配偶
slot_troop_spouse              = 30
###父亲
slot_troop_father              = 31
###母亲
slot_troop_mother              = 32
slot_troop_guardian            = 33 #Usually siblings are identified by a common parent.This is used for brothers if the father is not an active npc. At some point we might introduce geneologies
###未婚夫、未婚妻
slot_troop_betrothed           = 34 #Obviously superseded once slot_troop_spouse is filled
#other relations are derived from one's parents 
#slot_troop_daughter            = 33
#slot_troop_son                 = 34
#slot_troop_sibling             = 35
###troop追求的女士第1目标
slot_troop_love_interest_1     = 35 #each unmarried lord has three love interests
###troop追求的女士第2目标
slot_troop_love_interest_2     = 36
###troop追求的女士第3目标
slot_troop_love_interest_3     = 37
slot_troop_love_interests_end  = 38
#ways to court -- discuss a book, commission/compose a poem, present a gift, recount your exploits, fulfil a specific quest, appear at a tournament
#preferences for women - (conventional - father's friends)
slot_lady_no_messages          				= 37
slot_lady_last_suitor          				= 38
slot_lord_granted_courtship_permission      = 38

slot_troop_betrothal_time                   = 39 #used in scheduling the wedding

slot_troop_trainer_met                       = 30
slot_troop_trainer_waiting_for_result        = 31
slot_troop_trainer_training_fight_won        = 32
slot_troop_trainer_num_opponents_to_beat     = 33
slot_troop_trainer_training_system_explained = 34
slot_troop_trainer_opponent_troop            = 35
slot_troop_trainer_training_difficulty       = 36
slot_troop_trainer_training_fight_won        = 37


slot_lady_used_tournament					= 40


slot_troop_current_rumor       = 45
slot_troop_temp_slot           = 46
slot_troop_promised_fief       = 47   ###troop承诺封地

slot_troop_set_decision_seed       = 48 #Does not change
slot_troop_temp_decision_seed      = 49 #Resets at recalculate_ai
slot_troop_recruitment_random      = 50 #used in a number of different places in the intrigue procedures to overcome intermediate hurdles, although not for the final calculation, might be replaced at some point by the global decision seed
#Decision seeds can be used so that some randomness can be added to NPC decisions, without allowing the player to spam the NPC with suggestions
#The temp decision seed is reset 24 to 48 hours after the NPC last spoke to the player, while the set seed only changes in special occasions
#The single seed is used with varying modula to give high/low outcomes on different issues, without using a separate slot for each issue
###用于在一个数量的阴谋中程序不同的地方来克服中间的障碍，虽然没有最终的计算，可以取代在一些点的全局决策的种子
###决定种子可以使一些随机性可以被添加到全国人大的决定，不允许玩家垃圾邮件人大建议
###临时决定的种子是上次跟球员的NPC复位后24至48小时，而设定种子只有在特殊场合的变化
###单种子具有不同的模块使用不同的问题，给高/低的结果，而无需使用单独的插槽，每个问题


###troop阴谋渴望
slot_troop_intrigue_impatience = 51
#recruitment changes end

#slot_troop_honorable          = 50
#slot_troop_merciful          = 51
###性格类型 
###lrep_quarrelsome好辩的 lrep_debauched放荡的 lrep_goodnatured善良的 lrep_martial好战的 
###lrep_upstanding正直的 lrep_selfrighteous自命正直 lrep_cunning狡猾的 lrep_roguish无赖的

###lrep_adventurous冒险的 lrep_otherworldly幻想的 lrep_conventional传统的 lrep_moralist道德的 lrep_ambitious野心勃勃的
slot_lord_reputation_type     		  = 52
slot_lord_recruitment_argument        = 53 #the last argument proposed by the player to the lord
###领主招募国王的候选人
slot_lord_recruitment_candidate       = 54 #the last candidate proposed by the player to the lord

###troop更改阵营
slot_troop_change_to_faction          = 55

#slot_troop_readiness_to_join_army     = 57 #possibly deprecate
#slot_troop_readiness_to_follow_orders = 58 #possibly deprecate

# NPC-related constants

#NPC companion changes begin
###troop首先遇到
slot_troop_first_encountered          = 59
###troop的家乡
slot_troop_home                       = 60

###troop道德状态
slot_troop_morality_state       = 61

tms_no_problem         = 0
tms_acknowledged       = 1
tms_dismissed          = 2

###troop道德类型
slot_troop_morality_type = 62
###贵族的
tmt_aristocratic = 1
###平等的
tmt_egalitarian = 2
###人道主义
tmt_humanitarian = 3
###诚实的
tmt_honest = 4
###虔诚的
tmt_pious = 5

###troop道德值
slot_troop_morality_value = 63

###troop第二道德类型
slot_troop_2ary_morality_type  = 64
###troop第二道德状态
slot_troop_2ary_morality_state = 65
###troop第二道德值
slot_troop_2ary_morality_value = 66

###npc有关系网的城镇
slot_troop_town_with_contacts  = 67
slot_troop_town_contact_type   = 68 #1 are nobles, 2 are commons

###troop道德处罚
slot_troop_morality_penalties =  69 ### accumulated grievances from morality conflicts 积怨从道德冲突

###troop人物角色性格冲突对象
slot_troop_personalityclash_object     = 71
#(0 - they have no problem, 1 - they have a problem)
###troop人物角色性格冲突状态
slot_troop_personalityclash_state    = 72 #1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,
pclash_penalty_to_self  = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both  = 3
#(a string)
###troop人物角色性格冲突对象2
slot_troop_personalityclash2_object   = 73
###troop人物角色性格冲突2状态
slot_troop_personalityclash2_state    = 74

###troop人物角色性格匹配对象
slot_troop_personalitymatch_object   =  75
###troop人物角色性格匹配状态
slot_troop_personalitymatch_state   =  76

###troop人物角色性格冲突处罚
slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash
slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash

slot_troop_home_speech_delivered = 78 #only for companions
slot_troop_discussed_rebellion   = 78 #only for pretenders

#courtship slots
slot_lady_courtship_heroic_recited 	    = 74
slot_lady_courtship_allegoric_recited 	= 75
slot_lady_courtship_comic_recited 		= 76
slot_lady_courtship_mystic_recited 		= 77
slot_lady_courtship_tragic_recited 		= 78



#NPC history slots ###NPC历史slots
slot_troop_met_previously        = 80
slot_troop_turned_down_twice     = 81
slot_troop_playerparty_history   = 82   ###troop加入玩家队伍历史 pp_history_dismissed被解雇

pp_history_scattered         = 1
pp_history_dismissed         = 2
pp_history_quit              = 3
pp_history_indeterminate     = 4

slot_troop_playerparty_history_string   = 83
slot_troop_return_renown        = 84

slot_troop_custom_banner_bg_color_1      = 85 ###troop自定义旗帜
slot_troop_custom_banner_bg_color_2      = 86 ###troop自定义旗帜
slot_troop_custom_banner_charge_color_1  = 87 ###troop自定义旗帜
slot_troop_custom_banner_charge_color_2  = 88 ###troop自定义旗帜
slot_troop_custom_banner_charge_color_3  = 89 ###troop自定义旗帜
slot_troop_custom_banner_charge_color_4  = 90 ###troop自定义旗帜
slot_troop_custom_banner_bg_type         = 91 ###troop自定义旗帜
slot_troop_custom_banner_charge_type_1   = 92 ###troop自定义旗帜
slot_troop_custom_banner_charge_type_2   = 93 ###troop自定义旗帜
slot_troop_custom_banner_charge_type_3   = 94 ###troop自定义旗帜
slot_troop_custom_banner_charge_type_4   = 95 ###troop自定义旗帜
slot_troop_custom_banner_flag_type       = 96 ###troop自定义旗帜
slot_troop_custom_banner_num_charges     = 97 ###troop自定义旗帜
slot_troop_custom_banner_positioning     = 98 ###troop自定义旗帜位置
slot_troop_custom_banner_map_flag_type   = 99 ###troop自定义旗帜大地图标签类型

#conversation strings -- must be in this order! ###对话——必须在本命令字符串！
###troop简介
slot_troop_intro 						= 101
###troop简介响应1
slot_troop_intro_response_1 			= 102
###troop简介响应2
slot_troop_intro_response_2 			= 103
###troop背景故事a
slot_troop_backstory_a 					= 104
###troop背景故事b
slot_troop_backstory_b 					= 105
###troop背景故事c
slot_troop_backstory_c 					= 106
###troop背景故事延迟
slot_troop_backstory_delayed 			= 107
###troop背景故事响应1
slot_troop_backstory_response_1 		= 108
###troop背景故事响应2
slot_troop_backstory_response_2 		= 109
slot_troop_signup   					= 110
slot_troop_signup_2 					= 111
slot_troop_signup_response_1 			= 112
slot_troop_signup_response_2 			= 113
slot_troop_mentions_payment 			= 114 #Not actually used
slot_troop_payment_response 			= 115 #Not actually used
slot_troop_morality_speech   			= 116
slot_troop_2ary_morality_speech 		= 117
slot_troop_personalityclash_speech 		= 118
slot_troop_personalityclash_speech_b 	= 119
slot_troop_personalityclash2_speech 	= 120
slot_troop_personalityclash2_speech_b 	= 121
slot_troop_personalitymatch_speech 		= 122
slot_troop_personalitymatch_speech_b 	= 123
slot_troop_retirement_speech 			= 124
slot_troop_rehire_speech 				= 125
slot_troop_home_intro           		= 126
slot_troop_home_description    			= 127
slot_troop_home_description_2 			= 128
slot_troop_home_recap         			= 129
###troop的尊称、敬语，用于npc如何称呼玩家，例如队长、阁下。
slot_troop_honorific   					= 130
slot_troop_kingsupport_string_1			= 131
slot_troop_kingsupport_string_2			= 132
slot_troop_kingsupport_string_2a		= 133
slot_troop_kingsupport_string_2b		= 134
slot_troop_kingsupport_string_3			= 135
slot_troop_kingsupport_objection_string	= 136
slot_troop_intel_gathering_string	    = 137
slot_troop_fief_acceptance_string	    = 138
slot_troop_woman_to_woman_string	    = 139
slot_troop_turn_against_string	        = 140

slot_troop_strings_end 					= 141

###npc雇佣价格
slot_troop_payment_request 				= 141

#141, support base removed, slot now available

###npc支持国家状态
slot_troop_kingsupport_state			= 142
###npc支持国家争论
slot_troop_kingsupport_argument			= 143
###npc支持国家对手
slot_troop_kingsupport_opponent			= 144
###npc支持国家抗议状态 0默认 1需要声音 2表示
slot_troop_kingsupport_objection_state  = 145 #0, default, 1, needs to voice, 2, has voiced

###任务日期
slot_troop_days_on_mission		        = 150
###当前任务
slot_troop_current_mission			    = 151
###任务目标
slot_troop_mission_object               = 152
###npc支持国家任务
npc_mission_kingsupport					= 1
###npc收集信息任务
npc_mission_gather_intel                = 2
###npc请求和平任务
npc_mission_peace_request               = 3
###npc质押诸侯任务
npc_mission_pledge_vassal               = 4
###npc寻求识别任务
npc_mission_seek_recognition            = 5
###npc测试水域任务
npc_mission_test_waters                 = 6
###npc非侵略任务
npc_mission_non_aggression              = 7
###npc如果可能答辩
npc_mission_rejoin_when_possible        = 8

#Number of routed agents after battle ends. ###战争结束后的路由代理数目。
###玩家路由agents
slot_troop_player_routed_agents                 = 146
###友军路由agents
slot_troop_ally_routed_agents                   = 147
###敌军路由agents
slot_troop_enemy_routed_agents                  = 148

#Special quest slots ###特殊任务槽
slot_troop_mission_participation        = 149
mp_unaware                              = 0 
mp_stay_out                             = 1 
mp_prison_break_fight                   = 2 
mp_prison_break_stand_back              = 3 
mp_prison_break_escaped                 = 4 
mp_prison_break_caught                  = 5 

#Below are some constants to expand the political system a bit. The idea is to make quarrels less random, but instead make them serve a rational purpose -- as a disincentive to lords to seek 
###下面是一些常数扩大政治系统一点。这个想法是为了让争吵不随机，而是让他们为理性的目的——为防止领主寻求

###troop争论
slot_troop_controversy                     = 150 #Determines whether or not a troop is likely to receive fief or marshalship ###确定是否一个队伍有可能获得封地或元帅

###troop最近进攻类型，未能加入军队，如果不支持的同事
slot_troop_recent_offense_type 	           = 151 #failure to join army, failure to support colleague
###troop最近进攻目标，在那个人身上
slot_troop_recent_offense_object           = 152 #to whom it happened
###troop最近进攻时间
slot_troop_recent_offense_time             = 153
###troop立场在阵营问题上
slot_troop_stance_on_faction_issue         = 154 #when it happened

###troop加入军队失败
tro_failed_to_join_army                    = 1
###troop支持同事失败
tro_failed_to_support_colleague            = 2


#CONTROVERSY ###争议
#This is used to create a more "rational choice" model of faction politics, in which lords pick fights with other lords for gain, rather than simply because of clashing personalities
####这是用来创造派系政治更“理性选择”模型，其中主接战获得其他领主，而不是仅仅因为冲突的性格

#It is intended to be a limiting factor for players and lords in their ability to intrigue against each other. It represents the embroilment of a lord in internal factional disputes. In contemporary media English, a lord with high "controversy" would be described as "embattled."
####它的目的是为他们勾心斗角的能力的球员，上议院的一个限制因素。它代表着在内部派系纷争勋爵的混乱。英国当代媒体，具有很高的“争论”主会被描述为“四面楚歌”。

#The main effect of high controversy is that it disqualifies a lord from receiving a fief or an appointment
###高争议的主要影响是，它排除了一个主接收一封封地或预约

#It is a key political concept because it provides incentive for much of the political activity. For example, Lord Red Senior is worried that his rival, Lord Blue Senior, is going to get a fied which Lord Red wants. So, Lord Red turns to his protege, Lord Orange Junior, to attack Lord Blue in public. The fief goes to Lord Red instead of Lord Blue, and Lord Red helps Lord Orange at a later date.
###是关键的一个政治概念，因为它提供了大量的政治活动的激励。例如，红色的高级主担心他的对手，主蓝色高级，都将得到一个固定的红色要主。所以，耶和华他的门徒红色变为橙色，主少年，攻击主蓝在公共。封地去主红色而不是蓝色和红色的主，主有助于主橙在稍后的日期。

slot_troop_will_join_prison_break      = 161


troop_slots_reserved_for_relations_start        = 165 #this is based on id_troops, and might change

slot_troop_relations_begin				= 0 #this creates an array for relations between troops
											#Right now, lords start at 165 and run to around 290, including pretenders
											
											
											
########################################################
##  PLAYER SLOTS           #############################玩家slot
########################################################

slot_player_spawned_this_round                 = 0
slot_player_last_rounds_used_item_earnings     = 1
slot_player_selected_item_indices_begin        = 2
slot_player_selected_item_indices_end          = 11
slot_player_cur_selected_item_indices_begin    = slot_player_selected_item_indices_end
slot_player_cur_selected_item_indices_end      = slot_player_selected_item_indices_end + 9
slot_player_join_time                          = 21
slot_player_button_index                       = 22 #used for presentations
slot_player_can_answer_poll                    = 23
slot_player_first_spawn                        = 24
slot_player_spawned_at_siege_round             = 25
slot_player_poll_disabled_until_time           = 26
slot_player_total_equipment_value              = 27
slot_player_last_team_select_time              = 28
slot_player_death_pos_x                        = 29
slot_player_death_pos_y                        = 30
slot_player_death_pos_z                        = 31
slot_player_damage_given_to_target_1           = 32 #used only in destroy mod
slot_player_damage_given_to_target_2           = 33 #used only in destroy mod
slot_player_last_bot_count                     = 34
slot_player_bot_type_1_wanted                  = 35
slot_player_bot_type_2_wanted                  = 36
slot_player_bot_type_3_wanted                  = 37
slot_player_bot_type_4_wanted                  = 38
slot_player_spawn_count                        = 39


########################################################
##  TEAM SLOTS             #############################组slot
########################################################

slot_team_flag_situation                       = 0




#Rebellion changes end ###叛乱改变结束


# character backgrounds ###特征背景
cb_noble = 1              ###贵族
cb_merchant = 2           ###商人
cb_guard = 3              ###警卫
cb_forester = 4           ###林务官、猎人
cb_nomad = 5              ###游牧民族
cb_thief = 6              ###小偷
cb_priest = 7             ###牧师

cb2_page = 0              ###
cb2_apprentice = 1        ###学徒
cb2_urchin  = 2           ###顽童；淘气鬼
cb2_steppe_child = 3      ###草原的孩子
cb2_merchants_helper = 4  ###商人帮手

cb3_poacher = 3           ###偷猎者
cb3_craftsman = 4         ###工匠
cb3_peddler = 5           ###小贩
cb3_troubadour = 7        ###吟游诗人
cb3_squire = 8            ###乡绅
cb3_lady_in_waiting = 9   ###等待中的女人
cb3_student = 10          ###学生

cb4_revenge = 1           ###复仇
cb4_loss    = 2           ###损失
cb4_wanderlust =  3       ###旅行者
cb4_disown  = 5           ###被赶出了家门
cb4_greed  = 6            ###权力

#NPC system changes end ###npc系统改变结束
#Encounter types ###遭遇类型
enctype_fighting_against_village_raid = 1   ###村庄洗劫战斗时
enctype_catched_during_village_raid   = 2   ###抓住在村庄洗劫


### Troop occupations slot_troop_occupation
##slto_merchant           = 1
###不活跃的
slto_inactive           = 0 #for companions at the beginning of the game###同伴在游戏的开始

###王国领主
slto_kingdom_hero       = 2

###玩家同伴
slto_player_companion   = 5 #This is specifically for companions in the employ of the player -- ie, in the party, or on a mission
###王国女士
slto_kingdom_lady       = 6 #Usually inactive (Calradia is a traditional place). However, can be made potentially active if active_npcs are expanded to include ladies
###王国管家
slto_kingdom_seneschal  = 7
###强盗骑士
slto_robber_knight      = 8
###不活跃的伪装者
slto_inactive_pretender = 9


stl_unassigned          = -1  ###未分配的村庄
stl_reserved_for_player = -2  ###保留给玩家的村庄
stl_rejected_by_player  = -3  ###玩家保留的村庄

#NPC changes begin
slto_retirement      = 11
#slto_retirement_medium    = 12
#slto_retirement_short     = 13
#NPC changes end

########################################################
##  QUEST SLOTS            #############################任务slot
########################################################

slot_quest_target_center            = 1   ###任务触发中心
slot_quest_target_troop             = 2   ###任务触发troop
slot_quest_target_faction           = 3   ###任务触发阵营
slot_quest_object_troop             = 4   ###任务troop目标
##slot_quest_target_troop_is_prisoner = 5 ###任务触发troop是俘虏
slot_quest_giver_troop              = 6   ###给与troop任务：把 你 的 外 科 医 生 {s3}借 给 {s1}
slot_quest_object_center            = 7   ###任务目标中心
slot_quest_target_party             = 8   ###任务触发队伍
slot_quest_target_party_template    = 9   ###任务触发队伍模版
slot_quest_target_amount            = 10  ###任务触发数量
slot_quest_current_state            = 11  ###任务当前状态
slot_quest_giver_center             = 12  ###给与中心任务
slot_quest_target_dna               = 13  ###任务触发dna
slot_quest_target_item              = 14  ###任务触发组
slot_quest_object_faction           = 15  ###任务目标阵营

slot_quest_target_state             = 16  ###任务触发状态
slot_quest_object_state             = 17  ###任务目标状态

slot_quest_convince_value           = 19  ###任务说服值
slot_quest_importance               = 20  ###任务重要性
slot_quest_xp_reward                = 21  ###任务经验奖励
slot_quest_gold_reward              = 22  ###任务金钱奖励
slot_quest_expiration_days          = 23  ###任务截止日期
slot_quest_dont_give_again_period   = 24  ###不要再次给与任务时期
slot_quest_dont_give_again_remaining_days = 25  ###不要再次给与任务剩下的天数

slot_quest_failure_consequence      = 26  ###任务失败的后果
slot_quest_temp_slot      			= 27      ###任务临时slot

########################################################
##  PARTY TEMPLATE SLOTS   #############################队伍模版slot
########################################################

# Ryan BEGIN
slot_party_template_num_killed   = 1        ###队伍模版杀人数
slot_party_template_lair_type    	 	= 3     ###队伍模版巢穴类型
slot_party_template_lair_party    		= 4   ###队伍模版巢穴队伍
slot_party_template_lair_spawnpoint     = 5 ###队伍模版巢穴刷兵点


# Ryan END


########################################################
##  SCENE PROP SLOTS       #############################场景道具slot
########################################################

###场景道具打开还是关闭slot
scene_prop_open_or_close_slot       = 1
scene_prop_smoke_effect_done        = 2
scene_prop_number_of_agents_pushing = 3 #for belfries only
scene_prop_next_entry_point_id      = 4 #for belfries only
scene_prop_belfry_platform_moved    = 5 #for belfries only
scene_prop_slots_end                = 6

########################################################
rel_enemy   = 0 ###敌人
rel_neutral = 1 ###中立
rel_ally    = 2 ###友军


#Talk contexts ###谈话上下文环境
tc_town_talk                  = 0   ###城镇交谈
tc_court_talk   	      	  = 1     ###领主大厅交谈
tc_party_encounter            = 2   ###遭遇队伍
tc_castle_gate                = 3   ###城堡大门
tc_siege_commander            = 4   ###攻城指挥官
tc_join_battle_ally           = 5   ###加入友军战斗
tc_join_battle_enemy          = 6   ###加入敌人战斗
tc_castle_commander           = 7   ###城堡指挥官
tc_hero_freed                 = 8   ###释放英雄
tc_hero_defeated              = 9   ###战胜英雄
tc_entering_center_quest_talk = 10  ###进入中心任务交谈
tc_back_alley                 = 11  ###回到小巷
tc_siege_won_seneschal        = 12  ###攻城赢得管家
tc_ally_thanks                = 13  ###友军感谢
tc_tavern_talk                = 14  ###酒馆交谈
tc_rebel_thanks               = 15  ###造反者感谢
tc_garden            		  = 16      ###花园
tc_courtship            	  = 16    ###求爱
tc_after_duel            	  = 17    ###在决斗
tc_prison_break               = 18  ###越狱
tc_escape               	  = 19    ###逃脱
tc_give_center_to_fief        = 20  ###给封地
tc_merchants_house            = 21  ###商人房子


#Troop Commentaries begin ###troop评论开始
#Log entry types ###日志条目类型
#civilian ###平民

###村庄搜查事件日志
logent_village_raided            = 1
###村庄勒索事件日志
logent_village_extorted          = 2
###搭讪大篷车事件日志
logent_caravan_accosted          = 3 #in caravan accosted, center and troop object are -1, and the defender's faction is the object ###在大篷车搭讪，中心和部队的对象是1，和后卫的派系的对象
###旅行工具事件日志
logent_traveller_attacked        = 3 #in traveller attacked, origin and destination are center and troop object, and the attacker's faction is the object ###在攻击的来源和目的地的旅行，是中心、队伍的对象，和攻击者的派系的对象

###帮助农民事件日志
logent_helped_peasants           = 4 

###队伍贸易事件日志
logent_party_traded              = 5

logent_castle_captured_by_player              = 10  ###城堡捕获玩家事件日志
logent_lord_defeated_by_player                = 11  ###领主打败玩家事件日志
logent_lord_captured_by_player                = 12  ###领主捕获玩家事件日志
logent_lord_defeated_but_let_go_by_player     = 13  ###领主打败玩家但放走玩家事件日志
logent_player_defeated_by_lord                = 14  ###玩家打败领主事件日志
logent_player_retreated_from_lord             = 15  ###玩家从领主撤退事件日志
logent_player_retreated_from_lord_cowardly    = 16  ###玩家从弱小领主撤退事件日志
logent_lord_helped_by_player                  = 17  ###领主帮助玩家事件日志
logent_player_participated_in_siege           = 18  ###玩家参与攻城事件日志
logent_player_participated_in_major_battle    = 19  ###玩家参与主要的战斗事件日志
logent_castle_given_to_lord_by_player         = 20  ###给玩家城堡事件日志

logent_pledged_allegiance          = 21   ###承诺效忠事件日志
logent_liege_grants_fief_to_vassal = 22   ###封地给领主事件日志


logent_renounced_allegiance      = 23   ###放弃效忠事件日志

logent_player_claims_throne_1    		               = 24 ###玩家声称王位1事件日志
logent_player_claims_throne_2    		               = 25 ###玩家声称王位2事件日志


logent_troop_feels_cheated_by_troop_over_land		   = 26     ###troop感觉欺骗因为troop封地事件日志
logent_ruler_intervenes_in_quarrel                     = 27 ###争吵干预尺度事件日志
logent_lords_quarrel_over_land                         = 28 ###领主争吵因为封地事件日志
logent_lords_quarrel_over_insult                       = 29 ###领主争吵因为侮辱事件日志
logent_marshal_vs_lord_quarrel                  	   = 30   ###元帅和领主争吵事件日志
logent_lords_quarrel_over_woman                        = 31 ###领主因为女士争吵事件日志

logent_lord_protests_marshall_appointment			   = 32       ###领主抗议元帅任命事件日志
logent_lord_blames_defeat						   	   = 33             ###领主指责失败事件日志

logent_player_suggestion_succeeded					   = 35         ###玩家建议成功事件日志
logent_player_suggestion_failed					       = 36         ###玩家建议失败事件日志

logent_liege_promises_fief_to_vassal				   = 37         ###承诺给封地领主事件日志

logent_lord_insults_lord_for_cowardice                 = 38 ###领主侮辱领主懦弱事件日志
logent_lord_insults_lord_for_rashness                  = 39 ###领主侮辱领主轻率事件日志
logent_lord_insults_lord_for_abandonment               = 40 ###领主侮辱领主放弃事件日志
logent_lord_insults_lord_for_indecision                = 41 ###领主侮辱领主优柔寡断事件日志
logent_lord_insults_lord_for_cruelty                   = 42 ###领主侮辱领主残忍事件日志
logent_lord_insults_lord_for_dishonor                  = 43 ###领主侮辱领主不名誉事件日志




logent_game_start                           = 45 ###游戏开始事件日志
logent_poem_composed                        = 46 ##Not added
logent_tournament_distinguished             = 47 ##Not added
logent_tournament_won                       = 48 ##Not added

###求爱事件日志。夫人一直是参与者，求婚者总是troop对象
#logent courtship - lady is always actor, suitor is always troop object
###女士有利于求婚者事件日志
logent_lady_favors_suitor                   = 51 #basically for gossip ###基本上说闲话的
###女士答应求婚者未婚妻因为选择事件日志
logent_lady_betrothed_to_suitor_by_choice   = 52
###女士答应求婚者未婚妻因为家族事件日志
logent_lady_betrothed_to_suitor_by_family   = 53
###女士拒绝求婚者事件日志
logent_lady_rejects_suitor                  = 54
###女士父亲拒绝求婚者事件日志
logent_lady_father_rejects_suitor           = 55
###女士结婚领主事件日志
logent_lady_marries_lord                    = 56
###女士和领主私奔事件日志
logent_lady_elopes_with_lord                = 57
###女士被求婚者拒绝
logent_lady_rejected_by_suitor              = 58
###女士答应求婚者未婚妻因为压力事件日志
logent_lady_betrothed_to_suitor_by_pressure = 59 #mostly for gossip ###大多为八卦

###女士和求婚者打破订婚事件日志
logent_lady_and_suitor_break_engagement		= 60
###女士和求婚者结婚事件日志
logent_lady_marries_suitor				    = 61

###领主控制女士人质事件日志
logent_lord_holds_lady_hostages             = 62
###挑战领主决斗失败事件日志
logent_challenger_defeats_lord_in_duel      = 63
###放弃挑战领主决斗事件日志
logent_challenger_loses_to_lord_in_duel     = 64

###玩家从村庄偷牛事件日志
logent_player_stole_cattles_from_village    = 66

###队伍希望战斗地点
logent_party_spots_wanted_bandits           = 70

###边境偷牛事件日志
logent_border_incident_cattle_stolen          = 72 #possibly add this to rumors for non-player faction
###边境绑架新娘事件日志
logent_border_incident_bride_abducted         = 73 #possibly add this to rumors for non-player faction
###边境杀死村民事件日志
logent_border_incident_villagers_killed       = 74 #possibly add this to rumors for non-player faction
###边境虐待事件日志
logent_border_incident_subjects_mistreated    = 75 #possibly add this to rumors for non-player faction

#These supplement caravans accosted and villages burnt, in that they create a provocation. So far, they only refer to the player
logent_border_incident_troop_attacks_neutral  = 76
logent_border_incident_troop_breaks_truce     = 77
logent_border_incident_troop_suborns_lord   = 78


logent_policy_ruler_attacks_without_provocation 			= 80
logent_policy_ruler_ignores_provocation         			= 81 #possibly add this to rumors for non-player factions
logent_policy_ruler_makes_peace_too_soon        			= 82
logent_policy_ruler_declares_war_with_justification         = 83
logent_policy_ruler_breaks_truce                            = 84
logent_policy_ruler_issues_indictment_just                  = 85 #possibly add this to rumors for non-player faction
logent_policy_ruler_issues_indictment_questionable          = 86 #possibly add this to rumors for non-player faction

logent_player_faction_declares_war						    = 90 #this doubles for declare war to extend power
logent_faction_declares_war_out_of_personal_enmity		    = 91
logent_faction_declares_war_to_regain_territory 		    = 92
logent_faction_declares_war_to_curb_power					= 93
logent_faction_declares_war_to_respond_to_provocation	    = 94
logent_war_declaration_types_end							= 95


#logent_lady_breaks_betrothal_with_lord      = 58
#logent_lady_betrothal_broken_by_lord        = 59



#lord reputation type, for commentaries ###领主的声誉，评论
#"Martial" will be twice as common as the other types ###好战的将为其他类型的两倍

###lrep_quarrelsome好辩的  lrep_debauched放荡的          lrep_goodnatured善良的   lrep_martial好战的 
###lrep_upstanding正直的   lrep_selfrighteous自命正直    lrep_roguish无赖的        lrep_cunning狡猾的
###lrep_adventurous冒险的 lrep_otherworldly幻想的 lrep_conventional传统的 lrep_moralist道德的 lrep_ambitious野心勃勃的

lrep_none           = 0 
###侠义的但不太同情或反省，例如李察狮心王，你的平均第十四世纪法国男爵
lrep_martial        = 1 #chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
###恶意的，愤世嫉俗的，有点偏执，可能冲动——例如罗伯特Graves提比略，一些查尔斯六世的叔叔
lrep_quarrelsome    = 2 #spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, some of Charles VI's uncles
###冷血，教化，凶残的-例如，征服者威廉，帖木儿，屋大维，奥朗则布（虽然他是正直的相反，尤其是在他加入）
lrep_selfrighteous  = 3 #coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he is arguably upstanding instead, particularly after his accession)
###冷血的，务实的，不道德的：如路易斯西，吉斯卡尔，Akbar Khan，阿卜杜勒阿齐兹伊本沙特
lrep_cunning        = 4 #coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
###恶意的，不道德的，残暴的-例如卡利古拉，塔奇曼查尔斯纳瓦尔
lrep_debauched      = 5 #spiteful, amoral, sadistic - eg Caligula, Tuchman's Charles of Navarre
###侠义的，仁慈的，也许有点太体面是一个很好的军阀侯赛因伊本阿里。一些著名的历史上的例子也许。因为许多缺乏动力上升到派领导。兰吉特辛格方面
lrep_goodnatured    = 6 #chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein ibn Ali. Few well-known historical examples maybe. because many lack the drive to rise to faction leadership. Ranjit Singh has aspects
###说教，仁慈的，务实的，例如伯纳德Cornwell的艾尔弗雷德，查理曼大帝，萨拉赫尔DIN，Sher Shah苏瑞
lrep_upstanding     = 7 #moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Salah al-Din, Sher Shah Suri

###用于共享，特别是前的同伴。试图生活为主的
lrep_roguish        = 8 #used for commons, specifically ex-companions. Tries to live life as a lord to the full
###赞助者 用于共享，特别是前的同伴。很多人试图提高土地
lrep_benefactor     = 9 #used for commons, specifically ex-companions. Tries to improve lot of folks on land
###管理者 用于共享，特别是前的同伴。试图最大限度的采邑的收入潜力
lrep_custodian      = 10 #used for commons, specifically ex-companions. Tries to maximize fief's earning potential


#lreps specific to dependent noblewomen
###平常的 夏洛特约克SATC季节1-2，可能大多数中世纪贵族
lrep_conventional    = 21 #Charlotte York in SATC seasons 1-2, probably most medieval aristocrats
###爱冒险的顽皮的。然而，这基本上意味着她喜欢旅行和狩猎，也许渴望更大的冒险。然而，中世纪贵族妇女斗争是罕见的，和那些试图独立生活的人更是凤毛麟角，和最好的同伴一样代表个人前脚本
lrep_adventurous     = 22 #Tomboyish. However, this basically means that she likes to travel and hunt, and perhaps yearn for wider adventures. However, medieval noblewomen who fight are rare, and those that attempt to live independently of a man are rarer still, and best represented by pre-scripted individuals like companions
###超世俗的 倾向于神秘主义，浪漫主义。
lrep_otherworldly    = 23 #Prone to mysticism, romantic. 
###有雄心的 麦克白夫人
lrep_ambitious       = 24 #Lady Macbeth
###道德家 直立或恩人——以等效nobless帮忙，她作为库的道德传统的角色，很严重。基于松散的克里斯蒂娜比萨
lrep_moralist        = 25 #Equivalent of upstanding or benefactor -- takes nobless oblige, and her traditional role as repository of morality, very seriously. Based loosely on Christine de Pisa 



###一个更复杂的系统可以包括以下的声誉
#a more complicated system of reputation could include the following...

#成功与不成功的——基本表
#successful vs unlucky -- basic gauge of success
#大胆与谨慎——也许不是必要的
#daring vs cautious -- maybe not necessary
#光荣/虔诚/思想与不法——角色的执行行为的外部代码。未能捕捉到的人喜欢奥朗则布，复杂性，也许，但是好的NPC
#honorable/pious/ideological vs unscrupulous -- character's adherance to an external code of conduct. Fails to capture complexity of people like Aurangzeb, maybe, but good for NPCs
#（幻想/利他与正统/非正统的可能是上述的一个子集，或特定的外部代码可以被另一个标签）
#(visionary/altruist and orthodox/unorthodox could be a subset of the above, or the specific external code could be another tag)
#大方、忠诚与操纵/剥削——角色的责任感到具体的个人，他们之间的关系的基础上。对忠诚的军队，等
#generous/loyal vs manipulative/exploitative -- character's sense of duty to specific individuals, based on their relationship. Affects loyalty of troops, etc
#仁慈与残酷无情、反社会的同情——/角色的一般意义上的。Sher Shah是肆无忌惮，仁慈的例子（后者在一定程度上）。
#凝重与非常规——人物本身的社会习俗。非常重要的，给定的时代
#merciful vs cruel/ruthless/sociopathic -- character's general sense of compassion. Sher Shah is example of unscrupulous and merciful (the latter to a degree).
#dignified vs unconventional -- character's adherance to social conventions. Very important, given the times


#########################下面是5首诗歌
###强调的渴望，莱拉和油田
courtship_poem_tragic      = 1 #Emphasizes longing, Laila and Majnoon
###挪威传奇的女英雄
courtship_poem_heroic      = 2 #Norse sagas with female heroines
###重点对诙谐的妙语——contrasto（西西里学校讽刺）
courtship_poem_comic       = 3 #Emphasis on witty repartee -- Contrasto (Sicilian school satire) 
###苏菲诗歌。歌曲
courtship_poem_mystic      = 4 #Sufi poetry. Song of Songs
###将女人作为一个文明的力量——玫瑰的浪漫，爱的城堡围攻
courtship_poem_allegoric   = 5 #Idealizes woman as a civilizing force -- the Romance of the Rose, Siege of the Castle of Love

#courtship gifts currently deprecated ###目前使用的求爱礼物、诗歌


#Troop Commentaries end ###troop评论结束



tutorial_fighters_begin = "trp_tutorial_fighter_1"
tutorial_fighters_end   = "trp_tutorial_archer_1"

#Walker types: 
walkert_default            = 0
walkert_needs_money        = 1
walkert_needs_money_helped = 2
walkert_spy                = 3
num_town_walkers = 8
town_walker_entries_start = 32

reinforcement_cost_easy = 600
reinforcement_cost_moderate = 450
reinforcement_cost_hard = 300

###通行费关税的有效期为72小时
merchant_toll_duration        = 72 #Tolls are valid for 72 hours

###领主等英雄战斗逃跑的比较值
hero_escape_after_defeat_chance = 70


raid_distance = 4

surnames_begin = "str_surname_1"
surnames_end = "str_surnames_end"
names_begin = "str_name_1"
names_end = surnames_begin
countersigns_begin = "str_countersign_1"
countersigns_end = names_begin
secret_signs_begin = "str_secret_sign_1"
secret_signs_end = countersigns_begin

kingdom_titles_male_begin = "str_faction_title_male_player"
kingdom_titles_female_begin = "str_faction_title_female_player"

kingdoms_begin = "fac_player_supporters_faction"
kingdoms_end = "fac_kingdoms_end"

npc_kingdoms_begin = "fac_kingdom_1"
npc_kingdoms_end = kingdoms_end

bandits_begin = "trp_bandit"
bandits_end = "trp_black_khergit_horseman"

kingdom_ladies_begin = "trp_knight_1_1_wife"
kingdom_ladies_end = "trp_heroes_end"

#active NPCs in order: companions, kings, lords, pretenders

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = kingdom_ladies_begin

lords_begin = "trp_knight_1_1"
lords_end = pretenders_begin

kings_begin = "trp_kingdom_1_lord"
kings_end = lords_begin

companions_begin = "trp_npc1"
companions_end = kings_begin

active_npcs_begin = "trp_npc1"
active_npcs_end = kingdom_ladies_begin
#"active_npcs_begin replaces kingdom_heroes_begin to allow for companions to become lords. Includes anyone who may at some point lead their own party: the original kingdom heroes, companions who may become kingdom heroes, and pretenders. (slto_kingdom_hero as an occupation means that you lead a party on the map. Pretenders have the occupation "slto_inactive_pretender", even if they are part of a player's party, until they have their own independent party)
#If you're a modder and you don't want to go through and switch every kingdom_heroes to active_npcs, simply define a constant: kingdom_heroes_begin = active_npcs_begin., and kingdom_heroes_end = active_npcs_end. I haven't tested for that, but I think it should work.

active_npcs_including_player_begin = "trp_kingdom_heroes_including_player_begin"
original_kingdom_heroes_begin = "trp_kingdom_1_lord"

heroes_begin = active_npcs_begin
heroes_end = kingdom_ladies_end

soldiers_begin = "trp_farmer"
soldiers_end = "trp_town_walker_1"

#Rebellion changes

##rebel_factions_begin = "fac_kingdom_1_rebels"
##rebel_factions_end =   "fac_kingdoms_end"

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = active_npcs_end
#Rebellion changes

tavern_minstrels_begin = "trp_tavern_minstrel_1"
tavern_minstrels_end   = "trp_kingdom_heroes_including_player_begin"

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end   = tavern_minstrels_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end   = tavern_booksellers_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end   = tavern_travelers_begin

mercenary_troops_begin = "trp_watchman"
mercenary_troops_end = "trp_mercenaries_end"

multiplayer_troops_begin = "trp_swadian_crossbowman_multiplayer"
multiplayer_troops_end = "trp_multiplayer_end"

multiplayer_ai_troops_begin = "trp_swadian_crossbowman_multiplayer_ai"
multiplayer_ai_troops_end = multiplayer_troops_begin

multiplayer_scenes_begin = "scn_multi_scene_1"
multiplayer_scenes_end = "scn_multiplayer_maps_end"

multiplayer_scene_names_begin = "str_multi_scene_1"
multiplayer_scene_names_end = "str_multi_scene_end"

multiplayer_flag_projections_begin = "mesh_flag_project_sw"
multiplayer_flag_projections_end = "mesh_flag_projects_end"

multiplayer_flag_taken_projections_begin = "mesh_flag_project_sw_miss"
multiplayer_flag_taken_projections_end = "mesh_flag_project_misses_end"

multiplayer_game_type_names_begin = "str_multi_game_type_1"
multiplayer_game_type_names_end = "str_multi_game_types_end"

quick_battle_troops_begin = "trp_quick_battle_troop_1"
quick_battle_troops_end = "trp_quick_battle_troops_end"

quick_battle_troop_texts_begin = "str_quick_battle_troop_1"
quick_battle_troop_texts_end = "str_quick_battle_troops_end"

quick_battle_scenes_begin = "scn_quick_battle_scene_1"
quick_battle_scenes_end = "scn_quick_battle_maps_end"

quick_battle_scene_images_begin = "mesh_cb_ui_maps_scene_01"

quick_battle_battle_scenes_begin = quick_battle_scenes_begin
quick_battle_battle_scenes_end = "scn_quick_battle_scene_4"

quick_battle_siege_scenes_begin = quick_battle_battle_scenes_end
quick_battle_siege_scenes_end = quick_battle_scenes_end

quick_battle_scene_names_begin = "str_quick_battle_scene_1"

lord_quests_begin = "qst_deliver_message"
lord_quests_end   = "qst_follow_army"

lord_quests_begin_2 = "qst_destroy_bandit_lair"
lord_quests_end_2   = "qst_blank_quest_2"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end   = lord_quests_end

village_elder_quests_begin = "qst_deliver_grain"
village_elder_quests_end = "qst_eliminate_bandits_infesting_village"

village_elder_quests_begin_2 = "qst_blank_quest_6"
village_elder_quests_end_2   = "qst_blank_quest_6"

mayor_quests_begin  = "qst_move_cattle_herd"
mayor_quests_end    = village_elder_quests_begin

mayor_quests_begin_2 = "qst_blank_quest_11"
mayor_quests_end_2   = "qst_blank_quest_11"

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end   = mayor_quests_begin

lady_quests_begin_2 = "qst_blank_quest_16"
lady_quests_end_2   = "qst_blank_quest_16"

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end   = lady_quests_begin

army_quests_begin_2 = "qst_blank_quest_21"
army_quests_end_2   = "qst_blank_quest_21"

player_realm_quests_begin = "qst_resolve_dispute"
player_realm_quests_end = "qst_blank_quest_1"

player_realm_quests_begin_2 = "qst_blank_quest_26"
player_realm_quests_end_2 = "qst_blank_quest_26"

all_items_begin = 0
all_items_end = "itm_items_end"

all_quests_begin = 0
all_quests_end = "qst_quests_end"

towns_begin = "p_town_1"
castles_begin = "p_castle_1"
villages_begin = "p_village_1"

towns_end = castles_begin
castles_end = villages_begin
villages_end   = "p_salt_mine"

walled_centers_begin = towns_begin
walled_centers_end   = castles_end

centers_begin = towns_begin
centers_end   = villages_end

training_grounds_begin   = "p_training_ground_1"
training_grounds_end     = "p_Bridge_1"

scenes_begin = "scn_town_1_center"
scenes_end = "scn_castle_1_exterior"

spawn_points_begin = "p_zendar"
spawn_points_end = "p_spawn_points_end"

regular_troops_begin       = "trp_novice_fighter"
regular_troops_end         = "trp_tournament_master"

swadian_merc_parties_begin = "p_town_1_mercs"
swadian_merc_parties_end   = "p_town_8_mercs"

vaegir_merc_parties_begin  = "p_town_8_mercs"
vaegir_merc_parties_end    = "p_zendar"

arena_masters_begin    = "trp_town_1_arena_master"
arena_masters_end      = "trp_town_1_armorer"

training_gound_trainers_begin    = "trp_trainer_1"
training_gound_trainers_end      = "trp_ransom_broker_1"

town_walkers_begin = "trp_town_walker_1"
town_walkers_end = "trp_village_walker_1"

village_walkers_begin = "trp_village_walker_1"
village_walkers_end   = "trp_spy_walker_1"

spy_walkers_begin = "trp_spy_walker_1"
spy_walkers_end = "trp_tournament_master"

walkers_begin = town_walkers_begin
walkers_end   = spy_walkers_end

armor_merchants_begin  = "trp_town_1_armorer"
armor_merchants_end    = "trp_town_1_weaponsmith"

weapon_merchants_begin = "trp_town_1_weaponsmith"
weapon_merchants_end   = "trp_town_1_tavernkeeper"

tavernkeepers_begin    = "trp_town_1_tavernkeeper"
tavernkeepers_end      = "trp_town_1_merchant"

goods_merchants_begin  = "trp_town_1_merchant"
goods_merchants_end    = "trp_town_1_horse_merchant"

horse_merchants_begin  = "trp_town_1_horse_merchant"
horse_merchants_end    = "trp_town_1_mayor"

mayors_begin           = "trp_town_1_mayor"
mayors_end             = "trp_village_1_elder"

village_elders_begin   = "trp_village_1_elder"
village_elders_end     = "trp_merchants_end"

startup_merchants_begin = "trp_swadian_merchant"
startup_merchants_end = "trp_startup_merchants_end"

num_max_items = 10000 #used for multiplayer mode

average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

village_prod_min = 0 #was -5
village_prod_max = 20 #was 20

trade_goods_begin = "itm_spice"
trade_goods_end = "itm_siege_supply"
food_begin = "itm_smoked_fish"
food_end = "itm_siege_supply"
reference_books_begin = "itm_book_wound_treatment_reference"
reference_books_end   = trade_goods_begin
readable_books_begin = "itm_book_tactics"
readable_books_end   = reference_books_begin
books_begin = readable_books_begin
books_end = reference_books_end
horses_begin = "itm_sumpter_horse"
horses_end = "itm_arrows"
weapons_begin = "itm_wooden_stick"
weapons_end = "itm_wooden_shield"
ranged_weapons_begin = "itm_darts"
ranged_weapons_end = "itm_torch"
armors_begin = "itm_leather_gloves"
armors_end = "itm_wooden_stick"
shields_begin = "itm_wooden_shield"
shields_end = ranged_weapons_begin

# Banner constants

banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end_minus_one = "mesh_banner_f21"

arms_meshes_begin = "mesh_arms_a01"
arms_meshes_end_minus_one = "mesh_arms_f21"

custom_banner_charges_begin = "mesh_custom_banner_charge_01"
custom_banner_charges_end = "mesh_tableau_mesh_custom_banner"

custom_banner_backgrounds_begin = "mesh_custom_banner_bg"
custom_banner_backgrounds_end = custom_banner_charges_begin

custom_banner_flag_types_begin = "mesh_custom_banner_01"
custom_banner_flag_types_end = custom_banner_backgrounds_begin

custom_banner_flag_map_types_begin = "mesh_custom_map_banner_01"
custom_banner_flag_map_types_end = custom_banner_flag_types_begin

custom_banner_flag_scene_props_begin = "spr_custom_banner_01"
custom_banner_flag_scene_props_end = "spr_banner_a"

custom_banner_map_icons_begin = "icon_custom_banner_01"
custom_banner_map_icons_end = "icon_banner_01"

banner_map_icons_begin = "icon_banner_01"
banner_map_icons_end_minus_one = "icon_banner_136"

banner_scene_props_begin = "spr_banner_a"
banner_scene_props_end_minus_one = "spr_banner_f21"

khergit_banners_begin_offset = 63
khergit_banners_end_offset = 84

sarranid_banners_begin_offset = 105
sarranid_banners_end_offset = 125

banners_end_offset = 136

# Some constants for merchant invenotries
merchant_inventory_space = 30
num_merchandise_goods = 40

num_max_river_pirates = 25
num_max_zendar_peasants = 25
num_max_zendar_manhunters = 10

num_max_dp_bandits = 10
num_max_refugees = 10
num_max_deserters = 10

num_max_militia_bands = 15
num_max_armed_bands = 12

num_max_vaegir_punishing_parties = 20
num_max_rebel_peasants = 25

num_max_frightened_farmers = 50
num_max_undead_messengers  = 20

num_forest_bandit_spawn_points = 1
num_mountain_bandit_spawn_points = 1
num_steppe_bandit_spawn_points = 1
num_taiga_bandit_spawn_points = 1
num_desert_bandit_spawn_points = 1
num_black_khergit_spawn_points = 1
num_sea_raider_spawn_points = 2

peak_prisoner_trains = 4
peak_kingdom_caravans = 12
peak_kingdom_messengers = 3


# Note positions
note_troop_location = 3

##########################战斗战术
#battle tactics
btactic_hold = 1            ###坚守 
btactic_follow_leader = 2   ###跟随
btactic_charge = 3          ###冲锋
btactic_stand_ground = 4    ###站在原地

#default right mouse menu orders ###默认的鼠标右键菜单命令
cmenu_move = -7     ###移动
cmenu_follow = -6   ###跟随

# Town center modes - resets in game menus during the options ###镇中心的模式，将在游戏菜单中的选项
tcm_default 		= 0   ###默认
tcm_disguised 		= 1 ###潜入
tcm_prison_break 	= 2 ###越狱
tcm_escape      	= 3 ###逃脱


# Arena battle modes ###竞技场战斗模式
#abm_fight = 0
abm_training = 1    ###训练
abm_visit = 2       ###访问
abm_tournament = 3  ###锦标赛

# Camp training modes ###训练营的训练模式
ctm_melee    = 1  ###近战
ctm_ranged   = 2  ###投掷
ctm_mounted  = 3  ###骑术
ctm_training = 4  ###射击

# Village bandits attack modes ###村庄强盗攻击模式
vba_normal          = 1
vba_after_training  = 2

arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 5
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 10
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 25
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 60
arena_grand_prize = 250


#Additions ###增加的
price_adjustment = 25 #the percent by which a trade at a center alters price ###在中心贸易改变价格

fire_duration = 4 #fires takes 4 hours ###火灾需要4小时

###正常的成就
#NORMAL ACHIEVEMENTS
ACHIEVEMENT_NONE_SHALL_PASS = 1,
ACHIEVEMENT_MAN_EATER = 2,
ACHIEVEMENT_THE_HOLY_HAND_GRENADE = 3,
ACHIEVEMENT_LOOK_AT_THE_BONES = 4,
ACHIEVEMENT_KHAAAN = 5,
ACHIEVEMENT_GET_UP_STAND_UP = 6,
ACHIEVEMENT_BARON_GOT_BACK = 7,
ACHIEVEMENT_BEST_SERVED_COLD = 8,
ACHIEVEMENT_TRICK_SHOT = 9,
ACHIEVEMENT_GAMBIT = 10,
ACHIEVEMENT_OLD_SCHOOL_SNIPER = 11,
ACHIEVEMENT_CALRADIAN_ARMY_KNIFE = 12,
ACHIEVEMENT_MOUNTAIN_BLADE = 13,
ACHIEVEMENT_HOLY_DIVER = 14,
ACHIEVEMENT_FORCE_OF_NATURE = 15,

###技能与成就：
#SKILL RELATED ACHIEVEMENTS:
ACHIEVEMENT_BRING_OUT_YOUR_DEAD = 16,
ACHIEVEMENT_MIGHT_MAKES_RIGHT = 17,
ACHIEVEMENT_COMMUNITY_SERVICE = 18,
ACHIEVEMENT_AGILE_WARRIOR = 19,
ACHIEVEMENT_MELEE_MASTER = 20,
ACHIEVEMENT_DEXTEROUS_DASTARD = 21,
ACHIEVEMENT_MIND_ON_THE_MONEY = 22,
ACHIEVEMENT_ART_OF_WAR = 23,
ACHIEVEMENT_THE_RANGER = 24,
ACHIEVEMENT_TROJAN_BUNNY_MAKER = 25,

###地图相关成就
#MAP RELATED ACHIEVEMENTS:
ACHIEVEMENT_MIGRATING_COCONUTS = 26,
ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED = 27,
ACHIEVEMENT_SARRANIDIAN_NIGHTS = 28,
ACHIEVEMENT_OLD_DIRTY_SCOUNDREL = 29,
ACHIEVEMENT_THE_BANDIT = 30,
ACHIEVEMENT_GOT_MILK = 31,
ACHIEVEMENT_SOLD_INTO_SLAVERY = 32,
ACHIEVEMENT_MEDIEVAL_TIMES = 33,
ACHIEVEMENT_GOOD_SAMARITAN = 34,
ACHIEVEMENT_MORALE_LEADER = 35,
ACHIEVEMENT_ABUNDANT_FEAST = 36,
ACHIEVEMENT_BOOK_WORM = 37,
ACHIEVEMENT_ROMANTIC_WARRIOR = 38,

###政治导向成就
#POLITICALLY ORIENTED ACHIEVEMENTS:
ACHIEVEMENT_HAPPILY_EVER_AFTER = 39,
ACHIEVEMENT_HEART_BREAKER = 40,
ACHIEVEMENT_AUTONOMOUS_COLLECTIVE = 41,
ACHIEVEMENT_I_DUB_THEE = 42,
ACHIEVEMENT_SASSY = 43,
ACHIEVEMENT_THE_GOLDEN_THRONE = 44,
ACHIEVEMENT_KNIGHTS_OF_THE_ROUND = 45,
ACHIEVEMENT_TALKING_HELPS = 46,
ACHIEVEMENT_KINGMAKER = 47,
ACHIEVEMENT_PUGNACIOUS_D = 48,
ACHIEVEMENT_GOLD_FARMER = 49,
ACHIEVEMENT_ROYALITY_PAYMENT = 50,
ACHIEVEMENT_MEDIEVAL_EMLAK = 51,
ACHIEVEMENT_CALRADIAN_TEA_PARTY = 52,
ACHIEVEMENT_MANIFEST_DESTINY = 53,
ACHIEVEMENT_CONCILIO_CALRADI = 54,
ACHIEVEMENT_VICTUM_SEQUENS = 55,

###联网成就
#MULTIPLAYER ACHIEVEMENTS:
ACHIEVEMENT_THIS_IS_OUR_LAND = 56,
ACHIEVEMENT_SPOIL_THE_CHARGE = 57,
ACHIEVEMENT_HARASSING_HORSEMAN = 58,
ACHIEVEMENT_THROWING_STAR = 59,
ACHIEVEMENT_SHISH_KEBAB = 60,
ACHIEVEMENT_RUIN_THE_RAID = 61,
ACHIEVEMENT_LAST_MAN_STANDING = 62,
ACHIEVEMENT_EVERY_BREATH_YOU_TAKE = 63,
ACHIEVEMENT_CHOPPY_CHOP_CHOP = 64,
ACHIEVEMENT_MACE_IN_YER_FACE = 65,
ACHIEVEMENT_THE_HUSCARL = 66,
ACHIEVEMENT_GLORIOUS_MOTHER_FACTION = 67,
ACHIEVEMENT_ELITE_WARRIOR = 68,

###综合成就
#COMBINED ACHIEVEMENTS
ACHIEVEMENT_SON_OF_ODIN = 69,
ACHIEVEMENT_KING_ARTHUR = 70,
ACHIEVEMENT_KASSAI_MASTER = 71,
ACHIEVEMENT_IRON_BEAR = 72,
ACHIEVEMENT_LEGENDARY_RASTAM = 73,
ACHIEVEMENT_SVAROG_THE_MIGHTY = 74,

ACHIEVEMENT_MEN_HANDLER = 75,
ACHIEVEMENT_GIRL_POWER = 76,
ACHIEVEMENT_QUEEN = 77,
ACHIEVEMENT_EMPRESS = 78,
ACHIEVEMENT_TALK_OF_THE_TOWN = 79,
ACHIEVEMENT_LADY_OF_THE_LAKE = 80,
