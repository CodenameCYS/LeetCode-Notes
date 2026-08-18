'''
=== 3950. Exactly One Consecutive Set Bits Pair ===

You are given an integer n.
Return true if its binary representation contains exactly one pair of consecutive set bits, and false otherwise.

Example 1:
    Input: nums = 6
    Output: true
    Explanation:
    Binary representation of 6 is 110.
    There is exactly one pair of consecutive set bits ("11"). Thus, the answer is true​​​​​​​.
Example 2:
    Input: nums = 5
    Output: false
    Explanation:
    Binary representation of 5 is 101.
    There are no consecutive set bits. Thus, the answer is false​​​​​​​.
 
Constraints:
    1. 0 <= n <= 105
'''
# === 7ms && 19.41MB === #
class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        bits = bin(n)[2:]
        # print(bits)
        m = len(bits)
        pair = [bits[i:i+2] for i in range(m-1)]
        cnt = Counter(pair)
        return cnt["11"] == 1