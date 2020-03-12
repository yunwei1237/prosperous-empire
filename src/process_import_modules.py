# -*- coding: utf-8 -*-

from import_modules import modules
from module_dialogs import dialogs
from module_mission_templates import mission_templates
from module_scripts import scripts
from module_simple_triggers import simple_triggers
from module_strings import strings
from module_triggers import triggers


def checkDependentOn(checkModule):
    '''
        检测依赖的module是否存在和是否开启
    :param checkModule:
    :return:
    '''

    if checkModule.__contains__("enable") and not checkModule["enable"]:
        return False

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
            if module.__contains__("strings"):
                print "module：\t" + module["name"]
                print "------------------------------------------------------------------"
                print "process strings"
                print "before size:" + str(len(strings))
                for (k, v) in module["strings"].items():
                    print "add string : " + k.ljust(30) + " = " + v + ""
                    strings.append((k, v));
                print "process strings end"
                print "after size:" + str(len(strings))
    print "------------------------------------------------------------------"
def preprocessSimpleTrigger():
    '''
        预处理简单触发器模块
    :return:
    '''
    for module in modules:
        if checkDependentOn(module):
            if module.__contains__("simple_triggers"):
                print "module：\t" + module["name"]
                print "------------------------------------------------------------------"
                print "process simple_triggers"
                print "before size:" + str(len(simple_triggers))
                for object in module["simple_triggers"]:
                    print "add a trigger"
                    simple_triggers.append(object)
                print "process simple_triggers end"
                print "after size:" + str(len(simple_triggers))
    print "------------------------------------------------------------------"

def preprocessTrigger():
    '''
        预处理简单触发器模块
    :return:
    '''
    for module in modules:
        if checkDependentOn(module):
            if module.__contains__("triggers"):
                print "module：\t" + module["name"]
                print "------------------------------------------------------------------"
                print "process triggers"
                print "before size:" + str(len(triggers))
                for object in module["triggers"]:
                    print "add a trigger"
                    simple_triggers.append(object)
                print "process triggers end"
                print "after size:" + str(len(triggers))
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

def preprocessDialogs():
    '''
        预处理对话模块
    :return:
    '''
    for module in modules:
        if checkDependentOn(module):
            if module.__contains__("dialogs"):
                print "module：\t" + module["name"]
                print "------------------------------------------------------------------"
                print "process dialogs"
                print "before size:" + str(len(dialogs))
                for object in module["dialogs"]:
                    print "add a dialog:" + object[1]+":"+object[4]+"\t'"+object[3]+"'"
                    dialogs.append(object)
                print "process dialogs end"
                print "after size:" + str(len(dialogs))
    print "------------------------------------------------------------------"


def preprocessMissionTemplates():
    '''
        预处理战场模板模块
    :return:
    '''
    for module in modules:
        if checkDependentOn(module):
            if module.__contains__("mission_templates"):
                print "module：\t" + module["name"]
                print "------------------------------------------------------------------"
                print "process mission_templates"
                for (key,object) in module["mission_templates"].items():
                    ## mission_templates
                    if key == "create_mission_templates" and len(object) != 0:
                        create_mission_templates = object
                        print "process create_mission_templates"
                        addnum = len(mission_templates)
                        for mission_template in create_mission_templates:
                            print "add a mission template:" + mission_template[0]
                            mission_templates.append(mission_template)
                        print "add mission template nums: " + str(len(mission_templates) - addnum)
                    ## spawns
                    elif key == "add_mission_template_spawns" and len(object) != 0:
                        add_mission_template_spawns = object;
                        print "process add_mission_template_spawns"
                        for (mts_name,spawns) in add_mission_template_spawns.items():
                            for mission_template in mission_templates:
                                if mts_name == mission_template[0]:
                                    if len(spawns) != 0:
                                        addnum = len(mission_template[4])
                                        for spawn in spawns:
                                            print "in mission template ["+ mts_name +"] add a spawn"
                                            mission_template[4].append(spawn)
                                        print "add mission template spawn nums: " + str(len(mission_template[4]) - addnum)
                    ## triggers
                    elif key == "add_mission_template_triggers" and len(object) != 0:
                        print "process add_mission_template_triggers"
                        add_mission_template_triggers = object
                        for (mts_name,trgs) in add_mission_template_triggers.items():
                            for mission_template in mission_templates:
                                if mts_name == mission_template[0]:
                                    if len(trgs) != 0:
                                        addnum = len(mission_template[5])
                                        for trg in trgs:
                                            print "in mission template ["+ mts_name +"] add a trigger"
                                            mission_template[5].append(trg)
                                        print "add mission template trigger nums: " + str(len(mission_template[5]) -addnum)
                    # else:
                    #     print "Error in mission_templates not key: " + key
                print "process mission_templates end"
    print "------------------------------------------------------------------"