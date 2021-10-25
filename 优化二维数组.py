def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    p = m
    t = n
    flag = 0
    for i in range(0, n):
        if target < matrix[0][i]:
            t = i
            break
    for i in range(0, m):
        if target < matrix[i][0]:
            p = i
            break
    for x in range(0, p):
        for y in range(0, t):
            if target == matrix[x][y]:
                flag = 1
                break
    if flag == 1:
        print("true")
    elif flag == 0:
        print("false")

matrix = [[-1,3]]
target = -1

searchMatrix(matrix,target)