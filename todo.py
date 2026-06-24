from tkinter import *

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected
        listbox.delete(selected)

root = Tk()
root.title("To-Do List")

entry = Entry(root, width=30)
entry.pack()

Button(root, text="Add", command=add_task).pack()
Button(root, text="Delete", command=delete_task).pack()

listbox = Listbox(root)
listbox.pack()

root.mainloop()
