'''
=== 4026. Maximum Gap Between Stations ===

You are given two strings skill and station of lengths n and m, respectively.
skill[i] represents the skill of worker i, and station[j] represents the skill supported by station j.
You must assign every worker to a distinct station. Let ji be the index of the station assigned to worker i. A valid assignment must satisfy:
    - station[ji] == skill[i] for every 0 <= i < n.
    - The assigned station indices must be strictly increasing in worker order, meaning j0 < j1 < ... < jn - 1.
The gap of an assignment is the maximum difference between the station indices assigned to two consecutive workers. In other words, it is max(ji - ji - 1) over all 1 <= i < n.
If there is only one worker, the gap is 0.
Return the maximum possible gap among all valid assignments. It is guaranteed that at least one valid assignment exists.

Example 1:
    Input: skill = "aa", station = "aaaa"
    Output: 3
    Explanation:
    The two workers must be assigned to two different 'a' stations.
    Assigning them to stations [0, 3] gives a gap of 3.
Example 2:
    Input: skill = "xyz", station = "xyzz"
    Output: 2
    Explanation:
    Assign worker 0 to station j = 0, and worker 1 to station j = 1.
    To maximize the gap, assign worker 2 to station j = 3.
    This gives the assignment [0, 1, 3] with gaps [1, 2], so the gap is 2.
Example 3:
    Input: skill = "cbc", station = "cbcdbc"
    Output: 4
    Explanation:
    Assign worker 0 to station j = 0, and worker 1 to station j = 1.
    To maximize the gap, assign worker 2 to station j = 5.
    This gives the assignment [0, 1, 5] with gaps [1, 4], so the gap is 4.
 
Constraints:
    1. skill.length == n
    2. station.length == m
    3. 1 <= n <= m <= 105
    4. skill and station consist of lowercase English letters.
    5. It is guaranteed that a valid assignment exists for every worker.
'''
# === 709ms && 28.31MB === #
class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n, m = len(skill), len(station)
        closest = [0 for _ in range(n)]
        idx = 0
        for i, ch in enumerate(skill):
            while idx < m and station[idx] != ch:
                idx += 1
            closest[i] = idx
            idx += 1

        farest = [0 for _ in range(n)]
        i, j = n-1, m-1
        while i >= 0:
            while j >= 0 and station[j] != skill[i]:
                j -= 1
            farest[i] = j
            i -= 1
            j -= 1

        ans = 0
        for i in range(n-1):
            ans = max(ans, farest[i+1]-closest[i])
        return ans