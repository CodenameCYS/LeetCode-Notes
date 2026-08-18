'''
=== 3752. Lexicographically Smallest Negated Permutation that Sums to Target ===

You are given a positive integer n and an integer target.
Return the lexicographically smallest array of integers of size n such that:
    - The sum of its elements equals target.
    - The absolute values of its elements form a permutation of size n.
If no such array exists, return an empty array.
An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b.
A permutation of size n is a rearrangement of integers 1, 2, ..., n.

Example 1:
    Input: n = 3, target = 0
    Output: [-3,1,2]
    Explanation:
    The arrays that sum to 0 and whose absolute values form a permutation of size 3 are:
    [-3, 1, 2]
    [-3, 2, 1]
    [-2, -1, 3]
    [-2, 3, -1]
    [-1, -2, 3]
    [-1, 3, -2]
    [1, -3, 2]
    [1, 2, -3]
    [2, -3, 1]
    [2, 1, -3]
    [3, -2, -1]
    [3, -1, -2]
    The lexicographically smallest one is [-3, 1, 2].
Example 2:
    Input: n = 1, target = 10000000000
    Output: []
    Explanation:
    There are no arrays that sum to 10000000000 and whose absolute values form a permutation of size 1. Therefore, the answer is [].

Constraints:
    1. 1 <= n <= 105
    2. -1010 <= target <= 1010
'''
# === 106ms && 31.94MB === #
class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        s = n*(n+1)//2
        if s < abs(target):
            return []
        elif (s - target) % 2 == 1:
            return []
        delta = (s-target) // 2
        ans, used = [], set()
        for i in range(n, 0, -1):
            if delta == 0:
                break
            if delta > i:
                ans.append(-i)
                delta -= i
                used.add(i)
            else:
                ans.append(-delta)
                used.add(delta)
                break
        remain = [i for i in range(1, n+1) if i not in used]
        return ans + remain