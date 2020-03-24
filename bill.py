from tkinter import*

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg='white',font=("Times New Roman",35,"bold"),pady=2).pack(fill=X)
        
        #========Customer Detail Frame

        F1=LabelFrame(self.root,text="Customer Details",font=("Times New Roman",15,"bold"),fg='gold',bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lb1=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("Times New Roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lb1=Label(F1,text="Customer Phone No.",bg=bg_color,fg="white",font=("Times New Roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lb1=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("Times New Roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1)

        















root=Tk()
obj=Bill_App(root)
root.mainloop()