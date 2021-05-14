
from module_scripts import *


###########################
##
## 村庄基础业务
## 1.种植
## 2.畜牧
## 3.矿产
## 4.手工
##
###########################


## 丰收时间（4个月）
villageBasicBusinessUpdateTime = 24 * 30 * 4

## 配置
villageBasicBusinessConfig = {
    ## 每一级统率增加多少生产率
    "perLeadershipProductivityIncrease":0.1,
    ## 每一级统率可以多管理的土地数量
    "perLeadershipManageFieldCount":10,
    ## 每一块土地需要租金
    "perFieldCostAmount":50,
    ## 村庄最大生产能力（0：该村庄无法生产此类商品 100：该村庄非常善于生产此类产品）
    "perVillageMaxProductivityAbility":100,
    ## 工作间
    "workshopList":[
        {
            "name":"plant",
            "nameCns":"种植业",
            "prodectList":[
                {
                    "name":"grain",
                    "nameCns":"小麦",
                    "productionQuantity":100,
                    "itemNo":itm_grain,
                    "overhead":10
                },
                {
                    "name":"raw_grapes",
                    "nameCns":"葡萄",
                    "productionQuantity":30,
                    "itemNo":itm_raw_grapes,
                    "overhead":20
                },
                {
                    "name":"raw_olives",
                    "nameCns":"橄榄",
                    "productionQuantity":35,
                    "itemNo":itm_raw_olives,
                    "overhead":20
                },
                {
                    "name":"apples",
                    "nameCns":"苹果",
                    "productionQuantity":35,
                    "itemNo":itm_apples,
                    "overhead":30
                }
            ]
        },
        {
            "name":"husbandry",
            "nameCns":"畜牧业",
            "prodectList":[
                {
                    "name":"tutorial_saddle_horse",
                    "nameCns":"旅行马",
                    "productionQuantity":10,
                    "itemNo":itm_tutorial_saddle_horse,
                    "overhead":100
                },
                {
                    "name":"steppe_horse",
                    "nameCns":"草原马",
                    "productionQuantity":10,
                    "itemNo":itm_steppe_horse,
                    "overhead":150
                },
            ]
        },
        {
            "name":"minerals",
            "nameCns":"矿产业",
            "prodectList":[
                {
                    "name":"iron",
                    "nameCns":"生铁",
                    "productionQuantity":50,
                    "itemNo":itm_iron,
                    "overhead":200
                },
                {
                    "name":"raw_dyes",
                    "nameCns":"染料",
                    "productionQuantity":100,
                    "itemNo":itm_raw_dyes,
                    "overhead":80
                },
            ]
        },
        {
            "name":"manufacture",
            "nameCns":"制造业",
            "prodectList":[
                {
                    "name":"tools",
                    "nameCns":"工具",
                    "productionQuantity":20,
                    "itemNo":itm_tools,
                    "overhead":100
                },
                {
                    "name":"leatherwork",
                    "nameCns":"皮革制品",
                    "productionQuantity":30,
                    "itemNo":itm_leatherwork,
                    "overhead":180
                },
                {
                    "name":"bread",
                    "nameCns":"面包",
                    "productionQuantity":90,
                    "itemNo":itm_bread,
                    "overhead":30
                },
            ]
        },
    ],
}

## 解析配置
perLeadershipProductivityIncrease = villageBasicBusinessConfig["perLeadershipProductivityIncrease"]
perLeadershipManageFieldCount = villageBasicBusinessConfig["perLeadershipManageFieldCount"]
perFieldCostAmount = villageBasicBusinessConfig["perFieldCostAmount"]
perVillageMaxProductivityAbility = villageBasicBusinessConfig["perVillageMaxProductivityAbility"]
workshopList = villageBasicBusinessConfig["workshopList"]


## 1.初始化数据
## 2.


VillageBasicBusiness = {
    "name":"VillageBasicBusiness",
    "enable":False,
    "triggers":{
        "append":[
            ## 游戏开始时就初始化英雄信息(只更新一次)
            (0,0,ti_once,[],[
                #(display_message,"@heros is init"),
                (call_script,"script_init_village_base_basic_business_data"),
            ]),
        ],
    },
    "simple_triggers":{
        "append":[
            ## 增加税收
            (villageBasicBusinessUpdateTime,[
                (display_message,"@village basic business enable"),
            ]),
        ],
    },

    "scripts":{
        "append":[
            ("init_village_base_basic_business_data",[

            ])
        ]
    }
}