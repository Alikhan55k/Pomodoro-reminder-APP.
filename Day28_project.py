import tkinter
from tkinter import PhotoImage
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
steps=[1,5,25,5,25,5,25,20]
loop_no=0
number=steps[loop_no]*60
def rep(number):
    global loop_no
    if loop_no == 0 or loop_no == 2 or loop_no == 3 or loop_no ==5:
        label1.config(text="Work")
    elif loop_no == 7:
        label1.config(text="Long break",fg=RED)
    else:
        label1.config(text="Short Break",fg=PINK )
    if number>=0:
        min=int(number/60)
        if min<10:
            min=f"0{min}"
        sec=number%60
        if sec<10:
            sec=f"0{sec}"
        number -= 1
        canvas.itemconfig(timer_text,text=(f"{min}:{sec}"))
        window.after(1000,rep,number)
    else:
        loop_no+=1
        if loop_no==8:
            loop_no=0
        number=steps[loop_no]*60
        window.after(1000, rep, number)
def start_button():
    if label1["text"]=="Timer":
        window.after(1000,rep,number)
def reset_button():
    global loop_no
    loop_no=0
    window.after_cancel()
    window.after(1000,rep,number)
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50,bg=YELLOW)
label1 = tkinter.Label(window, text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
label2=tkinter.Label(text='✔',fg=GREEN,bg=YELLOW)
button1=tkinter.Button(window, text="Start",font=(FONT_NAME,10,"bold"),bg=YELLOW,command=start_button)
button2=tkinter.Button(window, text="Reset",font=(FONT_NAME,10,"bold"),bg=YELLOW,command=reset_button)
canvas = tkinter.Canvas(window, width=200, height=223,bg=YELLOW)
image=PhotoImage(file="tomato/tomato.png")
canvas.create_image(102,112,image=image)
timer_text=canvas.create_text(102,130,text="00:00",font=(FONT_NAME,35,'bold'),fill='white')
label1.grid(row=0,column=2)
canvas.grid(row=1,column=2)
button1.grid(row=3,column=0)
label2.grid(row=3,column=2)
button2.grid(row=3,column=3)



window.mainloop()