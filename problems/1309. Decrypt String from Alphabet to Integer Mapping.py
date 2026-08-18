'''
=== 1309. Decrypt String from Alphabet to Integer Mapping ===

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
    - Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    - Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.
It's guaranteed that a unique mapping will always exist.

Example 1:
    Input: s = "10#11#12"
    Output: "jkab"
    - Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:
    Input: s = "1326#"
    Output: "acz"
Example 3:
    Input: s = "25#"
    Output: "y"
Example 4:
    Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    Output: "abcdefghijklmnopqrstuvwxyz"
 
Constraints:
    1. 1 <= s.length <= 1000
    2. s[i] only contains digits letters ('0'-'9') and '#' letter.
    3. s will be valid string such that mapping is always possible.
'''
# === 24ms & 12.6MB === #
class Solution:
    def int2char(self, s: str) -> str:
        asc = ord("a") + int(s) - 1
        return chr(asc)
    
    def decrypt(self, s: str) -> str:
        ans = "".join([self.int2char(c) for c in s[:-2]]) + self.int2char(s[-2:])
        return ans
    
    def freqAlphabets(self, s: str) -> str:
        subs = s.split("#")
        ans = "".join([self.decrypt(substr) for substr in subs[:-1]]) + "".join([self.int2char(c) for c in subs[-1]])
        return ans