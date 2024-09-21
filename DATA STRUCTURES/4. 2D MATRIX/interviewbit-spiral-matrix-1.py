

def spiralOrder(matrix):
    rows, cols = len(matrix), len(matrix[0])
    top, left, right, bottom = 0, 0, cols-1, rows-1
    ans = [None] * (rows * cols)
    it  = 0
    while top <= bottom and left <= right :
        
        for col in range(left, right+1) :
            ans[it] = matrix[top][col]
            it     += 1
        top += 1
        
        for row in range(top, bottom+1):
            ans[it] = matrix[row][right]
            it     += 1
        right -= 1
        
        if top <= bottom :
            for col in range(right, left-1, -1) :
                ans[it] = matrix[bottom][col]
                it     += 1
            bottom -= 1
        
        if left <= right :
            for row in range(bottom, top-1, -1):
                ans[it] = matrix[row][left]
                it     += 1
            left += 1
        
    return ans

A = [[1]]
print(spiralOrder(A))