from tkinter import *
window=Tk()

window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='lime')

def calculate_interest():
    p = float(principal.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i,2)
    showlabel.destroy()
    message=Label(result_frame,text="Interest on Rs."+str(p)+" at rate of interest "+str(r)+" for "+str(t)+" years is Rs."+str(interest), bg = "lightcyan", font=("Calibri", 12), width=80)
    message.place(x=20,y=40)
    message.pack()

heading_label=Label(window, text="INTEREST CALCULATOR", fg = "black", bg = "lime", font=("Calibri", 20),bd=5)
heading_label.place(x=50, y=20)

principal_label=Label(window, text="Enter principal amount", fg = "black", bg = "lime", font=("Calibri", 12),bd=1)
principal_label.place(x=20, y=90)

principal = Entry(window, text="", bd=2, width=22)
principal.place(x=170, y=92)

rate_of_interest_label=Label(window, text="Enter rate of interest", fg = "black", bg = "lime", font=("Calibri", 12),bd=1)
rate_of_interest_label.place(x=20, y=140)

rate = Entry(window, text="", bd=2, width=15)
rate.place(x=170, y=142)

time_label=Label(window, text="Enter Time", fg = "black", bg = "lime", font=("Calibri", 12),bd=1)
time_label.place(x=20, y=185)

time=Entry(window, text="", bd=2, width=15)
time.place(x=170, y=187)

calculate_button=Button(window, text="Calculate", fg = "black", bg = "grey", bd=4, command=calculate_interest)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window,text="Result", bg = "lime", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

showlabel=Label(result_frame,text=" ", bg = "lime", font=("Calibri", 12), width=33)
showlabel.place(x=20,y=20)
showlabel.pack()

window.mainloop()