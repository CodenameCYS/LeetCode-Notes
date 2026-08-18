'''
=== 3076. Shortest Uncommon Substring in an Array ===

You are given an array arr of size n consisting of non-empty strings.
Find a string array answer of size n such that:
    - answer[i] is the shortest substring of arr[i] that does not occur as a substring in any other string in arr. If multiple such substrings exist, answer[i] should be the lexicographically smallest. And if no such substring exists, answer[i] should be an empty string.
Return the array answer.

Example 1:
    Input: arr = ["cab","ad","bad","c"]
    Output: ["ab","","ba",""]
    Explanation: We have the following:
    - For the string "cab", the shortest substring that does not occur in any other string is either "ca" or "ab", we choose the lexicographically smaller substring, which is "ab".
    - For the string "ad", there is no substring that does not occur in any other string.
    - For the string "bad", the shortest substring that does not occur in any other string is "ba".
    - For the string "c", there is no substring that does not occur in any other string.
Example 2:
    Input: arr = ["abc","bcd","abcd"]
    Output: ["","","abcd"]
    Explanation: We have the following:
    - For the string "abc", there is no substring that does not occur in any other string.
    - For the string "bcd", there is no substring that does not occur in any other string.
    - For the string "abcd", the shortest substring that does not occur in any other string is "abcd".
 
Constraints:
    1. n == arr.length
    2. 2 <= n <= 100
    3. 1 <= arr[i].length <= 20
    4. arr[i] consists only of lowercase English letters.
'''
# === 246ms && 17.5MB === #
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        
        @lru_cache(None)
        def get_substring(s):
            n = len(s)
            ans = defaultdict(int)
            for i in range(n):
                for j in range(i+1, n+1):
                    ans[s[i:j]] += 1
            return ans
        
        cnt = defaultdict(int)
        for s in arr:
            subs = get_substring(s)
            for k, v in subs.items():
                cnt[k] += v
        # print(cnt)
        
        ans = ["" for _ in arr]
        for i, s in enumerate(arr):
            subs = get_substring(s)
            valid = sorted([k for k in subs if subs[k] == cnt[k]], key=lambda x: (len(x), x))
            # print(s, valid)
            if valid != []:
                ans[i] = valid[0]
        # print("=" * 10)
        return ans