

class Gender(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="vaelg køn:", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        Button_2 = tk.Button(self, text ="Tilbage",
        command = lambda: controller.show_frame(StartPage))
        Button_2.pack()

        Button_3 = tk.Button(self, text ="Mand",
        command = lambda: controller.show_frame(StartPage))
        Button_3.pack()

        Button_4 = tk.Button(self, text ="Kvinde",
        command = lambda: controller.show_frame(StartPage))
        Button_4.pack()
