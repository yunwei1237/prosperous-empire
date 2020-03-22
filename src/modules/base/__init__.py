# # -*- coding: utf-8 -*-
#
#
# ## 本文件不能删除
#
#
#
# # str = u"中华人民共和国"
# #
# # print " ".join(list(u"中华人民共和国"))
#
#
#
#
# first = [u"陈",u"李",u"黄",u"张",u"梁",u"林",u"刘",u"吴",u"罗",u"杨"]
# second = [u"宛",u"丘",u"形",u"采",u"用",u"其",u"利",u"器",u"用",u"以",u"木",u"德"]
#
#
# def parseFirstStrings(chars):
#     result = []
#     for index in range(len(chars)):
#         result.append(("first_name_{}".format(index),chars[index]))
#     result.append(("first_name_end","end"))
#     return result
#
# def parseSecondStrings(chars):
#     result = []
#     for index in range(len(chars)):
#         result.append(("second_name_{}".format(index),chars[index]))
#     result.append(("second_name_end","end"))
#     return result
#
# def parseCnsFirstStrings(chars):
#     result = []
#     for index in range(len(chars)):
#         result.append("str_first_name_{}|{}".format(index," ".join(list(chars[index]))))
#     return result
#
# def parseCnsSecondStrings(chars):
#     result = []
#     for index in range(len(chars)):
#         result.append("str_second_name_{}|{}".format(index," ".join(list(chars[index]))))
#     return result