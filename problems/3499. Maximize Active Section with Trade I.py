'''
=== 3499. Maximize Active Section with Trade I ===

You are given a binary string s of length n, where:
    - '1' represents an active section.
    - '0' represents an inactive section.
You can perform at most one trade to maximize the number of active sections in s. In a trade, you:
    - Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
    - Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
Return the maximum number of active sections in s after making the optimal trade.
Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. The augmented '1's do not contribute to the final count.

Example 1:
    Input: s = "01"
    Output: 1
    Explanation:
    Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.
Example 2:
    Input: s = "0100"
    Output: 4
    Explanation:
    String "0100" → Augmented to "101001".
    Choose "0100", convert "101001" → "100001" → "111111".
    The final string without augmentation is "1111". The maximum number of active sections is 4.
Example 3:
    Input: s = "1000100"
    Output: 7
    Explanation:
    String "1000100" → Augmented to "110001001".
    Choose "000100", convert "110001001" → "110000001" → "111111111".
    The final string without augmentation is "1111111". The maximum number of active sections is 7.
Example 4:
    Input: s = "01010"
    Output: 4
    Explanation:
    String "01010" → Augmented to "1010101".
    Choose "010", convert "1010101" → "1000101" → "1111101".
    The final string without augmentation is "11110". The maximum number of active sections is 4.
    
Constraints:
    1. 1 <= n == s.length <= 105
    2. s[i] is either '0' or '1'
'''
# === 672ms && 19.8MB === #
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        pre = "1"
        cnt = 0
        mem = []
        for i, ch in enumerate(s):
            if ch == pre:
                cnt += 1
            else:
                mem.append(cnt)
                cnt = 1
            pre = ch
        mem.append(cnt)
        if s[-1] == "0":
            mem.append(0)
        n = len(mem)
        original = sum(mem[::2])
        ans = original
        for i in range(1, n-3, 2):
            ans = max(ans, original + mem[i] + mem[i+2])
        return ans
            
# === 914ms && 18.8MB === #
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        pre = "1"
        cnt = 0
        mem = []
        for i, ch in enumerate(s):
            if ch == pre:
                cnt += 1
            else:
                if pre == "0":
                    mem.append(cnt)
                cnt = 1
            pre = ch
        if pre == "0":
            mem.append(cnt)
        n = len(mem)
        ones = Counter(s)["1"]
        ans = ones
        for i in range(n-1):
            ans = max(ans, ones + mem[i] + mem[i+1])
        return ans
            