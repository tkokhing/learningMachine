# filename: matrixMultiList.py

def array_mult(A, B):

    M3row = []
    M3 = []


    lenColMxA = len(A[0][:])
    lenRowMxA = len(A)
    print('Matrix A row and colomn length are', lenRowMxA, lenColMxA)

    lenColMxB = len(B[0][:])
    lenRowMxB = len(B)

    print('Matrix B row and colomn length are', lenRowMxB, lenColMxB)

    # for h in range (0,lenColMxA):
    #     print(A[0][h])

    # for n in range (0,lenRowMxB):
    #     print(B[n][0])

    result = 0

    for i in range (0,lenRowMxA):
        for j in range (0,lenColMxB):
            for k in range (0, lenRowMxB):
                result = result + A[i][k]*B[k][j]
        
            M3row.insert(j,result)
            result = 0

        M3ListRow = M3row[:]    
        M3.append(M3ListRow)
        for l in range (0, lenColMxB):
            M3row.pop(0)

    return M3

# A = [[1, 2, 3, 6], [-2, 3, 7, 9], [-20, 3, 17, 9]]
# B = [[1,0,0,4],[7,1,0,5],[0,0,1,6],[10,0,0,1]]

M1 = [[1, 2, 3], [-2, 3, 7]]
M2 = [[1,0,0],[0,1,0],[0,0,1]]

C = array_mult(M1, M2)
print(C)

M3 = [[1], [0], [-1]]

D = array_mult(M1, M3)
print(D)
