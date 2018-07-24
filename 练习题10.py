# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:24:40 2018
作业
1、获取2300所学校的编号
2、获取142000数据，每个组有三个城市数据，后面组装在一起
3获取所有城市的编号
4、将所有数据使用spark统计

@author: Administrator
"""

ls=open('D:\\RT\\新建文件夹\\all_school.txt',encoding='utf-8').readlines()
schoolls=[]

for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
print("学校编号：",schoolls)


ls1=open('D:\\RT\\新建文件夹\\XML高考派城市.txt',encoding='gbk').readlines()
cityidls=[]
for line in ls1:
    text=line.split(", ")
    if len(text)==2:
       print(text[1].split(")")[1][2:4],text[1].split(")")[0])
    
    
 
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'}

f=open('D:\\RT\\新建文件夹\\全国高校贵州文科招生.txt','a',encoding='utf-8')
for schoolId in schoolls:
    for city in range(50,53):
        for type in (1,2):
            req=r.Request(url,data='id={}&type={}&city={}&state=1'.format(schoolId,type,city).encode(),headers=headers)
            try:
                data=r.urlopen(req).read().decode('utf-8','ignore')
                while '<!DOCTYPE HTML>' in data:
                    data=r.urlopen(req).read().decode('utf-8','ignore')
                f.write(data+'\n')
                print('success')
            except Exception as err:
                print('have an error')
f.close()#关闭保存程序  




f=open('D:\\RT\\新建文件夹\\贵州招生.txt',encoding='gbk').readlines()
schoolls=[]
data=[]
for line in f:
    schoolls.append(line.split('(')[1].split(',')[0])
    data.append(line.split(',')[1].split(')')[0])
    print(schoolls)
    print(data)
    
    

