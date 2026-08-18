'''
=== 1542. Find Longest Awesome Substring ===

Given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it palindrome.
Return the length of the maximum length awesome substring of s.

Example 1:
    Input: s = "3242415"
    Output: 5
    Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.
Example 2:
    Input: s = "12345678"
    Output: 1
Example 3:
    Input: s = "213123"
    Output: 6
    Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.
Example 4:
    Input: s = "00"
    Output: 2
 
Constraints:
    1. 1 <= s.length <= 10^5
    2. s consists only of digits.
'''
# === 4076ms && 14.7MB === #
class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        
        counter = [0 for i in range(10)]
        cache = {tuple(counter): 0}
        
        ans = 0
        for i, c in enumerate(s):
            digit = ord(c)-ord('0')
            counter[digit] = (counter[digit] + 1) % 2
            if tuple(counter) in cache.keys():
                ans = max(ans, i+1 - cache[tuple(counter)])
            else:
                cache[tuple(counter)] = i+1
                
            for j in range(10):
                counter[j] = (counter[j] + 1) % 2
                if tuple(counter) in cache.keys():
                    ans = max(ans, i+1 - cache[tuple(counter)])
                counter[j] = (counter[j] + 1) % 2
            
        return ans
    
# === 1408ms && 14.7MB === #
class SolutionV2:
    def longestAwesome(self, s: str) -> int:
        counter = 0
        cache = {counter: 0}
        
        ans = 0
        flag = 1
        for c in s:
            counter = counter ^ (1 << (ord(c)-ord('0')))
            if counter in cache:
                ans = max(ans, flag - cache[counter])
            else:
                cache[counter] = flag
                
            bias = 1
            for _ in range(10):
                tmp = counter ^ bias
                if tmp in cache:
                    ans = max(ans, flag - cache[tmp])
                bias = bias << 1
            flag += 1
            
            # print("{}: {} -> {} --> {}".format(i, counter, cache, ans))
            
        return ans