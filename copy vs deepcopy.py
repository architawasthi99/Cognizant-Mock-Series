import copy
a=[[1,2,3],[3,4,5],[6,7,8]]
b=copy.copy(a)
b[0][0]=100
print(a)
print(b)

c=[[11,22,33],[44,55,66],[77,88,99]]
d=copy.deepcopy(a)
print(d)
print(c)
