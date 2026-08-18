'''
=== 3661. Maximum Walls Destroyed by Robots ===

There is an endless straight line populated with some robots and walls. You are given integer arrays robots, distance, and walls:
    - robots[i] is the position of the ith robot.
    - distance[i] is the maximum distance the ith robot's bullet can travel.
    - walls[j] is the position of the jth wall.
Every robot has one bullet that can either fire to the left or the right at most distance[i] meters.
A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it immediately stops at that robot and cannot continue.
Return the maximum number of unique walls that can be destroyed by the robots.

Notes:
    - A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.
    - Robots are not destroyed by bullets.
 
Example 1:
    Input: robots = [4], distance = [3], walls = [1,10]
    Output: 1
    Explanation:
    robots[0] = 4 fires left with distance[0] = 3, covering [1, 4] and destroys walls[0] = 1.
    Thus, the answer is 1.
Example 2:
    Input: robots = [10,2], distance = [5,1], walls = [5,2,7]
    Output: 3
    Explanation:
    robots[0] = 10 fires left with distance[0] = 5, covering [5, 10] and destroys walls[0] = 5 and walls[2] = 7.
    robots[1] = 2 fires left with distance[1] = 1, covering [1, 2] and destroys walls[1] = 2.
    Thus, the answer is 3.
Example 3:
    Input: robots = [1,2], distance = [100,1], walls = [10]
    Output: 0
    Explanation:
    In this example, only robots[0] can reach the wall, but its shot to the right is blocked by robots[1]; thus the answer is 0.

Constraints:
    1. 1 <= robots.length == distance.length <= 105
    2. 1 <= walls.length <= 105
    3. 1 <= robots[i], walls[j] <= 109
    4. 1 <= distance[i] <= 105
    5. All values in robots are unique
    6. All values in walls are unique
'''
# === 1933ms && 304.63MB === #
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        robs = sorted([(i, d) for i, d in zip(robots, distance)])
        walls = sorted(walls)
        # print(robs)
        # print(walls)
        
        n, m = len(robs), len(walls)

        @lru_cache(None)
        def dp(idx, ori):
            if idx >= n:
                return 0
            loc, dis = robs[idx]
            rbound = min(loc + dis, robs[idx+1][0]) if idx < n-1 else loc + dis
            rcount = bisect_left(walls, rbound+1) - bisect_left(walls, loc)
            lbound = max(loc - dis, robs[idx-1][0]) if idx > 0 else loc - dis
            lcount = bisect_left(walls, loc+1) - bisect_left(walls, lbound)
            # print(idx, ori, lbound, lcount, rbound, rcount)
            if ori == "right":
                if robs[idx-1][0] + robs[idx-1][1] >= loc:
                    wid = bisect.bisect_left(walls, loc)
                    if wid < m and walls[wid] == loc:
                        return rcount + dp(idx+1, "right") - 1
                    else:
                        return rcount + dp(idx+1, "right")
                elif robs[idx-1][0] + robs[idx-1][1] >= lbound:
                    _lbound = min(robs[idx-1][0] + robs[idx-1][1]+1, loc+1)
                    _lcount = bisect_left(walls, loc+1) - bisect_left(walls, _lbound)
                    return max(rcount + dp(idx+1, "right"), _lcount + dp(idx+1, "left"))
                else:
                    return max(rcount + dp(idx+1, "right"), lcount + dp(idx+1, "left"))
            else:
                if ori == "left" and lbound == robs[idx-1][0]:
                    wid = bisect.bisect_left(walls, lbound)
                    if wid < m and walls[wid] == lbound:
                        return max(rcount + dp(idx+1, "right"), lcount + dp(idx+1, "left")-1)
                return max(rcount + dp(idx+1, "right"), lcount + dp(idx+1, "left"))
        
        return dp(0, "")

