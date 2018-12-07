import tkinter as tk
from tkinter import ttk
import InfoScreen
import json


TITLE_FONT = ("Verdana", 20, "bold")


class Age(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Hvor gammel er du?", font=TITLE_FONT)
        label.place(x=270, y=70)

        label_1 = tk.Label(self, text="Indtast alder:", font="TITLE_FONT")
        self.age_entry = tk.Entry(self)

        label_1.place(x=345, y=140)
        self.age_entry.place(x=300, y=100)


        Next_Age = tk.Button(self, text="Næste", width = 10, height = 3,
                            command=lambda: [self.update_json(),
                                             master.switch_frame(InfoScreen.Information)])
        Next_Age.place(x=540, y=220)

        Num1 = tk.Button(self, text="1", width = 10, height = 3, command = lambda:[self.age_entry.insert('end',"1")])
        Num2 = tk.Button(self, text="2", width = 10, height = 3, command = lambda:[self.age_entry.insert('end',"2")])
        Num3 = tk.Button(self, text="3", width = 10, height = 3, command = lambda:[self.age_entry.insert('end',"3")])
        Num4 = tk.Button(self, text="4", width = 10, height = 3, command = lambda:[self.age_entry.insert('end',"4")])
        Num5 = tk.Button(self, text="5", width = 10, height = 3, command = lambda:[self.age_entry.insert('end',"5")])
        Num6 = tk.Button(self, text="6", width = 10, height = 3, command = lambda:[self.age_entry.insert('end',"6")])
        Num7 = tk.Button(self, text="7", width = 10, height = 3, command = lambda:[self.age_entry.insert('end',"7")])
        Num8 = tk.Button(self, text="8", width = 10, height = 3, command = lambda:[self.age_entry.insert('end',"8")])
        Num9 = tk.Button(self, text="9", width = 10, height = 3, command = lambda:[self.age_entry.insert('end',"9")])
        Num10 = tk.Button(self, text="0", width = 10, height = 3, command = lambda:[self.age_entry.insert('end',"0")])
        Num11 = tk.Button(self, text="Slet alt", width = 10, height = 3, command = lambda: [self.age_entry.delete(0,'end')])

        Num1.place(x=240, y=160)
        Num2.place(x=340, y=160)
        Num3.place(x=440, y=160)
        Num4.place(x=240, y=220)
        Num5.place(x=340, y=220)
        Num6.place(x=440, y=220)
        Num7.place(x=240, y=280)
        Num8.place(x=340, y=280)
        Num9.place(x=440, y=280)
        Num10.place(x=340, y=340)
        Num11.place(x=540, y=160)

        def NumPad(self, num):
            self.age_entry.insert(0,num)









    def update_json(self):
        age_answer = self.age_entry.get()
        with open('../variables.json', 'r+') as f:
            data = json.load(f)
            data["Age"] = int(age_answer)
            f.seek(0)
            json.dump(data, f)
            f.truncate()
