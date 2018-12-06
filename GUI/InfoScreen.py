import tkinter as tk
from tkinter import ttk
import Test
import sys
sys.path.append('../Result')
import calculate_result
import json


TITLE_FONT = ("Verdana", 20, "bold")


class Information(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="[SKRIV TEKST OM TEST HER!]:",
                         font=TITLE_FONT)
        label.pack(pady=10, padx=10)

        with open("../variables.json", 'r') as f:
            data = json.load(f)
            age = data["Age"]
            gender = data["Gender"]
            list_left_ear = data["left_ear_test"]
            list_right_ear = data["right_ear_test"]

        start_test_button = ttk.Button(self, text="Start test",
                                       command= lambda:[master.switch_frame(Test.Test)])
        start_test_button.pack()
