#BRUTE FORCE
def sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
arr=[90,65,34,95,36,45,45]        
sort(arr)
print(arr)            

#DIRECT
arr=[90,65,34,95,36,45,45]  
arr.sort()
print(arr)     
