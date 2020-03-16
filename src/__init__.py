
# -*- coding: utf-8 -*-
import os

from header_common import find_object


# if(find_object("spr","village_fire_big") < 0):
#     raise RuntimeError("aaaaa")


# from process_import_modules import *
# #
# # preprocessString()

# xx = lambda x:x*2
#
# print xx(8)
from header_troops import *
from import_modules import *
from module_troops import *




# def repeatTroop(size,troop):
#     '''
#         将兵种重复多少个
#     :param start: 开始的编号
#     :param end: 结束的编号(不包含)
#     :param troop: 兵种模板
#     :return:
#     '''
#     return repeatTroop(0,size,troop)

# for troop in repeatTroop(12,18,["npc{}","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_boots,itm_knife],
#    str_8|agi_7|int_12|cha_7|level(3),wp(60),knows_tracker_npc|
#    knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
#    0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],):
#     print troop


# troops = repeatTroop(12,18,["npc{}","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_boots,itm_knife],
#    str_8|agi_7|int_12|cha_7|level(3),wp(60),knows_tracker_npc|
#    knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
#    0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],)
#
#
# for i in mergeList([0,1,2,3],[18,22,44],troops):
#     print i



# for i in repeatRandomTroop(18):
#     print i
#
# from process_import_modules import preprocessMissionTemplates
#
# preprocessMissionTemplates()


# print os.path.abspath("..")


# def body_armor2(x):
#   return (((bignum | x) & ibf_armor_mask) << ibf_body_armor_bits)
#
# def body_armor3(x):
#   return ((x & ibf_armor_mask) << ibf_body_armor_bits)
#
# print "2:" + str(body_armor2(255))
#
#
# print "3:" + str(body_armor3(256))



# print str((bignum | 10000))
#
#
# print bin(0x40000000000000000000000000000000 | 2)
# from process_import_modules import preprocessGameMenus
#
# preprocessGameMenus()


testData = [
    ["test1",12,18,22,["a","b","c"]],
    ["test2",12,18,22,["a","b","c"]],
    ["test3",12,18,22,["a","b","c"]],
    ["test4",12,18,22,["a","b","c"]],
    ["test5",12,18,22,["a","b","c"]],
    ["test6",12,18,22,["a","b","c"]],
]


## id
config = {
    "troops":{
        # "append":[
        #     # ["testAppend", 12, 18, 22],
        #     # ["testAppend2", 12, 18, 22]
        # ],
        # "insertAfter":[
        #     {
        #         "sign":"#0",
        #         "data":[
        #             ["testinsertAfter",12,18,22]
        #         ],
        #     }
        # ],
        # "insertBefore":[
        #     {
        #         "sign":"#3",
        #         "data":[
        #             ["testinsertAfter",12,18,22]
        #         ],
        #     }
        # ],
        # "replace":[
        #     {
        #         "sign":"test5",
        #         "data":[
        #             ["testinsertAfter",12,18,22],
        #             ["testinsertAfter2",12,18,22]
        #         ],
        #     },
        # ],
        # "delete":[
        #     {
        #         "signs":["#2","test5"],
        #     },
        # ],
        "children":{
            "test2:#4":{
                "append":[
                    "x","y","z"
                ]
            }
        },
    }
}




def log(type,text):
    print "{} - {}\n".format(type,text)

def debug(text):
    log("DEUBG",text)
def info(text):
    log("INFO",text)
def warn(text):
    log("WARN",text)
    print "---------------------------------------------------------------------------"
def error(text):
    log("ERROR",text)
    print "==========================================================================="
def fatal(text):
    log("FATAL",text)

