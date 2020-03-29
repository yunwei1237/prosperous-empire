# -*- coding: utf-8 -*-
from header_dialogs import *
from module_scripts import *

'''
    显示全部领主的性格

'''

showLordReputationType = {
    "name":"ShowLordReputationType",
    "enable":True,
    "strings":{
        "append":[
            ("lrep_none","none"),
            ("lrep_martial","martial"),
            ("lrep_quarrelsome","quarrelsome"),
            ("lrep_selfrighteous","selfrighteous"),
            ("lrep_cunning","cunning"),
            ("lrep_debauched","debauched"),
            ("lrep_goodnatured","goodnatured"),
            ("lrep_upstanding","upstanding"),
            ("lrep_roguish","roguish"),
            ("lrep_benefactor","benefactor"),
            ("lrep_custodian","custodian"),
        ],
    },
    "simple_triggers":{
        "append":[
            ##
            (2,[
                (try_for_range, ":lord_no", lords_begin, lords_end),

                    (troop_get_slot,":party",":lord_no",slot_troop_leaded_party),
                    (gt,":party",0),

                    (troop_get_slot,":reputation",":lord_no",slot_lord_reputation_type),
                    (store_add,":reputation_str_no","str_lrep_none",":reputation"),
                    (str_store_string,s1,":reputation_str_no"),

                    (party_set_extra_text,":party",s1),
                (try_end),
            ]),
        ],
    },

    "internationals":{
        "cns":{
            "game_strings":[
                "str_lrep_none|无 性 格",
                "str_lrep_martial|军 事 的",
                "str_lrep_quarrelsome|好 战 的",
                "str_lrep_selfrighteous|冷 酷 的",
                "str_lrep_cunning|狡 猾 的",
                "str_lrep_debauched|放 荡 的",
                "str_lrep_goodnatured|和 善 的",
                "str_lrep_upstanding|正 直 的",
                "str_lrep_roguish|流 氓 的",
                "str_lrep_benefactor|善 良 的",
                "str_lrep_custodian|贪 婪 的",
            ]
        }
    }
}