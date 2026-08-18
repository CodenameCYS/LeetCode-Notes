'''
=== 1705. Maximum Number of Eaten Apples ===

There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.
You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.
Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.

Example 1:
    Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
    Output: 7
    Explanation: You can eat 7 apples:
    - On the first day, you eat an apple that grew on the first day.
    - On the second day, you eat an apple that grew on the second day.
    - On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
    - On the fourth to the seventh days, you eat apples that grew on the fourth day.
Example 2:
    Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
    Output: 5
    Explanation: You can eat 5 apples:
    - On the first to the third day you eat apples that grew on the first day.
    - Do nothing on the fouth and fifth days.
    - On the sixth and seventh days you eat apples that grew on the sixth day.
 
Constraints:
    1. apples.length == n
    2. days.length == n
    3. 1 <= n <= 2 * 104
    4. 0 <= apples[i], days[i] <= 2 * 104
    5. days[i] = 0 if and only if apples[i] = 0.
'''
# === 700ms && 18.8MB === #
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = 0
        q = []
        n = len(apples)
        i = 0
        while i < n or q != []:
            # print(q)
            if i<n and apples[i] != 0:
                if q != [] and i+days[i] == q[0][0]:
                    q[0][1] += apples[i]
                else:
                    heapq.heappush(q, [i+days[i], apples[i]])
            while q != [] and q[0][0] <= i:
                heapq.heappop(q)
            if q != []:
                ans += 1
                q[0][1] -= 1
                if q[0][1] == 0:
                    heapq.heappop(q)
            i += 1
        return ans
                