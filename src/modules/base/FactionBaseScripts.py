# -*- coding: utf-8 -*-

## 包含一些对阵营常用的操作
from header_operations import *
from header_parties import *
from header_skills import skl_trainer
from module_constants import *



## args


factionBaseScripts={
    "name":"FactionBaseScripts",
     "enable":True,
    "scripts":{
        "append":[
            ## 创建部队通用方法
            ("get_num_of_enemy_state",[
                (store_script_param, ":faction_no", 1),
                (assign,":war_num",0),
                (try_for_range,":other_faction_no",kingdoms_begin,kingdoms_end),
                    (neq,":faction_no",":other_faction_no"),
                    (store_relation,":relation",":faction_no",":other_faction_no"),
                    (le,":relation",0),
                    (val_add,":war_num",1),
                (try_end),
                (assign,reg0,":war_num"),
              ]),
        ],
    }
}