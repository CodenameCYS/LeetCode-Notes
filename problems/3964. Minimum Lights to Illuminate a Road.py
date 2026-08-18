'''
=== 3964. Minimum Lights to Illuminate a Road ===

You are given an integer array lights of length n, representing positions 0 through n - 1 on a road.
For each position i:
    - If lights[i] = v, where v > 0, there is a working bulb at position i that illuminates every position from max(0, i - v) to min(n - 1, i + v), inclusive.
    - If lights[i] = 0, there is no working bulb at position i.
A position is visible if it is illuminated by at least one working bulb. 
You may install additional bulbs at any positions. Each additional bulb installed at position j illuminates positions from max(0, j - 1) to min(n - 1, j + 1), inclusive.
Return the minimum number of additional bulbs required to make every position on the road visible.

Example 1:
    Input: lights = [0,0,0,0]
    Output: 2
    Explanation:
    One optimal placement is:
    Install an additional bulb at position 1, illuminating positions [0, 1, 2].
    Install an additional bulb at position 3, illuminating positions [2, 3].
    Therefore, the minimum number of additional bulbs required is 2.
Example 2:
    Input: lights = [0,0,0,2,0]
    Output: 1
    Explanation:
    Since lights[3] = 2, the working bulb at position 3 illuminates positions [1, 2, 3, 4].
    Installing an additional bulb at position 1 illuminates positions [0, 1, 2], making every position visible.
    Therefore, the minimum number of additional bulbs required is 1.
    
Constraints:
    1. 1 <= n == lights.length <= 105
    2. 0 <= lights[i] <= n
'''
# === 311ms && 31.45MB === #
class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        status = [0 for _ in range(n+1)]
        for i, v in enumerate(lights):
            if v > 0:
                st, ed = max(0, i-v), min(n, i+v+1)
                status[st] += 1
                status[ed] -= 1
        status = list(accumulate(status))
        cnt = 0
        ans = 0
        for i in range(n):
            if status[i] == 0:
                cnt += 1
            else:
                ans += (cnt+2) // 3
                cnt = 0
        ans += (cnt+2) // 3
        return ans