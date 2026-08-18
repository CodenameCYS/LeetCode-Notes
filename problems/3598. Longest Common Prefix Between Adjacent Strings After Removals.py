'''
=== 3598. Longest Common Prefix Between Adjacent Strings After Removals ===

You are given an array of strings words. For each index i in the range [0, words.length - 1], perform the following steps:
    - Remove the element at index i from the words array.
    - Compute the length of the longest common prefix among all adjacent pairs in the modified array.
Return an array answer, where answer[i] is the length of the longest common prefix between the adjacent pairs after removing the element at index i. If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0.
A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.

Example 1:
    Input: words = ["jump","run","run","jump","run"]
    Output: [3,0,0,3,3]
    Explanation:
    Removing index 0:
    words becomes ["run", "run", "jump", "run"]
    Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
    Removing index 1:
    words becomes ["jump", "run", "jump", "run"]
    No adjacent pairs share a common prefix (length 0)
    Removing index 2:
    words becomes ["jump", "run", "jump", "run"]
    No adjacent pairs share a common prefix (length 0)
    Removing index 3:
    words becomes ["jump", "run", "run", "run"]
    Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
    Removing index 4:
    words becomes ["jump", "run", "run", "jump"]
    Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
Example 2:
    Input: words = ["dog","racer","car"]
    Output: [0,0,0]
    Explanation:
    Removing any index results in an answer of 0.
 
Constraints:
    1. 1 <= words.length <= 105
    2. 1 <= words[i].length <= 104
    3. words[i] consists of lowercase English letters.
    4. The sum of words[i].length is smaller than or equal 105.
'''
# === 1000ms && 40.39MB === #
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n == 1:
            return [0]
        if len(set(words)) == 1 and n > 2:
            return [len(words[0]) for _ in range(n)]
        
        def count_prefix(w1, w2):
            if len(w1) > len(w2):
                return count_prefix(w2, w1)
            ans = 0
            for ch1, ch2 in zip(w1, w2):
                if ch1 != ch2:
                    break
                ans += 1
            return ans

        adj = [count_prefix(words[i], words[i+1]) for i in range(n-1)]
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        for i in range(n-1):
            left[i+1] = max(left[i], adj[i])
            right[n-2-i] = max(right[n-1-i], adj[n-2-i])
        tri = [count_prefix(words[i-1], words[i+1]) for i in range(1, n-1)]
        # print(len(adj), len(tri))
        ans = []
        for i in range(n):
            if i == 0:
                m = right[1]
            elif i == n-1:
                m = left[n-2]
            else:
                m = max(left[i-1], right[i+1])
            ans.append(max(m, tri[i-1]) if 1 <= i < n-1 else m)
        return ans
