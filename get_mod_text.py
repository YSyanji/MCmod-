import requests
from bs4 import BeautifulSoup
import re

mod_text_l = {
    "name1": '',
    "name2": '',
    "img": '',
    "way": {},
}
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

def get_argument(html):  #获取类型,版本,运行,服务器客户端支持,

    #__________________________________获取图片
    ico = html.find('div', class_="class-cover-image")  # 寻找含有指定class的div
    img_src = if_is_url(str(ico.find('img')['src']))  # 补全https
    print(img_src)
    mod_text_l.update({   #保存到列表
        "img": img_src
    })
    print(mod_text_l)
    save_img(img_src)    #保存图片
    #__________________________________
    # _________标题
    tilite_mod = html.find('div',"class-title")
    t_E=''
    if tilite_mod.find('h4') == None:
        print('副标为空')
    else:
        t_E =str(tilite_mod.find('h4').text.encode('utf-8'), 'utf-8')
    t_C = str(tilite_mod.find('h3').text.encode('utf-8'),'utf-8')
    mod_text_l.update({
        'name1':t_C,
        'name2':t_E
    })
    print(t_C,t_E)
    # _________

    #__________________________________ 平台

    ul = html.find('ul',class_="common-link-icon-frame common-link-icon-frame-style-3")
    n=0
    for u in ul.find_all('li'):
        url_way = if_is_url(str(u.find('a')['href']))
        name_way = u.find('span')['title']
        mod_text_l['way'].update({  # 保存到列表
            "way{}".format(n): {
                'url': url_way,
                'name': name_way
            }
        })
        n+=1
    # __________________________________ 平台


    print(mod_text_l)



def get_mod_text(url_1):
    url = url_1
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }
    res = requests.get(url=url,headers=headers).text   #获取网页
    soup = BeautifulSoup(res, 'html.parser')   #转变格式
    get_argument(soup)    #将转变好的传给获取信息函数




    return mod_text_l
