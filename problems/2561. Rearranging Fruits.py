'''
=== 2561. Rearranging Fruits ===

You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:
    - Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
    - The cost of the swap is min(basket1[i],basket2[j]).
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.
Return the minimum cost to make both the baskets equal or -1 if impossible.

Example 1:
    Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
    Output: 1
    Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
Example 2:
    Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
    Output: -1
    Explanation: It can be shown that it is impossible to make both the baskets equal.
 
Constraints:
    1. basket1.length == bakste2.length
    2. 1 <= basket1.length <= 105
    3. 1 <= basket1[i],basket2[i] <= 109
'''
# === 813ms && 36.9MB === #
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = defaultdict(int)
        for u, v in zip(basket1, basket2):
            cnt[u] += 1
            cnt[v] -= 1
        # print(cnt)
        move_in, move_out = [], []
        for k, v in cnt.items():
            if v % 2 == 1:
                return -1
            elif v > 0:
                move_out.extend([k] * (v // 2))
            else:
                move_in.extend([k] * (-v // 2))
        # print(move_in, move_out)
        if move_in == []:
            return 0
        _min = min(cnt.keys())
        move_in = sorted(move_in)
        move_out = sorted(move_out, reverse=True)
        return sum(min(2*_min, min(x, y)) for x, y in zip(move_in, move_out))