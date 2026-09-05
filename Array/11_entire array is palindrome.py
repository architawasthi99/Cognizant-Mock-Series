def palindrome(arr):
  for i in range(len(arr)):
    if arr[i]!=arr[len(arr)-1-i]:
      return False
  return True
arr=[111, 222, 222, 222, 111] 
print(palindrome(arr))


def palindrome(arr):
  return arr==arr[::-1]
arr=[111, 222, 222, 222, 111] 
print(palindrome(arr))
