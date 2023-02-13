import tkinter as tk
from tkinter import *
from tkinter import ttk
from LRU_Page_Replacement_Algorithm import get_res
def create_label():
    global temp
    if temp>len(all_f)-1:
        return None
    i=all_f[temp]
    queue=all_queue[temp]
    pf=all_pf[temp]
    queue_fake=list(map(str,queue))
    label.config(text=",".join(queue_fake))

    for index1,j in enumerate(i):
        ttk.Label(root, text=str(j),font=("Helvetica", word_size), borderwidth=10, relief=SUNKEN).grid(row=index1+1, column=temp+1)
    ttk.Label(root,text=pf,font=("Helvetica", word_size), borderwidth=10, relief=SUNKEN).grid(row=frames+1, column=temp+1)
    temp+=1
temp=0
frames=3
lst=[1,2,3,4,3,1,4,2,5,2,1,2,3,4]
word_size=20
root = tk.Tk()
root.title('Replace')

# root.resizable(0, 0)
# layout on the root window
root.geometry('600x400+50+50')
for row in range(frames+2):
    root.grid_rowconfigure(row, weight=1)
for col in range(len(lst)+1):
    root.grid_columnconfigure(col, weight=1)

lst1=list(map(str, lst))
s1=",".join(lst1)
for index,i in enumerate(lst):

    ttk.Label(root, text=i,font=("Helvetica", word_size)).grid(column=index+1, row=0)
for i in range(frames):
    ttk.Label(root, text=f"f{i}",font=("Helvetica", word_size),borderwidth=1, relief=SUNKEN).grid(row=i+1, column=0)
all_f,all_queue,all_pf=get_res(lst, frames)
# for index,i in enumerate(all_f,1):
#     for index1,j in enumerate(i):
#         ttk.Label(root, text=str(j),font=("Helvetica", word_size), borderwidth=10, relief="solid").grid(row=index1+1, column=index)
label = ttk.Label(root, text="",font=("Helvetica", word_size), relief=SUNKEN)
label.grid(row=frames+2, column=4,columnspan=8, sticky=tk.E)
ttk.Label(root, text="Recently used order\n of previous column:",font=("Helvetica", word_size-7), relief=SUNKEN).grid(row=frames+2, column=4,columnspan=8, sticky=tk.W)

# root.rowconfigure(frames+1, weight=1)
ttk.Button(root, text="next step",command= lambda :create_label()).grid(row=frames+2, column=0,columnspan=4, sticky=tk.W,padx=60)

root.mainloop()
