# -*- coding: utf-8 -*-


## 用于测试的文件
from modules.HeroCollection_header import *

aaa = mergeList(repeatRandomTroop(50,"hero_{}"),repeatArcher1(1,"hero_end"))

for index in range(len(aaa)-1,-1,-1):
    print index