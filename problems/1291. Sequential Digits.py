'''
# === 1291. Sequential Digits === #

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
    Input: low = 100, high = 300
    Output: [123,234]
Example 2:
    Input: low = 1000, high = 13000
    Output: [1234,2345,3456,4567,5678,6789,12345]
 
Constraints:
    1. 10 <= low <= high <= 10^9
'''
# === 24ms & 12.8MB === #
class Solution:
    def calDigits(self, n):
        ans = 0
        while n != 0:
            ans += 1
            n = n // 10
        return ans
    
    def createSequentialDigits(self, n):
        ans = [i+1 for i in range(10-n)]
        for i in range(n-1):
            ans = [it * 10 + i+j+2 for j, it in enumerate(ans)]
        return ans
    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l = self.calDigits(low)
        h = self.calDigits(high)
        ans = []
        for i in range(h-l+1):
            digit = i + l
            tmp = [it for it in self.createSequentialDigits(digit) if it >= low and it <= high]
            ans.extend(tmp)
        return ans
            