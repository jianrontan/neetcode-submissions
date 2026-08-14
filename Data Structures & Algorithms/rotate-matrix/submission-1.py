class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        for i in range(n // 2):
            temp = matrix[i]
            matrix[i] = matrix[n - i - 1]
            matrix[n - i - 1] = temp
        print("flip", matrix)

        for j in range(0, n):
            for k in range(j + 1, n):
                if j != k:
                    print(" ")
                    temp = matrix[j][k]
                    print(temp, matrix[k][j])
                    matrix[j][k] = matrix[k][j]
                    matrix[k][j] = temp
        
        print(matrix)