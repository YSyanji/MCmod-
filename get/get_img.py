import re

import requests
import PIL
def img_url_get(text_url):
    for n in range(len(text_url)):
        get_img_(text_url['mod{}'.format(n)]['img'],n)

def if_is_url(u):
    if not re.match(r'^https:',u):
        url = 'https:'+u
        return url
    else:
        return u
def get_img_(url,p):

    url_1 = if_is_url(url)
    print(url_1)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }
    img = requests.get(headers=headers, url=url_1).content
    with open('get/img/{}.jpg'.format(p),'wb') as f:
        f.write(img)
        f.close()
