"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
"""
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat= ([[0 for i in range(m)] for j in range(n)])
        col = []
        odd = 0
        for i in indices:
            a = i[0]
            b = i[1]
            for col in range(m):
                mat[a][col] = mat[a][col] + 1
            for row in range(n):
                mat[row][b] = mat[row][b] + 1
        for i in range(n):
            for j in range(m):
                if (mat[i][j])%2 !=0:
                    odd = odd +1
        return (odd)

