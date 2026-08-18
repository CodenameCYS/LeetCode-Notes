'''
=== 826. Most Profit Assigning Work ===

We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 
Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 
Every worker can be assigned at most one job, but one job can be completed multiple times.
For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.
What is the most profit we can make?

Example 1:
    Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
    Output: 100 
    Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.

Notes:
    1. 1 <= difficulty.length = profit.length <= 10000
    2. 1 <= worker.length <= 10000
    3. difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
'''
# === 616ms(20.85%) && 16.7MB(25%) === #
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        cache = sorted([it for it in zip(difficulty, profit)], key = lambda x: x[1], reverse=True)
        
        worker = sorted(worker, reverse=True)
        
        ans = 0
        for w in worker:
            while cache != [] and cache[0][0] > w:
                cache.pop(0)
            if cache == []:
                break
            ans += cache[0][1]
        return ans