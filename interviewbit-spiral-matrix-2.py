
def generateMatrix(n):
    if n == 1 :
        return [[1]]
    matrix =  [[0 for _ in range(n)] for _ in range(n)]
    top, left, right, bottom = 0, 0, n-1, n-1
    k = 1
    while left <= right and top <= bottom :
        for col in range(left, right + 1):
            print("A", top, col, k)
            matrix[top][col] = k
            k += 1
        top += 1
        
        for row in range(top, bottom + 1):
            print("B", row, right, k)
            matrix[row][right] = k
            k += 1
        
        right -= 1
        
        if top <= bottom :
            for col in range(right, left-1, -1) :
                print("C", bottom, col, k)
                matrix[bottom][col] = k
                k += 1
            bottom -= 1
        
        if left <= right :
            for row in range(bottom, top-1, -1):
                print("D", row, left, k)
                matrix[row][left] = k
                k += 1
            left += 1
    return matrix
    



print(generateMatrix(2))