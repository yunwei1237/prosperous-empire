# 繁荣帝国
prosperous-empire



## 优势

- 几乎零耦合
- 一键启用和禁用
- 模块功能
- 功能整合简单
- 测试简单
- 代码统一规范

## 功能列表
### 模块(module)功能
每一个功能可以单独写在一个py文件中，包括 string,script,trigger,constans等待 [参看巡逻队功能](resources/oldmodule/PatrolParty.py)
创建一个功能只需要创建一个py文件，并在该文件中定义一个dict类型的变量，字典中每一个key代表一个数据集合，key不能随便定义，请参看key的语法。

#### 使用步骤
- 在modules（任何文件夹都可以）文件夹中创建一个py文件
- 在py文件中定义一个dict(字典)，编写功能时请参看key语法。
- 功能写完后，将dict变量添加到import_modules.py文件中的modules集合中
#### key的语法：
##### name
一个字符串，只是用于区别不同的功能，全局必须唯一
##### enable
一个布尔值，该module在编译时是否参与，不参与：False 参与：True，默认为True
##### dependentOn
一个列表，该module在编写时依赖了别的module时，就要将依赖的module名称保存到该列表，系统会在编译时提示依赖的module是否开启了，或者是否存在。如果使用了系统自带的数据（脚本，字符串，触发器等等），不必填写。

##### 模块项内容

对于本系统来说，每一个模块项都面临者增加（append），删除（delete），插入(insert)，替换(replace)功能。

例如：在module_strings.py中添加一个字符串项;重写module_scripts.py中的game_get_troop_wage功能;为module_mission_templates.py文件的visit_town_castle战场控制器添加一个触发器;为了测试脚本在module_game_menus.py中的start_game_0菜单的continue选项后添加一个新的选项等等。

我把这些功能全部都归结为：增加，删除，插入，替换，子操作(children)五个操作。

在简介这些功能之前，我们得先介绍一个新的概念，sign(信号，其实可以翻译成选择器)。

##### sign

信号（选择器）：适合于删除，插入，替换功能（增加不需要，直接添加到数据末尾就行了，不需要选择器）

信号有三种形式：

1.id形式

也叫简单选择器，使用数据的id作为选择器，如，（玩家的id：player，斯瓦迪亚阵营的id：kingdom_1），适用于选择数据。

2.下标形式

注：下标从0开始！！！

也叫下标选择器，使用#数字的方式作为选择器，如，（troops兵种集合的第一个数据：#0，factions阵营集合的第10个数据#11），适用于数据中的某一列。

3.复杂形式

复杂选择器主要分成两部分，

例如（对话）：

```
[anyone,"member_castellan_pretalk", [], "Anything else?", "member_castellan_talk",[]],
```

第一部分：是选择器，如：**member_castellan_pretalk:member_castellan_talk**，注：符号之间以冒号隔开（英文符号）

第二部分：是下标选择器，如：**[1,4]**，注：符号外使用方括号，符号之间使用逗号隔开（英文符号）

完整格式：member_castellan_pretalk:member_castellan_talk:[1,4]

选择器的格式的含义是，从数据中的1下标和4下标中选择数据，拼成一个新的字符串，与member_castellan_pretalk:member_castellan_talk作对比，如果相同就代表选择到，如果不相等，代表没有选择任何数据。

复杂选择器适用于没有id的数据行，从数据行中选择n（逻辑上无限）个数据，组成类似id的符号。以便能够在数据集合中准确定位。

了解了sign选择器以后，我们就可以学习操作命令了

##### append

append命令对应的数据类型是List，list中保存的数据会追加的数据集合的末尾。

##### delete

delete命令对应的数据类型是List,list中保存的是sign集合，也就是选择器集合，只要选择到，就会从数据集合中删除。

##### insert

insert命令其实是两个命令：insertAfter和insertBefore。

insert集合对应的数据类型是list,list中的保存的数据是dict。

**insertAfter**中包含两个参数：

sing:指定一个选择器

data:指定要插入的数据集合

**insertBefore**的参数与insertAfter命令相同，唯一不同的是，insertBefore会将数据添加到选择器所对应数据行的前边，insertAfter会将数据添加到选择器所对应数据行的后边。

##### replace

replace参数与insertBefore命令相同。行为不同的是，将选中的数据删除后，进行添加到选择器所对应数据的前边。

为了更加深入理解命令，以strings添加数据为例：

```python
"strings":{
    "append":[
        ("s5_s_patrol_party","数据会被添加到strings集合的末尾"),
    ],
    "insertBefore":[
        {
            "sign":"empty_string",
            "data":[
                ("test_string_insertBefore","在empty_string后方插入数据"),
                ("test_string_insertBefore2","在empty_string后方插入数据"),
            ]
        }
    ],
    "insertAfter":[
        {
            "sign":"yes",
            "data":[
                ("test_string_insertAfter","在yes前方插入数据"),
            ],
        }
    ],
    "replace": [
        {
            "sign": "empty_string",
            "data": [
                ("empty_string", "替换id为empty_string的数据"),
                ("empty_string2", "会被插入在id为empty_string的后边"),
            ],
        }
    ],
    ## 删除id为color_no_1的字符串，删除strings集合中第109个的字符串
    ## 删除复合选择器（从下标为0和1取值拼成字符串与【no:No.】作对比，如果符合就删除）
    "delete":["color_no_1","#108","no:No.[0,1]"],
},
```

如果想看更多使用方法，请参考：src/modules文件夹下功能文件。