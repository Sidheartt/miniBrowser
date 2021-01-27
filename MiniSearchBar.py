from tkinter import *
import webbrowser
root = Tk()
root.title("Search it")


def search():
    url = entry.get()
    webbrowser.open(url)


label1 = Label(root, text="Enter URL here:  ", font=("arial", 14, "bold"))

label1.grid(row=0, column=0)
entry = Entry(root, width=35)
entry.grid(row=0, column=1)
btn = Button(root, text="Search", command=search, bg="blue", fg="coral", font=("arial", 14, "bold"))
btn.grid(row=1, column=0, columnspan=2, pady=10)
root.mainloop()
