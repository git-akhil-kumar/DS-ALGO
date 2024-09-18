from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        top, left, bottom, right = 0, 0, 0, 0
        total = rows * cols 
        counter = 1
        matrix = []
        while counter <= total :
            for col in range(left, right + 1):
                if rStart + top >= 0 and rStart + top < rows and cStart + col >= 0 and cStart + col < cols :
                    matrix.append([rStart + top, cStart + col])
                    counter += 1
            right += 1

            for row in range(top, bottom + 1):
                if rStart + row >= 0 and rStart + row < rows and cStart + right >= 0 and cStart + right < cols :
                    matrix.append([rStart + row, cStart + right])
                    counter += 1
            bottom += 1

            for col in range(right, left - 1, -1):
                if rStart + bottom >= 0 and rStart + bottom < rows and cStart + col >= 0 and cStart + col < cols :
                    matrix.append([rStart + bottom, cStart + col])
                    counter += 1
            left -= 1

            for row in range(bottom, top - 1, -1):
                if rStart + row >= 0 and rStart + row < rows and cStart + left >= 0 and cStart + left < cols :
                    matrix.append([rStart + row, cStart + left])
                    counter += 1
            top -= 1

        return matrix
    
sol = Solution()
testCases = [1,4,0,0,5,6,1,4]
results = [[[0,0],[0,1],[0,2],[0,3]], [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]]
for i in range(0, len(testCases), 4) :
    testCase = testCases[i:i+5]
    print(sol.spiralMatrixIII(testCase[0], testCase[1], testCase[2], testCase[3]) == results[i//4])

