'''
=== 214. Shortest Palindrome ===

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:
    Input: "aacecaaa"
    Output: "aaacecaaa"
Example 2:
    Input: "abcd"
    Output: "dcbabcd"
'''
# === 56ms(84.2%) && 14.4MB(33.4%) === #
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        counter = 1
        pre = s[0]
        cache = []
        for c in s[1:]:
            if c == pre:
                counter += 1
            else:
                cache.append((pre, counter))
                counter = 1
                pre = c
        cache.append((pre, counter))
        n = len(cache)
        # print(n, cache)

        def is_possible(mid):
            for i in range(1, mid+1):
                if mid +i >= n:
                    return False
                if cache[mid-i][0] != cache[mid+i][0]:
                    return False
                elif i != mid and cache[mid-i][1] != cache[mid+i][1]:
                    return False
                elif i == mid and cache[mid-i][1] > cache[mid+i][1]:
                    return False
            return True

        def recover_string(mid):
            s1 = cache[mid][0] * cache[mid][1]
            s2 = "".join(c * n for c, n in cache[mid+1:])
            return s2[::-1] + s1 + s2

        mid = n // 2
        while mid > 0:
            if is_possible(mid):
                return recover_string(mid)
            mid -= 1
        return recover_string(mid)
