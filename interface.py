import customtkinter as CTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter as tk
from time import strftime
new = CTk.CTk()
new.title("GESTION DE STOCK YANN")
new.geometry("1200x1200")

E = CTk.IntVar()
XA =  CTk.StringVar()
XB =  CTk.StringVar()
XC =  CTk.StringVar()
XD =  CTk.StringVar()



def Effacer():
    XA.set("")
    XB.set("")
    XC.set("")
    XD.set("")
    E.set("")

def Heure():
    heur = strftime("%H : %M  %S")
    var0.config(text=heur)
    var0.after(1000,Heure)

var0 = tk.Label(new,text="HH : MM : SS",font=("Arial",28))
var0.place(x=5,y=930)

Heure()
import subprocess
def DECONNEXION ():

    new.destroy()
    subprocess.run(["python","reine.py"])
    

        
def ADD():
    A = Frame3.get()
    B = Frame5.get()
    C = Frame7.get()
    D = Frame9.get()
    if A == "" or B == "" or C == "" or D == "":
        messagebox.showinfo("Info", "Veuillez renseigner tous les champs 😎")
    else:
                 
        connexion = mysql.connector.connect(host="localhost",user="root",password="",database="stock")
        cuseur = connexion.cursor()
        sql = "INSERT INTO Produit( Nom_du_Produit, Prix_du_Produit, Quantité, Code) VALUES (%s ,%s ,%s ,%s)"
        values = (A,B,C,D)
        cuseur.execute(sql,values)
        connexion.commit()

        messagebox.showinfo("Succès","Produit ajouter")

        cuseur.execute("SELECT * FROM Produit ORDER BY Id DESC LIMIT 100")
        nouveau_patient = cuseur.fetchone()
        FrameX1.insert('', 'end',values=nouveau_patient)
        connexion.close()
        Effacer()




def Supprimer():
    XE = E.get()
    if XE =="":
        messagebox.showerror("Erreur","Veuiller entrer un Id dans la barre de recherche")
    else :
        if XE == 0:
            messagebox.showerror("Erreur","Id Invalide")
        else:

            connexion = mysql.connector.connect(host="localhost",user="root",password="",database="stock")
            curseur = connexion.cursor()
            sql = "DELETE FROM Produit WHERE Id = %s"
            curseur.execute(sql,(XE,))
            connexion.commit()
            E.set("")
            messagebox.showinfo("Succès","Produit supprimer")
            Effacer()
            connexion.close()

def Rechercher():
    yann = E.get()
    if yann =="":
        messagebox.showerror("Erreur","Veuiller entrer un Id dans la barre de recherche")
    else :
        if yann == 0 :
            messagebox.showerror("Erreur","Id Invalide")
        else:
            connexion = mysql.connector.connect(host="localhost",user="root",password="",database="stock")
            curseur = connexion.cursor()
            sql = "SELECT Nom_du_Produit, Prix_du_Produit, Quantité, Code FROM Produit WHERE Id = %s"
            curseur.execute(sql,(yann,))
            produit = curseur.fetchone()
            if produit :
                XA.set(produit[0])
                XB.set(produit[1])
                XC.set(produit[2])
                XD.set(produit[3])
            else:
                messagebox.showerror("Erreur","Le Produit n'existe pas ❌")
                connexion.commit()
                connexion.close()

def Effacer():
    XA.set("")
    XB.set("")
    XC.set("")
    XD.set("")
    E.set("")

def Modifier():
    franck = E.get()
    if franck == "":
        messagebox.showerror("Erreur","Entrer un Id dans la barre de recherche")
    else:

        a = XA.get()
        b = XB.get()
        c = XC.get()
        d = XD.get()

        connexion = mysql.connector.connect(host="localhost",user="root",password="",database="stock")
        curseur = connexion.cursor()
        sql = "UPDATE Produit SET Nom_du_Produit=%s, Prix_du_Produit=%s, Quantité=%s, Code=%s  WHERE Id=%s"
        valeur = (a,b,c,d,franck)

        curseur.execute(sql,valeur)
        connexion.commit()
        Effacer()
        messagebox.showinfo("Succès","Produit modifier avec succès")
        connexion.close()


            
