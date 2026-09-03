def palindrome(s):
    s=s.lower()
    if s==s[::-1]:
        return ("PALINDROME")
    
    else:
        return ("NOT PALINDROME")    
print(palindrome("Kayak"))
