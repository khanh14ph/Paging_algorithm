#Optimal page replacement algorithm (OPT or OPR) implementation in python
#Created By: Suman Adhikari
if __name__=="__main__":
    print("Enter the number of frames: ",end="")
    capacity = int(input())
    f,fault,pf = [],0,'No'
    print("Enter the reference string: ",end="")
    s = list(map(int,input().strip().split()))
    print("\nString|Frame →\t",end='')
    for i in range(capacity):
        print(i,end=' ')
    print("Fault\n   ↓\n")
    occurance = [None for i in range(capacity)]
    for i in range(len(s)):
        if s[i] not in f:
            if len(f)<capacity:
                f.append(s[i])
            else:
                for x in range(len(f)):
                    if f[x] not in s[i+1:]:
                        f[x] = s[i]
                        break
                    else:
                        occurance[x] = s[i+1:].index(f[x])
                else:
                    f[occurance.index(max(occurance))] = s[i]
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        print("   %d\t\t"%s[i],end='')
        for x in f:
            print(x,end=' ')
        for x in range(capacity-len(f)):
            print(' ',end=' ')
        print(" %s"%pf)
    print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
import copy
def get_res(s, capacity):
    f,fault,pf = [],0,'No'
    all_f=[]
    all_pf=[]
    all_occur=[]
    occurance = [None for i in range(capacity)]
    # occur1=copy.deepcopy(occurance)
    
    for i in range(len(s)):
        
        if s[i] not in f:
            if len(f)<capacity:
                f.append(s[i])
            else:
                for x in range(len(f)):
                    if f[x] not in s[i+1:]:
                        f[x] = s[i]
                        break
                    else:
                        occurance[x] = s[i+1:].index(f[x])
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

