import tkinter as tk

# Function to display info
def show_info():
    name = entry.get()
    gender = gender_var.get()
    subscribe = "Yes" if subscribe_var.get() == 1 else "No"
    
    result_label.config(text=f"Name: {name}\nGender: {gender}\nSubscribed: {subscribe}")

# Main window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x250")

# 1. Label
tk.Label(root, text="Enter your name:").pack()
 
# 2. Entry
entry = tk.Entry(root)
entry.pack()

# 3. Radiobutton
tk.Label(root, text="Select Gender:").pack()
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# 4. Checkbutton
subscribe_var = tk.IntVar()
tk.Checkbutton(root, text="Subscribe to newsletter", variable=subscribe_var).pack()

# 5. Button
tk.Button(root, text="Submit", command=show_info).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Start GUI loop
root.mainloop()
