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

        label4 = tk.Label(self, text="Om testen",font=TITLE_FONT)

        label = tk.Label(self, text="Under denne høretest vil din hørelse blive testet og kan bruges som en indikation \n for eventuelle høreskader/høretab. Testen kan derfor ikke anvendes som erstatning\n for konsultation hos en læge. Ved mistanke om høreskader anbefales det altid \n at se en læge for en mere præcis høretest",
                         font="TITLE_FONT")
        label2 = tk.Label(self, text="Testen udføres med høretelefoner og udføres i et stille rum, gerne så stille som muligt\n for at få det mest pålidelige resultat uden forstyrrende støj. Under testen vil \n du høre forskellige toner i forskellig lydstyrke. Når du hører en tone, trykkes på knappen",
                                          font="TITLE_FONT")
        label3 = tk.Label(self, text="Resultatet af høretesten vil vise hvor din hørelse ligger i forhold til din alder. \n Her sammenlignes dit resultat med hvor din alderstilsvarende hørelse burde ligge")
        label.place(x=250, y=120)
        label2.place(x=250, y=190)
        label3.place(x=250, y=250)
        label4.place(x=420, y=80)
        with open("../variables.json", 'r') as f:
            data = json.load(f)
            age = data["Age"]
            gender = data["Gender"]
            list_left_ear = data["left_ear_test"]
            list_right_ear = data["right_ear_test"]

        StartTest = tk.Button(self, text="Start test", width = 20, height = 5,
                                       command= lambda:[master.switch_frame(Test.Test)])
        StartTest.place(x=400, y=320)
