import calendar
print(calendar.prmonth(2013,7))
print(dir(calendar))
print([x for x in dir(calendar) if 'leap' in x])
help(calendar.isleap)
print(calendar.isleap(2077))
# from tkinter import *
# widget = Label(None,text='I love Python!')
# widget.pack()
import math
def hypotenuse(num1,num2):
    # return '{0:.2f}'.format(math.sqrt(num1**2 + num2**2))
    # return round(math.sqrt(num1**2 + num2**2),2)
    return f'{math.sqrt(num1**2 + num2**2):.2f}'

c= calendar.TextCalendar()
print(c.formatmonth(2021,2))

# import tkinter as tk
# s= 'Life is short\nUse Python'
# root = tk.Tk()
# t= tk.Text(root,height=10,width=15)
# t.insert(tk.END,)
# t.pack()
# tk.mainloop()
