'''
=== 3714. Longest Balanced Substring II ===

You are given a string s consisting only of the characters 'a', 'b', and 'c'.
A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
Return the length of the longest balanced substring of s.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: s = "abbac"
    Output: 4
    Explanation:
    The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.
Example 2:
    Input: s = "aabcc"
    Output: 3
    Explanation:
    The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.
Example 3:
    Input: s = "aba"
    Output: 2
    Explanation:
    One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

Constraints:
    1. 1 <= s.length <= 105
    2. s contains only the characters 'a', 'b', and 'c'.
'''
# === 1669ms && 48.55MB === #
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        chars = set(s)

        def longest_balanced_1(s):
            ans = 0
            prev, cnt = "", 0
            for ch in s:
                if ch == prev:
                    cnt += 1
                else:
                    prev, cnt = ch, 1
                ans = max(ans, cnt)
            return ans

        def longest_balanced_2(s, a, b):
            ans = 0
            cache = defaultdict(list)
            diff = 0
            cache[diff].append(0)
            for i, ch in enumerate(s):
                if ch == a:
                    diff += 1
                elif ch == b:
                    diff -= 1
                else:
                    ans = max(ans, max(loc[-1]-loc[0] for loc in cache.values()))
                    cache = defaultdict(list)
                    diff = 0
                    cache[diff].append(i+1)
                    continue
                cache[diff].append(i+1)
            return max(ans, max(loc[-1]-loc[0] for loc in cache.values()))

        def longest_balanced_3(s):
            cache = defaultdict(list)
            diff_ab, diff_ac = 0, 0
            cache[(diff_ab,diff_ac)].append(0)
            for i, ch in enumerate(s):
                if ch == 'a':
                    diff_ab += 1
                    diff_ac += 1
                elif ch == "b":
                    diff_ab -= 1
                else:
                    diff_ac -= 1
                cache[(diff_ab,diff_ac)].append(i+1)
            return max(loc[-1]-loc[0] for loc in cache.values())

        if len(chars) == 1:
            return n
        elif len(chars) == 2:
            a, b = list(chars)
            return max(longest_balanced_2(s, a, b), longest_balanced_1(s))
        else:
            # print(longest_balanced_3(s), longest_balanced_2(s, "a", "b"), longest_balanced_2(s, "a", "c"), longest_balanced_2(s, "b", "c"), longest_balanced_1(s))
            return max(longest_balanced_3(s), longest_balanced_2(s, "a", "b"), longest_balanced_2(s, "a", "c"), longest_balanced_2(s, "b", "c"), longest_balanced_1(s))