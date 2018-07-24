## -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:55:29 2018

@author: Administrator
"""
1、函数优化题目        
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
def msg( c):
    print('第a天的温度信息为：')
    print(str(data['list'][c]['weather'][c]['description']))
msg(2)
msg(10)
msg(18)
msg(26)
msg(34)
    

      
    
def chart(b):
    char=str('-')*int(data['list'][b]['main']['temp'])
    return char
print('五天内折线图为：')
print('第一天'+chart(2))
print('第二天'+chart(10))
print('第三天'+chart(18))
print('第四天'+chart(26))
print('第五天'+chart(34))

2、商品信息题目
url1='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r
data=r.urlopen(url1).read().decode('utf-8','ignore')

import  json 
data=json.loads(data)
##6.1
def item(a):
    print(data['mods']['itemlist']['data']['auctions'][a]['title'])
    print(data['mods']['itemlist']['data']['auctions'][a]['view_price'])
    print(data['mods']['itemlist']['data']['auctions'][a]['item_loc'])
    print(data['mods']['itemlist']['data']['auctions'][a]['view_sales'])

item(0)
item(1)
item(2)
item(3)
##6.2
def show():
 for b in range(0,36):
        print('商品名称'+str(data['mods']['itemlist']['data']['auctions'][b]['title']))
        print('商品价格'+str(data['mods']['itemlist']['data']['auctions'][b]['view_price']))
        print('商品产地'+str(data['mods']['itemlist']['data']['auctions'][b]['item_loc']))
        print('商品销量'+str(data['mods']['itemlist']['data']['auctions'][b]['view_sales']))
        if((b+1)%4==0):
          print('/'*20)
show()

##6.3
price_list=[]
def price():
    for b in range(0,36):  
        y=data['mods']['itemlist']['data']['auctions'][b]['view_price']
        price_list.append(y)
    return price_list
price()
c=sorted(price_list)
print('价格从低到高排序')
print(c)
d=list(reversed(c))
print('商品按价格高低销量排序为：')
print(d)
##6.4
def free():
    for b in range(0,36):
        if float(data['mods']['itemlist']['data']['auctions'][b]['view_fee'])==0.00:
           print('第{}件商品包邮'.format(b+1))
free()
##6.5

3、天气预测题目
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r  #导入联网工具包，名为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json  #将字符串转换成字典
data=json.loads(data)

def day(a,b): 
    print('day'+str(a)+'的天气情况：')
    print('温度:'+str(data['list'][b]['main']['temp'])+' '+'情况:'+str(data['list'][2+b*8]['weather'][0]['main']))
    temp=data['list'][b]['main']['temp']
    main=data['list'][2+b*8]['weather'][0]['main']
    if temp>=30:
        print('出门记得带伞，以免晒伤')
    elif temp>=20 and main=='Rain':
        print('小心感冒')
    elif temp>=20:
        print('适合徒步旅行 ')
    elif main=='Rain':
        print('天冷记得添衣')
    else:
        print('保护好自己')
day(1,0)
day(2,1)
day(3,2)
day(4,3)
day(5,4)

 