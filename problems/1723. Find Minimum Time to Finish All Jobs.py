'''
=== 1723. Find Minimum Time to Finish All Jobs ===

You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.
There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.
Return the minimum possible maximum working time of any assignment.

Example 1:
    Input: jobs = [3,2,3], k = 3
    Output: 3
    Explanation: By assigning each person one job, the maximum time is 3.
Example 2:
    Input: jobs = [1,2,4,7,8], k = 2
    Output: 11
    Explanation: Assign the jobs the following way:
    Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
    Worker 2: 4, 7 (working time = 4 + 7 = 11)
    The maximum working time is 11.
 
Constraints:
    1. 1 <= k <= jobs.length <= 12
    2. 1 <= jobs[i] <= 107
'''
# === 2060ms && 83.5MB === #
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        if k == n:
            return max(jobs)
        elif k == 1:
            return sum(jobs)
        jobs = sorted(jobs)
        if k == n-1:
            return max(jobs[-1], jobs[0] + jobs[1])
        
        @lru_cache(None)
        def dp(work):
            # print(work, k)
            if len(work) == k:
                return max(work)
            m = len(work)
            res = math.inf
            work = list(work)
            for i in range(1, m):
                work[i] += work[0]
                res = min(dp(tuple(work[1:])), res)
                work[i] -= work[0]
            return res
        ans = dp(tuple(jobs))
        # print("=" * 20)
        return ans
            