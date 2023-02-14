import tkinter as tk
from tkinter import *
from tkinter import TclError, ttk
from tkinter.ttk import Combobox
import copy
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
            all_queue.append(queue1)
            for x in range(capacity-len(f1)):
                f1.append(" ")
            all_f.append(f1)
        return all_f,all_queue, all_pf
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
                else:
                    for x in range(len(f)):
                        if f[x] not in lst[i+1:]:
                            f[x] = lst[i]
                            break
                        else:
                            occurance[x] = lst[i+1:].index(f[x])
                    else:
                        f[occurance.index(max(occurance))] = s[i]
                fault += 1
                pf = 'Yes'
            else:

                pf = 'No'
            all_pf.append(pf)
            occur1=copy.deepcopy(occurance)
            all_occur.append(occur1)
            f1=copy.deepcopy(f)
            for x in range(capacity-len(f1)):
                f1.append(" ")
            all_f.append(f1)
        return all_f, all_occur, all_pf
    elif algo=="lru":
        all_f=[]
        order_lst=[]
        all_pf=[]
        f,st,fault,pf = [],[],0,'No'
        st1=copy.deepcopy(st)
        for i in lst:
            order_lst.append(st1)
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
            all_pf.append(pf)
            print("   %d\t\t"%i,end='')
            f1=copy.deepcopy(f)
            for x in range(capacity-len(f1)):
                f1.append(" ")
            all_f.append(f1)
        return all_f,order_lst,all_pf
    else:
        return None

    
def create_input_frame(container):

    frame = ttk.Frame(container)
    dropdown = [1,2,3,4,5,6,7,8,9,10]
    
    framevalue = IntVar()
    stringvalue = StringVar()
    algovalue = StringVar()
    algovalue.set("fifo")  # This is done so that all the buttons aren't checked



    title_label = Label(frame, text="Page Replacement Algorithm", bg="CYAN", font="comicsansms 30 bold", width=45)
    title_label.grid(row=0,columnspan=2)
    

    frame_label = Label(frame, text="Frame Size : ", bg="YELLOW", font="comicsansms 20 bold", width=10)
    frame_label.grid(row=1, column=0,padx=100,pady=10)

    frameentry = Combobox(frame, textvariable=framevalue, width=20, value=dropdown, font="comicsansms 19 bold", state="readonly")
    frameentry.grid(row=1, column=1,padx=100,pady=10)


    string_label = Label(frame, text="Enter String: ", bg="YELLOW", font="comicsansms 20 bold", width=10)
    string_label.grid(row=2, column=0, padx=100,pady=10)
    algo_label = Label(frame, text="Algorithm   : ", bg="YELLOW", font="comicsansms 20 bold", width=10)
    algo_label.grid(row=3, column=0, padx=100,pady=10)
    
    stringentry = Entry(frame, textvariable=stringvalue, width=20, font="comicsansms 20 bold")
    stringentry.grid(row=2, column=1,padx=100,pady=10)
    fifoentry = Radiobutton(frame, text="First In First Out", variable=algovalue, value="fifo", font="comicsansms 20 bold")
    optentry = Radiobutton(frame, text="Optimal Page Replacement ", variable=algovalue, value="opt", font="comicsansms 20 bold")
    lruentry = Radiobutton(frame, text="Least Recently Used", variable=algovalue, value="lru", font="comicsansms 20 bold")

    fifoentry.grid(row=3, column=1,padx=100,pady=10)
    optentry.grid(row=4, column=1,padx=100,pady=10)
    lruentry.grid(row=5, column=1,padx=100,pady=10)

    cal = Button(frame, text="Submit", bg="ORANGE", width=20, height=2, command= lambda :openNewWindow(stringvalue,framevalue,algovalue), font="comicsansms")
    cal.grid(row=6, column=0,padx=100,pady=10)
    return frame
temp=0
def get_queue_name(s):
    if s=="fifo":
        return "queue"
    if s=="lru":
        return "Recently used order\n of previous column"
    if s=="opt":
        return "distance to reference\n in future"
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
    newWindow.title("New Window")
 
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
        queue_fake=list(map(str,queue))
        label.config(text=",".join(queue_fake))
        print(i)

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
        ttk.Label(newWindow, text=f"f{i}",font=("Helvetica", word_size),borderwidth=1, relief=SUNKEN).grid(row=i+1, column=0)
    all_f,all_queue,all_pf=get_res(algo,lst, frames)
    label = ttk.Label(newWindow, text="",font=("Helvetica", word_size), relief=SUNKEN)
    label.grid(row=frames+2, column=6,columnspan=2, sticky=tk.W)
    
    ttk.Label(newWindow, text=get_queue_name(algo),font=("Helvetica", word_size), relief=SUNKEN).grid(row=frames+2, column=5, sticky=tk.W)

    root.rowconfigure(frames+1, weight=1)
    ttk.Button(newWindow, text="next step",command= lambda :create_label()).grid(row=frames+2, column=0,columnspan=4, sticky=tk.W,padx=60)



root = tk.Tk()
root.geometry("1000x750")
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

