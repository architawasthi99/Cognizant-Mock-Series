def display(**kwargs):
    print(kwargs)
display(name="archit",age=21,height=172)          

def display(**kwargs):
    print(kwargs["age"]+kwargs["height"])
display(name="archit",age=21,height=172)          
