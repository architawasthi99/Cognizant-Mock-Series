# O(n)
arr=[1,2,3,4,5,6]
n=len(arr)
isSorted=True
for i in range(1,n-1):
    if arr[i]<arr[i-1]:
        isSorted=False
        break
if isSorted:
    print("array is sored: ",arr)
else:
    print("not sorted")  

#0(nlogn)
arr=[11,2,3,4,5,6]
new_arr=sorted(arr)
if arr==new_arr:
    print("Sorted")
else:
    print("not sorted")   
