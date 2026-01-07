import tkinter as tk 
from tkinter import ttk

# create main application window
root = tk.Tk()
root.title("my first tkinter app")
# Add a frame and widgets
frame = ttk.Frame(root, padding=10)
frame.grid()

ttk.Label(frame, text="Hello, Tkinter!").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()