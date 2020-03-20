# -*- coding: utf-8 -*-
import os
import re
import string

from config_modules import modules
from module_dialogs import dialogs
from module_game_menus import game_menus
from module_info import export_dir
from module_mission_templates import mission_templates
from module_scripts import scripts
from module_simple_triggers import simple_triggers
from module_strings import strings
from module_triggers import triggers
from process_global_variables import compile_all_global_vars


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
                if(not module.has_key("enable") or module["enable"]):
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



## 最重要的功能之一

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

    if config == None:
        raise RuntimeError("[ {} > {} ]:module Item config is None".format(moduleName,moduleItem));

    if type(config) != dict:
        raise RuntimeError("[ {} > {} ]:module Item config must a dict".format(moduleName, moduleItem))

    for (command,cfgList) in config.items():

        if "children" != command and type(cfgList) != list:
            raise RuntimeError("[ {} > {} > {} ]:config must a list".format(moduleName, moduleItem, command))

        ## append命令只使用：data参数
        if "append" == command:
            data = cfgList;

            if data == None or len(data) == 0:
                warn("[ {} > {} > {} ]:data is empty".format(moduleName, moduleItem,command))
                continue
            else:
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

                for index in range(len(data) - 1, -1, -1):
                    item = data[index]
                ##for item in data:
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
    index = -1
    ## 处理信号1
    matcher = re.match(r"^#(\d+)$", sign)
    if matcher:
        text = matcher.group(1)
        index = int(text)

    # ## 处理信号2
    # matcher = re.match(r"^(\w+)$", sign)
    # if matcher:
    #     text = matcher.group(1)
    #     index = findIndex(datas, text, None, moduleName, moduleItem, command)
    #
    # ## 处理信号3
    # matcher = re.match(r"^(\w+(:\w+)+)\[(\d+(,\d+)+)\]$", sign)
    # if matcher:
    #     text = matcher.group(1)
    #     indexs = matcher.group(3)
    #     index = findIndex(datas, text, [ int(x) for x in indexs.split(",")], moduleName, moduleItem, command)

    ## 处理信号4
    matcher = re.match(r"^(\w+@?(:\w+@?)*)(\[(\d+(,\d+)*)\])?$", sign)
    if matcher:
        signs = matcher.group(1).split(":")
        text = matcher.group(4)
        if text == None or len(text) == 0:
            indexs = [0]
        else:
            indexs = matcher.group(4).split(",")
        ## 如果参数大于等于2时，就需要双方参数必须相同
        if len(signs) == 1 or (len(signs) >1 and len(signs) == len(indexs)):
            index = findIndex(datas, signs, [int(x) for x in indexs], moduleName, moduleItem, command)

    if index > -1:
        ## 显示命中数据
        debug(
            "[ {} > {} > {} ]:(sign = {},index = {}) hit data : {}".format(moduleName, moduleItem, command, sign, index,
                                                                           datas[index]))
    else:
        ## 其它格式不支持
        raise RuntimeError(
            "[ {} > {} > {} ]:sign({}) format is error".format(moduleName, moduleItem,command,sign))
    return index


# ## 模糊匹配类型
# class LikeType():
#     none  = 1
#     left     = 2
#     right   = 3
#     center    = 4
#
#
#
# ## 在数据对比之前作预处理，
# class PreHandle():
#     ## 不做任何处理
#     none = 1
#     ## 将所有特殊符号转换成下划线，可以参考方法：process_common.py文件的convert_to_identifier_with_no_lowercase
#     convertToIdentifier = 2


def convert_to_identifier_with_no_lowercase(s0):
  s1 = string.replace(s0," ","_")
  s1 = string.replace(s1,"'","_")
  s1 = string.replace(s1,"`","_")
  s1 = string.replace(s1,"(","_")
  s1 = string.replace(s1,")","_")
  s1 = string.replace(s1,"-","_")
  s1 = string.replace(s1,",","_")
  s1 = string.replace(s1,"|","_")
  s1 = string.replace(s1,".","_")
  s1 = string.replace(s1,"?","_")
  s1 = string.replace(s1,"{","_")
  s1 = string.replace(s1,"}","_")
  s1 = string.replace(s1,"[","_")
  s1 = string.replace(s1,"]","_")
  s1 = string.replace(s1,"!","_")
  s1 = string.replace(s1,":","_")
  s1 = string.replace(s1,"\t","_") #Tab
  return s1


def findIndex(datas,signs,idIndexs,moduleName,moduleItem,command):
    '''
        从原始数据中根据信号对象获得对应的下标
    :param datas: 原始数据
    :param sign:  信号对象
    :param idIndexs: 信号对象所依赖的下标
    :param moduleName: module的名称，每一个module唯一的名称
    :param moduleItem: module的项，如,scripts,items,troops等等
    :param command: 命令名称，如，append,insertBefore,delete等等
    :param likeType: 模糊匹配类型  ：none(精确匹配),left（匹配开头）,right（匹配末尾）,center（匹配包含）
    :return:
    '''

    if(datas == None or len(datas) == 0):
        raise RuntimeError("[ {} > {} > {} ]:datas is empty".format(moduleName,moduleItem,command))

    if(signs == None or len(signs) == 0):
        raise RuntimeError("[ {} > {} > {} ]:signs is empty".format(moduleName,moduleItem,command))

    for index in range(len(datas)):
        data = datas[index]
        ## 所有选择器是否都匹配
        allMatch = True
        for signIndex in range(len(signs)):
            dateItem = data[idIndexs[signIndex]]
            sign = signs[signIndex]

            if(sign.endswith("@")):
                dateItem = convert_to_identifier_with_no_lowercase(dateItem)
                allMatch = allMatch and dateItem.startswith(sign[0:len(sign)-1])
            else:
                allMatch = allMatch and dateItem == sign
            ## 一旦不匹配，就不必再进行其它比较
            if allMatch == False:
                break
        if allMatch:
            return index
    print datas
    raise RuntimeError("[ {} > {} > {} ]:sign({}) is not found".format(moduleName,moduleItem,command,":".join(signs)))



## 处理各种模块
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
            # else:
            #     info("[ {} > {} ] is empty".format(moduleName,moduleItemName))


## 汉化
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


## 向外暴露的方法

def recompileGlobalVars(variable_list,variable_uses, triggers_args=[], sentences_args = [], game_menus_args = [], mission_templates_args = [], scripts_args = [], simple_triggers_args = []):
    '''
        重新编译生成全部全局变量

    :param variable_list:
    :param variable_uses:
    :param triggers:
    :param sentences:
    :param game_menus:
    :param mission_templates:
    :param scripts:
    :param simple_triggers:
    :return:
    '''
    compile_all_global_vars(variable_list, variable_uses, triggers_args, sentences_args, game_menus_args, mission_templates_args, scripts_args,
                            simple_triggers_args)
    debug("recompile global vars")

#preprocess(strings,"strings")

#preprocess(dialogs,"dialogs")

# preprocess(scripts,"scripts")

# print len(game_menus)
# preprocess(game_menus,"game_menus")
# print len(game_menus)

# preprocess(mission_templates,"mission_templates")

#preprocess(mission_templates,"mission_templates")

#preprocessInternational()