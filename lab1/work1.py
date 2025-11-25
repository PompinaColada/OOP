import tkinter as tk

class ListDialog:
    def __init__(self, parent, callback):
        self.callback = callback
        self.window = tk.Toplevel(parent)
        self.window.title("Work 1: Select Group")
        self.window.geometry("300x500")
        self.window.transient(parent)
        self.window.grab_set()

        label = tk.Label(self.window, text="Select a faculty group:")
        label.pack(pady=10)

        self.listbox = tk.Listbox(self.window, selectmode=tk.SINGLE)
        groups = ["ІМ-43", "43-ІМ", "І4-М3", "34-МІ", "Б-52"]
        
        for group in groups:
            self.listbox.insert(tk.END, group)
            
        self.listbox.pack(pady=5, fill=tk.BOTH, expand=True, padx=20)

        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=20)

        yes_btn = tk.Button(btn_frame, text="Yes", command=self.on_yes, width=10)
        yes_btn.pack(side=tk.LEFT, padx=10)

        cancel_btn = tk.Button(btn_frame, text="Cancel", command=self.window.destroy, width=10)
        cancel_btn.pack(side=tk.LEFT, padx=10)

    def on_yes(self):
        selection = self.listbox.curselection()
        if selection:
            selected_text = self.listbox.get(selection[0])
            self.callback(selected_text)
        self.window.destroy()