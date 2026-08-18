'''
=== 2312. Selling Pieces of Wood ===

You are given two integers m and n that represent the height and width of a rectangular piece of wood. You are also given a 2D integer array prices, where prices[i] = [hi, wi, pricei] indicates you can sell a rectangular piece of wood of height hi and width wi for pricei dollars.
To cut a piece of wood, you must make a vertical or horizontal cut across the entire height or width of the piece to split it into two smaller pieces. After cutting a piece of wood into some number of smaller pieces, you can sell pieces according to prices. You may sell multiple pieces of the same shape, and you do not have to sell all the shapes. The grain of the wood makes a difference, so you cannot rotate a piece to swap its height and width.
Return the maximum money you can earn after cutting an m x n piece of wood.
Note that you can cut the piece of wood as many times as you want.

Example 1:
    Input: m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]
    Output: 19
    Explanation: The diagram above shows a possible scenario. It consists of:
    - 2 pieces of wood shaped 2 x 2, selling for a price of 2 * 7 = 14.
    - 1 piece of wood shaped 2 x 1, selling for a price of 1 * 3 = 3.
    - 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2.
    This obtains a total of 14 + 3 + 2 = 19 money earned.
    It can be shown that 19 is the maximum amount of money that can be earned.
Example 2:
    Input: m = 4, n = 6, prices = [[3,2,10],[1,4,2],[4,1,3]]
    Output: 32
    Explanation: The diagram above shows a possible scenario. It consists of:
    - 3 pieces of wood shaped 3 x 2, selling for a price of 3 * 10 = 30.
    - 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2.
    This obtains a total of 30 + 2 = 32 money earned.
    It can be shown that 32 is the maximum amount of money that can be earned.
    Notice that we cannot rotate the 1 x 4 piece of wood to obtain a 4 x 1 piece of wood.
 
Constraints:
    1. 1 <= m, n <= 200
    2. 1 <= prices.length <= 2 * 104
    3. prices[i].length == 3
    4. 1 <= hi <= m
    5. 1 <= wi <= n
    6. 1 <= pricei <= 106
    7. All the shapes of wood (hi, wi) are pairwise distinct.
'''
# === 1086ms && 23.1MB === #
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        prices = sorted(prices, key=lambda x: -x[2] / (x[0] * x[1]))
        print(prices)
        
        @lru_cache(None)
        def dp(w, h, idx):
            res = 0
            for x, y, p in prices[idx:]:
                if x > w or y > h:
                    continue
                if p / (x * y) * (w * h) <= res:
                    break
                if w % x == 0 and h % y == 0:
                    res = max(res, (w//x) * (h//y)*p)
                    break
                elif w % x == 0:
                    i = w // x
                    for j in range(h//y, 0, -1):
                        s = i * j * p
                        wr, hr = w - x*i, h - y*j
                        res = max(res, s + dp(wr, h, idx+1) + dp(w-wr, hr, idx+1), s + dp(wr, h-hr, idx+1) + dp(w, hr, idx+1))
                elif h % y == 0:
                    j = h // y
                    for i in range(w//x, 0, -1):
                        s = i * j * p
                        wr, hr = w - x*i, h - y*j
                        res = max(res, s + dp(wr, h, idx+1) + dp(w-wr, hr, idx+1), s + dp(wr, h-hr, idx+1) + dp(w, hr, idx+1))
                else:
                    for i in range(w//x, 0, -1):
                        for j in range(h//y, 0, -1):
                            s = i * j * p
                            wr, hr = w - x*i, h - y*j
                            res = max(res, s + dp(wr, h, idx+1) + dp(w-wr, hr, idx+1), s + dp(wr, h-hr, idx+1) + dp(w, hr, idx+1))
            return res
        
        return dp(m, n, 0)