titre = tk.Label(new,text="G-STOCK-YANN",font=("Arial",38),foreground="green")
titre.place(x=5,y=10)


ya0 = CTk.CTkButton(new,text="AJOUTER UN ADMINISTRATEUR",font=("Arial",30),width=300,fg_color="blue")
ya0.place(x=400,y=10)

ya1 = CTk.CTkButton(new,text="DECONNEXION",font=("Arial",30),width=300,command=DECONNEXION,fg_color="green")
ya1.place(x=900,y=10)


ya2 = CTk.CTkLabel(new,text="Chercher un produit",font=("Arial",30))
ya2.place(x=10,y=100)

ya3 = CTk.CTkEntry(new,font=("Arial",30),width=420,textvariable=E)
ya3.place(x=10,y=150)



ya4 = CTk.CTkButton(new,font=("Arial",30),width=150,text="Entrer",fg_color="grey",command=Rechercher)
ya4.place(x=280,y=100)

yann = CTk.CTkButton(new,font=("Arial",30),width=150,text="VIDER",command=Effacer)
yann.place(x=460,y=150)

ya5 = CTk.CTkButton(new,font=("Arial",30),width=150,text="AJOUTER",fg_color="red",command=ADD)
ya5.place(x=660,y=150)

ya6 = CTk.CTkButton(new,font=("Arial",30),width=150,text="MODIFIER",fg_color="black",command=Modifier)
ya6.place(x=880,y=150)

ya4 = CTk.CTkButton(new,font=("Arial",30),width=150,text="SUPPRIMER",fg_color="orange",command=Supprimer)
ya4.place(x=1080,y=150)

Frame1 = CTk.CTkFrame(new,width=400,height=400)
Frame1.place(x=10,y=200)

Frame2 = CTk.CTkLabel(Frame1,text="Nom du Produit",font=("Arial",26))
Frame2.place(x=10,y=10)

Frame3 = CTk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=XA)
Frame3.place(x=10,y=50)

Frame4 = CTk.CTkLabel(Frame1,text="Prix du Produit",font=("Arial",26))
Frame4.place(x=10,y=100)

Frame5 = CTk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=XB)
Frame5.place(x=10,y=140)

Frame6 = CTk.CTkLabel(Frame1,text="Quantité",font=("Arial",26))
Frame6.place(x=10,y=190)
   
Frame7 = CTk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=XC)
Frame7.place(x=10,y=230)

Frame8 = CTk.CTkLabel(Frame1,text="Code",font=("Arial",26))
Frame8.place(x=10,y=280)

Frame9 = CTk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=XD)
Frame9.place(x=10,y=320)

style = ttk.Style()
style.configure("Treeview", font=("Arial", 14))

FrameX1 = ttk.Treeview(new,columns=(1,2,3,4,5),height=5,show="headings")
FrameX1.place(x=730,y=300,width=1100,height=900)



FrameX1.heading(1,text="Id")
FrameX1.heading(2,text="Nom du Produit")
FrameX1.heading(3,text="Prix du Produit")
FrameX1.heading(4,text="Quantité")
FrameX1.heading(5,text="Code")

FrameX1.column(1,width=20)
FrameX1.column(2,width=150)
FrameX1.column(3,width=150)
FrameX1.column(4,width=150)
FrameX1.column(5,width=150)


connexion = mysql.connector.connect(host="localhost", user="root", password="", database="stock")
curseur = connexion.cursor()
curseur.execute("SELECT * FROM Produit ORDER BY Id DESC LIMIT 100")  
rows = curseur.fetchall()
for row in rows:
    FrameX1.insert('', 'end', values=row)
connexion.close()





new.mainloop()
