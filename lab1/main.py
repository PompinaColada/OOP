import tkinter as tk
from tkinter import messagebox
from work1 import ListDialog
from work3 import TextDialog

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Application Window")
        self.root.geometry("400x300")

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        work_menu = tk.Menu(menubar, tearoff=0)
        work_menu.add_command(label="Work1 (Список)", command=lambda: ListDialog(self.root, self.update_label))
        work_menu.add_command(label="Work3 (Инпут)", command=lambda: TextDialog(self.root, self.update_label))
        menubar.add_cascade(label="Work", menu=work_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        instruction_label = tk.Label(self.root, text="Result:", font=("Arial", 10))
        instruction_label.pack(pady=20)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), fg="blue")
        self.result_label.pack(pady=10)

    def update_label(self, text):
        self.result_label.config(text=text)

    def show_about(self):
        messagebox.showinfo("About", "Tkinter Lab Work")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()