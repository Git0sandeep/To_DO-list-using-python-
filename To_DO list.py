from tkinter import *

class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.listbox = Listbox(self.root)
        self.entry = Entry(self.root)
        self.addButton = Button(self.root, text="Add Task", command=self.add_task)
        self.delButton = Button(self.root, text="Delete Task", command=self.delete_task)

        # GUI Layout
        self.entry.pack()
        self.addButton.pack()
        self.listbox.pack()
        self.delButton.pack()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
        except:
            pass


root = Tk()
root.title("Python ToDo List")
root.geometry("300x400") # Setting Window Size
to_do_list = ToDoList(root)
root.mainloop() 
