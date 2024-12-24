from tkinter import *
import time

def Counter():
    try:
        start = int(entry1.get())
        while start > 0:
            label1['text'] = start
            start -= 1
            root.update()
            time.sleep(1)
        label1['text'] = "Time's Up!"
    except ValueError:
        label1['text'] = "Invalid input!"






root = Tk()
root.geometry('512x512')

entry1 = Entry(root, font=('', 21), justify=CENTER)
entry1.insert(INSERT, 10)
entry1.place(relx=0.5, rely=0.5, anchor='center')

label1 = Label(root, text='Start From :', font=('Comic Sans MS', 21), justify=CENTER)
label1.place(relx=0.5, rely=0.4, anchor='center')

btn1 = Button(root, text='Count Down', font=('Comic Sans MS', 21), anchor=CENTER, command=Counter)
btn1.place(relx=0.5, rely=0.6, anchor='center')










root.mainloop()