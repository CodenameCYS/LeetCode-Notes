'''
=== 2327. Number of People Aware of a Secret ===

On day 1, one person discovers a secret.
You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.
Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: n = 6, delay = 2, forget = 4
    Output: 5
    Explanation:
    Day 1: Suppose the first person is named A. (1 person)
    Day 2: A is the only person who knows the secret. (1 person)
    Day 3: A shares the secret with a new person, B. (2 people)
    Day 4: A shares the secret with a new person, C. (3 people)
    Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
    Day 6: B shares the secret with E, and C shares the secret with F. (5 people)
Example 2:
    Input: n = 4, delay = 1, forget = 3
    Output: 6
    Explanation:
    Day 1: The first person is named A. (1 person)
    Day 2: A shares the secret with B. (2 people)
    Day 3: A and B share the secret with 2 new people, C and D. (4 people)
    Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)
 
Constraints:
    1. 2 <= n <= 1000
    2. 1 <= delay < forget <= n
'''
# === 933ms && 17.1MB === #
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def fp(idx):
            return np(idx-forget) 
        
        @lru_cache(None)
        def np(idx):
            if idx == 1:
                return 1
            elif idx <= delay:
                return 0
            res = 0
            for i in range(idx-forget+1, idx-delay+1):
                res += np(i)
            return res % MOD
        
        @lru_cache(None)
        def dp(idx):
            # print(idx)
            if idx <= 0:
                return 0
            elif idx <= delay:
                return 1
            return (dp(idx-1) - fp(idx) + np(idx)) % MOD
        
        # print("fp: ", [fp(i) for i in range(1, n+1)])
        # print("np: ", [np(i) for i in range(1, n+1)])
        # print("dp: ", [dp(i) for i in range(1, n+1)])
        # print("=" * 10)
        return dp(n)