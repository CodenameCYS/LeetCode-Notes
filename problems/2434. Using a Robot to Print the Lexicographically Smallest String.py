'''
=== 2434. Using a Robot to Print the Lexicographically Smallest String ===

You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:
    - Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
    - Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.

Example 1:
    Input: s = "zza"
    Output: "azz"
    Explanation: Let p denote the written string.
    Initially p="", s="zza", t="".
    Perform first operation three times p="", s="", t="zza".
    Perform second operation three times p="azz", s="", t="".
Example 2:
    Input: s = "bac"
    Output: "abc"
    Explanation: Let p denote the written string.
    Perform first operation twice p="", s="c", t="ba". 
    Perform second operation twice p="ab", s="c", t="". 
    Perform first operation p="ab", s="", t="c". 
    Perform second operation p="abc", s="", t="".
Example 3:
    Input: s = "bdda"
    Output: "addb"
    Explanation: Let p denote the written string.
    Initially p="", s="bdda", t="".
    Perform first operation four times p="", s="", t="bdda".
    Perform second operation four times p="addb", s="", t="".
 
Constraints:
    1. 1 <= s.length <= 105
    2. s consists of only English lowercase letters.
'''
# === 3017ms && 16.9MB === #
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        used = [0 for _ in s]
        last = 0
        res = ""
        for ch in string.ascii_lowercase:
            while last-1 >= 0 and s[last-1] <= ch:
                if used[last-1] == 0:
                    res += s[last-1]
                    used[last-1] = 1
                last -= 1
            for i, c in enumerate(s):
                if i >= last and c == ch and used[i] == 0:
                    res += ch
                    last = i
                    used[i] = 1
        s = "".join([ch for i, ch in enumerate(s) if used[i] == 0])
        return res + s[::-1]