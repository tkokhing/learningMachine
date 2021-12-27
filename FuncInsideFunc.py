# Filename: FuncInsideFunc.py

def add_n(n,myList):
    tempList=[]
    for j in range (0,len(myList)):
        
        tempList.insert(j,myList[j]+n)
 
    return tempList


new_v = add_n(10,[1, 5, 3])
print(new_v)
new_v = add_n(2,(list(range(-5, 25, 3))))

print(new_v)


'''
Explanation:
The ability to create and return functions as values in Python is crucial here. add_n creates and returns the new function new_fun, which is then called later on the argument vector. The variable n is defined in the surrounding scope of new_fun (having been created when add_n is called with a particular value for n), and so the lookup of n evaluates to that value when the body of new_fun is eventually evaluated later.
'''
# # Below is the model answer


# v = [1, 5, 3]
v = list(range(-5, 25, 3))
def add_n(n):
    def new_fun(v):
        print(n)
        print(v)
        return [elt + n for elt in v]
    return new_fun




print('hello')
print(add_n(10)([1, 5, 3]))
print('hello')
print(add_n(2)(list(range(-5, 25, 3))))



# def add_n(n,myList):
#     tempList=[]
#     for j in range (0,len(myList)):
        
#         tempList.insert(j,myList[j]+n)
 
#     return tempList



# new_v = add_n(2,(list(range(-5, 25, 3))))
# print(new_v)


# does not even need a comma between the functions

# def array_mult(A, B):
#     listColSizeA = len(A)
#     listRowSizeA = len(A[0])

#     print(listColSizeA)
#     print(listRowSizeA)

#     listColSizeB = len(B)
#     listRowSizeB = len(B[0])
#     print(listColSizeB)
#     print(listRowSizeB)


#     # for i in A:
#     #     print (i) 

#     # for i in B:
#     #     print (i) 


# M1 = [[1, 2, 3], [-2, 3, 7]]
# M2 = [[1,0,0],[0,1,0],[0,0,1]]
# # M1 = [1, 2, 3]
# # M2 = [1,0,0] 
# array_mult(M1, M2)

