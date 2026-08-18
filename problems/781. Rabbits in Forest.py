'''
=== 781. Rabbits in Forest ===

In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.
Return the minimum number of rabbits that could be in the forest.

Examples:
    Input: answers = [1, 1, 2]
    Output: 5
    - Explanation:
    The two rabbits that answered "1" could both be the same color, say red.
    The rabbit than answered "2" can't be red or the answers would be inconsistent.
    Say the rabbit that answered "2" was blue.
    Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
    The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

    Input: answers = [10, 10, 10]
    Output: 11

    Input: answers = []
    Output: 0

Note:
    1. answers will have length at most 1000.
    2. Each answers[i] will be an integer in the range [0, 999].
'''
import math
# === 40ms(78.82%) && 14.1MB(33.33%) === #
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = {}
        for a in answers:
            if a not in counter.keys():
                counter[a] = 1
            else:
                counter[a] += 1
        num = 0
        for a, n in counter.items():
            num += (a+1) * int(math.ceil(n / (a+1)))
        return num