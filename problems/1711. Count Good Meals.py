'''
=== 1711. Count Good Meals ===

A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.
You can pick any two different foods to make a good meal.
Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.
Note that items with different indices are considered different even if they have the same deliciousness value.

Example 1:
    Input: deliciousness = [1,3,5,7,9]
    Output: 4
    Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
    Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
Example 2:
    Input: deliciousness = [1,1,1,3,3,3,7]
    Output: 15
    Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
 
Constraints:
    1. 1 <= deliciousness.length <= 105
    2. 0 <= deliciousness[i] <= 220
'''
# === 692ms && 20.6MB === #
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = Counter(deliciousness)
        elems = sorted(counter.keys())
        # print(counter)
        # print(elems)
        ans = 0
        s = 1
        for _ in range(22):
            for i in elems:
                if i > s // 2:
                    break
                elif i == s / 2:
                    # print(i, s-i, (counter[i] * (counter[i]-1)) // 2)
                    ans += (counter[i] * (counter[i]-1)) // 2
                    break
                elif s-i in counter:
                    # print(i, s-i, counter[i] * counter[s-i])
                    ans += counter[i] * counter[s-i]
                ans = ans % 1000000007
            s *= 2
        # print("=" * 20)
        return ans