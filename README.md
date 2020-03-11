# 繁荣帝国
prosperous-empire

## 功能列表：
### module功能
每一个功能可以单独写在一个py文件中，包括 string,script,trigger,constans等待 [参看巡逻队功能](src/modules/PatrolParty.py)
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
##### strings
一个字典（dict）,key代表字符串id,val代表字符串内容，在编译时，将字符串写入到module_strings.py中的strings的list中。将字符串写入到字典中，和写入module_strings.py中的strings集合中是一样的。
##### simple_triggers
一个列表，列表中每一个项都是一个简单触发器，也就是simple_trigger。编译前会自动加入到module_simple_trigger.py文件中的simple_triggers。
##### triggers
一个列表，列表中每一个项都是一个复杂触发器，也就是trigger。编译前会自动加入到module_trigger.py文件中的triggers。
##### scripts
一个列表，列表中每一个项都是一个脚本，也就是script。编译前会自动加入到module_scripts.py文件中的scripts。
##### dialogs
一个列表，列表中每一个项都是一句对话，也就是dialog。编译前会自动加入到module_dialogs.py文件中的dialogs。