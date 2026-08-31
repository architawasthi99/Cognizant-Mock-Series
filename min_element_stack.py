'''BRUTE FORCE'''
t=[23,12,99,100,-1,44,63]
mini = float('inf')
for i in range(len(st)):
    mini=min(mini,st[i])
print("minimum value is: ",mini)


'''(value, minimum)'''
class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,val):
        if not self.stack:
            self.stack.append((val,val))
        else:
            self.stack.append((val,min(val,self.stack[-1][1])))

    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[-1][0]
    def getMin(self):
        return self.stack[-1][1]

st=Stack()
st.push(5)
st.push(2)
st.push(8)
st.push(1)
st.push(4)

print("top: ",st.top())
print("Minimum:", st.getMin())

st.pop()

print("Minimum after pop:", st.getMin())
