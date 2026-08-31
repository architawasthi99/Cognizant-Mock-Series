def reverse(s):
    result=""
    for i in reversed(s):
        result=result+i
    return result
s="archit awasthi"
ans=reverse(s)
print(ans)

//OR
def reverse(s):
    return s[::-1]

//inplace
def reverse(s):
    s=list(s)
    left=0;
    right=len(s)-1
    while(left<right):
        s[left],s[right]=s[right],s[left]
        left=left+1
        right=right-1
     return ''.join(s)
