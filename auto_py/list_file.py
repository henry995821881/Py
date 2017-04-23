#!/usr/bin/python
#用Python写一个列举当前目录以及所有子目录下的文件，并打印出绝对路径
import os
for root,dirs,files in os.walk('/tmp'):
    for name in files:
        print (os.path.join(root,name))
