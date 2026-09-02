# 0(n)
def second(arr):
    arr.sort(reverse=True)
    print(arr[1])
arr=[7,54,23,99,4,1]    
second(arr)

#no sort
def second_largest(arr):
    largest=float('-inf')
    second=float('-inf')
    for x in arr:
        if x>largest:
            second=largest
            largest=x
        elif largest>x>second:
            second=x
    return second

arr=[43,67,21,43,67,92]                
print(second_largest(arr))
