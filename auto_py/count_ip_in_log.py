#!/usr/bin/python
#!coding=utf-8
#统计出每个IP的访问量有多少？（从日志文件中查找）
list = []
f = file('/tmp/1.log')
str1 = f.readlines() 
f.close() 
for i in str1:
    ip =  i.split()[0]

    list.append(ip) 

list_num = set(list)

for j in list_num: 
    num = list.count(j) 
    print '%s : %s' %(j,num)