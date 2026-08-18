'''
=== 2167. Minimum Time to Remove All Cars Containing Illegal Goods ===

You are given a 0-indexed binary string s which represents a sequence of train cars. s[i] = '0' denotes that the ith car does not contain illegal goods and s[i] = '1' denotes that the ith car does contain illegal goods.
As the train conductor, you would like to get rid of all the cars containing illegal goods. You can do any of the following three operations any number of times:
    - Remove a train car from the left end (i.e., remove s[0]) which takes 1 unit of time.
    - Remove a train car from the right end (i.e., remove s[s.length - 1]) which takes 1 unit of time.
    - Remove a train car from anywhere in the sequence which takes 2 units of time.
Return the minimum time to remove all the cars containing illegal goods.
Note that an empty sequence of cars is considered to have no cars containing illegal goods.

Example 1:
    Input: s = "1100101"
    Output: 5
    Explanation: 
    One way to remove all the cars containing illegal goods from the sequence is to
    - remove a car from the left end 2 times. Time taken is 2 * 1 = 2.
    - remove a car from the right end. Time taken is 1.
    - remove the car containing illegal goods found in the middle. Time taken is 2.
    This obtains a total time of 2 + 1 + 2 = 5. 
    An alternative way is to
    - remove a car from the left end 2 times. Time taken is 2 * 1 = 2.
    - remove a car from the right end 3 times. Time taken is 3 * 1 = 3.
    This also obtains a total time of 2 + 3 = 5.
    5 is the minimum time taken to remove all the cars containing illegal goods. 
    There are no other ways to remove them with less time.
Example 2:
    Input: s = "0010"
    Output: 2
    Explanation:
    One way to remove all the cars containing illegal goods from the sequence is to
    - remove a car from the left end 3 times. Time taken is 3 * 1 = 3.
    This obtains a total time of 3.
    Another way to remove all the cars containing illegal goods from the sequence is to
    - remove the car containing illegal goods found in the middle. Time taken is 2.
    This obtains a total time of 2.
    Another way to remove all the cars containing illegal goods from the sequence is to 
    - remove a car from the right end 2 times. Time taken is 2 * 1 = 2. 
    This obtains a total time of 2.
    2 is the minimum time taken to remove all the cars containing illegal goods. 
    There are no other ways to remove them with less time.
 
Constraints:
    1. 1 <= s.length <= 2 * 105
    2. s[i] is either '0' or '1'.
'''
# === 7526ms && 39.7MB === #
class Solution:
    def minimumTime(self, s: str) -> int:
        cnt = 0
        for ch in s:
            if ch == "1":
                cnt += 1
        tot = 2*cnt
        # print(tot)
        
        n = len(s)
        l2r = [0 for _ in range(n+1)]
        for i in range(n):
            l2r[i+1] = l2r[i] + 1 if s[i] == "0" else l2r[i] - 1
        # print(l2r) 
        r2l = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            r2l[i] = r2l[i+1] + 1 if s[i] == "0" else r2l[i+1] - 1
        # print(r2l)
        
        for i in range(n):
            l2r[i+1] = min(l2r[i+1], l2r[i])
            r2l[n-i-1] = min(r2l[n-i-1], r2l[n-i])
        # print(l2r, r2l)
        res = tot + min([x + y for x, y in zip(l2r, r2l)])
        # print("=" * 10)
        return res
        
        