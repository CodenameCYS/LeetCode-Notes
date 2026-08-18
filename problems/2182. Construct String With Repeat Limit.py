'''
=== 2182. Construct String With Repeat Limit ===

You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.
Return the lexicographically largest repeatLimitedString possible.
A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

Example 1:
    Input: s = "cczazcc", repeatLimit = 3
    Output: "zzcccac"
    Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
    The letter 'a' appears at most 1 time in a row.
    The letter 'c' appears at most 3 times in a row.
    The letter 'z' appears at most 2 times in a row.
    Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
    The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
    Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
Example 2:
    Input: s = "aababab", repeatLimit = 2
    Output: "bbabaa"
    Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
    The letter 'a' appears at most 2 times in a row.
    The letter 'b' appears at most 2 times in a row.
    Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
    The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
    Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
 
Constraints:
    1. 1 <= repeatLimit <= s.length <= 105
    2. s consists of lowercase English letters.
'''
# === 84ms && 15.7MB === #
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        # print(cnt)
        res = ""
        letters = string.ascii_lowercase[::-1]
        for i, ch in enumerate(letters):
            if cnt[ch] == 0:
                continue
            j = i+1
            while j < 26 and cnt[ch] >= repeatLimit:
                while j < 26 and cnt[letters[j]] == 0:
                    j += 1
                if j >= 26:
                    break
                r = min(cnt[ch] // repeatLimit, cnt[letters[j]])
                res += (ch * repeatLimit + letters[j]) * r
                cnt[ch] -= repeatLimit * r
                cnt[letters[j]] -= r
            if j >= 26:
                res += ch * min(repeatLimit, cnt[ch])
            elif 0 < cnt[ch] < repeatLimit:
                res += ch * cnt[ch]
            elif cnt[ch] == 0:
                res = res[:-1]
                cnt[letters[j]] += 1
            cnt[ch] = 0
            # print(res, cnt, i, j)
        return res
                