# -*- coding: utf-8 -*-
from modules.center.BuildingSystem import buildingSystem
from modules.center.CenterRents import centerRents
from modules.center.PatrolGuardParty import patrolGuardParty
from modules.center.ProsperitySystem import prosperitySystem
from modules.TestMode import testMode
from modules.base.FactionBaseScripts import factionBaseScripts
from modules.base.PartyBaseScripts import partyBaseScripts
from modules.base.TroopBaseScripts import troopBaseScripts
from modules.lord.LadiesGoOut import ladiesGoOut
from modules.lord.LordCollectionRents import lordCollectionRents
from modules.lord.LordSoldiersManage import lordSoldiersManage
from modules.lord.ShowLordReputationType import showLordReputationType

'''
    剧本模块
'''
modModules = [
    prosperitySystem,
    buildingSystem,
    centerRents,
    lordCollectionRents,
    lordSoldiersManage,
    showLordReputationType,
    patrolGuardParty,
    ladiesGoOut,
    #partyManage,
    #heroCollection,
    #testMode,
]


'''
    保存所有modules
'''
modules = []


'''
    基础模块
'''
baseModules = [
    partyBaseScripts,
    factionBaseScripts,
    troopBaseScripts,
]

modules.extend(baseModules)
modules.extend(modModules)