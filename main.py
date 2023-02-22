import tkinter as tk
from tkinter import *
from tkinter import TclError, ttk
from tkinter.ttk import Combobox
import copy
def get_dis(s,f):
    order_lst=[]
    order_lst1=[]
    check=[]
    for i in s:
        if i in f:
            if i not in check:
                check.append(i)
                order_lst.append(i)
    for i in f:
        if i not in s:
            order_lst.append(i)
    print("lst",order_lst)
    print("f",f)

    for i in order_lst:
        order_lst1.append(f.index(i))
    print("order", order_lst1)
    return order_lst1

def get_res(algo,lst, capacity):
    if algo=="fifo":
        all_f=[]
        all_pf=[]
        f,fault,top,pf = [],0,0,'No'
        all_queue=[]
        queue=[]
        for i in lst:
            if i not in f:
                queue.append(i)
                if len(f)<capacity:
                    f.append(i)
                else:
                    queue.pop(0)
                    f[top] = i
                    top = (top+1)%capacity
                fault += 1
                pf = 'Yes'
            else:
                pf = 'No'
            all_pf.append(pf)
            f1=copy.deepcopy(f)
            queue1=copy.deepcopy(queue)
            queue2=[]
            for m in queue1:
                queue2.append(f.index(m))
            all_queue.append(queue2)
            for x in range(capacity-len(f1)):
                f1.append(" ")
            all_f.append(f1)
        return all_f,all_queue, all_pf, fault
    elif algo=="opt":
        f,fault,pf = [],0,'No'
        all_f=[]
        all_pf=[]
        all_occur=[]
        occurance = [None for i in range(capacity)]
        # occur1=copy.deepcopy(occurance)
        
        for i in range(len(lst)):
            
            if lst[i] not in f:
                if len(f)<capacity:
                    f.append(lst[i])
                    order_lst=get_dis(lst[i+1:],f)
                else:
                    order_lst=get_dis(lst[i+1:],f)

                    index_of_max=order_lst[-1]
                    print(index_of_max)
                    f[index_of_max]=lst[i]
                                    
                fault += 1
                pf = 'Yes'
            else:

                pf = 'No'
            fake=copy.deepcopy(get_dis(lst[i+2:],f))
            all_occur.append(fake)
            all_pf.append(pf)
            f1=copy.deepcopy(f)
            for x in range(capacity-len(f1)):
                f1.append(" ")
            all_f.append(f1)
        return all_f, all_occur, all_pf, fault
    elif algo=="lru":
        all_f=[]
        order_lst=[]
        all_pf=[]
        f,st,fault,pf = [],[],0,'No'
        st1=copy.deepcopy(st)
        for i in lst:
            
            if i not in f:
                if len(f)<capacity:
                    f.append(i)
                    st.append(len(f)-1)
                else:
                    ind = st.pop(0)
                    f[ind] = i
                    st.append(ind)
                pf = 'Yes'
                fault += 1
            else:
                st.append(st.pop(st.index(f.index(i))))
                pf = 'No'
            st1=copy.deepcopy(st)
            order_lst.append(st1)
            all_pf.append(pf)
            print("   %d\t\t"%i,end='')
            f1=copy.deepcopy(f)
            for x in range(capacity-len(f1)):
                f1.append(" ")
            all_f.append(f1)
        return all_f,order_lst,all_pf, fault

    elif algo=="lfu":
        all_f=[]
        all_freq=[]
        all_pf=[]
        f,st,fault,pf = [],[],0,'No'
        frequency_dict=dict()
        for i in lst:
            print(i, end=" ")
            frequency_dict[i]=frequency_dict.get(i,0)+1
            f_freq=dict()
            for index,l in enumerate(f):
                f_freq[index]=frequency_dict[l]
            f_freq = dict(sorted(f_freq.items(), key=lambda item: item[1]))
            

            
            print(frequency_dict)
            if i not in f:
                if len(f)<capacity:
                    f.append(i)
                    for index,l in enumerate(f):
                        f_freq[index]=frequency_dict[l]
                    f_freq = dict(sorted(f_freq.items(), key=lambda item: item[1]))
                else:
                    f[list(f_freq.keys())[0]]=i
                    
                    
                    

                pf = 'Yes'
                fault += 1
            else:
                
                pf = 'No'
            
            all_freq.append(f_freq)
            all_pf.append(pf)
            f1=copy.deepcopy(f)
            for x in range(capacity-len(f1)):
                f1.append(" ")
            all_f.append(f1)
        return all_f,all_freq,all_pf, fault
    else:
        return None
import matplotlib.pyplot as plt
import numpy as np
def plot(s):
    s=s.get()
    s=list(map(int,s.split()))
    for algo in ["fifo","opt","lru","lfu"]:
        # if algo=="fifo":
            y=[]
            x=[]
            for i in range(1,10):
                print("frames",i)
                fault=get_res(algo,s,i)[-1]
                faultrate=fault/len(s)
                x.append(i)
                y.append(faultrate)
            plt.plot(x, y, label =algo)
    plt.xlabel("number of frames")
    plt.ylabel("fault rate")
    plt.legend()
    plt.show()

    
