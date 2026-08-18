'''
=== 3796. Find Maximum Value in a Constrained Sequence ===

You are given an integer n, a 2D integer array restrictions, and an integer array diff of length n - 1. Your task is to construct a sequence of length n, denoted by a[0], a[1], ..., a[n - 1], such that it satisfies the following conditions:
    - a[0] is 0.
    - All elements in the sequence are non-negative.
    - For every index i (0 <= i <= n - 2), abs(a[i] - a[i + 1]) <= diff[i].
    - For each restrictions[i] = [idx, maxVal], the value at position idx in the sequence must not exceed maxVal (i.e., a[idx] <= maxVal).
Your goal is to construct a valid sequence that maximizes the largest value within the sequence while satisfying all the above conditions.
Return an integer denoting the largest value present in such an optimal sequence.

Example 1:
    Input: n = 10, restrictions = [[3,1],[8,1]], diff = [2,2,3,1,4,5,1,1,2]
    Output: 6
    Explanation:
    The sequence a = [0, 2, 4, 1, 2, 6, 2, 1, 1, 3] satisfies the given constraints (a[3] <= 1 and a[8] <= 1).
    The maximum value in the sequence is 6.
Example 2:
    Input: n = 8, restrictions = [[3,2]], diff = [3,5,2,4,2,3,1]
    Output: 12
    Explanation:
    The sequence a = [0, 3, 3, 2, 6, 8, 11, 12] satisfies the given constraints (a[3] <= 2).
    The maximum value in the sequence is 12.

Constraints:
    1. 2 <= n <= 105
    2. 1 <= restrictions.length <= n - 1
    3. restrictions[i].length == 2
    4. restrictions[i] = [idx, maxVal]
    5. 1 <= idx < n
    6. 1 <= maxVal <= 106
    7. diff.length == n - 1
    8. 1 <= diff[i] <= 10
    9. The values of restrictions[i][0] are unique.
'''
# === 438ms && 57.18MB === #
class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        lbound, rbound = [math.inf for _ in range(n)], [math.inf for _ in range(n)]
        lbound[0] = 0
        rbound[0] = 0
        for idx, max_val in restrictions:
            lbound[idx] = max_val
            rbound[idx] = max_val
        
        for i in range(n-1):
            if lbound[i+1] == math.inf:
                lbound[i+1] = lbound[i] + diff[i]
            else:
                lbound[i+1] = min(lbound[i] + diff[i], lbound[i+1])
        
        for i in range(n-2, -1, -1):
            if rbound[i] == math.inf:
                rbound[i] = rbound[i+1] + diff[i]
            else:
                rbound[i] = min(rbound[i+1] + diff[i], rbound[i])

        # print(lbound, rbound)
        
        return max(min(x, y) for x, y in zip(lbound, rbound))
