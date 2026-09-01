#Iterative Approach - O(n) Time and O(1) Space
def largest(arr):
        n=len(arr)
        max=arr[0]
        for i in range(1,n):
            if arr[i]>max:
                max=arr[i]
        return max 
arr = [200, 10, 20, 4, 100]     
ans=largest(arr)
print(ans) 


