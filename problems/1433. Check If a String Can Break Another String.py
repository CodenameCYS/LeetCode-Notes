'''
=== 1433. Check If a String Can Break Another String ===

Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa (in other words s2 can break s1).
A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

Example 1:
    Input: s1 = "abc", s2 = "xya"
    Output: true
    Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".
Example 2:
    Input: s1 = "abe", s2 = "acd"
    Output: false 
    Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.
Example 3:
    Input: s1 = "leetcodee", s2 = "interview"
    Output: true
 
Constraints:
    1. s1.length == n
    2. s2.length == n
    3. 1 <= n <= 10^5
    4. All strings consist of lowercase English letters.
'''
# === 140ms(91.62%) && 16.2MB === #
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        return all(c1 <= c2 for c1, c2 in zip(s1, s2)) or all(c1 >= c2 for c1, c2 in zip(s1, s2))