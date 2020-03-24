from tkinter import*

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg='white',font=("Times New Roman",35,"bold"),pady=2).pack(fill=X)
        
        #========Customer Detail Frame

        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("Times New Roman",15,"bold"),fg='gold',bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lb1=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("Times New Roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lb1=Label(F1,text="Customer Phone No.",bg=bg_color,fg="white",font=("Times New Roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lb1=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("Times New Roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 15 bold").grid(row=0,column=6,pady=10,padx=10)


        #Cosmetics Frame

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("Times New Roman",15,"bold"),fg='gold',bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lb1=Label(F2,text="Bath Soap",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lb1=Label(F2,text="Face Cream",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_w_lb1=Label(F2,text="Face Wash",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lb1=Label(F2,text="Hair Serum",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lb1=Label(F2,text="Hair gel",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lb1=Label(F2,text="Body Lotion",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt=Entry(F2,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)




        # Cold Drink Frame

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("Times New Roman",15,"bold"),fg='gold',bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        c1_lb1=Label(F3,text="Mazza",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F3,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lb1=Label(F3,text="Coke",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F3,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lb1=Label(F3,text="Frooty",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F3,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lb1=Label(F3,text="Thumbs Up",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F3,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lb1=Label(F3,text="Limca",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F3,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lb1=Label(F3,text="Sprite",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F3,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



         # Grocery Frame

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Groceries",font=("Times New Roman",15,"bold"),fg='gold',bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        g1_lb1=Label(F4,text="Rice",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F4,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lb1=Label(F4,text="Food Oil",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F4,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lb1=Label(F4,text="Dal",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F4,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lb1=Label(F4,text="Wheat",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F4,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lb1=Label(F4,text="Sugar",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F4,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lb1=Label(F4,text="Tea",font=("Times New Roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F4,width=10,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #Bill Area

        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()


        #Button Frame

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("Times New Roman",15,"bold"),fg='gold',bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1=Label(F6,text="Total Cosmetics Price",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky='w')
        m1_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Grocery Price",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky='w')
        m2_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky='w')
        m3_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1=Label(F6,text="Cosmetics Tax",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky='w')
        c1_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2=Label(F6,text="Grocery Tax",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky='w')
        c2_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="lightgreen",font=("Times New Roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky='w')
        c3_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=770,width=540,height=105)

        total_btn=Button(btn_F,text="Total",bg="cadetblue",fg="white",pady=15,width=15).grid(row=0,column=0,padx=5,pady=5)
        Gbill_btn=Button(btn_F,text="Generate Bill",bg="cadetblue",fg="white",pady=15,width=15).grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",pady=15,width=15).grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",pady=15,width=15).grid(row=0,column=3,padx=5,pady=5)









root=Tk()
obj=Bill_App(root)
root.mainloop()