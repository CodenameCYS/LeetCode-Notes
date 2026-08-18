'''
=== 1738. Find Kth Largest XOR Coordinate Value ===

You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.
The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).
Find the kth largest value (1-indexed) of all the coordinates of matrix.

Example 1:
    Input: matrix = [[5,2],[1,6]], k = 1
    Output: 7
    Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
Example 2:
    Input: matrix = [[5,2],[1,6]], k = 2
    Output: 5
    Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
Example 3:
    Input: matrix = [[5,2],[1,6]], k = 3
    Output: 4
    Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.
Example 4:
    Input: matrix = [[5,2],[1,6]], k = 4
    Output: 0
    Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which is the 4th largest value.
 
Constraints:
    1. m == matrix.length
    2. n == matrix[i].length
    3. 1 <= m, n <= 1000
    4. 0 <= matrix[i][j] <= 106
    5. 1 <= k <= m * n
'''
# === 3964ms && 50.4MB === #
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        nums = [matrix[0][0] for _ in range(n*m)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    matrix[i][j] = matrix[i][j] ^ matrix[i][j-1]
                elif j == 0:
                    matrix[i][j] = matrix[i-1][j] ^ matrix[i][j]
                else:
                    matrix[i][j] = matrix[i][j] ^ matrix[i-1][j] ^ matrix[i][j-1] ^ matrix[i-1][j-1]
                nums[i*m+j] = matrix[i][j]
        nums = sorted(nums, reverse=True)
        return nums[k-1]