'''
=== 3468. Find the Number of Copy Arrays ===

You are given an array original of length n and a 2D array bounds of length n x 2, where bounds[i] = [ui, vi].
You need to find the number of possible arrays copy of length n such that:
    - (copy[i] - copy[i - 1]) == (original[i] - original[i - 1]) for 1 <= i <= n - 1.
    - ui <= copy[i] <= vi for 0 <= i <= n - 1.
Return the number of such arrays.

Example 1:
    Input: original = [1,2,3,4], bounds = [[1,2],[2,3],[3,4],[4,5]]
    Output: 2
    Explanation:
    The possible arrays are:
    [1, 2, 3, 4]
    [2, 3, 4, 5]
Example 2:
    Input: original = [1,2,3,4], bounds = [[1,10],[2,9],[3,8],[4,7]]
    Output: 4
    Explanation:
    The possible arrays are:
    [1, 2, 3, 4]
    [2, 3, 4, 5]
    [3, 4, 5, 6]
    [4, 5, 6, 7]
Example 3:
    Input: original = [1,2,1,2], bounds = [[1,1],[2,3],[3,3],[2,3]]
    Output: 0
    Explanation:
    No array is possible.

Constraints:
    1. 2 <= n == original.length <= 105
    2. 1 <= original[i] <= 109
    3. bounds.length == n
    4. bounds[i].length == 2
    5. 1 <= bounds[i][0] <= bounds[i][1] <= 109
'''
# === 61ms && 64.3MB === #
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)
        delta = [x-original[0] for x in original]
        
        lb, rb = bounds[0][0], bounds[0][1]
        for d, (l, r) in zip(delta, bounds):
            x = lb + d
            y = rb + d
            if x > r or y < l:
                return 0
            lb += max(0, l - x)
            rb -= max(0, y - r)
            if lb > rb:
                return 0
        
        return rb-lb+1
        
        