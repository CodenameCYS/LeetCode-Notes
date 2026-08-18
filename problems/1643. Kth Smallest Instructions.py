'''
=== 1643. Kth Smallest Instructions ===

Bob is standing at cell (0, 0), and he wants to reach destination: (row, column). He can only travel right and down. You are going to help Bob by providing instructions for him to reach destination.
The instructions are represented as a string, where each character is either:
    - 'H', meaning move horizontally (go right), or
    - 'V', meaning move vertically (go down).
Multiple instructions will lead Bob to destination. For example, if destination is (2, 3), both "HHHVV" and "HVHVH" are valid instructions.
However, Bob is very picky. Bob has a lucky number k, and he wants the kth lexicographically smallest instructions that will lead him to destination. k is 1-indexed.
Given an integer array destination and an integer k, return the kth lexicographically smallest instructions that will take Bob to destination.

Example 1:
    Input: destination = [2,3], k = 1
    Output: "HHHVV"
    Explanation: All the instructions that reach (2, 3) in lexicographic order are as follows:
    ["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"].
Example 2:
    Input: destination = [2,3], k = 2
    Output: "HHVHV"
Example 3:
    Input: destination = [2,3], k = 3
    Output: "HHVVH"
 
Constraints:
    1. destination.length == 2
    2. 1 <= row, column <= 15
    3. 1 <= k <= nCr(row + column, row), where nCr(a, b) denotes a choose b​​​​​.
'''
# === 40ms && 14.2MB === #
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        n, m = destination
        cnm = [[1 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                cnm[i][j] = cnm[i][j-1] * (i+j) // j
        # print(cnm)
        ans = ""
        while m > 0 and k > 0:
            # print(n, m, k)
            if k > cnm[n][m-1]:
                ans += "V"
                k -= cnm[n][m-1]
                n -= 1
            else:
                ans += "H"
                m -= 1
        # print("=" * 10)
        return ans + "H" * m + "V" * n