'''
=== 2217. Find Palindrome With Fixed Length ===

Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.
A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

Example 1:
    Input: queries = [1,2,3,4,5,90], intLength = 3
    Output: [101,111,121,131,141,999]
    Explanation:
    The first few palindromes of length 3 are:
    101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 201, ...
    The 90th palindrome of length 3 is 999.
Example 2:
    Input: queries = [2,4,6], intLength = 4
    Output: [1111,1331,1551]
    Explanation:
    The first six palindromes of length 4 are:
    1001, 1111, 1221, 1331, 1441, and 1551.
    
Constraints:
    1. 1 <= queries.length <= 5 * 104
    2. 1 <= queries[i] <= 109
    3. 1 <= intLength <= 15
'''
# === 1989ms && 125.7MB === #
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        
        @lru_cache(None)
        def fn(n, middle):
            # print(n, middle)
            if n == 0:
                return 0
            if n <= 2:
                return 10 if middle else 9
            return 10 * fn(n-2, True) if middle else 9 * fn(n-2, True)
        
        @lru_cache(None)
        def query(idx, n, middle):
            if idx >= fn(n, middle):
                return -1
            elif n == 1:
                return idx if middle else idx+1
            elif n == 2:
                return 11*idx if middle else 11*(idx+1)
            
            k = idx // fn(n-2, True)
            r = idx % fn(n-2, True)
            k = k if middle else k+1
            return k*(10**(n-1)) + 10 * query(r, n-2, True) + k
        
        # print(fn(3, False))
        # print(fn(1, True))
        return [query(q-1, intLength, False) for q in queries]

# === 1035ms && 28MB === #
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        n = (intLength + 1) // 2
        base = 10**(n-1)
        
        @lru_cache(None)
        def query(k):
            if k >= 9 * base:
                return -1
            k = k + base
            res = k
            if intLength % 2 == 1:
                k = k // 10
            while k != 0:
                res = res * 10 + k % 10
                k = k // 10
            return res
            
        return [query(q-1) for q in queries]