# -*- coding: utf-8 -*-
import os
import re

from config_modules import modules, export_dir
from module_dialogs import dialogs
from module_game_menus import game_menus
from module_mission_templates import mission_templates
from module_scripts import scripts
from module_simple_triggers import simple_triggers
from module_strings import strings
from module_triggers import triggers



## 日志处理功能

def log(type,text):
    print "{} - {}".format(type,text)

def debug(text):
    log("DEUBG".ljust(5),text)
def info(text):
    log("INFO".ljust(5),text)
def warn(text):
    log("WARN".ljust(5),text+"\n---------------------------------------------------------------------------")
def error(text):
    log("ERROR".ljust(5),text+"\n===========================================================================")
def fatal(text):
    log("FATAL".ljust(5),text+"\n==========================================================================="*2)

## module处理功能
def checkDependentOn(checkModule):
    '''
        检测依赖的module是否存在和是否开启
    :param checkModule:
    :return:  true：处理数量，并将module数据加入到系统中  false：放弃数据处理，该module任何数据都不会加入到系统中
    '''

    if checkModule == None:
        error("module is None")

    enable = checkModule.get("enable")

    ## 如果module 没有启用，就不做任何处理
    if enable == None or enable == False:
        return False

    ## 如果没有依赖的module需要检测的数据就直接返回
    dependentOns = checkModule.get("dependentOn")

    if dependentOns == None or len(dependentOns) == 0:
        return True

    ## 错误数量
    errorNum = 0;
    for dependentOn in dependentOns:
        isExist = False;
        isEnable = False;
        for module in modules:
            if(dependentOn == module["name"]):
                isExist = True
                ## 没有设置enable，或设置为True时代表启用
                if(not module.contains("enable") or module["enable"]):
                    isEnable = True
        if(not isExist):
            error("module({})'s dependent on module({}) is not exists".format(checkModule["name"],dependentOn))
            errorNum =  errorNum+ 1
        else:
            if(not isEnable):
                error("module({})'s dependent on module({}) is not enable".format(checkModule["name"],dependentOn))
                errorNum = errorNum + 1
    if(errorNum > 0):
        return False
    return True


