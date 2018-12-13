import tkinter as tk
from tkinter import ttk
import MainGUI
import json

TITLE_FONT = ("Verdana", 20, "bold")
headline = ("Verdana", 15, "bold")

class Result(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
    #    label = tk.Label(self, text="Resultater:", font = TITLE_FONT)
    #    label.place(x=340, y=20)

        New_Test = tk.Button(self, width = 10, height = 3, text ="Ny test",
        command = lambda: master.switch_frame(MainGUI.StartPage))
        New_Test.place(x=520, y=400)


        with open("../variables.json", 'r') as f:
            data = json.load(f)
            noise_induced_250=data["age_related_loss"]["250"]
            noise_induced_500=data["age_related_loss"]["500"]
            noise_induced_1000=data["age_related_loss"]["1000"]
            noise_induced_2000=data["age_related_loss"]["2000"]
            noise_induced_4000=data["age_related_loss"]["4000"]
            noise_induced_8000=data["age_related_loss"]["8000"]


        noise_induced_label = tk.Label(self, text="Dette er dit støj inducerede høretab ved forskellige frekvenser.\n En værdi under 0 repræsenterer en bedre hørelse end gennemsnittet\n for den valgte alder, mens en værdi over 0, repræsenterer\n en ringere hørelse end gennemsnittet.")
        noise_induced_label.place(x=20, y=130)

        noise_250 = tk.Label(self, text="Dit høretab ved lyde på 250 Hz er " + str(int(noise_induced_250)) + " dB.")
        noise_250.place(x=85, y=200)

        noise_500 = tk.Label(self, text="Dit høretab ved lyde på 500 Hz er " + str(int(noise_induced_500)) + " dB.")
        noise_500.place(x=85, y=230)

        noise_1000 = tk.Label(self, text="Dit høretab ved lyde på 1000 Hz er " + str(int(noise_induced_1000)) + " dB.")
        noise_1000.place(x=85, y=260)

        noise_2000 = tk.Label(self, text="Dit høretab ved lyde på 2000 Hz er " + str(int(noise_induced_2000)) + " dB.")
        noise_2000.place(x=85, y=290)

        noise_4000 = tk.Label(self, text="Dit høretab ved lyde på 4000 Hz er " + str(int(noise_induced_4000)) + " dB.")
        noise_4000.place(x=85, y=320)

        noise_8000 = tk.Label(self, text="Dit høretab ved lyde på 8000 Hz er " + str(int(noise_induced_8000)) + " dB.")
        noise_8000.place(x=85, y=350)


        avg_loss = (noise_induced_250 + noise_induced_500 + noise_induced_1000 + noise_induced_2000 + noise_induced_4000 + noise_induced_8000)/6

        print(avg_loss)
        if avg_loss <= 25:
            evaluate_loss = "ingen nedsættelse"
        elif avg_loss <= 40:
            evaluate_loss = "svag nedsættelse"
        elif avg_loss <= 60:
            evaluate_loss = "moderat nedsættelse"
        elif avg_loss <= 80:
            evaluate_loss = "alvorlig nedsættelse"
        elif avg_loss >= 81:
            evaluate_loss = "dybtgående nedsættelse"

        avg_noise_loss = tk.Label(self, text="Du har " + evaluate_loss + " af din hørelse.", font=TITLE_FONT)
        avg_noise_loss.place(x=30, y=30)

        if avg_loss <= 25:
            recommendation = "Ingen handing nødvendig."
        elif avg_loss <= 40:
            recommendation = "      Kontakt læge. \n       Høreapparat muligvis nødvendigt."
        elif avg_loss <= 60:
            recommendation = "                    Kontakt læge. \n               Høreapparat anbefales."
        elif avg_loss <= 80:
            recommendation = "Kontakt læge \n Høreapparat er nødvendigt. \n Hvis disse ikke er tilgængelige, \n burde mundaflæsning og tegnsprog læres"
        elif avg_loss >= 81:
            recommendation = "Høreapparat hjælper muligvis \n med at forstå ord. Udover det er \n rehabilitering nødvendigt. Mundaflæsning, \n og nogle gange tegnsprog, er essentiel"

        recommendation_label = tk.Label(self, text="Anbefaling:", font=headline)
        recommendation_label.place(x=529, y=130)

        recommendation_eval = tk.Label(self, text=recommendation)
        recommendation_eval.place(x=480, y=180)
