from tkinter import *

window = Tk()
window.title("Miles to Km Convertor")
window.minsize(width=300, height=300)


def button_clicked():
    miles = entry.get()
    km = "{:.2f}".format(float(miles) * 1.60934)
    entry2.insert(END, str(km))


label = Label(font=("Times New Roman", 12, "normal"), text="The number of miles : ")
label.grid(column=0, row=0)

entry = Entry(width=7)
entry.grid(row=0, column=2)

button = Button(text="Convert", fg="white", bg="black", command=button_clicked)
button.grid(row=1, column=1)

label2 = Label(text="Number of kilometers are : ",font=("Times New Roman", 12, "normal"))
label2.grid(row=2, column=0)

entry2 = Entry(width=7)
entry2.grid(row=2, column=2)


window.mainloop()
