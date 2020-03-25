# -*- coding: utf-8 -*-
from modules.HeroCollection import heroCollection
from modules.LadiesGoOut import ladiesGoOut
from modules.PartyManage import partyManage
from modules.PatrolParty import patrolParty
from modules.TestMode import testMode
from modules.VillageManage import villageMange
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
    patrolParty,
    partyManage,
    testMode,
    heroCollection,
    ladiesGoOut,
    villageMange,
]