def processHasId(datas, config, moduleName, moduleItem):
    if(datas == None):
        raise RuntimeError("[{}.{}]:source is None".format(moduleName,moduleItem));

    if config == None or len(config) == 0:
        raise RuntimeError("[{}.{}]:config is None".format(moduleName,moduleItem));

    for (command,cfgList) in config.items():
        ## append命令只使用：data参数
        if "append" == command:
            data = cfgList;
            if data == None or len(data) == 0:
                warn("[{}.{}.{}]:data is empty".format(moduleName, moduleItem,command))
                continue
            else:
                datas.extend(data)
                debug("[{}.{}.{}]: add data size is 【{}】".format(moduleName, moduleItem,command, len(data)))
        elif "insertBefore" == command or "insertAfter" == command or "replace" == command:
            for itemCfg in cfgList:

                sign = itemCfg.get("sign")
                idIndexs = itemCfg.get("idIndexs")
                data = itemCfg.get("data")

                if sign == None:
                    raise RuntimeError("[{}.{}.{}]:sign must provide !".format(moduleName,moduleItem,command))

                if data == None or len(data) == 0:
                    warn("[{}.{}.{}]: data is empty".format(moduleName, moduleItem,command))
                    continue

                realIndex = getRealIndexBySign(datas, sign, idIndexs, moduleName, moduleItem, command);
                if "replace" == command:
                    ## 删除当前数据
                    del datas[realIndex]
                    info("[{}.{}.{}]:remove a data".format(moduleName, moduleItem, command))
                for item in data:
                    if "insertAfter" == command:
                        datas.insert(realIndex + 1, item)
                    elif "insertBefore" == command or "replace" == command:
                        datas.insert(realIndex, item)
                info("[{}.{}.{}]:add data size is 【{}】".format(moduleName, moduleItem, command,len(data) - 1 if "replace" == command else len(data)))
        elif "delete" == command:
            for itemCfg in cfgList:
                signs = itemCfg.get("signs")
                idIndexs = itemCfg.get("idIndexs")
                if signs != None and len(signs) > 0:
                    for sign in signs:
                        del datas[getRealIndexBySign(datas, sign, idIndexs, moduleName, moduleItem, command)]
                    info("[{}.{}.{}]:remove data size is 【{}】".format(moduleName, moduleItem, command,len(signs)))
                else:
                    warn("[{}.{}.{}]:signs is empty".format(moduleName,moduleItem,command))
        ### children命令会使用到：id,idIndexs,index,data参数
        elif "children" == command:
            for (sign,childrenCfg) in cfgList.items():
                if not sign.count(":") == 1:
                    raise RuntimeError("[{}.{}.{}]:children sign({}) must contains [:]".format(moduleName,moduleItem,command,sign))

                items = sign.split(":")

                rowSign = items[0]
                colSign = items[1]

                parentIndex = getRealIndexBySign(datas, colSign, None, moduleName, moduleItem, command)

                if len(rowSign) == 0:
                    for data in datas:
                        processHasId(data[parentIndex], childrenCfg, moduleName,
                                     "{}[{}]".format(moduleItem, parentIndex))
                else:
                    data = datas[getRealIndexBySign(datas, rowSign, None, moduleName, moduleItem, command)]
                    processHasId(data[parentIndex], childrenCfg, moduleName,
                                 "{}[{}]".format(moduleItem, parentIndex))


                debug("children:{}".format(parentIndex))


        else:
            warn("[{}.{}.{}]:unknow command 【{}】".format(moduleName,moduleItem,command,command))


def getRealIndexBySign(datas, sign, idIndexs, moduleName, moduleItem, command):
    if sign.startswith("#"):
        try:
            realIndex = int(sign[1:])
        except BaseException, e:
            raise RuntimeError(
                "[{}.{}.{}]:children item key must is a number !!!".format(moduleName, moduleItem, command))
    else:
        realIndex = findIndex(datas, sign, idIndexs, moduleName, moduleItem, command)

    if realIndex != None and realIndex < 0:
        raise RuntimeError(
            "[{}.{}.{}]:sign({}) format is error".format(moduleName, moduleItem,
                                                                   command,sign))
    return realIndex

def findIndex(datas,sign,idIndexs,moduleName,moduleItem,command):
    '''
        数据，
    :param datas: 数据集合
    :param sign: 指定名称  多个名称之间使用:隔开
    :param idIndexs: 指定id索引集合 ,如果数据为空，就使用第一个索引
    :return:
    '''

    if(datas == None or len(datas) == 0):
        raise RuntimeError("[{}.{}.{}]:data is empty".format(moduleName,moduleItem,command))

    if(sign == None or len(sign) == 0):
        raise RuntimeError("[{}.{}.{}]:sign is empty".format(moduleName,moduleItem,command))

    if(idIndexs == None or len(idIndexs) == 0):
        idIndexs = [0]

    for index in range(len(datas)):
        data = datas[index]
        nameList = []
        for id in idIndexs:
            nameList.append(data[id])
        name = ":".join(nameList)
        if(sign == name):
            return index;
    raise RuntimeError("[{}.{}.{}]:sign({}) is not found".format(moduleName,moduleItem,command,sign))




print  testData



print "------------------------------------------------------"
processHasId(testData,config["troops"],"testMode","troops")

print "------------------------------------------------------"



print testData