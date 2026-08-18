'''
=== 3621. Number of Integers With Popcount-Depth Equal to K I ===

You are given two integers n and k.
For any positive integer x, define the following sequence:
    - p0 = x
    - pi+1 = popcount(pi) for all i >= 0, where popcount(y) is the number of set bits (1's) in the binary representation of y.
This sequence will eventually reach the value 1.
The popcount-depth of x is defined as the smallest integer d >= 0 such that pd = 1.
For example, if x = 7 (binary representation "111"). Then, the sequence is: 7 → 3 → 2 → 1, so the popcount-depth of 7 is 3.
Your task is to determine the number of integers in the range [1, n] whose popcount-depth is exactly equal to k.
Return the number of such integers.

Example 1:
    Input: n = 4, k = 1
    Output: 2
    Explanation:
    The following integers in the range [1, 4] have popcount-depth exactly equal to 1:
    x	Binary	Sequence
    2	"10"	2 → 1
    4	"100"	4 → 1
    Thus, the answer is 2.
Example 2:
    Input: n = 7, k = 2
    Output: 3
    Explanation:
    The following integers in the range [1, 7] have popcount-depth exactly equal to 2:
    x	Binary	Sequence
    3	"11"	3 → 2 → 1
    5	"101"	5 → 2 → 1
    6	"110"	6 → 2 → 1
    Thus, the answer is 3.

Constraints:
    1. 1 <= n <= 1015
    2. 0 <= k <= 5
'''
# === 41ms && 18.14MB === #
class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        m = len(bin(n)[2:])
        if k == 0:
            return 1
        elif k == 1:
            return m-1
        
        def get_valid(k):
            if k == 1:
                return {i for i in range(2, m+1) if Counter(bin(i)[2:])['1'] == 1}
            candi = get_valid(k-1)
            ans = set()
            for i in range(2, m+1):
                if Counter(bin(i)[2:])["1"] in candi:
                    ans.add(i)
            return ans
        
        def C(n, i):
            if i > n:
                return 0
            ans = 1
            i = min(i, n-i)
            for j in range(1, i+1):
                ans = ans * (n+1-j) // j
            return ans
        
        def get_count(n, cnt):
            if n == 0:
                return 1 if cnt == 0 else 0
            l = len(bin(n)[2:])
            if l < cnt:
                return 0
            if cnt == 0:
                return 1
            return C(l-1, cnt) + get_count(n-(1<<(l-1)), cnt-1)

        ans = 0
        ones = get_valid(k-1)
        print(ones)
        for cnt in ones:
            ans += get_count(n, cnt)
        return ans
