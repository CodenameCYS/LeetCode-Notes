'''
# === 1478. Allocate Mailboxes === #

Given the array houses and an integer k. where houses[i] is the location of the ith house along a street, your task is to allocate k mailboxes in the street.
Return the minimum total distance between each house and its nearest mailbox.
The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:
    Input: houses = [1,4,8,10,20], k = 3
    Output: 5
    Explanation: Allocate mailboxes in position 3, 9 and 20.
    Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 
Example 2:
    Input: houses = [2,3,5,12,18], k = 2
    Output: 9
    Explanation: Allocate mailboxes in position 3 and 14.
    Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.
Example 3:
    Input: houses = [7,4,6,1], k = 1
    Output: 8
Example 4:
    Input: houses = [3,6,14,10], k = 4
    Output: 0
 
Constraints:
    1. n == houses.length
    2. 1 <= n <= 100
    3. 1 <= houses[i] <= 10^4
    4. 1 <= k <= n
    5. Array houses contain unique integers.
'''
import math
import numpy
# === 1488ms && 31.4MB === #
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses = sorted(houses)
        n = len(houses)
        
        @lru_cache(None)
        def cal_distance(st, ed):
            m = int(numpy.median(houses[st:ed]))
            return sum([abs(d-m) for d in houses[st:ed]])
        
        @lru_cache(None)
        def dp(st, k):
            if k == 0:
                return cal_distance(st, n)
            ans = math.inf
            for i in range(st+1, n-k+1):
                s = cal_distance(st, i)
                ans = min(ans, s + dp(i, k-1))
            return ans
        return dp(0, k-1)