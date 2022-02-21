
from tkinter import *
from subprocess import call
from tkinter import ttk
import tkinter
from wsgiref.handlers import format_date_time
from PIL import Image,ImageTk


class window:
    def __init__(self,root):
        self.root=root
        self.root.title("ENOTEL BEACH")
        self.root.geometry("2048x1368+640+100")
        #========== les frame de ma fenetre principale =======#
        frame1= LabelFrame(root,width=1973,height=60,bg="#a1b0c7")
        frame1.place(x=0,y=0)

        frame_footer= LabelFrame(root,width=2000,height=98,bg="#a1b0c7")
        frame_footer.pack(side=BOTTOM)
        #========== les boutons de ma fenetre principale =======#
        btn1 = Button(frame1,width=10,height=2,bg="teal",text="Accueil",highlightbackground="white",borderwidth=10)
        btn1.place(x=800,y=5)
        #========== les image de ma fenetre principale =======#
        self.image_accueil=ImageTk.PhotoImage(file="/Users/imac_33/Projet tourisme/image_accuei.jpeg")
        self.lbl1=Label(self.root,image=self.image_accueil,bd=0,width=1973,height=368)
        self.lbl1.place(x=0,y=60)

        
        #==========  =======#
        def toogle_win():
            f1=Frame(root,width=200,height=800,bg="#262626")
            f1.place(x=0,y=0)

            def dele():
                f1.destroy()
            global img2
            img2=ImageTk.PhotoImage(Image.open("close.png"))
            
            Button(f1,text="close",image=img2,command=dele,border=0,activebackground="#12c4c0",bg="#12c4c0").place(x=5,y=10)
            
        #img1=ImageTk.PhotoImage(Image.open("hamberger.png"))
            
        Button(root,command=toogle_win,text="open").place(x=5,y=10)

        
        
        

        """self.image2=ImageTk.PhotoImage(file="img2.jpeg")
        self.lbl2=Label(self.root,image=self.image2,bd=0)
        self.lbl2.place(x=500,y=200)
        self.x=500
        self.slider_fonct

        self.image3=ImageTk.PhotoImage(file="téléchargement.jpeg")
        self.lbl2=Label(self.root,image=self.image3,bd=0)
        self.lbl2.place(x=800,y=200)
        self.x=500
        self.slider_fonct()"""

        l4=Label(root,text="MIEUX SE DIVERTIR CEST BIEN CHOISIR LENDROIT\n",bg="white",font=("sans serif",25))
        l4.place(x=650,y=480)

        l5=Label(root,text="Le cadre\nSTORIA PALACE est un l'une des meilleurs hotels de San-pedro,situee plus précisement dans le quartier balmaire epargné par les construction glopantes,\n une petite crique acec plage privée entre deux énorme rochers rouge abrite la storia palace ",bg="white",font=("sans serif",15))
        l5.place(x=450,y=550)

        l5=Label(root,text="Le cadre\nSTORIA PALACE est un l'une des meilleurs hotels de San-pedro,situee plus précisement dans le quartier balmaire epargné par les construction glopantes,\n une petite crique acec plage privée entre deux énorme rochers rouge abrite la storia palace ",bg="white",font=("sans serif",15))
        l5.place(x=450,y=650)

        

        #l5=Label(frame_footer,text="www.Palmsshetan.com",bg="#c4c0c0")
        #l5.place(x=450,y=5)

        l6=Label(frame_footer,text="Copyright ©  2010-2022 Storia palace, Tous droits réservés.",bg="#c4c0c0")
        l6.place(x=550,y=10)

        l7=Label(frame_footer,text="Contacts \n 07-77-50-71-39\n01-73-24-29-18",font=("Bahnschrift Light",15,"bold"),bg="#c4c0c0",fg="gold")
        l7.place(x=1550,y=5)

        lbtitre= Label(frame_footer,text="VOTRE BIEN-ETRE,NOTRE PRIORITE",font=("sans serif",25),background="white",foreground="lavender",relief=SUNKEN)
        lbtitre.place(x=2500,y=200)


        #self.root2=root
        #self.root2.title(" BEACH")
        #self.root2.geometry("2048x1368+640+100")

        
            
        #btn2 =Button(frame1,width=10,height=2,bg="teal",text="Nos hotels",highlightbackground="white",borderwidth=10)
        #btn2.place(x=900,y=5)
        def visite():
            
            frame_vsite= LabelFrame(root,width=1800,height=926,bg="lavender")
            frame_vsite.place(x=50,y=80)

            l4=Label(frame_vsite,text="MIEUX SE DIVERTIR CEST BIEN CHOISIR LENDROIT\n",bg="lavender",font=("sans serif",25))
            l4.place(x=650,y=0)

            

            def quit():
                frame_vsite.destroy()
            btn_quit_visit =Button(frame_vsite,width=10,height=2,bg="teal",text="Quitter",highlightbackground="red",fg="blue",borderwidth=10,command=quit)
            btn_quit_visit.place(x=1685,y=200)
            
            #frame_chbr1= LabelFrame(frame1,width=1800,height=926,bg="lavender")
            #frame_chbr1.place(x=50,y=80)

            

                
                
            def quit():
                frame_vsite.destroy()
            btn_quit_chmbre =Button(frame_vsite,width=10,height=2,bg="teal",text="Quitter",highlightbackground="red",fg="blue",borderwidth=10,command=quit)
            btn_quit_chmbre.place(x=1685,y=100)

            def voir_phto():
                

                frame_voir= LabelFrame(root,width=1800,height=926,bg="lavender")
                frame_voir.place(x=50,y=80)

            photo1 = PhotoImage(file="/Users/imac_33/Projet tourisme/win1_img.png")
            photoimage = photo1.subsample(5,5)
            Button(frame_vsite,text="voir",image=photoimage,compound=BOTTOM,command=voir_phto,width=100,height=100).place(x=100,y=200)
            #photo1 = PhotoImage(file="image_accueil.png")
            #photoimage = photo1.subsample(5,5)
            #Button(frame_vsite,text="voir",image=photoimage,command=voir_phto)

            """imagCadre4 = ImageTk.PhotoImage(Image.open("téléchargement.jpeg"))
            img_label4=Label(frame_vsite,image= imagCadre4, width=600, height=450)
            img_label4.place(x=300,y=400)

            self.image_accueil=ImageTk.PhotoImage(file="/Users/imac_33/Projet tourisme/image_accuei.jpeg")
            self.lbl1=Label(frame_vsite,image=self.image_accueil,text="voir",bd=0,width=1500,height=150)
            self.lbl1.place(x=300,y=500)"""

            

                
            
            #photo1=PhotoImage(file=r"/Users/imac_33/Projet tourisme/image_accueil.png")
            #Button(frame_vsite,text="Voir",image=photo1,command=voir_phto).pack(side=LEFT)
        btn2 =Button(frame1,width=10,height=2,bg="teal",text="Visitez",highlightbackground="red",borderwidth=10,command=visite)
        btn2.place(x=900,y=5)

        def chambre():

            
            frame2= LabelFrame(root,width=1800,height=926,bg="lavender")
            frame2.place(x=50,y=80)

            lbl_titre=Label(frame2,borderwidth=3,text="LISTE DES CHAMBRE",font=("sans serif",35),fg="black")
            lbl_titre.place(x=0,y=0,width=1800)

            frm_cherch= LabelFrame(frame2,width=1000,height=45,bg="white")
            frm_cherch.place(x=70,y=75)

            lbl_rech1=Label(frm_cherch,borderwidth=3,text="Recherche",font=("sans serif",0),fg="black")
            lbl_rech1.place(x=0,y=5)
            lbl_rech1_Entry1 = Entry(frm_cherch)
            lbl_rech1_Entry1.place(x=80,y=5)

            lbl_rech2=Label(frm_cherch,borderwidth=3,text="Periode Du:",font=("sans serif",0),fg="black")
            lbl_rech2.place(x=310,y=5)
            lbl_rech2_Entry1 = Entry(frm_cherch)
            lbl_rech2_Entry1.place(x=400,y=5)

            lbl_rech2=Label(frm_cherch,borderwidth=3,text="AU:",font=("sans serif",0),fg="black")
            lbl_rech2.place(x=590,y=5)
            lbl_rech2_Entry1 = Entry(frm_cherch)
            lbl_rech2_Entry1.place(x=630,y=5)
            

            treeframe = LabelFrame(frame2)
            treeframe.configure(bg="white")
            treeframe.place(x=10,y=150,width=1670,height=750)

            column = ["Nom Client","Date d'occupation","Date de sortir","Heure D'arriver","Heure de Depart","Chambre","Montant","Remise","Reglé"]

            myTree = ttk.Treeview(treeframe,height=200,column=column)
            myTree.pack(fill="both")
            myTree['show']='headings'
            for each in column:
                myTree.column(each,width=150)
                myTree.heading(each,text=each.capitalize())
            
            def quit():
                frame2.destroy()
            btn_quit_chmbre =Button(frame2,width=10,height=2,bg="teal",text="Quitter",highlightbackground="red",fg="blue",borderwidth=10,command=quit)
            btn_quit_chmbre.place(x=1685,y=100)
        btn3 =Button(frame1,width=10,height=2,bg="teal",text="Chambres",highlightbackground="white",borderwidth=10,command=chambre)
        btn3.place(x=1000,y=5)
        #---------------Reservation----------------#
        def reservation():

            frame3= LabelFrame(root,width=1800,height=926,bg="lavender")
            frame3.place(x=50,y=80)

            lbl_re=Label(frame3,borderwidth=3,text="ALLOCATION DES CHAMBRES AUX CLIENTS",font=("sans serif",35),fg="black")
            lbl_re.place(x=0,y=0,width=1800)
            def quit():
                frame3.destroy()
            
            frm_reser_1= LabelFrame(frame3,width=1600,height=800,bg="white")
            frm_reser_1.place(x=60,y=80)

            self.image_accueil=ImageTk.PhotoImage(file="/Users/imac_33/Projet tourisme/image_accuei.jpeg")
            self.lbl1=Label(frm_reser_1,image=self.image_accueil,bd=0,width=770,height=350)
            self.lbl1.place(x=860,y=400)

            image1=ImageTk.PhotoImage(file="img2.jpeg")
            lbl1=Label(frame3,image=image1,bd=0)
            lbl1.place(x=400,y=100)

            frm_date= LabelFrame(frame3,width=600,height=50,bg="white")
            frm_date.place(x=70,y=90)

            lb1=Label(frm_date,text="Date",bg="white",font=("sans serif",15))
            lb1.place(x=5,y=10)
            lb_Entry1 = Entry(frm_date)
            lb_Entry1.place(x=50,y=10)

            lb2=Label(frm_date,text="N° récu",bg="white",font=("sans serif",15))
            lb2.place(x=250,y=10)
            lb_Entry2 = Entry(frm_date)
            lb_Entry2.place(x=350,y=10)

            frm_clt= LabelFrame(frame3,text="Informations sur le client",width=800,height=300,bg="white")
            frm_clt.place(x=70,y=150)

            lb_clt1=Label(frm_clt,text="Nom:",bg="white",font=("sans serif",15))
            lb_clt1.place(x=5,y=20)
            lb_Entry1 = Entry(frm_clt)
            lb_Entry1.place(x=70,y=20)

            lb_clt2=Label(frm_clt,text="Prenom:",bg="white",font=("sans serif",15))
            lb_clt2.place(x=5,y=60)
            lb_Entry2 = Entry(frm_clt)
            lb_Entry2.place(x=70,y=60,width=510)

            lb_clt3=Label(frm_clt,text="Né(e) Le:",bg="white",font=("sans serif",15))
            lb_clt3.place(x=5,y=100)
            lb_Entry3 = Entry(frm_clt)
            lb_Entry3.place(x=70,y=100)

            lb_clt3_4=Label(frm_clt,text="A:",bg="white",font=("sans serif",15))
            lb_clt3_4.place(x=280,y=100)
            lb_Entry1 = Entry(frm_clt)
            lb_Entry1.place(x=320,y=100)

            lb_clt3_4=Label(frm_clt,text="Contact:",bg="white",font=("sans serif",15))
            lb_clt3_4.place(x=5,y=140)
            lb_Entry1 = Entry(frm_clt)
            lb_Entry1.place(x=60,y=140,width=300)


            frm_option= LabelFrame(frame3,width=600,height=50,bg="white")
            frm_option.place(x=85,y=480)

            chbre= LabelFrame(frame3,width=800,height=300,bg="white")
            chbre.place(x=70,y=560)

            lb_clt1=Label(chbre,text="Chambre:",bg="white",font=("sans serif",15),fg="green")
            lb_clt1.place(x=5,y=20,)
            lb_Entry1 = Entry(chbre)
            lb_Entry1.place(x=90,y=20,width=500)

            lb_clt1=Label(chbre,text="Date d'occupation:",bg="white",font=("sans serif",15))
            lb_clt1.place(x=5,y=60,)
            lb_Entry1 = Entry(chbre)
            lb_Entry1.place(x=135,y=60)

            lb_clt1=Label(chbre,text="Heure d'arrivée:",bg="white",font=("sans serif",15))
            lb_clt1.place(x=5,y=100,)
            lb_Entry1 = Entry(chbre)
            lb_Entry1.place(x=135,y=100)

            lb_clt2=Label(chbre,text="Prix unitaire:",bg="white",font=("sans serif",15))
            lb_clt2.place(x=5,y=150,)
            lb_Entry1 = Entry(chbre)
            lb_Entry1.place(x=135,y=150)

            lb_clt1=Label(chbre,text="Date de sortir:",bg="white",font=("sans serif",15))
            lb_clt1.place(x=345,y=60,)
            lb_Entry1 = Entry(chbre)
            lb_Entry1.place(x=450,y=60)

            lb_clt1=Label(chbre,text="Heure Depart:",bg="white",font=("sans serif",15))
            lb_clt1.place(x=345,y=100,)
            lb_Entry1 = Entry(chbre)
            lb_Entry1.place(x=450,y=100)

            image_reserva=ImageTk.PhotoImage(file="/Users/imac_33/Projet tourisme/image_accueil.png")
            lbl1=Label(frm_reser_1,image=image_reserva,bd=0,width=100,height=300)
            lbl1.place(x=500,y=400)

            #frm_clt= LabelFrame(frame3,text="Informations sur le client",width=600,height=500,bg="white")
            #frm_clt.place(x=70,y=150)
            
            btn_quit =Button(frame3,width=10,height=2,bg="teal",text="Quitter",highlightbackground="red",fg="blue",borderwidth=10,command=quit)
            btn_quit.place(x=1685,y=100)
        btn4 =Button(frame1,width=10,height=2,bg="teal",text="Reservation",highlightbackground="white",borderwidth=10,command=reservation)
        btn4.place(x=1100,y=5)

    

        #scrol= Scrollbar(orient=VERTICAL,width=25)
        #scrol.pack(side=RIGHT,fill= Y)
        #scrol= Scrollbar(root,orient=HORIZONTAL)
        #scrol.pack(side=BOTTOM,fill=X)
        
        

        
        
        
        #=====image====
        

        
        

        

"""def slider_fonct(self):
        
        self.x-=1
        if self.x==0:
            self.x=500

            #self.new_im=self.image1
            self.image1=self.image2
            self.image2=self.image3
        self.lbl2.place(x=self.x,y=200)
        self.lbl2.after(1,self.slider_fonct)"""     
root=Tk()
obj=window(root)
root.mainloop()


    