"""
-adding objects to a list or dictionary to be able to retrieve an object from there

problem:
when you pass a func without arguments it will assume that I always use the last one,
but with args it works instantly, without activation

steps:
-click chosen button
-get the button's name
-the buttons function pastes it's name into text field
"""
import tkinter as tk
from tkinter import ttk
from functools import partial


ob_list = ['Bob', 'Greg', 'George']
my_dict = {}


def func_in_app_butt():
    def this_command(n):
        if my_dict[n].instate(['selected']):
            text_t.configure(state='normal')
            text_t.insert(tk.END, f"\n{n}\n")
            text_t.configure(state='disabled')
        else:
            text_t.configure(state='normal')
            n_text = text_t.get('1.0', f'{tk.END}-1c').replace(f"\n{n}\n", "")
            text_t.delete('1.0', tk.END)
            text_t.insert(tk.END, n_text)
            text_t.configure(state='disabled')

    for el in ob_list:
        act_arg = partial(this_command, el)
        button = ttk.Checkbutton(root, text=el, command=act_arg)
        my_dict[el] = button
    print(my_dict)


def iter_cre_func():
    for el in my_dict.values():
        el.pack()


root = tk.Tk()
text_t = tk.Text(root, wrap='word')

text_t.pack()

func_in_app_butt()
iter_cre_func()

root.mainloop()