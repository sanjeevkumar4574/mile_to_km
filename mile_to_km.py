from tkinter import *

windom = Tk()

windom.title('mile to kilometer convertor')
windom.config(padx=20,pady= 20,bg ='white')

# Entry widget to get input in miles.
entry = Entry(width=7, background ='red')
entry.grid(column =1, row=0)

# label1
label1 = Label(text= 'Miles', background ='white')
label1.grid(column=2, row=0)

# create function for calculate mile to kilometer.
def calculate():
    inp = float(entry.get())
    km = round(inp*1.609)
    label4.config(text=f'{km}')


#label2
label2 = Label(text = 'is equal to',background ='white')
label2.grid(column=0,row=1)

#label3
label3 = Label(text = 'km',background ='white')
label3.grid(column=2,row=1)

label4 = Label(text ='0',background ='white')
label4.grid(column=1,row=1)

# button for calculate mile in kilometer.
btn = Button(text ='Calculate',command =calculate)
btn.grid(column=1,row=3)

windom.mainloop()