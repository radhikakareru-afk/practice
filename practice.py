import tkinter as tk

root = tk.Tk()
root.title("Entry to Label using StringVar")

# Create a StringVar to hold the text
text_var = tk.StringVar()

# Entry widget linked to text_var
entry = tk.Entry(root, textvariable=text_var, width=30)
entry.pack(pady=10)

# Label widget that shows the current value of text_var
label = tk.Label(root, textvariable=text_var, font=("Arial", 14))
label.pack(pady=10)

root.mainloop()
