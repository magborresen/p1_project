from tkinter import*

Answers = [0,0]


root = Tk() #laver en blank skærm. Tk er en class fra tkinter

Top_Frame = Frame(root) #et rektangel i vinduet, som kan sætte ting i.
Top_Frame.pack()#indsætter rektanglen i root.

Bottom_Frame = Frame(root)#et rektangel i vinduet, som kan sæte ting i.
Bottom_Frame.pack(side=BOTTOM) #indætter rektanglen i bunden af root.

def mand_valg():# Sker når kønnet bliver valgt til Mand
    Answers[0] = 1
    print("Du valgte mand" + "\n")
    print(Answers)



def kvinde_valg(): # Sker når kønnet bliver valgt til Kvinde
    Answers[0] = 2
    print("du valgte kvinde"+ "\n")
    print(Answers)



def Kon_valg():
    label_1 = Label(root, text="Hvad er du?")
    label_1.pack(side=TOP)

    Button_1 = Button(Bottom_Frame, text="Mand", fg="blue", command=mand_valg)#definere en knap
    Button_2 = Button(Bottom_Frame, text="Kvinde", fg="red", command=kvinde_valg)#definere en knap

    Button_1.pack(side=LEFT)#Indsætter knap 1
    Button_2.pack(side=RIGHT)#Indsætter knap 2


Kon_valg()
root.mainloop()#for at holde vinduet åben, så det ikke lukker efter en gennemlæsning
