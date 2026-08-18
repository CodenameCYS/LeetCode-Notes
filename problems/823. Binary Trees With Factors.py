'''
=== 823. Binary Trees With Factors ===

Given an array of unique integers, each integer is strictly greater than 1.
We make a binary tree using these integers and each number may be used for any number of times.
Each non-leaf node's value should be equal to the product of the values of it's children.
How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

Example 1:
    Input: A = [2, 4]
    Output: 3
    Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:
    Input: A = [2, 4, 5, 10]
    Output: 7
    Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 
Note:
    1. 1 <= A.length <= 1000.
    2. 2 <= A[i] <= 10 ^ 9.
'''
import math
# === 140ms(95.18%) && 13.9MB(50%) === #
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        A = sorted(A)
        counter = [1 for i in A]
        loc = {v:l for l, v in enumerate(A)}
        for i, num in enumerate(A):
            k = int(math.sqrt(num))
            j = 0
            while A[j] <= k:
                if num % A[j] == 0 and num // A[j] in loc.keys():
                    if A[j] == num // A[j]:
                        counter[i] = (counter[i] + counter[j] ** 2) % MOD
                    else:
                        counter[i] = (counter[i] + 2 * counter[j] * counter[loc[num // A[j]]]) % MOD
                j += 1
        return sum(counter) % MOD