import datetime
import json
import requests
from bs4 import BeautifulSoup
import get.get_img
from get.get_img import img_url_get
type_name = {'资源':8,'世界':9,'群系':10,'结构':35,'生物':11,'能源':12,'存储':13,'物流':14,'道具':15,'安全':6,'红石':16,'食物':17,'模型':18,'关卡':34,'指南':19,'破坏':20,'Meme':22,'中式':25,'日式':26,'西式':27,'恐怖':28,'建材':29,'生存':30,'指令':31,'优化':32,'国创':33,'科技':1,'魔法':2,'冒险':3,'农业':4,'装饰':5,'实用':23,'辅助':24,'魔改':21,'LIB':7}
way_name = {'Forge':1,'Fabric':2,'Quilt':11,'NeoForge':13,'Rift':3,'LiteLoader':4,'数据包':5,'行为包':8,'命令方块':6,'文件覆盖':7}
def save_html(name,text_html,type):
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    name = '{}-html-{}.{}'.format(name,time,type)
    print(name)
    f = open('./mod_list/{}'.format(name),'w+',encoding = 'utf-8')
    f.write(str(text_html))
    f.close()

def get_html(text):
    mod_text = {}
    mcver=text['version']
    category=type_name[str(text['type'])]
    api_v=way_name[str(text['way'])]
    page=text['page']
    url = 'https://www.mcmod.cn/modlist.html'
    print(url)
    data = {
        "mcver":mcver,   #版本
        "category":category,    #类型
        "api":api_v, #运行方式
        "page":page  #页数
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }
    html = requests.get(headers=headers, url=url,params=data).text
    soup = BeautifulSoup(html,'html.parser')
    b=0
    for div in soup.find_all('div',class_='modlist-block'):
        print(b)
        name_m = str(div.find('p').text.encode('utf-8'),'utf-8')
        url_m ='https://www.mcmod.cn' + str(div.find('a')['href'].encode('utf-8'),'utf-8')
        img_m = str(div.find('img')['src'].encode('utf-8'), 'utf-8')
        print(str(div.find('p').text.encode('utf-8'),'utf-8'),'name')
        print(str(div.find('a')['href'].encode('utf-8'),'utf-8'),'url')
        print(str(div.find('img')['src'].encode('utf-8'), 'utf-8'), 'img')
        mod_text.update({
            "mod{}".format(b):{
                'name':name_m,
                'url':url_m,
                'img':img_m
            }
        })
        print(mod_text['mod{}'.format(b)])
        b += 1
        if b == 32 :
            break
            break
    #save_html('YS',mod_text,'json')
    #img_url_get(mod_text)
    return mod_text

