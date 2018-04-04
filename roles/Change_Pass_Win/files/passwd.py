#!/usr/bin/python
#coding=utf8

#import tab
from random import choice
import string,re
passwd_seed = string.digits + string.ascii_lowercase + string.ascii_letters

"""function to generate a passwd"""
def get_passwd(passwd_length=30): ####默认值
    passwd = []
    while len(passwd) < passwd_length:
        passwd.append(choice(passwd_seed))
        password=''.join(passwd)
    password=password.replace("'","\\\'")
    password=password.replace('"','\\\"')
    return password
if __name__ == "__main__":
    #content_length = "\033[5;42;3m'length of passwd:'\033[0m" ########密码的长度
    #content_count = "\033[5;44;3m'count of passwd:'\033[0m"   #######生成密码的个数
    #length = int(raw_input('passwd length:'))
   # count = int(raw_input())
    #if length == '':
    #        print get_passwd()
    print get_passwd()
    #else:
    #        print get_passwd(length)
