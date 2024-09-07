
import customtkinter as CTk
import tkinter as tk
import mysql.connector
from tkinter import messagebox

fenetre = CTk.CTk()
fenetre.title("GESTION DE STOCK YANN")
fenetre.geometry("1900x1900")

A = CTk.StringVar()
B = CTk.StringVar()


var1 = tk.Label(fenetre,text="GESTION DE STOCK",font=("Arial",46),fg="blue")
var1.place(x=600,y=20)


var2  =  CTk.CTkLabel(fenetre,text="Email",font=("Arial",30))
var2.place(x=380,y=200)

var3  =  CTk.CTkEntry(fenetre,font=("Arial",30),width=370,textvariable=A)
var3.place(x=560,y=200)

var4  =  CTk.CTkLabel(fenetre,text="Mot_Passe",font=("Arial",30))
var4.place(x=380,y=280)

var5  =  CTk.CTkEntry(fenetre,font=("Arial",30),width=370,show="*",textvariable=B)
var5.place(x=560,y=280)

def Connnexion(Email,Mot_Passe):
    Email = var3.get()
    Mot_Passe= var5.get()
    if Email==" " or Mot_Passe=="":
        messagebox.showinfo("Info","Veuillez renseingner tous les champs ")
    else:
        connexion = mysql.connector.connect(host="localhost",user="root",password="",database="stock")
        curseur = connexion.cursor()
        curseur.execute("SELECT * FROM `administrateur` WHERE Email = %s AND Mot_Passe = %s",(Email,Mot_Passe))
        resultat = curseur.fetchone()
        connexion.commit()
    return resultat
import subprocess


def Authentifier():
    Email = var3.get()
    Mot_Passe = var5.get()

    resultat = Connnexion(Email,Mot_Passe)
    if resultat :

        messagebox.showinfo("Succes","Bienvenue")
        A.set("")
        B.set("")
        fenetre.destroy()
        subprocess.run(["python","interface.py"])
    else : 
        messagebox.showerror("Erreur","Email ou Mot de Passe incorrect ")

var6  =  CTk.CTkButton(fenetre,font=("Arial",30),width=300,text="Connexion",command=Authentifier)
var6.place(x=480,y=350)



fenetre.mainloop()

