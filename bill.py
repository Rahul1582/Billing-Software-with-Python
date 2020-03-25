from tkinter import*
import math,random


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#90EE90"
        title=Label(self.root,text="BILLING APPLICATION USING PYTHON",bd=12,relief=GROOVE,bg=bg_color,fg='black',font=("Baskerville Old Face",40,"bold"),pady=2).pack(fill=X)
        
        #Variables

        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()

        self.rice=IntVar()
        self.food_oil=IntVar()
        self.dal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()


        self.mazza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()


        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        self.c_name=StringVar()
        self.c_phon=StringVar()
      
        self.bill_no=StringVar()
        x=random.randint(2000,9999)

        self.bill_no.set(str(x))

        self.search_bill=StringVar()








        #========Customer Detail Frame

        F1=LabelFrame(self.root,bd=10,relief=RIDGE,text="Customer Details",font=("Baskerville Old Face",15,"bold"),fg='black',bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lb1=Label(F1,text="Customer Name",bg=bg_color,fg="black",font=("Baskerville Old Face",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,font="Arial 15",textvariable=self.c_name,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lb1=Label(F1,text="Customer Phone No.",bg=bg_color,fg="black",font=("Baskerville Old Face",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,font="Arial 15",textvariable=self.c_phon,bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lb1=Label(F1,text="Bill Number",bg=bg_color,fg="black",font=("Baskerville Old Face",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,font="Arial 15",textvariable=self.search_bill,bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font=("Baskerville Old Face", 10," bold")).grid(row=0,column=6,pady=10,padx=10)


        #Cosmetics Frame

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("Baskerville Old Face",15,"bold"),fg='black',bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lb1=Label(F2,text="Bath Soap",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.soap,bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lb1=Label(F2,text="Face Cream",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.face_cream,bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_w_lb1=Label(F2,text="Face Wash",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.face_wash,bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lb1=Label(F2,text="Hair Serum",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.spray,bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lb1=Label(F2,text="Hair gel",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.gel,bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lb1=Label(F2,text="Body Lotion",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt=Entry(F2,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.lotion,bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)




        # Cold Drink Frame

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("Baskerville Old Face",15,"bold"),fg='black',bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        c1_lb1=Label(F3,text="Mazza",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F3,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.mazza,bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lb1=Label(F3,text="Coke",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F3,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.coke,bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lb1=Label(F3,text="Frooty",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F3,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.frooti,bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lb1=Label(F3,text="Thumbs Up",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F3,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.thumbsup,bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lb1=Label(F3,text="Limca",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F3,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.limca,bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lb1=Label(F3,text="Sprite",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F3,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.sprite,bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



         # Grocery Frame

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Groceries",font=("Baskerville Old Face",15,"bold"),fg='black',bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        g1_lb1=Label(F4,text="Rice",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F4,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.rice,bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lb1=Label(F4,text="Food Oil",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F4,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.food_oil,bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lb1=Label(F4,text="Dal",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F4,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.dal,bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lb1=Label(F4,text="Wheat",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F4,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.wheat,bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lb1=Label(F4,text="Sugar",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F4,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.sugar,bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lb1=Label(F4,text="Tea",font=("Baskerville Old Face",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F4,width=10,font=("Baskerville Old Face",16,"bold"),textvariable=self.tea,bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #Bill Area

        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font=("Baskerville Old Face",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()


        #Button Frame

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("Baskerville Old Face",15,"bold"),fg='black',bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1=Label(F6,text="Total Cosmetics Price",bg=bg_color,fg="black",font=("Baskerville Old Face",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky='w')
        m1_txt=Entry(F6,width=18,font=("Baskerville Old Face", 10," bold"),textvariable=self.cosmetic_price,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Grocery Price",bg=bg_color,fg="black",font=("Baskerville Old Face",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky='w')
        m2_txt=Entry(F6,width=18,font=("Baskerville Old Face", 10," bold"),textvariable=self.grocery_price,bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="black",font=("Baskerville Old Face",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky='w')
        m3_txt=Entry(F6,width=18,font=("Baskerville Old Face", 10," bold"),textvariable=self.cold_drink_price,bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1=Label(F6,text="Cosmetics Tax",bg=bg_color,fg="black",font=("Baskerville Old Face",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky='w')
        c1_txt=Entry(F6,width=18,font=("Baskerville Old Face", 10," bold"),textvariable=self.cosmetic_tax,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2=Label(F6,text="Grocery Tax",bg=bg_color,fg="black",font=("Baskerville Old Face",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky='w')
        c2_txt=Entry(F6,width=18,font=("Baskerville Old Face", 10," bold"),textvariable=self.grocery_tax,bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="black",font=("Baskerville Old Face",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky='w')
        c3_txt=Entry(F6,width=18,font=("Baskerville Old Face", 10," bold"),textvariable=self.cold_drink_tax,bd=7,relief=RIDGE).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=770,width=540,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=15).grid(row=0,column=0,padx=5,pady=5)
        Gbill_btn=Button(btn_F,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",pady=15,width=15).grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",pady=15,width=15).grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",pady=15,width=15).grid(row=0,column=3,padx=5,pady=5)

        self.welcome_bill()


    def total(self):

            self.sp= self.soap.get()*40
            self.fc=(self.face_cream.get()*120)
            self.fw=(self.face_wash.get()*60)
            self.spr=(self.spray.get()*180)
            self.ge=(self.gel.get()*140)
            self.lo=(self.lotion.get()*180)

            self.total_cosmetic_price=float(
                                        self.sp+
                                       self.fc+
                                       self.fw+
                                       self.spr+
                                       self.ge+
                                       self.lo
                                       
                                       )

            self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))

            self.cosmetic_tax.set("Rs. "+str(round((self.total_cosmetic_price*0.05),2)))


            self.ri=(self.rice.get()*80)
            self.fo=(self.food_oil.get()*180)
            self.da=(self.dal.get()*60)
            self.wh= (self.wheat.get()*240)
            self.su=(self.sugar.get()*45)
            self.te=(self.tea.get()*150)


            self.total_grocery_price=float(
                                       self.ri+
                                       self.fo+
                                       self.da+
                                      self.wh+
                                       self.su+
                                       self.te
                                       
                                       )

            self.grocery_price.set("Rs. " +str(self.total_grocery_price))
            self.grocery_tax.set("Rs. "+str(round((self.total_grocery_price*0.1),2)))
            
            
            self.ma=(self.mazza.get()*60)
            self.co= (self.coke.get()*60)
            self.fr=(self.frooti.get()*50)
            self.th=(self.thumbsup.get()*45)
            self.lm=(self.limca.get()*40)
            self.sprt=(self.sprite.get()*60)

            self.total_cold_drink_price=float(
                                       self.ma+
                                      self.co+
                                      self.fr +
                                        self.th+
                                       self.lm+
                                       self.sp
                                       
                                       )

            self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
            self.cold_drink_tax.set("Rs. "+str(round((self.total_cold_drink_price*0.05),2)))

    def welcome_bill(self):
         self.txtarea.delete('1.0',END)
         self.txtarea.insert(END,"\tWELCOME TO OUR RETAIL SHOP\n")
         self.txtarea.insert(END,f"\n BILL NUMBER {self.bill_no.get()}")
         self.txtarea.insert(END,f"\n CUSTOMER NAME {self.c_name.get()}")
         self.txtarea.insert(END,f"\n PHONE NUMBER {self.c_phon.get()}")
         self.txtarea.insert(END,f"\n*************************************")
         self.txtarea.insert(END,f"\n*************************************")
         self.txtarea.insert(END,f"\n PRODUCTS\t\t QTY \t\t PRICE")
         self.txtarea.insert(END,f"\n*************************************")
         self.txtarea.insert(END,f"\n*************************************")



    def bill_area(self):
        self.welcome_bill()
        if self.soap.get()!=0:
            self.txtarea.insert(END,f"\n BATH SOAP \t\t {self.soap.get()}\t\t {self.sp}")

        if self.face_cream.get()!=0:
            self.txtarea.insert(END,f"\n FACE CREAM \t\t {self.face_cream.get()}\t\t {self.fc}")

        if self.face_wash.get()!=0:
            self.txtarea.insert(END,f"\n FACE WASH \t\t {self.face_wash.get()}\t\t {self.fw}")
             
        if self.spray.get()!=0:
            self.txtarea.insert(END,f"\n HAIR SPRAY \t\t {self.spray.get()}\t\t {self.spr}")

        if self.gel.get()!=0:
            self.txtarea.insert(END,f"\n HAIR GEL \t\t {self.gel.get()}\t\t {self.ge}")
 
        if self.lotion.get()!=0:
            self.txtarea.insert(END,f"\n BODY LOTION \t\t {self.lotion.get()}\t\t {self.lo}")




        if self.mazza.get()!=0:
            self.txtarea.insert(END,f"\n MAZZA \t\t {self.mazza.get()}\t\t {self.ma}")

        if self.coke.get()!=0:
            self.txtarea.insert(END,f"\n COKE \t\t {self.coke.get()}\t\t {self.co}")

        if self.frooti.get()!=0:
            self.txtarea.insert(END,f"\n FROOTI \t\t {self.frooti.get()}\t\t {self.fr}")
             
        if self.thumbsup.get()!=0:
            self.txtarea.insert(END,f"\n THUMBS UP \t\t {self.thumbsup.get()}\t\t {self.th}")

        if self.limca.get()!=0:
            self.txtarea.insert(END,f"\n LIMCA \t\t {self.limca.get()}\t\t {self.lm}")
 
        if self.sprite.get()!=0:
            self.txtarea.insert(END,f"\n SPRITE \t\t {self.sprite.get()}\t\t {self.sprt}")    
            




        if self.rice.get()!=0:
            self.txtarea.insert(END,f"\n RICE \t\t {self.rice.get()}\t\t {self.ri}")

        if self.dal.get()!=0:
            self.txtarea.insert(END,f"\n DAL \t\t {self.dal.get()}\t\t {self.da}")

        if self.food_oil.get()!=0:
            self.txtarea.insert(END,f"\n FOOD OIL \t\t {self.food_oil.get()}\t\t {self.fo}")
             
        if self.wheat.get()!=0:
            self.txtarea.insert(END,f"\n WHEAT \t\t {self.wheat.get()}\t\t {self.wh}")

        if self.sugar.get()!=0:
            self.txtarea.insert(END,f"\n SUGAR \t\t {self.sugar.get()}\t\t {self.su}")
 
        if self.tea.get()!=0:
            self.txtarea.insert(END,f"\n TEA \t\t {self.tea.get()}\t\t {self.te}")


root=Tk()
obj=Bill_App(root)
root.mainloop()