'''
=== 1976. Number of Ways to Arrive at Destination ===

You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.
You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.
Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

Example 1:
    Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    Output: 4
    Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
    The four ways to get there in 7 minutes are:
    - 0 ➝ 6
    - 0 ➝ 4 ➝ 6
    - 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
    - 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
Example 2:
    Input: n = 2, roads = [[1,0,10]]
    Output: 1
    Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
 
Constraints:
    1. 1 <= n <= 200
    2. n - 1 <= roads.length <= n * (n - 1) / 2
    3. roads[i].length == 3
    4. 0 <= ui, vi <= n - 1
    5. 1 <= timei <= 109
    6. ui != vi
    7. There is at most one road connecting any two intersections.
    8. You can reach any intersection from any other intersection.
'''
# === 354ms && 20.5MB === #
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        # if n == 1:
        #     return 1 if num != "0" else 0
        
        @lru_cache(None)
        def dp(idx, pre):
            if idx >= n:
                return 1
            k = idx - pre
            pre = num[pre:idx]
            if num[idx] == "0" or n-idx < k or (n-idx == k and pre > num[idx:]):
                return 0
            res = 1 if n-idx > k or (n-idx == k and num[idx:] >= pre) else 0
            i = k + idx
            if k != 0 and n - i >= k and num[idx:idx+k] >= pre:
                res += dp(idx+k, idx)
            # print(f"idx = {idx} & pre = {pre}: init: {res}")
            for i in range(idx+k+1, n+1):
                if i - idx > n - i:
                    break
                # nxt = num[idx:i]
                res += dp(i, idx)
            # print(f"idx = {idx} & pre = {pre}: final: {res}")
            return res % MOD
        # print("=" * 10)
        return dp(0, 0)
                
            
        
        