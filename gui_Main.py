from tkinter import ttk, Label
from  PIL import Image,ImageTk
import tkinter as tk
import webbrowser

from click import command
from ttkbootstrap.constants import *

import ttkbootstrap as tttk

from gethtml import get_html
from get_img import img_url_get
from gui_mod_text import op_top_win
def get_html_data():
    version_text =comb_1.get()
    type_text = comb_3.get()
    way_text = comb_2.get()
    page_text = comb_4.get()
    res ={
        'version':version_text,
        'way':way_text,
        'type':type_text,
        'page':page_text
    }
    print(res)
    return res

def close_window_1():   # 关闭窗口
    Modulemain.destroy()

def on_drag_start(event):   #鼠标按下事件
    global x,y
    x= event.x
    y= event.y

def on_drag(event):   #鼠标移动事件
    deltax = event.x-x
    deltay = event.y-y
    new_x = Modulemain.winfo_x() +deltax
    new_y = Modulemain.winfo_y() +deltay
    Modulemain.geometry(f"+{new_x}+{new_y}")

def on_drag_stop(event):  #鼠标释放事件
    global x, y
    x = 0
    y = 0

def open_url(index):  #打开链接
    print(index)
    url_1 = str(index['url'])
    name_url_ = str(index['name'])
    f = open('./get/url_d.text','w+', encoding='utf-8')
    f.write(url_1)
    f.close()
    f = open('./get/url_name.text', 'w+', encoding='utf-8')
    f.write(name_url_)
    f.close()
    webbrowser.open_new(url_1)
    op_top_win()

def mod_list():   #mod列表显示
    for widget in Label_fr.winfo_children():
        widget.destroy()
    data_1 = get_html_data()
    list_ls = get_html(data_1)
    print(list_ls)
    img_url_get(list_ls)
    name_mod = tk.StringVar()
    n = 0
    z = 1
    for m in range(len(list_ls)):
        img = Image.open('./get/img/{}.jpg'.format(m))
        img = img.resize((100, 80))
        photo = ImageTk.PhotoImage(img)
        nme = str(list_ls["mod{}".format(m)]["name"])
        print(nme)
        name_mod.set(nme)
        print(name_mod.get)
        print(m)
        if n == 7:
            n = 0
            z +=1
        id_list = {
            "id":m,
            'name':name_mod.get(),
            "url":list_ls["mod{}".format(m)]['url']
        }
        exec(f'Label_text_{m} = ttk.LabelFrame(Label_fr)')
        exec(f'Label_text_{m}.grid(row={z}, column={n})')
        exec(f'Label_text_{m}_1 = tk.Label(Label_text_{m},width=100,height=80,image=photo)')
        exec(f'Label_text_{m}_1.image = photo')
        exec(f'Label_text_{m}_2 = ttk.Label(Label_text_{m}, text=name_mod.get(), width=22,anchor="center", justify="center")')
        exec(f'Label_text_{m}_1.grid(row=0)')
        exec(f'Label_text_{m}_2.grid(row=1)')
        exec(f'Label_text_{m}_1.bind("<Button-1>",lambda event, index=id_list,:open_url(index))')
        exec(f'Label_text_{m}_2.bind("<Button-1>",lambda event, index=id_list,:open_url(index))')
        n +=1

