#FIFO page replacement algorithm implementation in python
#Created By: Suman Adhikari
import copy
def get_res(lst, frames):
    all_f=[]
    all_pf=[]
    f,fault,top,pf = [],0,0,'No'
    all_queue=[]
    queue=[]
    for i in lst:
        if i not in f:
            queue.append(i)
            if len(f)<frames:
                f.append(i)
            else:
                queue.pop(0)
                f[top] = i
                top = (top+1)%frames
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        all_pf.append(pf)
        f1=copy.deepcopy(f)
        queue1=copy.deepcopy(queue)
        all_queue.append(queue1)
        for x in range(frames-len(f1)):
            f1.append(" ")
        all_f.append(f1)
    return all_f,all_queue, all_pf
if __name__=="__main__":
    print("Enter the number of frames: ",end="")
    capacity = int(input())
    f,fault,top,pf = [],0,0,'No'
    print("Enter the reference string: ",end="")
    # s = list(map(int,input().strip().split()))
    s=[3,2,1,4,3,4,5]
    print("\nString|Frame →\t",end='')
    for i in range(capacity):
        print(i,end=' ')
    print("Fault\n   ↓\n")

    for i in s:
        if i not in f:
            if len(f)<capacity:
                f.append(i)
            else:
                f[top] = i
                top = (top+1)%capacity
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        
        print("   %d\t\t"%i,end='')
        for x in f:
            print(x,end=' ')
        for x in range(capacity-len(f)):
            print(' ',end=' ')
        print("top",f[top])
        print(" %s"%pf)
    print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
    print(get_res(s,capacity))