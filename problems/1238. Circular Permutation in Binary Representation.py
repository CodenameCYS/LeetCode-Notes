'''
=== 1238. Circular Permutation in Binary Representation ===

Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :
    - p[0] = start
    - p[i] and p[i+1] differ by only one bit in their binary representation.
    - p[0] and p[2^n -1] must also differ by only one bit in their binary representation.
 
Example 1:
    Input: n = 2, start = 3
    Output: [3,2,0,1]
    - Explanation: The binary representation of the permutation is (11,10,00,01). 
    All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]
Example 2:
    Input: n = 3, start = 2
    Output: [2,6,7,5,4,0,1,3]
    - Explanation: The binary representation of the permutation is (010,110,111,101,100,000,001,011).
 
Constraints:
    1. 1 <= n <= 16
    2. 0 <= start < 2 ^ n
'''
# === 640ms & 37.3MB === #
class Solution:
    def bin2dec(self, arr):
        ans = 0
        for i in arr:
            ans = 2*ans + i
        return ans
    
    def circularPermutation(self, n: int, start: int) -> List[int]:
        tmp = []
        for i in range(n):
            if i == 0:
                tmp = [[0], [1]]
            else:
                tmp = [[0] + it for it in tmp] + [[1] + it for it in tmp[::-1]]
        tmp = [self.bin2dec(it) for it in tmp]
        index = tmp.index(start)
        return tmp[index:] + tmp[:index]

# === 228ms & 21.5MB === #
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        tmp = [0]
        cur = 1
        for i in range(n):
            tmp = [it for it in tmp] + [cur + it for it in tmp[::-1]]
            cur *= 2
        index = tmp.index(start)
        return tmp[index:] + tmp[:index]
        
        