def mod_get_button():
    # --------------------------版本
    text_1.place(relx=0, rely=0)
    comb_1.place(relx=0, rely=0.03)
    comb_1['values'] = ['1.21.x', '1.20.x', '1.19.x', '1.18.x', '1.17.x', '1.16.x', '1.15.x', '1.14.', '1.13.x',
                        '1.12.x', '1.11.x', '1.10.x', '1.9.x', '1.8.x', '1.7.x', '1.6.x']
    comb_1.set("1.21.x")
    # --------------------------版本
    # --------------------------运行方式
    text_2.place(relx=0.05, rely=0)
    comb_2['values'] = ['Forge', 'Fabric', 'Quilt', 'NeoForge', 'Rift', 'LiteLoader', '数据包', '行为包', '命令方块',
                        '文件覆盖']
    comb_2.place(relx=0.05, rely=0.03)
    comb_2.set("Forge")
    # --------------------------运行方式
    # --------------------------类型
    text_3.place(relx=0.11, rely=0)
    comb_3['values'] = ['资源', '世界', '群系', '结构', '生物', '能源', '存储', '物流', '道具', '安全', '红石', '食物',
                        '模型', '关卡', '指南', '破坏', 'Meme', '中式', '日式', '西式', '恐怖', '建材', '生存', '指令',
                        '优化', '国创', '科技', '魔法', '冒险', '农业', '装饰', '实用', '辅助', '魔改', 'LIB']
    comb_3.place(relx=0.11, rely=0.03)
    comb_3.set("资源")
    # --------------------------类型
    # --------------------------页码
    text_4.place(relx=0.16, rely=0)
    comb_4['values'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                        '18', '19', '20']
    comb_4.place(relx=0.16, rely=0.03)
    comb_4.set(1)
    # --------------------------页码
    # --------------------------刷新mod列表
    modList = ttk.Button(windows_bord, text='刷新mod', command=mod_list, bootstyle=(SUCCESS, OUTLINE))
    modList.place(relx=0.21, rely=0.03)
    # --------------------------刷新mod列表
Modulemain = tk.Tk()
Modulemain.title('MCmod百科玩家自制客户端-只用于查询mod')
Modulemain.geometry("1300x800") #大小
Modulemain.resizable(1300,800) #锁定大小
Modulemain.iconbitmap('./image/icon_16x16.ico') #图标
Modulemain .overrideredirect(1)  #隐藏菜单
Modulemain.attributes("-alpha",0.92) #窗口透明度 -alpha
Modulemain.attributes("-topmost",False)  #窗口置顶 -topmost
Modulemain.attributes('-transparentcolor',"grey") #背景颜色 -transparentcolor

#--------------------------顶部选项
tool_windows = ttk.LabelFrame(Modulemain)
tool_windows.place(y=0,x=0,width=1300,height=50)
tool_But1 = ttk.Button(tool_windows,text='mod筛选',command=mod_get_button,bootstyle=(SUCCESS, SOLID))
tool_But1.place(rely=0,relx=0,height=30)
tool_But2 = ttk.Button(tool_windows,text='整合包',bootstyle=(SUCCESS, SOLID))
tool_But2.place(rely=0,relx=0.05,height=30)
#--------------------------顶部选项

#--------------------------应用窗口拖动
tool_windows.bind("<ButtonPress-1>",on_drag_start)
tool_windows.bind("<B1-Motion>",on_drag)
tool_windows.bind("<ButtonRelease-1>",on_drag_stop)
#--------------------------应用窗口拖动

#--------------------------关闭窗口
close_window = ttk.Button(Modulemain,text='X',command=close_window_1,bootstyle=(SUCCESS, OUTLINE))
close_window.place(x=1260,y=15,height=30)
#--------------------------关闭窗口
windows_bord = ttk.LabelFrame(Modulemain)
windows_bord.place(y=50,x=1,width=1298,height=749)
# --------------------------mod信息显示#
Label_fr = ttk.LabelFrame(windows_bord)  # 主标签容器
Label_fr.place(relx=0, rely=0.1)
# --------------------------mod信息显示
text_1 = ttk.Label(windows_bord,text='版本')
comb_1 = tttk.Combobox(windows_bord, width=5, state='readonly')
text_2 = ttk.Label(windows_bord, text='运行方式')
comb_2 = tttk.Combobox(windows_bord, width=7, state='readonly')
text_3 = ttk.Label(windows_bord,text='类型')
comb_3 = tttk.Combobox(windows_bord, width=5, state='readonly')
text_4 = ttk.Label(windows_bord,text='页码')
comb_4 = tttk.Combobox(windows_bord, width=5, state='readonly')
mod_get_button()
Modulemain.mainloop()