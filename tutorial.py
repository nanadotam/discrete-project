import tkinter as tk

root = tk.Tk()


root.geometry("500x500")
root.title("My First GUI")


label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 15))
textbox.pack(padx=10, pady=10)

# text_entry1 = tk.Entry(root)
button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack(padx=12, pady=12)

root.mainloop() 