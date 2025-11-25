import tkinter as tk

class TextDialog:
    def __init__(self, parent, callback):
        self.callback = callback
        self.window = tk.Toplevel(parent)
        self.window.title("Work 3: Input Text")
        self.window.geometry("300x150")
        self.window.transient(parent)
        self.window.grab_set()

        label = tk.Label(self.window, text="Enter text below:")
        label.pack(pady=10)

        self.entry = tk.Entry(self.window, width=30)
        self.entry.pack(pady=5)

        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=20)

        yes_btn = tk.Button(btn_frame, text="Yes", command=self.on_yes, width=10)
        yes_btn.pack(side=tk.LEFT, padx=10)

        cancel_btn = tk.Button(btn_frame, text="Cancel", command=self.window.destroy, width=10)
        cancel_btn.pack(side=tk.LEFT, padx=10)

    def on_yes(self):
        text = self.entry.get()
        if text:
            self.callback(text)
        self.window.destroy()