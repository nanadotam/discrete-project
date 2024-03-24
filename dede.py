import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("Set no ay3 serious")

label = tk.Label(root, text="Sets", font=('Arial',20))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height = 3, font = ('Arial', 18))
textbox.pack()


root.mainloop()