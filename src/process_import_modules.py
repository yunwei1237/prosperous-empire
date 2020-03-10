# -*- coding: utf-8 -*-

from import_modules import modules
from module_scripts import scripts
from module_simple_triggers import simple_triggers
from module_strings import strings

# print "Import modules ..."
# print "=================================================================="
# for module in modules:
#     print "module：\t" + module["name"]
#     print "------------------------------------------------------------------"
#     print "process strings"
#     print "size:" + str(len(strings))
#     for string in module["strings"]:
#         for (k,v) in  string.items():
#             print "add string : (" + k + "," + v + ")"
#             strings.append((k, v));
#     print "process strings end"
#     print "contains:" + str(strings.__contains__("s5_s_patrol_party"));
#
#     print "size:"+str(len(strings))
# print "=================================================================="

def preprocessAll():
    preprocessString()
    preprocessMapTrigger()
    preprocessScripts()


def preprocessString():
    '''
        预处理字符串模块
    :return:
    '''
    print "=================================================================="
    for module in modules:
        print "module：\t" + module["name"]
        print "------------------------------------------------------------------"
        print "process strings"
        print "before size:" + str(len(strings))
        for object in module["strings"]:
            for (k, v) in object.items():
                print "add string : (" + k + "," + v + ")"
                strings.append((k, v));
        print "process strings end"
        print "after size:" + str(len(strings))
    print "=================================================================="

def preprocessMapTrigger():
    '''
        预处理地图触发器模块
    :return:
    '''
    print "=================================================================="
    for module in modules:
        print "module：\t" + module["name"]
        print "------------------------------------------------------------------"
        print "process map_trigger"
        print "before size:" + str(len(simple_triggers))
        for object in module["map_trigger"]:
            print "add a map trigger"
            simple_triggers.append(object)
        print "process map_trigger end"
        print "after size:" + str(len(simple_triggers))
    print "=================================================================="

def preprocessScripts():
    '''
        预处理地图触发器模块
    :return:
    '''
    print "=================================================================="
    for module in modules:
        print "module：\t" + module["name"]
        print "------------------------------------------------------------------"
        print "process scripts"
        print "before size:" + str(len(scripts))
        for object in module["scripts"]:
            print "add a script ：" + object[0]
            scripts.append(object)
        print "process scripts end"
        print "after size:" + str(len(scripts))
    print "=================================================================="


## 导入时使用
## preprocessAll()