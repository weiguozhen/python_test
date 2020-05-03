#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time      : 2020/5/3 2:19 下午
# Software  : PyCharm
import zipfile
import os
def unzip():
    zfile = zipfile.ZipFile('archive.zip','r')
    for filename in zfile.namelist():
        data = zfile.read(filename)
        file = open(filename,'w+b')
        file.write(data)
        file.close()

def zipdir(sourcedir):
    targetdir = sourcedir + '.zip'
    f = zipfile.ZipFile(targetdir,'w',zipfile.ZIP_DEFLATED)
    for dirpath,dirnames,filenames in os.walk(sourcedir):
        print(f'{dirpath}--{dirnames}--{filenames}')
        #这段代码很重要不replace从根目录开始复制
        fpath = dirpath.replace(sourcedir,'')
        fpath = fpath and fpath + os.sep or ''
        # 实现当前文件夹以及所有文件的压缩
        for filename in filenames:
            f.write(os.path.join(dirpath,filename),fpath+filename)
    f.close()
if __name__ == '__main__':
    zipdir('/Users/wgz/gitup/restapi-teach')