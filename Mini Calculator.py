from tkinter import *

def sum():
    try:
        n = float(entry1.get())
        m = float(entry2.get())
        label1['text'] = n + m
    except ValueError:
        label1['text'] = "Invalid input!"

def sub():
    try:
        n = float(entry1.get())
        m = float(entry2.get())
        label1['text'] = n - m
    except ValueError:
        label1['text'] = "Invalid input!"    

def mul():
    try:
        n = float(entry1.get())
        m = float(entry2.get())
        label1['text'] = n * m
    except ValueError:
        label1['text'] = "error!"    

def div():
    try:
        n = float(entry1.get())
        m = float(entry2.get())
        if m == 0:
            label1['text'] = "Error"
        else:
            label1['text'] = n / m
    except ValueError:
        label1['text'] = "Error"    


root = Tk()
root.geometry('512x256')
root.resizable(False, False)
root['bg'] = '#283149'
root.title("Mini Calculator")

entry1 = Entry(root,
               width = 5,
               font = ('Arial', 15, 'bold'),
               bg = '#404b69',
               fg = '#f73859',
               bd = 5,
               relief = 'flat',
               justify = 'center')

entry1.insert(INSERT, '0')
entry1.place(relx = 0.25,
             rely = 0.15,
             anchor = 'center')

entry2 = Entry(root,
               width = 5,
               font = ('Arial', 15, 'bold'),
               bg = '#404b69',
               fg = '#f73859',
               bd = 5,
               relief = 'flat',
               justify = 'center')

entry2.insert(INSERT, '0')
entry2.place(relx = 0.75,
             rely = 0.15,
             anchor = 'center')


btn1 = Button(root,
              font = ('', 15, 'bold'),
              text = "+",
              width = 2,
              height = 2,
              bg = '#f73859',
              fg = '#404b69',
              justify = 'center',
              bd = 5,
              relief = 'flat',
              command = sum)
btn1.place(relx = 0.25,
           rely = 0.4,
           anchor = 'center')
btn2 = Button(root,
              font = ('', 15, 'bold'),
              text = "-",
              width = 2,
              height = 2,
              bg = '#f73859',
              fg = '#404b69',
              justify = 'center',
              bd = 5,
              relief = 'flat',
              command = sub)
btn2.place(relx = 0.25,
           rely = 0.6,
           anchor = 'center')
btn3 = Button(root,
              font = ('', 15, 'bold'),
              text = "*",
              width = 2,
              height = 2,
              bg = '#f73859',
              fg = '#404b69',
              justify = 'center',
              bd = 5,
              relief = 'flat',
              command = mul)
btn3.place(relx = 0.75,
           rely = 0.4,
           anchor = 'center')
btn4 = Button(root,
              font = ('', 15, 'bold'),
              text = "/",
              width = 2,
              height = 2,
              bg = '#f73859',
              fg = '#404b69',
              justify = 'center',
              bd = 5,
              relief = 'flat',
              command = div)
btn4.place(relx = 0.75,
           rely = 0.6,
           anchor = 'center')


label1 = Label(root,
               font = ('', 15, 'bold'),
               width = 10,
               text = "0",
               bg = '#404b69',
               fg = '#f73859',
               justify = 'center',
               bd = 5,
               relief = 'flat')
label1.place(relx = 0.5,
             rely = 0.85,
             anchor = 'center')


root.mainloop()