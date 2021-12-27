# Filename: dotProdVector.py

v1 = [1,2,3]
v2 = [4,5,6]

def dot(v1, v2):
    c = 0
    for i in range (0,len(v1)):
        c = c + v1[i]*v2[i]
    return c    
    
print(dot(v1, v2))