# -*- coding: utf-8 -*-


## 日志处理功能

def log(type,text):
    print "{} - {}".format(type,text)

def debug(text):
    log("DEBUG".ljust(5),text)
def info(text):
    log("INFO".ljust(5),text)
def warn(text):
    log("WARN".ljust(5),text+"\n---------------------------------------------------------------------------")
def error(text):
    log("ERROR".ljust(5),text+"\n===========================================================================")
def fatal(text):
    log("FATAL".ljust(5),text+"\n==========================================================================="*2)