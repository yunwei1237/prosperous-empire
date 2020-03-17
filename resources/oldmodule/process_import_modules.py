# # -*- coding: utf-8 -*-
# import os
#
# from config_modules import modules, export_dir
# from module_dialogs import dialogs
# from module_game_menus import game_menus
# from module_mission_templates import mission_templates
# from module_scripts import scripts
# from module_simple_triggers import simple_triggers
# from module_strings import strings
# from module_triggers import triggers
#
#
# def checkDependentOn(checkModule):
#     '''
#         检测依赖的module是否存在和是否开启
#     :param checkModule:
#     :return:
#     '''
#
#     if checkModule.__contains__("enable") and not checkModule["enable"]:
#         return False
#
#     ## 如果没有需要检测的数据就直接返回
#     if(not checkModule.__contains__("dependentOn") or len(checkModule["dependentOn"]) == 0):
#         return True
#
#     dependentOns = checkModule["dependentOn"];
#     errorNum = 0;
#     for dependentOn in dependentOns:
#         isExist = False;
#         isEnable = False;
#         for module in modules:
#             if(dependentOn == module["name"]):
#                 isExist = True
#                 ## 没有设置enable，或设置为True时代表启用
#                 if(not module.__contains__("enable") or module["enable"]):
#                     isEnable = True
#         if(not isExist):
#             print "Error ["+ checkModule["name"] +"]'s dependent on module["+dependentOn+"] is not exists"
#             errorNum =  errorNum+ 1
#         else:
#             if(not isEnable):
#                 print "Error ["+ checkModule["name"] +"]'s dependent on module["+dependentOn+"] is not enable"
#                 errorNum = errorNum + 1
#     if(errorNum > 0):
#         return False
#     return True
#
#
# def preprocessString():
#     '''
#         预处理字符串模块
#     :return:
#     '''
#     for module in modules:
#         if checkDependentOn(module):
#             if module.__contains__("strings"):
#                 print "module：\t" + module["name"]
#                 print "------------------------------------------------------------------"
#                 print "process strings"
#                 for string in module["strings"]:
#                     print "add string : " + str(string)
#                     strings.append(string);
#                 print "process strings end"
#                 print "add size:" + str(len(module["strings"]))
#     print "------------------------------------------------------------------"
#
# def preprocessSimpleTrigger():
#     '''
#         预处理简单触发器模块
#     :return:
#     '''
#     for module in modules:
#         if checkDependentOn(module):
#             if module.__contains__("simple_triggers"):
#                 print "module：\t" + module["name"]
#                 print "------------------------------------------------------------------"
#                 print "process simple_triggers"
#                 print "before size:" + str(len(simple_triggers))
#                 for object in module["simple_triggers"]:
#                     print "add a trigger"
#                     simple_triggers.append(object)
#                 print "process simple_triggers end"
#                 print "after size:" + str(len(simple_triggers))
#     print "------------------------------------------------------------------"
#
# def preprocessTrigger():
#     '''
#         预处理简单触发器模块
#     :return:
#     '''
#     for module in modules:
#         if checkDependentOn(module):
#             if module.__contains__("triggers"):
#                 print "module：\t" + module["name"]
#                 print "------------------------------------------------------------------"
#                 print "process triggers"
#                 print "before size:" + str(len(triggers))
#                 for object in module["triggers"]:
#                     print "add a trigger"
#                     simple_triggers.append(object)
#                 print "process triggers end"
#                 print "after size:" + str(len(triggers))
#     print "------------------------------------------------------------------"
#
# def preprocessScripts():
#     '''
#         预处理地图触发器模块
#     :return:
#     '''
#     for module in modules:
#         if checkDependentOn(module):
#             print "module：\t" + module["name"]
#             print "------------------------------------------------------------------"
#             print "process scripts"
#             print "before size:" + str(len(scripts))
#             for object in module["scripts"]:
#                 print "add a script ：" + object[0]
#                 scripts.append(object)
#             print "process scripts end"
#             print "after size:" + str(len(scripts))
#     print "------------------------------------------------------------------"
#
# def preprocessDialogs():
#     '''
#         预处理对话模块
#     :return:
#     '''
#     for module in modules:
#         if checkDependentOn(module):
#             if module.__contains__("dialogs"):
#                 print "module：\t" + module["name"]
#                 print "------------------------------------------------------------------"
#                 print "process dialogs"
#                 print "before size:" + str(len(dialogs))
#                 for object in module["dialogs"]:
#                     print "add a dialog:" + object[1]+":"+object[4]+"\t'"+object[3]+"'"
#                     dialogs.append(object)
#                 print "process dialogs end"
#                 print "after size:" + str(len(dialogs))
#     print "------------------------------------------------------------------"
#
#
# def preprocessMissionTemplates():
#     '''
#         预处理战场模板模块
#     :return:
#     '''
#     for module in modules:
#         if checkDependentOn(module):
#             if module.__contains__("mission_templates"):
#                 print "module：\t" + module["name"]
#                 print "------------------------------------------------------------------"
#                 print "process mission_templates"
#                 for (key,object) in module["mission_templates"].items():
#                     ## mission_templates
#                     if key == "create_mission_templates" and len(object) != 0:
#                         create_mission_templates = object
#                         print "process create_mission_templates"
#                         addnum = len(mission_templates)
#                         for mission_template in create_mission_templates:
#                             print "add a mission template:" + mission_template[0]
#                             mission_templates.append(mission_template)
#                         print "add mission template nums: " + str(len(mission_templates) - addnum)
#                     ## spawns
#                     elif key == "add_mission_template_spawns" and len(object) != 0:
#                         add_mission_template_spawns = object;
#                         print "process add_mission_template_spawns"
#                         for (mts_name,spawns) in add_mission_template_spawns.items():
#                             for mission_template in mission_templates:
#                                 if mts_name == mission_template[0]:
#                                     if len(spawns) != 0:
#                                         addnum = len(mission_template[4])
#                                         for spawn in spawns:
#                                             print "in mission template ["+ mts_name +"] add a spawn"
#                                             mission_template[4].append(spawn)
#                                         print "add mission template spawn nums: " + str(len(mission_template[4]) - addnum)
#                     ## triggers
#                     elif key == "add_mission_template_triggers" and len(object) != 0:
#                         print "process add_mission_template_triggers"
#                         add_mission_template_triggers = object
#                         for (mts_name,trgs) in add_mission_template_triggers.items():
#                             for mission_template in mission_templates:
#                                 if mts_name == mission_template[0]:
#                                     if len(trgs) != 0:
#                                         addnum = len(mission_template[5])
#                                         for trg in trgs:
#                                             print "in mission template ["+ mts_name +"] add a trigger"
#                                             mission_template[5].append(trg)
#                                         print "add mission template trigger nums: " + str(len(mission_template[5]) -addnum)
#                     # else:
#                     #     print "Error in mission_templates not key: " + key
#                 print "process mission_templates end"
#     print "------------------------------------------------------------------"
#
#
# def preprocessInternational():
#     '''
#         处理汉化功能
#         将汉化信息写入到导出目录的languages对应的汉化文件夹中的文件里
#     :return:
#     '''
#     for module in modules:
#         if checkDependentOn(module):
#             if module.__contains__("internationals"):
#                 for (key,fileInfo) in module.items():
#                     if "internationals" == key:
#                         for (fold,files) in fileInfo.items():
#                             csvPath = export_dir + "languages/" + fold + "/"
#                             if not os.path.exists(csvPath):
#                                 print "Error path not exists :" + csvPath
#                                 continue
#                             for (filename,infos) in files.items():
#                                 csvFile = csvPath + filename + ".csv"
#                                 print "process file :" + csvFile
#                                 for str in infos:
#                                     replaceIfExists(csvFile,str)
#                                 print "process file over:" + csvFile
#
# '''
#     检测内容在文件数据中是否已经存在
# '''
# def replaceIfExists(csvFile,str):
#     ## 读取文件内容
#     file = open(csvFile,"r")
#     lines = file.readlines()
#     file.close()
#
#     info = str + " \n"
#     isReplace = False
#
#     index = 0;
#     while(index < len(lines)):
#         line = lines[index]
#         ## 删除指定key的行
#         if len(line) != 0 and line.split("|")[0].strip() == str.split("|")[0].strip():
#             lines[index] = info
#             isReplace = True
#             print "replace: " + info
#         index += 1
#     if not isReplace:
#         lines.append(info)
#         print "write: " + info
#     ## 定入文件中
#     file = open(csvFile,"w")
#     file.writelines(lines)
#     file.close()
#
#
# def preprocessGameMenus():
#     '''
#         处理游戏中的菜单
#     :return:
#     '''
#     for module in modules:
#         if checkDependentOn(module):
#             if module.__contains__("game_menus"):
#                 for (key,infos) in module["game_menus"].items():
#                     if "create_game_menus" == key:
#                         game_menus.extend(infos)
#                         print "add game menu num: " + str(len(infos))
#                 for (key,infos) in module["game_menus"].items():
#                     if "add_game_menu_options" == key:
#                         for (parent,menus) in infos.items():
#                             for (type,options) in menus.items():
#                                 index = findGameMenuByMenuId(parent)
#                                 system_options = game_menus[index][5]
#                                 for (optionId,opts) in options.items():
#                                     optionIdIndex = findGameMenuOptionByOptionId(system_options, optionId)
#                                     for option in opts:
#                                         if "after" == type:
#                                             print "add option["+ option[0] +"] after "+ parent +"'s[" + optionId + "] option"
#                                             game_menus[index][5].insert(optionIdIndex + 1, option)
#                                         elif "before" == type:
#                                             print "add option[" + option[0] + "] before "+ parent+"'s[" + optionId + "] option"
#                                             game_menus[index][5].insert(optionIdIndex, option)
#                                         elif "replace" == type:
#                                             print "replace option[" + option[0] + "(deleted)] after "+ parent +"' [" + optionId + "] option"
#                                             del game_menus[index][5][optionIdIndex]
#                                             game_menus[index][5].insert(optionIdIndex, option)
#
#
# def findGameMenuByMenuId(menuId):
#     for index in range(len(game_menus)):
#         if game_menus[index][0] == menuId:
#             return index;
#     raise Exception("Error game menu id: " + menuId)
#
# def findGameMenuOptionByOptionId(options,optionId):
#     for index in range(len(options)):
#         if(options[index][0] == optionId):
#             return index
#     raise Exception("Error game menu option id: " + optionId)
#
#
#
#
#
#
