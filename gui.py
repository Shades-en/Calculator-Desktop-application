from tkinter import *

root=Tk()

#text input area
space=Entry(root, width=35 , borderwidth=5)
space.grid(row=0, column=0, columnspan=3,padx=100)

list_of_numbers=[]
#funtion to get numbers

def number_input(number):
    current_value=space.get()
    space.delete(0, END)
    space.insert(0,str(current_value)+str(number))


def clear_value():
    list_of_numbers.clear()
    space.delete(0,END)


def sum_of_values():
    num1=space.get()
    list_of_numbers.append(num1)
    space.delete(0,END)


def equals():
    num1=space.get()
    list_of_numbers.append(num1)
    space.delete(0,END)

    SUM=0
    for values in list_of_numbers:
        SUM+=int(values)

    space.insert(0,str(SUM))



#buttons 9-0, add buttn, clear, equals
buttn9= Button(root, text='9', padx=40, pady=20, command = lambda: number_input(9)).grid(row=1, column=0)
buttn8= Button(root, text='8', padx=40, pady=20, command = lambda: number_input(8)).grid(row=1, column=1)
buttn7= Button(root, text='7', padx=40, pady=20, command = lambda: number_input(7)).grid(row=1, column=2)

buttn6= Button(root, text='6', padx=40, pady=20, command = lambda: number_input(6)).grid(row=2, column=0)
buttn5= Button(root, text='5', padx=40, pady=20, command = lambda: number_input(5)).grid(row=2, column=1)
buttn4= Button(root, text='4', padx=40, pady=20, command = lambda: number_input(4)).grid(row=2, column=2)

buttn3= Button(root, text='3', padx=40, pady=20, command = lambda: number_input(3)).grid(row=3, column=0)
buttn2= Button(root, text='2', padx=40, pady=20, command = lambda: number_input(2)).grid(row=3, column=1)
buttn1= Button(root, text='1', padx=40, pady=20, command = lambda: number_input(1)).grid(row=3, column=2)

buttn0= Button(root, text='0', padx=40, pady=20, command = lambda: number_input(0)).grid(row=4, column=0)

buttn_add= Button(root, text='+', padx=40, pady=20, command = sum_of_values).grid(row=4, column=1,columnspan=2)
buttn_clear= Button(root, text='clear', padx=40, pady=20, command = clear_value).grid(row=5, column=0)
buttn_equals= Button(root, text='=', padx=40, pady=20, command = equals).grid(row=5, column=1,columnspan=2)


root.mainloop()