# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:15:52 2018

@author: Administrator



"""
import urllib.request as r#导入联网工具包，名为为r 

for page in range(1,101):
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E4%BA%91%E5%8D%97&ajax=true&s='+str((page-1)*44)
    data=r.urlopen(url).read().decode('utf-8','ignore')
    file=open('D:\\RT\\新建文件夹\\云南裙子.txt','a',encoding='utf-8') 
    file.write(data+'\n')
    print('第'+str(page)+'条')
    file.close()


import urllib.request as r#导入联网工具包，名为为r 
for page in range(1,101):
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E4%BA%91%E5%8D%97&ajax=true&s='+str((page-1)*44)
    data=r.urlopen(url).read().decode('gbk','ignore')
    file=open('D:\\RT\\新建文件夹\\云南裙子.csv','a',encoding='gbk') 
    file.write(data+'\n')
    print('第'+str(page)+'条')
    file.close()

import urllib.request as r
data=r.urlopen('https://s.taobao.com/search?q=%E9%9B%B6%E9%A3%9F&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true').read().decode('utf-8','ignore')
import json
data=json.loads(data)
def information(m): 
#商品：data字典--》mods字典--》itemlist字典--》data字典--》auctions列表--》0 index--》title变量
    print('商品：'+data['mods']['itemlist']['data']['auctions'][m]['title'])
#价格：data字典--》mods字典--》itemlist字典--》data字典--》auctions列表--》0 index--》view_price变量
    print('价格：'+data['mods']['itemlist']['data']['auctions'][m]['view_price'])
#邮费：data字典--》mods字典--》itemlist字典--》data字典--》auctions列表--》0 index--》view_fee变量
    print('邮费：'+data['mods']['itemlist']['data']['auctions'][m]['view_fee'])
#销量：data字典--》mods字典--》itemlist字典--》data字典--》auctions列表--》0 index--》view_sales变量
    print('销量：'+data['mods']['itemlist']['data']['auctions'][m]['view_sales'])
information(0) 
information(1)
information(2)
information(3)
print('+'*30)

ls=[]
def price():
    for i in range(0,36):
        m=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
        ls.append(m)
    return ls
price()
n=sorted(ls)
print('商品价格从高到低为')
x=list(reversed(n))
print(x)

def free():
    for i in range(0,36):
        if float (data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0.00:
            print('第{}件商品包邮'.format(i+1))
            print('商品名称为'+data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
            print('商品的售价为'+data['mods']['itemlist']['data']['auctions'][i]['view_price'])
            print('销量为'+data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
            print('店名为'+data['mods']['itemlist']['data']['auctions'][i]['nick'])
            print(' ')
            print(str('-')*20) 
free()
