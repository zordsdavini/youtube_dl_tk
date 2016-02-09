#!/usr/bin/python3

import os
import tkinter as tk
from tkinter import filedialog, messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.llink = tk.Label(self)
        self.llink["text"] = "Įrašyk linką Youtūbės"
        self.llink.pack(side="top")

        self.link = tk.Entry(self)
        self.link.pack(side="top")

        self.ltraget = tk.Label(self)
        self.ltraget["text"] = "Nenuroyta dyrektorija"
        self.ltraget.pack(side="top")

        self.path = None
        self.target_btn = tk.Button(self)
        self.target_btn["text"] = "Kur rašyti?"
        self.target_btn["command"] = self.set_target
        self.target_btn.pack(side="top")

        self.down_btn = tk.Button(self)
        self.down_btn["text"] = "Siųsti"
        self.down_btn["command"] = self.down
        self.down_btn.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def down(self):
        if self.path == None:
            messagebox.showerror('Klaida!', 'Nenurodyta, kur įrašyti')
            return

        if not self.link.get():
            messagebox.showerror('Klaida!', 'Nenurodytas linkas iš Youtūbės :(')
            return

        os.system("cd %s; youtube-dl --audio-format mp3 -x %s" % (self.path, self.link.get()))

        messagebox.showinfo('!!!', 'Parsiuntė :) Dėkui, kad naudojies \n© Zordsdavini, 2016')


    def set_target(self):
        self.path = filedialog.askdirectory()
        self.ltraget['text'] = self.path




root = tk.Tk()
app = Application(master=root)
app.mainloop()
