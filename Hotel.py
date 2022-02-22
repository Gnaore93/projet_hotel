
from tkinter import *
import tkinter as tk
from subprocess import call
from tkinter import messagebox
from tkinter import ttk
import tkinter
from turtle import right
from PIL import Image,ImageTk
import sqlite3





class window:
    def __init__(self,root):
        self.root=root
        self.root.title("ENOTEL BEACH")
        self.root.geometry("1800x1300+100+300")
        #self.root.resizable(FALSE,FALSE)
        #========== les frame de ma fenetre principale =======#
        frame1= LabelFrame(root,width=1800,height=60,bg="#a1b0c7")
        frame1.place(x=0,y=0)

        frame_footer= LabelFrame(root,width=1800,height=120,bg="#a1b0c7")
        frame_footer.pack(side=BOTTOM)
        #========== les boutons de ma fenetre principale =======#
        def liste_chambre():
            

            

            frame_liste_chambre= LabelFrame(root,width=1800,height=900,bg="lavender")
            frame_liste_chambre.place(x=0,y=80)

            titre_frm3=Label(frame_liste_chambre,borderwidth=3,text="ENREGISTRER UNE CHAMBRE",font=("sans serif",20),fg="black")
            titre_frm3.place(x=0,y=0,width=1800)

            frm_clt= LabelFrame(frame_liste_chambre,text="Informations sur le client",width=400,height=300,bg="white")
            frm_clt.place(x=8,y=110)

            nom_chbre =Label(frm_clt,text="Chambre:",bg="white",font=("sans serif",10))
            nom_chbre.place(x=5,y=20)
            Entry_nom_cbre = Entry(frm_clt,bg="azure")
            Entry_nom_cbre.place(x=70,y=20)

            sejour=Label(frm_clt,text="Passage:",bg="white",font=("sans serif",10))
            sejour.place(x=5,y=60)
            Entry_sejour = Entry(frm_clt,bg="azure")
            Entry_sejour.place(x=70,y=60)

            etat=Label(frm_clt,text="Nuit:",bg="white",font=("sans serif",10))
            etat.place(x=5,y=100)
            Entry_etat = Entry(frm_clt,bg="azure")
            Entry_etat.place(x=70,y=100)

            lb_chbre4=Label(frm_clt,text="Categories:",bg="white",font=("sans serif",10))
            lb_chbre4.place(x=5,y=150,)

            list_categorie = ["climatisée","ventilateur"]
            listecombobox = ttk.Combobox(frm_clt,values = list_categorie)
            listecombobox.place(x=135,y=150)
            #lb_chbre_Entry4 = Entry(frm_clt,bg="azure")
            #lb_chbre_Entry4.place(x=135,y=150)

            lb_chbre5=Label(frm_clt,text="Date De Sorties:",bg="white",font=("sans serif",10))
            lb_chbre5.place(x=5,y=200,)
            lb_chbre_Entry5 = Entry(frm_clt,bg="azure")
            lb_chbre_Entry5.place(x=135,y=200)

            treeframe = LabelFrame(frame_liste_chambre)
            treeframe.configure(bg="white")
            treeframe.place(x=470,y=100,width=1200,height=1500)


            column = ["Libellé","Passage ","Nuit","Categorie","Etat"]

            myTree = ttk.Treeview(treeframe,height=50,column=column)
            myTree.pack(fill="both")
            myTree['show']='headings'
            for each in column:
                myTree.column(each,width=50)
                myTree.heading(each,text=each.capitalize())


            

            frm_bouton_list_chbre= LabelFrame(frame_liste_chambre,width=100,height=1300,bg="#a1b0c7")
            frm_bouton_list_chbre.place(x=1698,y=40,)

            btn_enrg_frm_list_chbr =Button(frm_bouton_list_chbre,width=8,height=2,bg="white",text="Enregistrer",highlightbackground="purple",fg="red",borderwidth=3)
            btn_enrg_frm_list_chbr.place(x=2,y=50)

            def quit():
                   frame_liste_chambre.destroy()
            btn_quit_frm_list_chbr =Button(frm_bouton_list_chbre,width=8,height=2,bg="white",text="Quitter",highlightbackground="purple",fg="red",borderwidth=3,command=quit)
            btn_quit_frm_list_chbr.place(x=2,y=120)

        btn1 = Button(frame1,width=10,height=1,bg="#a1b0c7",text="Créer chambre",highlightthickness=5,highlightbackground="green",command=liste_chambre)
        btn1.place(x=800,y=5)
        #========== les image de ma fenetre principale =======#
        self.image_accueil=ImageTk.PhotoImage(file="image_accuei.jpeg")
        self.lbl1=Label(self.root,image=self.image_accueil,bd=0,width=1800,height=240)
        self.lbl1.place(x=0,y=60)

        
        
        #==========  =======#
        """def toogle_win():
            f1=Frame(root,width=200,height=800,bg="#262626")
            f1.place(x=0,y=0)

            def dele():
                
                f1.destroy()
            
            img2=ImageTk.PhotoImage(Image.open("projet_hotel\close.png"))
            Button(f1,text="close",image=img2,command=dele,border=0,activebackground="#12c4c0",bg="#12c4c0").place(x=5,y=10)
        Button(root,command=toogle_win,text="open").place(x=5,y=10)"""

    
        l6=Label(frame_footer,text="Copyright ©  2010-2022 Storia palace, Tous droits réservés.",bg="#c4c0c0")
        l6.place(x=460,y=7)

        l7=Label(frame_footer,text="Contacts \n 07-77-50-71-39\n01-73-24-29-18",font=("Bahnschrift Light",10,"bold"),bg="black",fg="gold")
        l7.place(x=860,y=7)

        lbtitre= Label(frame_footer,text="VOTRE BIEN-ETRE,NOTRE PRIORITE",font=("sans serif",25),background="white",foreground="lavender",relief=SUNKEN)
        lbtitre.place(x=2500,y=200)
  
        
        def visite():
            
            frame_vsite= LabelFrame(root,width=1800,height=925,bg="lavender")
            frame_vsite.place(x=0,y=55)

            #image_accueil=ImageTk.PhotoImage(file="pho.jpeg")
            #lbl1=Label(frame_vsite,image=image_accueil,bd=0,width=100,height=150)
            #lbl1.place(x=0,y=60)
            
            
            image = Image.open('image_accuei.jpeg')
            photo = ImageTk.PhotoImage(image)
            labelimg =tk.Label(frame_vsite,image=photo,)
            labelimg.place(x=600,y=500,width=500,height=150)

            l4=Label(frame_vsite,text="MIEUX SE DIVERTIR CEST BIEN CHOISIR LENDROIT\n",bg="lavender",font=("sans serif",25))
            l4.place(x=280,y=0)

            frm_bouton= LabelFrame(frame_vsite,width=100,height=1300,bg="#a1b0c7")
            frm_bouton.place(x=1698,y=40,)


            

            def quit():
                frame_vsite.destroy()
            btn_quit_visit =Button(frm_bouton,width=10,height=1,bg="#a1b0c7",text="Quitter",highlightbackground="red",borderwidth=3,fg="blue",command=quit)
            btn_quit_visit.place(x=2,y=100)
        btn2 =Button(frame1,width=10,height=1,bg="#a1b0c7",text="Visite",highlightthickness=5,highlightbackground="azure",borderwidth=3,command=visite)
        btn2.place(x=910,y=5)

        
        #---------------Reservation----------------#
        def reservation():

            
            #-------frame3 (fenetre principale de loption reservation)--------#
            
            frame3= LabelFrame(root,width=1800,height=900,bg="lavender")
            frame3.place(x=0,y=80)

            titre_frm3=Label(frame3,borderwidth=3,text="ALLOCATION DES CHAMBRES AUX CLIENTS",font=("sans serif",20),fg="black")
            titre_frm3.place(x=0,y=0,width=1800)

            #-------frm_reser_1 (fenetre secondaire de loption reservation a laquelle mes formulaires sont rataches)--------#
            
            frm_reser_1= LabelFrame(frame3,width=1670,height=900,bg="white")
            frm_reser_1.place(x=10,y=40)

            #frame_footer= LabelFrame(frame3,width=1800,height=120,bg="#a1b0c7")
            #frame_footer.pack(side=BOTTOM)

            image_accueil=ImageTk.PhotoImage(file="/Users/imac_33/Projet tourisme/image_accuei.jpeg")
            lbl1=Label(frm_reser_1,image=image_accueil,bd=0,width=700,height=600)
            lbl1.place(x=860,y=400)

            frm_date= LabelFrame(frame3,width=800,height=40,bg="white")
            frm_date.place(x=40,y=60,)

            lb_date=Label(frm_date,text="Date",bg="white",font=("sans serif",10))
            lb_date.place(x=5,y=7)
            lb_Entry_date = Entry(frm_date,bg="azure")
            lb_Entry_date.place(x=50,y=6,)

            lb_recu=Label(frm_date,text="N° récu",bg="white",font=("sans serif",10))
            lb_recu.place(x=250,y=7)
            lb_Entry_recu = Entry(frm_date,bg="azure")
            lb_Entry_recu.place(x=350,y=6)

            #--------   --------#

            frm_clt= LabelFrame(frame3,text="Informations sur le client",width=800,height=200,bg="white")
            frm_clt.place(x=40,y=120)

            lb_nom_clt1=Label(frm_clt,text="Nom:",bg="white",font=("sans serif",10))
            lb_nom_clt1.place(x=5,y=20)
            lb_nom_clt_Entry1 = Entry(frm_clt,bg="azure")
            lb_nom_clt_Entry1.place(x=70,y=20)

            lb_prenom_clt2=Label(frm_clt,text="Prenom:",bg="white",font=("sans serif",10))
            lb_prenom_clt2.place(x=5,y=60)
            lb_prenom_clt_Entry2 = Entry(frm_clt,bg="azure")
            lb_prenom_clt_Entry2.place(x=70,y=60,width=510)

            lb_ne_clt3=Label(frm_clt,text="Né(e) Le:",bg="white",font=("sans serif",10))
            lb_ne_clt3.place(x=5,y=100)
            lb_ne_clt_Entry3 = Entry(frm_clt,bg="azure")
            lb_ne_clt_Entry3.place(x=70,y=100)

            lb_a_clt_4=Label(frm_clt,text="A:",bg="white",font=("sans serif",10))
            lb_a_clt_4.place(x=280,y=100)
            lb_a_clt_Entry4 = Entry(frm_clt,bg="azure")
            lb_a_clt_Entry4.place(x=320,y=100)

            lb_contact_clt_5=Label(frm_clt,text="Contact:",bg="white",font=("sans serif",10))
            lb_contact_clt_5.place(x=5,y=140)
            lb_contact_clt_Entry5 = Entry(frm_clt,bg="azure")
            lb_contact_clt_Entry5.place(x=60,y=140,width=300)

            #--------   --------#

            frm_option= LabelFrame(frame3,width=500,height=35,bg="white")
            frm_option.place(x=70,y=340)
            #--------   --------#

            chbre= LabelFrame(frame3,width=800,height=200,bg="white")
            chbre.place(x=40,y=380)

            lb_chbre1=Label(chbre,text="Chambre:",bg="white",font=("sans serif",10),fg="green")
            lb_chbre1.place(x=5,y=20,)
            lb_chbre_Entry1 = Entry(chbre,bg="azure")
            lb_chbre_Entry1.place(x=90,y=20,width=500)

            lb_chbre2=Label(chbre,text="Date d'occupation:",bg="white",font=("sans serif",10))
            lb_chbre2.place(x=5,y=60,)
            lb_chbre_Entry2 = Entry(chbre,bg="azure")
            lb_chbre_Entry2.place(x=135,y=60)

            lb_chbre3=Label(chbre,text="Heure D'arrivée:",bg="white",font=("sans serif",10))
            lb_chbre3.place(x=5,y=100,)
            lb_chbre_Entry3 = Entry(chbre,bg="azure")
            lb_chbre_Entry3.place(x=135,y=100)

            lb_chbre4=Label(chbre,text="Prix Unitaire:",bg="white",font=("sans serif",10))
            lb_chbre4.place(x=5,y=150,)
            lb_chbre_Entry4 = Entry(chbre,bg="azure")
            lb_chbre_Entry4.place(x=135,y=150)

            lb_chbre5=Label(chbre,text="Date De Sorties:",bg="white",font=("sans serif",10))
            lb_chbre5.place(x=345,y=60,)
            lb_chbre_Entry5 = Entry(chbre,bg="azure")
            lb_chbre_Entry5.place(x=450,y=60)

            lb_chbre6=Label(chbre,text="Heure Depart:",bg="white",font=("sans serif",10))
            lb_chbre6.place(x=345,y=100,)
            lb_chbre_Entry6 = Entry(chbre,bg="azure")
            lb_chbre_Entry6.place(x=450,y=100)

            lb_chbre7=Label(chbre,text="Nbre(Heure/Jour) :",bg="white",font=("sans serif",10))
            lb_chbre7.place(x=345,y=140,)
            lb_chbre_Entry7 = Entry(chbre,bg="azure")
            lb_chbre_Entry7.place(x=450,y=140)
            #------------- POINTS DES DIFFERENTES SITUATIONS--------------#
            frm_point= LabelFrame(frame3,text="TOTAL A CE JOUR",font=("sans serif",11),width=760,height=280,bg="white")
            frm_point.place(x=900,y=40)

            lbl_point_1=Label(frm_point,borderwidth=3,text="Total Encaissement",font=("sans serif",0),fg="black")
            lbl_point_1.place(x=105,y=35)
            lbl_point_1_Entry1 = Entry(frm_point,bg="azure")
            lbl_point_1_Entry1.place(x=260,y=35)

            lbl_point_2=Label(frm_point,borderwidth=3,text="Total Enccai Passage",font=("sans serif",0),fg="black")
            lbl_point_2.place(x=105,y=65)
            Entry2_lbl_point2 = Entry(frm_point,bg="azure")
            Entry2_lbl_point2.place(x=260,y=65)

            lbl_point_3=Label(frm_point,borderwidth=3,text="Total Encai Sejours",font=("sans serif",0),fg="black")
            lbl_point_3.place(x=105,y=95)
            Entry3_lbl_point3 = Entry(frm_point,bg="azure")
            Entry3_lbl_point3.place(x=260,y=95)

            lbl_point_4=Label(frm_point,borderwidth=3,text="Total Des Clients",font=("sans serif",0),fg="black")
            lbl_point_4.place(x=105,y=150)
            Entry4_lbl_point4 = Entry(frm_point,bg="azure")
            Entry4_lbl_point4.place(x=260,y=150)

            lbl_point_5=Label(frm_point,borderwidth=3,text="Total Des Passages",font=("sans serif",0),fg="black")
            lbl_point_5.place(x=105,y=180)
            Entry5_lbl_point5 = Entry(frm_point,bg="azure")
            Entry5_lbl_point5.place(x=260,y=180)

            lbl_point_6=Label(frm_point,borderwidth=3,text="Total Des Sejours",font=("sans serif",0),fg="black")
            lbl_point_6.place(x=105,y=210)
            Entry6_lbl_point6 = Entry(frm_point,bg="azure")
            Entry6_lbl_point6.place(x=260,y=210)

            frm_bouton= LabelFrame(frame3,width=100,height=1300,bg="#a1b0c7")
            frm_bouton.place(x=1698,y=40)

            


            
            
            def valider_donnes():

                
                d={
                    "dates": lb_Entry_date.get(),
                    "n_recu":lb_Entry_recu.get(),
                    "nom":lb_nom_clt_Entry1.get(),
                    "prenom":lb_prenom_clt_Entry2.get(),
                    "dates_naiss":lb_ne_clt_Entry3.get(), 
                    "lieux_naiss":lb_a_clt_Entry4.get(),
                    "contact":lb_contact_clt_Entry5.get(),
                    "chambre":lb_chbre_Entry1.get(),
                    "dates_occupation":lb_chbre_Entry2.get(),
                    "heure_arrive":lb_chbre_Entry3.get(),
                    "prix_unitaire":lb_chbre_Entry4.get(),
                    "dates_sortie":lb_chbre_Entry5.get(),
                    "heure_depart":lb_chbre_Entry6.get(),
                    "nombre_heure":lb_chbre_Entry7.get()
                }

                

                
                

                conn=sqlite3.connect('myBD_reservation.db')

                cur =conn.cursor()

            
                cur.execute("""CREATE TABLE IF NOT EXISTS reservations(
                   dates str,
                   nom text,
                   prenom text,
                   dates_naiss text,
                   lieux_naiss text,
                   contact text,
                   chambre text,
                   dates_occupation text,
                   heure_arrive text,
                   prix_unitaire str,
                   dates_sortie text,
                   heure_depard str,
                   nombre_heure str
                )""")

                #mysqldb = mysql.connector.connect(host = "localhost,user = "root",)

                
                cur.execute("INSERT INTO reservations VALUES(:dates, :nom, :prenom, :dates_naiss, :lieux_naiss, :contact, :chambre, :dates_occupation, :heure_arrive, :prix_unitaire, :dates_sortie, :heure_depart, :nombre_heure)",d)
                conn.commit()
                conn.close()
                
                
                if (lb_Entry_date.get() == "" or lb_Entry_recu.get() == "" or lb_nom_clt_Entry1.get() == "" or lb_prenom_clt_Entry2.get() == "" or lb_ne_clt_Entry3.get() == "" or lb_a_clt_Entry4.get()=="" or 
                    lb_contact_clt_Entry5.get() or lb_chbre_Entry1.get() == "" or lb_chbre_Entry2.get() == "" or lb_chbre_Entry3.get() == "" or lb_chbre_Entry4.get() == "" or 
                    lb_chbre_Entry5.get() == "" or lb_chbre_Entry6.get() == "" or lb_chbre_Entry7.get() == ""):
                    
                    messagebox.showerror("Incomplet","veuillez renseigner tout les shamps svp")
                else:
                    messagebox.showwarning("succes","Enregistrer avec succes")
                
                

                

                lb_Entry_date.delete(0,END)
                lb_Entry_recu.delete(0,END)
                lb_nom_clt_Entry1.delete(0,END)
                lb_prenom_clt_Entry2.delete(0,END)
                lb_ne_clt_Entry3.delete(0,END)
                lb_a_clt_Entry4.delete(0,END)
                lb_contact_clt_Entry5.delete(0,END)
                lb_chbre_Entry1.delete(0,END)
                lb_chbre_Entry2.delete(0,END)
                lb_chbre_Entry3.delete(0,END)
                lb_chbre_Entry4.delete(0,END)
                lb_chbre_Entry5.delete(0,END)
                lb_chbre_Entry6.delete(0,END)
                lb_chbre_Entry7.delete(0,END)

            btn_enreg_form =Button(frm_bouton,width=10,height=1,bg="white",text="Enregistrer",highlightbackground="red",highlightthickness=5,fg="green",borderwidth=3,command=valider_donnes)
            btn_enreg_form.place(x=2,y=70)

            def quit():
               frame3.destroy()
            btn_quit_frm_reser1 =Button(frm_bouton,width=10,height=1,bg="white",text="Quitter",highlightbackground="purple",fg="red",borderwidth=3,command=quit)
            btn_quit_frm_reser1.place(x=2,y=120)
            

            
            

            #------------- INSERTION DE LIMAGE DU FRM_POINT(des situations)--------------#

            image_reserva=ImageTk.PhotoImage(file="projet_hotel\téléchargement.jpeg")
            lbl1=Label(frm_reser_1,image=image_reserva,bd=0,width=100,height=300)
            lbl1.place(x=1000,y=400)
        btn4 =Button(frame1,width=10,height=1,bg="#a1b0c7",text="Reservation",highlightbackground="teal",highlightthickness=5,borderwidth=3,command=reservation)
        btn4.place(x=1130,y=5)

        def liste_chambre():
    
            
            frame2= LabelFrame(root,width=1860,height=980,bg="lavender")
            frame2.place(x=0,y=0)

            lbl_titre=Label(frame2,borderwidth=3,text="LISTE DES CHAMBRES",font=("sans serif",20),fg="black")
            lbl_titre.place(x=0,y=0,width=1800)

            frm_cherch= LabelFrame(frame2,width=1000,height=35,bg="white")
            frm_cherch.place(x=70,y=75)

            lbl_rech1=Label(frm_cherch,borderwidth=3,text="Recherche",font=("sans serif",0),fg="black")
            lbl_rech1.place(x=0,y=3)
            lbl_rech1_Entry1 = Entry(frm_cherch)
            lbl_rech1_Entry1.place(x=80,y=3)

            lbl_rech2=Label(frm_cherch,borderwidth=3,text="Periode Du:",font=("sans serif",0),fg="black")
            lbl_rech2.place(x=310,y=3)
            lbl_rech2_Entry1 = Entry(frm_cherch)
            lbl_rech2_Entry1.place(x=400,y=3)

            lbl_rech2=Label(frm_cherch,borderwidth=3,text="AU:",font=("sans serif",0),fg="black")
            lbl_rech2.place(x=590,y=3)
            lbl_rech2_Entry1 = Entry(frm_cherch)
            lbl_rech2_Entry1.place(x=630,y=3)
            

            treeframe = LabelFrame(frame2)
            treeframe.configure(bg="white")
            treeframe.place(x=30,y=150,width=1600,height=1500)


            column = ["Nom Client","Date d'occupation","Date de sortir","Heure D'arriver","Heure de Depart","Chambre","Contact","Montant","Remise","Reglé"]

            myTree = ttk.Treeview(treeframe,height=50,column=column)
            myTree.pack(fill="both")
            myTree['show']='headings'
            for each in column:
                myTree.column(each,width=50)
                myTree.heading(each,text=each.capitalize())
            

            frm_bouton= LabelFrame(frame2,width=130,height=1300,bg="#a1b0c7")
            frm_bouton.place(x=1660,y=40,)

            #details_table= Frame(table_frame,bd=2,relief=RIDGE)
            #details_table.place(x=0,y=75,width=855,height=400)

            #scrol= Scrollbar(treeframe,orient=HORIZONTAL)
            #scrol.pack(side=BOTTOM,fill=X)

            
                 

                
                
                
                
            
                
            
            def quit():
                frame2.destroy()
            btn_quit_chmbre =Button(frm_bouton,width=10,height=2,bg="#a1b0c7",text="Quitter",highlightbackground="red",highlightthickness=5,fg="blue",borderwidth=3,command=quit)
            btn_quit_chmbre.place(x=5,y=75)

            def delete():
                pass
                
            btn_delete_chmbre =Button(frm_bouton,width=10,height=2,bg="#a1b0c7",text="Supprimer",highlightbackground="red",highlightthickness=5,fg="blue",borderwidth=3,command=delete)
            btn_delete_chmbre.place(x=5,y=200)

        btn3 =Button(frame1,width=10,height=1,bg="#a1b0c7",text="Chambres",highlightbackground="blue",highlightthickness=5,borderwidth=3,command=liste_chambre)
        btn3.place(x=1020,y=5)

        

        #scrol= Scrollbar(orient=VERTICAL,width=25)
        #scrol.pack(side=RIGHT,fill= Y)
        #scrol= Scrollbar(root,orient=HORIZONTAL)
        #scrol.pack(side=BOTTOM,fill=X)
            
        
        

        
        
        
        #=====image====
        

        
        

        

root=Tk()
obj=window(root)
root.mainloop()


    