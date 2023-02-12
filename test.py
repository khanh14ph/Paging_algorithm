import tkinter as tk

root = tk.Tk()
root.title("Grid Frame with Blank Row")

for i in range(5):
    for j in range(10):
        tk.Label(root, text="({}, {})".format(i, j), relief="solid").grid(row=i, column=j)
        # root.rowconfigure(i, weight=1)
        root.columnconfigure(j, weight=1)

# Add a blank row between rows 2 and 3
root.rowconfigure(2, minsize=20)

root.grid_propagate(False)
root.mainloop()