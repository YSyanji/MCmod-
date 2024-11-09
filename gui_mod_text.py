import os
from tkinter import ttk, Label
import tkinter as tk
from  PIL import Image,ImageTk
import webbrowser
from turtledemo.penrose import start
def open_url(index):  #打开链接
    print(index)
    url_1 = str(index['url'])
    name_url_ = str(index['name'])
    webbrowser.open_new(url_1)
from get_mod_text import get_mod_text
def op_top_win():
    url = open('get/url_d.text', "r", encoding='utf-8').read()
    print(url, '1')
    name = str(open('get/url_name.text', "r", encoding='utf-8').read())
    mod_text_w = tk.Toplevel()
    mod_text_w.title('{}'.format(name))
    mod_text_w.geometry("1300x800")  # 大小
    mod_text_w.resizable(0, 0)
    mod_text_w.iconbitmap('./image/icon_16x16.ico')  # 图标
    mod_text_w.attributes("-alpha", 0.9)  # 窗口透明度 -alpha
    mod_text_w.attributes("-topmost", False)  # 窗口置顶 -topmost
    mod_text_w.attributes('-transparentcolor', "grey")  # 背景颜色 -transparentcolor
    mod_text_w.attributes('-toolwindow', 1)


# -----------------------------------------------------------------mod图片

    modtext = get_mod_text(url)
    print(modtext)
    print('114',modtext['name2'],'114')
    img = Image.open('./get/mod_text_img/1.jpg')
    img = img.resize((200, 120))
    photo = ImageTk.PhotoImage(img)
    ico_img_Fr = ttk.LabelFrame(mod_text_w,borderwidth=2,relief=tk.RAISED)
    ico_img_Fr.place(x=5, y=5)
    ico_img = ttk.Label(ico_img_Fr,image= photo,width=200)
    ico_img.pack()

#------------------------------------------------------------------mod名字

    name_Fr = ttk.LabelFrame(mod_text_w,borderwidth=2,width=100)
    name_Fr.place(x=225,y=5)
    name_text_1 = tk.Label(name_Fr, text=modtext['name1'])
    name_text_1.grid(row=0)
    name_text_2 = tk.Label(name_Fr, text=modtext['name2'])
    name_text_2.grid(row=1)

# ------------------------------------------------------------------mod相关网页
    way_Fr = ttk.LabelFrame(mod_text_w,borderwidth=2)
    way_Fr.place(x=225,y=80)
    url_way = tk.Label(way_Fr,text='相关链接')
    url_way.grid(row=0)
    for i in range(len(modtext['way'])) :
        print(i)
        id_list ={
            "name":modtext["way"]["way{}".format(i)]["name"],
            "url":modtext["way"]["way{}".format(i)]["url"]
        }
        exec(f'way_Fr_{i} = ttk.LabelFrame(way_Fr,borderwidth=2)')
        exec(f'way_Fr_{i}.grid(row=1,column={i})')
        exec(f'way{i}=tk.Label(way_Fr_{i},text=modtext["way"]["way{i}"]["name"],width=10) ')
        exec(f'way{i}.grid(row=0)')
        exec(f'way{i}.bind("<Button-1>",lambda event, index=id_list,:open_url(index))')
    mod_text_w.mainloop()




