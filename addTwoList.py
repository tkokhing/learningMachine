# Filename: addTwoList.py

a = [1,2,3]
b = [4,5,6]
def add_two_lists(a, b):
    c =[]
    for i in range (0,len(a)):
        c.append(((~a[i]+1)^(~b[i]+1))+2)
    return c    
    

print(add_two_lists(a, b))