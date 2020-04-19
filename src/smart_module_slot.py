# -*- coding: utf-8 -*-

## slot编号 操作

import os

from module_info import src_dir

slot_dir = src_dir + "/slot/"
#path = os.path.abspath(".");
#slot_dir = path + "/slot/"


slotNoConfig={
    "troop":{
        "start":165,
    },
    "party":{
        "start":370,
    },
    "faction":{
        "start":160,
    },
    "scene":{
        "start":15,
    },
    "party_template":{
        "start":10,
    },
    "agent":{
        "start":30,
    },
    "quest":{
        "start":30,
    },
    "item":{
        "start":65,
    },
    "player":{
        "start":40,
    },
    "team":{
        "start":15,
    },
    "scene_prop":{
        "start":10,
    }
}


def getConfigPath(type):
    return slot_dir + type + ".slot";


## 用于初始化slot文件
def initSlot():
    for (type,config) in slotNoConfig.items():
        open(getConfigPath(type),mode="w").close()

def getSlotNo(type,slotName):
    config = slotNoConfig.get(type)
    path = getConfigPath(type)
    ## 读取数据
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    ## 处理编号数据
    if len(lines) == 0 or len(lines[0]) == 0:
        numText = str(config.get("start"))
    else:
        numText = lines[0]
    num = int(numText)
    ## 处理slot数据
    if len(lines) < 2 or len(lines[1]) == 0:
        dataText = "{}"
    else:
        dataText = lines[1]
    data = eval(dataText)
    if(data.has_key(slotName)):
        return data.get(slotName)
    else:
        num += 1
        file = open(path, "w")
        file.write(str(num) + "\n")
        data[slotName] = num
        file.write(str(data) + "\n")
        file.close()
    return num;


def getTroopSlotNo(slotName):
    return getSlotNo("troop",slotName)

def getPartySlotNo(slotName):
    return getSlotNo("party",slotName)

def getFactionSlotNo(slotName):
    return getSlotNo("faction",slotName)

def getSceneSlotNo(slotName):
    return getSlotNo("scene",slotName)

def getPartyTemplateSlotNo(slotName):
    return getSlotNo("party_template",slotName)

def getAgentSlotNo(slotName):
    return getSlotNo("agent",slotName)

def getQuestSlotNo(slotName):
    return getSlotNo("quest",slotName)

def getItemSlotNo(slotName):
    return getSlotNo("item",slotName)

def getPlayerSlotNo(slotName):
    return getSlotNo("player",slotName)

def getTeamSlotNo(slotName):
    return getSlotNo("team",slotName)

def getScenePropSlotNo(slotName):
    return getSlotNo("scene_prop",slotName)


if __name__ == 'smart_module_slot':
    initSlot()
    ##print "初始化slot数据"

