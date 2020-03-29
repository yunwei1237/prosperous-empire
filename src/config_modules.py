# -*- coding: utf-8 -*-
from modules.center.BuildingSystem import buildingSystem
from modules.center.ProsperitySystem import prosperitySystem
from modules.TestMode import testMode
from modules.base.FactionBaseScripts import factionBaseScripts
from modules.base.PartyBaseScripts import partyBaseScripts
from modules.base.TroopBaseScripts import troopBaseScripts

'''
    配置所有modules
'''

modules = [
    partyBaseScripts,
    factionBaseScripts,
    troopBaseScripts,
    testMode,
    #patrolGuardParty,
    prosperitySystem,
    buildingSystem,
    #partyManage,
    #heroCollection,
    #ladiesGoOut,
    #villageMange,
]