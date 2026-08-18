'''
=== 1864. Minimum Number of Swaps to Make the Binary String Alternating ===

Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.
The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
Any two characters may be swapped, even if they are not adjacent.

Example 1:
    Input: s = "111000"
    Output: 1
    Explanation: Swap positions 1 and 4: "111000" -> "101010"
    The string is now alternating.
Example 2:
    Input: s = "010"
    Output: 0
    Explanation: The string is already alternating, no swaps are needed.
Example 3:
    Input: s = "1110"
    Output: -1
 
Constraints:
    1. 1 <= s.length <= 1000
    2. s[i] is either '0' or '1'.
'''
# === 24ms && 14.3MB === #
class Solution:
    def minSwaps(self, s: str) -> int:
        cnt = Counter(s)
        def count_diff(s1, s2):
            cnt = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    cnt += 1
            return cnt // 2
        
        if abs(cnt["0"] - cnt["1"]) > 1:
            return -1
        elif cnt['0'] == cnt['1'] + 1:
            return count_diff("0" + "10" * (len(s) // 2), s)
        elif cnt["0"] == cnt['1'] - 1:
            return count_diff("1" + "01" * (len(s) // 2), s)
        else:
            return min(count_diff("10" * (len(s) // 2), s), count_diff("01" * (len(s) // 2), s))
            