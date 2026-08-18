'''
=== 3184. Count Pairs That Form a Complete Day I ===

Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.
A complete day is defined as a time duration that is an exact multiple of 24 hours.
For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

Example 1:
    Input: hours = [12,12,30,24,24]
    Output: 2
    Explanation:
    The pairs of indices that form a complete day are (0, 1) and (3, 4).
Example 2:
    Input: hours = [72,48,24,3]
    Output: 3
    Explanation:
    The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).

Constraints:
    1. 1 <= hours.length <= 100
    2. 1 <= hours[i] <= 109
'''
# === 43ms && 16.4MB === #
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = Counter([x % 24 for x in hours])
        return cnt[0] * (cnt[0]-1) // 2 + cnt[12] * (cnt[12]-1) // 2 + sum(cnt[i] * cnt[24-i] for i in range(1, 12))
        