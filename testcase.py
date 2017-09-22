import json

import requests
import password_encryption
import yaml


def login():  # 使用加密参数登录
    login_P = yaml.load(open('config/login.yaml'))
    passwword_encryption = password_encryption.Login_Passwword_Encryption(login_P['phonenumber'],
                                                                          login_P['password']).encryption()
    login_P['login']['param']['data'] = passwword_encryption
    re = requests.post(login_P['login']['url'], data=login_P['login']['param'])
    return re


def praise():
    param = yaml.load(open('config/praise.yaml'))


def CallProcTest(procname, parameters):
    # cur.callproc('SpilePage',('Admin','1=1',1,20))
    # 是否有参数
    if len(parameters) > 0:
        procname += '('
        for i in range(len(parameters)):
            procname += '%s,'
        procname = procname[0:len(procname) - 1] + ')'

    # 拼装字符串
    procname = 'call ' + procname
    return procname


print(CallProcTest('SpilePage', ('Dictionary', '1=1', 1, 10)))

