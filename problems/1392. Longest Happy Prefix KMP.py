class Solution:
    def longestPrefix(self, s: str) -> str:
        prefix = [0] * len(s)

        for right in range(1, len(s)):
            matched = prefix[right - 1]
            while matched > 0 and s[right] != s[matched]:
                matched = prefix[matched - 1]
            if s[right] == s[matched]:
                matched += 1
            prefix[right] = matched

        return s[:prefix[-1]] if s else ""