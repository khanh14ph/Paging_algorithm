#LRU page replacement algorithm implementation in python
#Created By: Suman Adhikari
if __name__=="__main__":
    print("Enter the number of frames: ",end="")
    capacity = int(input())
    f,st,fault,pf = [],[],0,'No'
    print("Enter the reference string: ",end="")
    # s = list(map(int,input().strip().split()))
    s=list(map(int,"7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1".split()))
    print("\nString|Frame →\t",end='')
    for i in range(capacity):
        print(i,end=' ')
    print("Fault\n   ↓\n")
    for i in s:
        # print("st", st)
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
        
        print("   %d\t\t"%i,end='')
        for x in f:
            print(x,end=' ')
        for x in range(capacity-len(f)):
            print(' ',end=' ')
        
        print(" %s"%pf)
        
    print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
import copy
def get_res(s,capacity):
    all_f=[]
    order_lst=[]
    all_pf=[]
    f,st,fault,pf = [],[],0,'No'
    st1=copy.deepcopy(st)
    for i in s:
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
