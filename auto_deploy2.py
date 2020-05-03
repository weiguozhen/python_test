#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time      : 2020/5/3 2:42 下午
# Software  : PyCharm
from time import sleep

import paramiko
ssh = paramiko.SSHClient()
#信任机器
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.20.10.4',22,'wgz','wgz123')
sftp = ssh.open_sftp()

#删除原来的文件
ssh.exec_command('rm -rf restapi-teach restapi-teach.zip')

sleep(1)
#上传压缩包到远程服务器
# source要传的文件，target目录
source = '/Users/wgz/gitup/restapi-teach.zip'
target = '/home/wgz/restapi-teach.zip'
sftp.put(source,target)

# ssh.exec_command()
#解压缩
targetdir = '/home/wgz/restapi-teach'
cmd = f'unzip -d {targetdir} restapi-teach.zip'
ssh.exec_command(cmd)
sleep(2)
#进入项目目录执行运行脚本
cmd2 = 'cd restapi-teach && sh run.sh'
ssh.exec_command(cmd2)
# mag = stdout.read()
# errors = stderr.read()
# print(mag+errors)
#执行自动化测试

sftp.close()
ssh.close()