def processModuleItem(datas, config, moduleName, moduleItem):
    '''
        处理module数据的功能
    :param datas: 原始数据
    :param config: 配置信息对象
    :param moduleName: module的名称，每一个module唯一的名称
    :param moduleItem: module的项，如,scripts,items,troops等等
    :return:
    '''
    if(datas == None):
        raise RuntimeError("[ {} > {} ]:module Item source is None".format(moduleName,moduleItem));

    if config == None or len(config) == 0:
        raise RuntimeError("[ {} > {} ]:module Item config is None".format(moduleName,moduleItem));

    if type(config) != dict:
        error("[ {} > {} ]:module Item config must a dict".format(moduleName, moduleItem))

    for (command,cfgList) in config.items():

        if "children" != command and type(cfgList) != list:
            error("[ {} > {} > {} ]:config must a list".format(moduleName, moduleItem, command))

        ## append命令只使用：data参数
        if "append" == command:
            data = cfgList;

            if data == None or len(data) == 0:
                warn("[ {} > {} > {} ]:data is empty".format(moduleName, moduleItem,command))
                continue
            else:
                datas.extend(data)
                for dataLine in data:
                    datas.append(dataLine)
                    info("[ {} > {} > {} ]:append data : {}".format(moduleName, moduleItem, command, dataLine))
                info("[ {} > {} > {} ]: add data size is 【{}】".format(moduleName, moduleItem,command, len(data)))
        elif "insertBefore" == command or "insertAfter" == command or "replace" == command:
            for itemCfg in cfgList:

                sign = itemCfg.get("sign")
                data = itemCfg.get("data")

                if sign == None:
                    raise RuntimeError("[ {} > {} > {} ]:sign must provide !".format(moduleName,moduleItem,command))

                if data == None or len(data) == 0:
                    warn("[ {} > {} > {} ]: data is empty".format(moduleName, moduleItem,command))
                    continue

                realIndex = getRealIndexBySign(datas, sign, moduleName, moduleItem, command);
                if "replace" == command:
                    ## 删除当前数据
                    oldData = datas[realIndex]
                    del datas[realIndex]
                    info("[ {} > {} > {} ]:(sign = {},index = {}) remove data : {}".format(moduleName, moduleItem, command,sign,realIndex,oldData))
                for item in data:
                    if "insertAfter" == command:
                        datas.insert(realIndex + 1, item)
                        info("[ {} > {} > {} ]:(sign = {},index = {}) insert data : {}".format(moduleName, moduleItem, command,sign,realIndex, item))
                    elif "insertBefore" == command or "replace" == command:
                        datas.insert(realIndex, item)
                        if "replace" == command:
                            info("[ {} > {} > {} ]: replace data : {}".format(moduleName, moduleItem, command, item))
                        else:
                            info("[ {} > {} > {} ]:(sign = {},index = {}) insert data : {}".format(moduleName, moduleItem, command,sign,realIndex, item))
                info("[ {} > {} > {} ]:add data size is 【{}】".format(moduleName, moduleItem, command,len(data) - 1 if "replace" == command else len(data)))
        elif "delete" == command:
            signs = cfgList
            if signs != None and len(signs) > 0:
                for sign in signs:
                    realIndex = getRealIndexBySign(datas, sign, moduleName, moduleItem, command)
                    oldData = datas[realIndex]
                    del datas[realIndex]
                    info("[ {} > {} > {} ]:(sign = {},index = {}) remove data : {}".format(moduleName, moduleItem, command,sign,realIndex, oldData))
                info("[ {} > {} > {} ]:remove data size is 【{}】".format(moduleName, moduleItem, command, len(signs)))
            else:
                warn("[ {} > {} > {} ]:signs is empty".format(moduleName, moduleItem, command))

        ### children命令会使用到：id,idIndexs,index,data参数
        elif "children" == command:
            for (sign,childrenCfg) in cfgList.items():
                if not sign.count(">") == 1:
                    raise RuntimeError("[ {} > {} > {} ]:children sign({}) must contains [>]".format(moduleName,moduleItem,command,sign))

                items = sign.split(">")
                rowSign = items[0]
                colSign = items[1]

                parentIndex = getRealIndexBySign(datas, colSign, moduleName, moduleItem, command)

                if len(rowSign) == 0:
                    for data in datas:
                        processModuleItem(data[parentIndex], childrenCfg, moduleName,
                                     "{}[{}]".format(moduleItem, parentIndex))
                else:
                    data = datas[getRealIndexBySign(datas, rowSign, moduleName, moduleItem, command)]
                    processModuleItem(data[parentIndex], childrenCfg, moduleName,
                                 "{}[{}]".format(moduleItem, parentIndex))


                debug("children:{}".format(parentIndex))
        else:
            warn("[ {} > {} > {} ]:unknow command 【{}】".format(moduleName,moduleItem,command,command))


def getRealIndexBySign(datas, sign, moduleName, moduleItem, command):
    '''
        根据信号选择对象
        信号1： #1  #号代表是下标，使用下标来进行数据选取
        信号2： name 没有前缀代表是选择id，通常是数据的0位
        信号3： name:age[18,22] 中括号内的数字代表name是由数据中的第18位和22位组成的唯一依据符，
    :param datas: 原始数据
    :param sign: 信号对象
    :param moduleName: module的名称，每一个module唯一的名称
    :param moduleItem: module的项，如,scripts,items,troops等等
    :param command: 命令名称，如，append,insertBefore,delete等等
    :return:
    '''
    ## 处理信号1
    matcher = re.match(r"^#(\d+)$", sign)
    if matcher:
        text = matcher.group(1)
        return int(text)

    ## 处理信号2
    matcher = re.match(r"^(\w+)$", sign)
    if matcher:
        text = matcher.group(1)
        return findIndex(datas, text, None, moduleName, moduleItem, command)

    ## 处理信号3
    matcher = re.match(r"^(\w+(:\w+)+)\[(\d+(,\d+)+)\]$", sign)
    if matcher:
        text = matcher.group(1)
        indexs = matcher.group(3)
        return findIndex(datas, text, [ int(x) for x in indexs.split(",")], moduleName, moduleItem, command)

    ## 其它格式不支持
    raise RuntimeError(
        "[ {} > {} > {} ]:sign({}) format is error".format(moduleName, moduleItem,command,sign))

