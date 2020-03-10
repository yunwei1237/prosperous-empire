# -*- coding: utf-8 -*-

from import_modules import modules
from module_scripts import scripts
from module_simple_triggers import simple_triggers
from module_strings import strings

def checkDependentOn(checkModule):
    '''
        检测依赖的module是否存在和是否开启
    :param checkModule:
    :return:
    '''
    ## 如果没有需要检测的数据就直接返回
    if(not checkModule.__contains__("dependentOn") or len(checkModule["dependentOn"]) == 0):
        return True

    dependentOns = checkModule["dependentOn"];
    errorNum = 0;
    for dependentOn in dependentOns:
        isExist = False;
        isEnable = False;
        for module in modules:
            if(dependentOn == module["name"]):
                isExist = True
                ## 没有设置enable，或设置为True时代表启用
                if(not module.__contains__("enable") or module["enable"]):
                    isEnable = True
        if(not isExist):
            print "Error ["+ checkModule["name"] +"]'s dependent on module["+dependentOn+"] is not exists"
            errorNum =  errorNum+ 1
        else:
            if(not isEnable):
                print "Error ["+ checkModule["name"] +"]'s dependent on module["+dependentOn+"] is not enable"
                errorNum = errorNum + 1
    if(errorNum > 0):
        return False
    return True
def preprocessString():
    '''
        预处理字符串模块
    :return:
    '''
    for module in modules:
        if checkDependentOn(module):
            print "module：\t" + module["name"]
            print "------------------------------------------------------------------"
            print "process strings"
            print "before size:" + str(len(strings))
            for (k, v) in module["strings"].items():
                print "add string : (" + k + "," + v + ")"
                strings.append((k, v));
            print "process strings end"
            print "after size:" + str(len(strings))
    print "------------------------------------------------------------------"
def preprocessMapTrigger():
    '''
        预处理地图触发器模块
    :return:
    '''
    for module in modules:
        if checkDependentOn(module):
            print "module：\t" + module["name"]
            print "------------------------------------------------------------------"
            print "process map_trigger"
            print "before size:" + str(len(simple_triggers))
            for object in module["map_trigger"]:
                print "add a map trigger"
                simple_triggers.append(object)
            print "process map_trigger end"
            print "after size:" + str(len(simple_triggers))
    print "------------------------------------------------------------------"

def preprocessScripts():
    '''
        预处理地图触发器模块
    :return:
    '''
    for module in modules:
        if checkDependentOn(module):
            print "module：\t" + module["name"]
            print "------------------------------------------------------------------"
            print "process scripts"
            print "before size:" + str(len(scripts))
            for object in module["scripts"]:
                print "add a script ：" + object[0]
                scripts.append(object)
            print "process scripts end"
            print "after size:" + str(len(scripts))
    print "------------------------------------------------------------------"