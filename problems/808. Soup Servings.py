'''
=== 808. Soup Servings ===

There are two types of soup: type A and type B. Initially we have N ml of each type of soup. There are four kinds of operations:
    - Serve 100 ml of soup A and 0 ml of soup B
    - Serve 75 ml of soup A and 25 ml of soup B
    - Serve 50 ml of soup A and 50 ml of soup B
    - Serve 25 ml of soup A and 75 ml of soup B
When we serve some soup, we give it to someone and we no longer have it.  Each turn, we will choose from the four operations with equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as we can.  We stop once we no longer have some quantity of both types of soup.
Note that we do not have the operation where all 100 ml's of soup B are used first.  
Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time.

Example:
    Input: N = 50
    Output: 0.625
    Explanation: 
    If we choose the first two operations, A will become empty first. For the third operation, A and B will become empty at the same time. For the fourth operation, B will become empty first. So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Notes:
    1. 0 <= N <= 10^9. 
    2. Answers within 10^-6 of the true value will be accepted as correct.
'''
# === 32ms(91.47%) && 14.3MB(100%) === #
class Solution:
    def soupServings(self, N: int) -> float:
        @lru_cache(None)
        def dp(x, y):
            if x <= 0 and y <= 0:
                return 0.5
            elif x <= 0:
                return 1
            elif y <= 0:
                return 0
            else:
                return 0.25 * (dp(x-100, y) + dp(x-75, y-25) + dp(x-50, y-50) + dp(x-25, y-75))
            
        return dp(N, N) if N < 5000 else 1