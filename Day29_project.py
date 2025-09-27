import tkinter
from tkinter import PhotoImage
from tkinter import messagebox
import random
import pyperclip
window = tkinter.Tk()
window.title('Password Manager')
window.configure(background='white',padx=50,pady=50)

#add the data into txt file when add button is clicked.
def add_button():
    if len(entry1.get())==0 or len(entry2.get())==0 or len(entry3.get())==0:
        messagebox.showerror("Error","Please enter all fields")
    else:
        is_okay = messagebox.askyesno("Account info", "Do you really want to Save it?")
        if is_okay:
            file=open("C:/Users/IT LAND/Desktop/Ali/Python is my Love/Day29/data.txt","a")
            file.write(f"{entry1.get()} | {entry2.get()} | {entry3.get()}|\n")
            file.close()
            entry1.delete(0,len(entry1.get()))
            entry3.delete(0,len(entry3.get()))

#If Generate Button is pressed.
def generate_password():
    capital="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    capital1=capital.split(",")
    small="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    small1=small.split(",")
    special="!,@,$,%,&,?"
    special1=special.split(",")
    string1=""

    for e in range(1,2):
        cap=random.choice(capital1)
        string1+=str(cap)
    for f in range(1,4):
        sml=random.choice(small1)
        string1+=str(sml)
    for g in range(1,4):
        nm=random.randint(0,10)
        string1+=str(nm)
    for h in range(1,2):
        sp=random.choice(special1)
        string1+=str(sp)
    entry3.insert(0,string1)
    pyperclip.copy(string1)

#Generate image, labels, entries and buttons
picture=PhotoImage(file="C:/Users/IT LAND/Desktop/Ali/Python is my Love/Day29/logo.png")
canvas = tkinter.Canvas(window,width=200,height=200,background='white',highlightthickness=0)
canvas.create_image(100,100,image=picture)
label1 = tkinter.Label(window,text='Website:',background='white',fg='black')
label2 = tkinter.Label(window,text='Email/Username:',background='white',fg='black')
label3 = tkinter.Label(window,text='Password:',background='white',fg='black')
entry1 = tkinter.Entry(window,background='white',fg='black',width=52)
entry2 = tkinter.Entry(window,background='white',fg='black',width=52)
entry3 = tkinter.Entry(window,background='white',fg='black',width=33)
button1 = tkinter.Button(window,text='Generate Password',background='white',fg='black',command=generate_password)
button2 = tkinter.Button(window,text='Add',background='white',fg='black',width=44,command=add_button)

#Place all the Labels entries and button on places
canvas.grid(row=1,column=2)
label1.grid(row=2,column=1)
label2.grid(row=3,column=1)
label3.grid(row=4,column=1)
entry1.grid(row=2,column=2,columnspan=2)
entry1.focus()
entry2.grid(row=3,column=2,columnspan=2)
entry2.insert(0,'alikhan5727@gmail.com')
entry3.grid(row=4,column=2)
button1.grid(row=4,column=3)
button2.grid(row=5,column=2,columnspan=2)




window.mainloop()