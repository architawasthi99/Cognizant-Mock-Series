#O(2n)
def zero(arr):
    count=0
    i=0
    while i<len(arr):
        if arr[i]==0:
            count=count+1
            arr.pop(i)
        else:
            i+=1    
    while count!=0:
        arr.append(0)  
        count=count-1
    return arr        
print(zero([1,2,0,4,3,0,5,0]))

# O(n) 2 pointer
def zero(arr):
    pos=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[pos],arr[i]=arr[i],arr[pos]
            pos+=1
    return arr
print(zero([0,1,0,3,12]))            

