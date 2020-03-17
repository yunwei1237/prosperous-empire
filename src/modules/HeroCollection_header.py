import random

from src import *


def mergeList(*lists):
    result = []
    for list in lists:
        result.extend(list)
    return result

def repeatTroop(start,end,troop,isHero = True):
    '''
        将兵种重复多少个
    :param start: 开始的编号
    :param end: 结束的编号(不包含)
    :param troop: 兵种模板
    :return:
    '''
    troops = []
    for i in range(start,end):
        newTroop = list(troop)
        troopId = newTroop[0]
        troopId = troopId.format(str(i))
        newTroop[0] = troopId
        if isHero:
            newTroop[3] = newTroop[3]|tf_hero
        troops.append(newTroop)
    return troops


'''
    以下是一些额外功能
'''

def repeatArcher1(size,name = "archer_{}"):
    return repeatTroop(1,size + 1,[name,"Nord Huntsman","Nord Huntsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,[itm_arrows,itm_rawhide_coat,itm_hatchet,itm_hunting_bow,itm_hide_boots],str_10 | agi_5 | int_4 | cha_4|level(11),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (70) | wp_crossbow (60) | wp_throwing (60),knows_ironflesh_1|knows_power_draw_1|knows_athletics_2,nord_face_young_1, nord_face_old_2])

def repeatArcher2(size,name = "archer_{}"):
    return repeatTroop(1,size + 1,[name,"Nord Archer","Nord Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,[itm_arrows,itm_axe,itm_short_bow,itm_padded_leather,itm_leather_jerkin,itm_padded_leather,itm_leather_boots,itm_nasal_helmet,itm_nordic_archer_helmet,itm_leather_cap],str_11 | agi_5 | int_4 | cha_4|level(15),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (95) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_2|knows_power_draw_3|knows_athletics_5,nord_face_young_1, nord_face_old_2])

def repeatArcher3(size,name = "archer_{}"):
    return repeatTroop(1,size + 1,[name,"Nord Veteran Archer","Nord Veteran Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,[itm_bodkin_arrows,itm_sword_viking_2,itm_fighting_axe,itm_two_handed_axe,itm_long_bow,itm_mail_shirt,itm_mail_shirt,itm_byrnie,itm_leather_boots,itm_nordic_archer_helmet,itm_nordic_veteran_archer_helmet],str_12 | agi_5 | int_4 | cha_4|level(19),wp_one_handed (95) | wp_two_handed (95) | wp_polearm (95) | wp_archery (120) | wp_crossbow (95) | wp_throwing (95),knows_power_strike_3|knows_ironflesh_4|knows_power_draw_5|knows_athletics_7,nord_face_middle_1, nord_face_older_2])



def repeatFootMan1(size,name = "foot_name_{}"):
    return repeatTroop(1,size + 1,[name,"Vaegir Footman","Vaegir Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,[itm_spiked_club,itm_hand_axe,itm_sword_viking_1,itm_two_handed_axe,itm_tab_shield_kite_a,itm_tab_shield_kite_b,itm_spear,itm_nomad_cap,itm_vaegir_fur_cap,itm_rawhide_coat,itm_nomad_armor,itm_nomad_boots],def_attrib|level(9),wp(75),knows_common, vaegir_face_young_1, vaegir_face_middle_2])

def repeatFootMan2(size,name = "foot_name_{}"):
    return repeatTroop(1,size + 1,[name,"Vaegir Infantry","Vaegir Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,[itm_pike,itm_battle_axe,itm_sword_viking_2,itm_sword_khergit_2,itm_tab_shield_kite_c,itm_spear,itm_mail_hauberk,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],def_attrib|level(19),wp_melee(100),knows_athletics_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2])

def repeatFootMan3(size,name = "foot_name_{}"):
    return repeatTroop(1,size + 1,[name,"Vaegir Guard","Vaegir Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,[itm_ashwood_pike,itm_fighting_axe,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_d,itm_banded_armor,itm_lamellar_vest,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_leather_gloves],def_attrib|level(24),wp_melee(130),knows_riding_2|knows_athletics_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2])


def repeatKnight1(size,name = "knight_{}"):
    return repeatTroop(1,size + 1,[name,"Vaegir Veteran","Vaegir Veterans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,[itm_spiked_mace,itm_two_handed_axe,itm_sword_viking_1,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_spear,itm_steppe_cap,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_leather_jerkin,itm_studded_leather_coat,itm_nomad_boots,itm_saddle_horse],def_attrib|level(14),wp_melee(85),knows_athletics_2|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,vaegir_face_young_1, vaegir_face_old_2])

def repeatKnight2(size,name = "knight_{}"):
    return repeatTroop(1,size + 1,[name,"Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,[itm_lance,itm_fighting_pick,itm_bastard_sword_b,itm_sword_medieval_b,itm_sword_medieval_c_small,itm_tab_shield_heater_cav_a,itm_haubergeon,itm_mail_with_surcoat,itm_mail_chausses,itm_norman_helmet,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_warhorse,itm_warhorse,itm_hunter],def_attrib|level(21),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2])

def repeatKnight3(size,name = "knight_{}"):
    return repeatTroop(1,size + 1,[name,"Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,[itm_heavy_lance,itm_sword_two_handed_b,itm_sword_medieval_d_long,itm_morningstar,itm_morningstar,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_coat_of_plates_red,itm_cuir_bouilli,itm_plate_boots,itm_guard_helmet,itm_great_helmet,itm_bascinet,itm_charger,itm_warhorse,itm_gauntlets,itm_mail_mittens],def_attrib|level(28),wp_one_handed (150) | wp_two_handed (130) | wp_polearm (130) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_common|knows_riding_5|knows_shield_5|knows_ironflesh_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2])


def repeatRandomTroop(size,name = "random_npc_{}"):
    result = []
    funcs = [repeatArcher1, repeatArcher2, repeatArcher3, repeatFootMan1, repeatFootMan2, repeatFootMan3, repeatKnight1,
     repeatKnight2, repeatKnight3]
    for i in range(size):
        randomFun = random.choice(funcs)
        result.extend(randomFun(1,name.format(i+1)))
    return result