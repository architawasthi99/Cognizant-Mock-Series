#BRUTE FORCE
def rotate(nums,k):
    n=len(nums)
    k=k%n
    def reverse(left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left=left+1
            right=right-1
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
nums=[1,2,3,4,5,6,7]
rotate(nums,3)
print(nums)        

#SLICING
def rotate(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
print(rotate(arr, 2))
