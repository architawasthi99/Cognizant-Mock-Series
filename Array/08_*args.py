def add(*args):
    result=sum(args)
    print(result)    
add(10,20,30)

def add(*args):
    total=0
    for x in args:
        total+=x
    return total
print(add(11,22,33,55))  
