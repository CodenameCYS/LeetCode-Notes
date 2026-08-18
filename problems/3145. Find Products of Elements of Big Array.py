'''
=== 3145. Find Products of Elements of Big Array ===

A powerful array for an integer x is the shortest sorted array of powers of two that sum up to x. For example, the powerful array for 11 is [1, 2, 8].
The array big_nums is created by concatenating the powerful arrays for every positive integer i in ascending order: 1, 2, 3, and so forth. Thus, big_nums starts as [1, 2, 1, 2, 4, 1, 4, 2, 4, 1, 2, 4, 8, ...].
You are given a 2D integer matrix queries, where for queries[i] = [fromi, toi, modi] you should calculate (big_nums[fromi] * big_nums[fromi + 1] * ... * big_nums[toi]) % modi.
Return an integer array answer such that answer[i] is the answer to the ith query.

Example 1:
    Input: queries = [[1,3,7]]
    Output: [4]
    Explanation:
    There is one query.
    big_nums[1..3] = [2,1,2]. The product of them is 4. The remainder of 4 under 7 is 4.
Example 2:
    Input: queries = [[2,5,3],[7,7,4]]
    Output: [2,2]
    Explanation:
    There are two queries.
    First query: big_nums[2..5] = [1,2,4,1]. The product of them is 8. The remainder of 8 under 3 is 2.
    Second query: big_nums[7] = 2. The remainder of 2 under 4 is 2.

Constraints:
    1. 1 <= queries.length <= 500
    2. queries[i].length == 3
    3. 0 <= queries[i][0] <= queries[i][1] <= 1015
    4. 1 <= queries[i][2] <= 105
'''
# === 7624ms && 662.3MB === #
class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        
        @lru_cache(None)
        def power(i, k, mod):
            if i==1 or k == 0:
                return 1
            elif k == 1:
                return i % mod
            return (power(i, k//2, mod) * power(i, k-k//2, mod)) % mod
        
        @lru_cache(None)
        def num2digits(n):
            return tuple([int(x) for x in bin(n)[2:][::-1]])
        
        def digits2num(digits):
            num = 0
            for d in digits[::-1]:
                num = num * 2 + d
            return num

        @lru_cache(None)
        def count_power(n, k):
            digits = list(num2digits(n))
            if k >= len(digits):
                return 0
            if digits[k] == 0:
                i = 0
                while i < k:
                    digits[i] = 1
                    i += 1
                while digits[i] == 0:
                    digits[i] = 1
                    i += 1
                digits[i] = 0
            digits.pop(k)
            return digits2num(digits) + 1
        
        @lru_cache(None)
        def get_big_num_end_index(num):
            ans = 0
            k = 0
            while True:
                cnt = count_power(num, k)
                if cnt == 0:
                    break
                ans += cnt
                k += 1
            return ans
        
        @lru_cache(None)
        def _count(idx, k):
            # print(f"_count: idx={idx}, k={k}")
            i, j = 0, idx+1
            while j-i > 1:
                m = (i+j) // 2
                cnt = get_big_num_end_index(m)
                if cnt <= idx:
                    i = m
                else:
                    j = m
            loc = get_big_num_end_index(i)
            r = idx-loc
            digits_j = num2digits(j)
            # print(f"_count: idx={idx}, k={k}, i={i}, j={j}, loc={loc}, r={r}, digits_j={digits_j}")
            extra = 1 if len(digits_j) > k and digits_j[k] == 1 and sum(digits_j[:k+1]) <= r else 0
            # print(f"_count: idx={idx}, k={k}, i={i}, j={j}, loc={loc}, r={r}, digits_j={digits_j}, ans={count_power(i, k) + extra}")
            return count_power(i, k) + extra
        
        @lru_cache(None)
        def count(idx):
            # print(f"count: idx={idx}", end=" ")
            if idx == 0:
                return defaultdict(int)
            cnt = defaultdict(int)
            # print("{", end="")
            k = 0
            while True:
                c = _count(idx, k)
                if c == 0:
                    break
                # print(f"{2**k}:{c}", end=", ")
                cnt[k] = c
                k += 1
            # print("}")
            return cnt
        
        @lru_cache(None)
        def query(i, j, mod):
            if i == 0:
                cnt1 = defaultdict(int)
            else:
                cnt1 = count(i-1)
            cnt2 = count(j)
            # print(f"query: i={i}, cnt1={cnt1}, j={j}, cnt2={cnt2}")
            ans = 1
            p, k = 1, 0
            while cnt2[k] > 0:
                c = cnt2[k] - cnt1[k]
                ans = (ans * power(p, c, mod)) % mod
                p = (p * 2) % mod
                k += 1
            # print(f"query: i={i}, j={j}, mod={mod}, cnt1={cnt1}, cnt2={cnt2}, ans={ans}")
            return ans
        
        # print(list([count_power(i, k) for i in range(1, 9)] for k in [0,1,2,3]))
        # print([get_big_num_end_index(i) for i in range(1, 9)])
        # print(list([_count(i, k) for i in range(1, 14)] for k in [0,1,2,3]))
        # list([count(i) for i in range(1, 14)])
            
        return [query(i+1, j+1, mod) for i, j, mod in queries]