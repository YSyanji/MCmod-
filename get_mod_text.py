import requests
from bs4 import BeautifulSoup
import re

mod_text_l = {
    "name1": '',
    "name2": '',
    "img": '',
    "way": {},
    "vision":{},
}

def if_is_url_mod(u):
    if not re.match(r'^https://www.mcmod.cn',u):
        url = 'https://www.mcmod.cn'+u
        return url
    else:
        return u

def get_mod_text(url_1):
    url = url_1
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }
    res = requests.get(url=url, headers=headers).text  # 获取网页
    soup = BeautifulSoup(res, 'html.parser')  # 转变格式
    get_argument(soup)  # 将转变好的传给获取信息函数
    return mod_text_l   #返回获取的信息

def save_img(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }
    img = requests.get(headers=headers, url=url).content
    with open('get/mod_text_img/1.jpg', 'wb') as f:
        f.write(img)
        f.close()

def if_is_url(u):     #补全网址
    if not re.match(r'^https:',u):
        url = 'https:'+u
        return url
    else:
        return u


def get_img_mod_text(html):   #  图片获取
    # __________________________________获取图片
    ico = html.find('div', class_="class-cover-image")  # 寻找含有指定class的div
    img_src = if_is_url(str(ico.find('img')['src']))  # 补全https
    print(img_src)
    mod_text_l.update({  # 保存到列表
        "img": img_src
    })
    print(mod_text_l)
    save_img(img_src)  # 保存图片



def get_title_name_mod_text(html):    #mod名字获取
    # _________标题
    tilite_mod = html.find('div', "class-title")
    t_E = ''
    if tilite_mod.find('h4') == None:
        print('副标为空')
    else:
        t_E = str(tilite_mod.find('h4').text.encode('utf-8'), 'utf-8')
    t_C = str(tilite_mod.find('h3').text.encode('utf-8'), 'utf-8')
    mod_text_l.update({
        'name1': t_C,
        'name2': t_E
    })
    print(t_C, t_E)

def get_platform_url_mod_text(html): #获取相关平台
    ul = html.find('ul', class_="common-link-icon-frame common-link-icon-frame-style-3")
    n = 0
    for u in ul.find_all('li'):
        url_way = if_is_url(str(u.find('a')['href']))
        name_way = u.find('span')['title']
        mod_text_l['way'].update({  # 保存到列表
            "way{}".format(n): {
                'url': url_way,
                'name': name_way
            }
        })
        n += 1
def get_version_mod_text(html):  #获取支持版本
    vasion = html.find('li', class_="col-lg-12 mcver")
    v_1 = vasion.find("ul")
    n = 1
    for v in v_1.find_all('ul'):  # 获取支持版本
        name_ver = str(v.find('li').text.encode('utf-8'), 'utf-8')  # 启动方式获取
        y = 0
        mod_text_l['vision'].update({  # 保存到列表
            "{}".format(name_ver): {}
        })
        for x in v_1.find_all('li', class_='text-danger'):  # 详细版本列表
            text_ver = str(x.find('a').text.encode('utf-8'), 'utf-8')
            mod_text_l['vision']['{}'.format(name_ver)].update({
                'ver{}'.format(y): text_ver,
            })
            y += 1
            print('114514', text_ver)
        n += 1
        print('5525', name_ver)

def get_argument(html):  #获取类型,版本,运行,服务器客户端支持,

    #get_img_mod_text(html)  #图片
    #get_title_name_mod_text(html)   #mod名字
    #get_platform_url_mod_text(html)  #相关平台
    #get_version_mod_text(html)   #获取支持版本
    # __________________________________ mod关系 relationship
    mod_relationship = html.find('ul', class_="class-relation-list")
    print(mod_relationship)
    quantity = 0
    for i in mod_relationship.find_all('fieldset'):
        print('1')#获取版本相关
        title_version = str(i.find('legend').text.encode('utf-8'),'utf-8')  #相关版本的名字
        for t in i.find_all('li',class_='col-lg-12 relation'):   #获取详情
            is_ld ='1'
            try:
                is_ld = t.find('i',class_="fas fa-vector-square")  #依赖
                if is_ld != '1':
                    depend = '依赖'
            except:
                print('无依赖')
            try:
                is_ld = t.find('i',class_="fas fa-sitemap")  #前置
                if is_ld != '1':
                    depend = '前置'
            except:
                print('无前置')
            try:
                is_ld = t.find('i',class_="fas fa-bezier-curve")  #联动
                if is_ld != '1':
                    depend = '联动'
            except:
                print('无联动')
            print(depend,'状态')
            name_4 = str(t.find('a').text) #相关mod名字
            url_2 = if_is_url_mod(str(t.find('a')['href']))
            print(url_2,'相关mod链接',name_4)
        quantity+=1
    print(mod_text_l)
var = get_mod_text('https://www.mcmod.cn/class/12113.html')
print(var)
