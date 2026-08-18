'''
=== 875. Koko Eating Bananas ===

Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.
Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
Return the minimum integer K such that she can eat all the bananas within H hours.

Example 1:
    Input: piles = [3,6,7,11], H = 8
    Output: 4
Example 2:
    Input: piles = [30,11,23,4,20], H = 5
    Output: 30
Example 3:
    Input: piles = [30,11,23,4,20], H = 6
    Output: 23
 
Constraints:
    1. 1 <= piles.length <= 10^4
    2. piles.length <= H <= 10^9
    3. 1 <= piles[i] <= 10^9
'''
# === 448ms(87.92%) && 15.1MB(58.95%) === #
class Solution:
    def count_hour(self, piles, speed):
        return sum([(p-1) // speed +1 for p in piles])
    
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low_speed = 1
        high_speed = max(piles)
        if self.count_hour(piles, low_speed) <= H:
            return low_speed
        while low_speed < high_speed-1:
            s = (low_speed + high_speed) // 2
            t = self.count_hour(piles, s)
            if t <= H:
                high_speed = s
            else:
                low_speed = s
        return high_speed
                