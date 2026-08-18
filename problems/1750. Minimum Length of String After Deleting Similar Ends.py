'''
=== 1750. Minimum Length of String After Deleting Similar Ends ===

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:
    1. Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
    2. Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
    3. The prefix and the suffix should not intersect at any index.
    4. The characters from the prefix and suffix must be the same.
    5. Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).

Example 1:
    Input: s = "ca"
    Output: 2
    Explanation: You can't remove any characters, so the string stays as is.
Example 2:
    Input: s = "cabaabac"
    Output: 0
    Explanation: An optimal sequence of operations is:
    - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
    - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
    - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
    - Take prefix = "a" and suffix = "a" and remove them, s = "".
Example 3:
    Input: s = "aabccabba"
    Output: 3
    Explanation: An optimal sequence of operations is:
    - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
    - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
 
Constraints:
    1. 1 <= s.length <= 105
    2. s only consists of characters 'a', 'b', and 'c'.
'''
# === 584ms && 22.2MB === #
class Solution:
    def minimumLength(self, s: str) -> int:
        record = []
        n = len(s)
        cnt = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                record.append((s[i-1], cnt))
                cnt = 1
        record.append((s[n-1], cnt))
        while len(record) > 1 and record[0][0] == record[-1][0]:
            record.pop(0)
            record.pop(-1)
        if len(record) == 1:
            return 0 if record[0][1] > 1 else record[0][1]
        
        return sum([x[1] for x in record])
                