def create_input_frame(container):

    frame = ttk.Frame(container)
    dropdown = [1,2,3,4,5,6,7,8,9,10]
    # frame.columnconfigure(0, minsize=100, weight=2)
    # frame.columnconfigure(1, minsize=100, weight=1)
    framevalue = IntVar()
    stringvalue = StringVar()
    algovalue = StringVar()
    algovalue.set("fifo")  # This is done so that all the buttons aren't checked



    title_label = Label(frame, text="Page Replacement Algorithm", bg="#009999", font="comicsansms 30 bold")
    title_label.grid(row=0,columnspan=2,sticky='we')
    
    
    frame_label = Label(frame, text="Frame Size : ", font="comicsansms 20 bold")
    frame_label.grid(row=1, column=0,padx=50,pady=10,sticky='w')

    frameentry = Combobox(frame, textvariable=framevalue, width=20, value=dropdown, font="comicsansms 19 bold", state="readonly")
    frameentry.grid(row=1, column=1,padx=50,pady=10,sticky='w')


    string_label = Label(frame, text="Enter String(seperated by space): ", font="comicsansms 20 bold")
    string_label.grid(row=2, column=0, padx=50,pady=10,sticky='w')
    algo_label = Label(frame, text="Algorithm : ",font="comicsansms 20 bold")
    algo_label.grid(row=3, column=0, padx=50,pady=10,sticky='w')
    
    stringentry = Entry(frame, textvariable=stringvalue, width=20, font="comicsansms 20 bold")
    stringentry.grid(row=2, column=1,padx=50,pady=10,sticky='w')
    fifoentry = Radiobutton(frame, text="First In First Out", variable=algovalue, value="fifo", font="comicsansms 20 bold")
    optentry = Radiobutton(frame, text="Optimal Page Replacement ", variable=algovalue, value="opt", font="comicsansms 20 bold")
    lruentry = Radiobutton(frame, text="Least Recently Used", variable=algovalue, value="lru", font="comicsansms 20 bold")
    lfuentry = Radiobutton(frame, text="Least frequently Used", variable=algovalue, value="lfu", font="comicsansms 20 bold")

    fifoentry.grid(row=4, column=0,padx=50,pady=10,sticky='w')
    optentry.grid(row=5, column=0,padx=50,pady=10,sticky='w')
    lruentry.grid(row=4, column=1,padx=50,pady=10,sticky='w')
    lfuentry.grid(row=5, column=1,padx=50,pady=10,sticky='w')

    cal = Button(frame, text="Submit", bg="#66B2FF", width=20, height=2, command= lambda :openNewWindow(stringvalue,framevalue,algovalue), font="comicsansms")
    cal.grid(row=7, column=0,padx=100,pady=10)
    cal1 = Button(frame, text="plot fault rate", bg="#66B2FF", width=20, height=2, command= lambda : plot(stringvalue), font="comicsansms")
    cal1.grid(row=7, column=1,padx=100,pady=10,sticky='w')
    return frame
temp=0
def get_queue_name(s):
    if s=="fifo":
        return "Queue:"
    if s=="lru":
        return "Least recently used:"
    if s=="opt":
        return "Closest to farthest:"
    if s=="lfu":
        return "frequency dict:"
    else: 
        return None
def openNewWindow(stringvalue,framevalue,algovalue):
    global temp
    temp=0
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
    lst=stringvalue.get()
    frames=framevalue.get()
    algo=algovalue.get()
    print(algo)
    # sets the title of the
    # Toplevel widget
    newWindow.title("Frames table")
 
    # sets the geometry of toplevel
    newWindow.geometry('600x400+50+50')
    for row in range(frames+2):
        newWindow.grid_rowconfigure(row, weight=1)
    for col in range(len(lst)+1):
        newWindow.grid_columnconfigure(col, weight=1)
 
    # A Label widget to show in toplevel
        
    

    
    
    def create_label():
        global temp
        if temp>len(all_f)-1:
            return None
        i=all_f[temp]
        queue=all_queue[temp]
        pf=all_pf[temp]
        if type(queue)==list:

            queue_fake=list(map(str,queue))
            queue_fake=["f"+r for r in queue_fake ]
        elif type(queue)==dict:
            queue_fake=["f"+str(r)+":"+str(queue[r]) for r in queue.keys() ]
        label.config(text=",".join(queue_fake))

        for index1,j in enumerate(i):
            ttk.Label(newWindow, text=str(j),font=("Helvetica", word_size), borderwidth=10, relief=SUNKEN).grid(row=index1+1, column=temp+1)
        ttk.Label(newWindow,text=pf,font=("Helvetica", word_size), borderwidth=10, relief=SUNKEN).grid(row=frames+1, column=temp+1)
        temp+=1

    lst=list(map(int,lst.split()))
    print(lst)
    word_size=15

    for index,i in enumerate(lst):

        ttk.Label(newWindow, text=i,font=("Helvetica", word_size)).grid(column=index+1, row=0)
    for i in range(frames):
        ttk.Label(newWindow, text=f"f{i}",font=("Helvetica", word_size),borderwidth=1, relief=SUNKEN).grid(row=i+1, column=0, padx=20)
    all_f,all_queue,all_pf, fault=get_res(algo,lst, frames)
    ttk.Label(newWindow, text=get_queue_name(algo),font=("Helvetica", word_size), relief=SUNKEN).grid(row=frames+2, column=1, columnspan=100, padx=150,sticky=tk.W)
    label = ttk.Label(newWindow, text="",font=("Helvetica", word_size), relief=SUNKEN)
    label.grid(row=frames+3, column=1,columnspan=100,padx=150,sticky="ew")
    
    

    root.rowconfigure(frames+1, weight=1)
    ttk.Button(newWindow, text="next step",command= lambda :create_label()).grid(row=frames+2, column=0,columnspan=100, sticky=tk.W,padx=60)



root = tk.Tk()
# root.geometry("900x750")
root.resizable(0, 0)
try:
    # windows only (remove the minimize/maximize button)
    root.attributes('-toolwindow', True)
except TclError:
    print('Not supported on your platform')

# layout on the root window

input_frame = create_input_frame(root)
input_frame.grid(row=0, column=0,columnspan=3)

root.mainloop()
# 1 2 3 4 1 2 5 1 2 3 4 5