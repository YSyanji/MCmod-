import os
import tkinter as tk
from turtledemo.penrose import start
url= open('get/url_d.text',"r",encoding='utf-8').read()
def op_top_win():
    mod_text_w = tk.Toplevel()
    mod_text_w.title()
    mod_text_w.geometry("1300x800")  # 大小
    mod_text_w.resizable(1300, 800)  # 锁定大小
    mod_text_w.iconbitmap('./image/icon_16x16.ico')  # 图标
    mod_text_w.attributes("-alpha", 0.9)  # 窗口透明度 -alpha
    mod_text_w.attributes("-topmost", False)  # 窗口置顶 -topmost
    mod_text_w.attributes('-transparentcolor', "grey")  # 背景颜色 -transparentcolor
    mod_text_w.attributes('-toolwindow', 1)




