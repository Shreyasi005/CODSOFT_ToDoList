import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task)

def delete_task():
    selected = listbox_tasks.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_listbox()


window = tk.Tk()
window.title("To-Do List")
window.geometry("400x400")

label_title = tk.Label(window, text="📝 To-Do List", font=("Arial", 18, "bold"))
label_title.pack(pady=10)

entry_task = tk.Entry(window, width=30)
entry_task.pack(pady=5)

btn_add = tk.Button(window, text="Add Task", width=15, command=add_task)
btn_add.pack(pady=5)

listbox_tasks = tk.Listbox(window, width=45, height=10)
listbox_tasks.pack(pady=10)

btn_delete = tk.Button(window, text="Delete Task", width=15, command=delete_task)
btn_delete.pack(pady=5)

btn_clear = tk.Button(window, text="Clear All", width=15, command=clear_tasks)
btn_clear.pack(pady=5)

window.mainloop()