'''
=== 1776. Car Fleet II ===

There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:
    - positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
    - speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.
Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.

Example 1:
    Input: cars = [[1,2],[2,1],[4,3],[7,2]]
    Output: [1.00000,-1.00000,3.00000,-1.00000]
    Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
Example 2:
    Input: cars = [[3,4],[5,4],[6,3],[9,1]]
    Output: [2.00000,1.00000,1.50000,-1.00000]
 
Constraints:
    1. 1 <= cars.length <= 105
    2. 1 <= positioni, speedi <= 106
    3. positioni < positioni+1
'''
# === 2372ms && 59.8MB === #
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        starting_points = [i-1 for i in range(n)]
        res = [-1 for _ in range(n)]
        
        def cal_time(st, ed):
            return (cars[ed][0] - cars[st][0]) / (cars[st][1] - cars[ed][1])
        
        q = []
        for i in range(n-1):
            if cars[i][1] > cars[i+1][1]:
                t = cal_time(i, i+1)
                heapq.heappush(q, (t, i, i+1))
        while q:
            t, st, ed = heapq.heappop(q)
            if res[st] != -1:
                continue
            res[st] = t
            starting_points[ed] = starting_points[st]
            st, ed = starting_points[st], ed
            if st == -1:
                continue
            if cars[st][1] > cars[ed][1]:
                t = cal_time(st, ed)
                heapq.heappush(q, (t, st, ed))
        return res
            