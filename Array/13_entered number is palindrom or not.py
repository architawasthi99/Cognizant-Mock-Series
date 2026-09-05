n=int(input("enter the number: "))
original=n
reverse=0
while n>0:
  digit=n%10
  reverse=reverse*10+digit
  n=n//10
if original==reverse:
  print("true")
else:
  print("false")




n = input("Enter a number: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