def findIndex(datas,sign,idIndexs,moduleName,moduleItem,command):
    '''
        从原始数据中根据信号对象获得对应的下标
    :param datas: 原始数据
    :param sign:  信号对象
    :param idIndexs: 信号对象所依赖的下标
    :param moduleName: module的名称，每一个module唯一的名称
    :param moduleItem: module的项，如,scripts,items,troops等等
    :param command: 命令名称，如，append,insertBefore,delete等等
    :return:
    '''

    if(datas == None or len(datas) == 0):
        raise RuntimeError("[ {} > {} > {} ]:data is empty".format(moduleName,moduleItem,command))

    if(sign == None or len(sign) == 0):
        raise RuntimeError("[ {} > {} > {} ]:sign is empty".format(moduleName,moduleItem,command))

    if(idIndexs == None or len(idIndexs) == 0):
        idIndexs = [0]

    for index in range(len(datas)):
        data = datas[index]
        nameList = []
        for id in idIndexs:
            nameList.append(str(data[id]))
        name = ":".join(nameList)
        if(sign == name):
            return index;
    raise RuntimeError("[ {} > {} > {} ]:sign({}) is not found".format(moduleName,moduleItem,command,sign))

def preprocess(datas,moduleItemName):
    '''
        预处理模块
    :return:
    '''
    for module in modules:
        if checkDependentOn(module):
            moduleName = module.get("name")
            if module.has_key(moduleItemName):
                info("[ {} > {} ] begin".format(moduleName,moduleItemName))
                moduleItem = module.get(moduleItemName)
                if moduleItem != None:
                    processModuleItem(datas,moduleItem,moduleName,moduleItemName)
                info("[ {} > {} ] end".format(moduleName,moduleItemName))
            else:
                info("[ {} > {} ] is empty".format(moduleName,moduleItemName))


def preprocessInternational():
    '''
        处理汉化功能
        将汉化信息写入到导出目录的languages对应的汉化文件夹中的文件里
    :return:
    '''
    for module in modules:
        if checkDependentOn(module):
            if module.has_key("internationals"):
                for (key,fileInfo) in module.items():
                    if "internationals" == key:
                        for (fold,files) in fileInfo.items():
                            csvPath = export_dir + "languages/" + fold + "/"
                            if not os.path.exists(csvPath):
                                error("path({}) not exists".format(csvPath))
                                continue
                            for (filename,infos) in files.items():
                                csvFile = csvPath + filename + ".csv"
                                info("process file({}) begin".format(csvFile))
                                for str in infos:
                                    replaceIfExists(csvFile,str)
                                info("process file({}) end".format(csvFile))

'''
    检测内容在文件数据中是否已经存在
'''
def replaceIfExists(csvFile, hanStr):
    ## 读取文件内容
    file = open(csvFile,"r")
    lines = file.readlines()
    file.close()

    hanLine = hanStr + " \n"
    isReplace = False

    index = 0;
    while(index < len(lines)):
        line = lines[index]
        ## 删除指定key的行
        if len(line) != 0 and line.split("|")[0].strip() == hanStr.split("|")[0].strip():
            lines[index] = hanLine
            isReplace = True
            info("replace:{}".format(hanStr))
        index += 1
    if not isReplace:
        lines.append(hanLine)
        info("write:{}".format(hanStr))
    ## 定入文件中
    file = open(csvFile,"w")
    file.writelines(lines)
    file.close()




#preprocess(strings,"strings")

##preprocess(dialogs,"dialogs")

# preprocess(scripts,"scripts")

# preprocess(game_menus,"game_menus")

# preprocess(mission_templates,"mission_templates")

#preprocess(mission_templates,"mission_templates")

#preprocessInternational()