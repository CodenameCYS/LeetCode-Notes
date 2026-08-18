'''
=== 846. Hand of Straights ===

Alice has a hand of cards, given as an array of integers.
Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
Return true if and only if she can.

Example 1:
    Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
    Output: true
    Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:
    Input: hand = [1,2,3,4,5], W = 4
    Output: false
    Explanation: Alice's hand can't be rearranged into groups of 4.
 
Constraints:
    1. 1 <= hand.length <= 10000
    2. 0 <= hand[i] <= 10^9
    3. 1 <= W <= hand.length

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
'''
# === 192ms(87.43%) && 15.3MB(70.80%) === #
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        counter = {}
        for n in hand:
            counter[n] = 1 if n not in counter.keys() else counter[n] + 1
        # print(counter)
        for n in sorted(counter.keys()):
            if counter[n] == 0:
                continue
            for i in range(n+1, n+W):
                counter[i] = counter.get(i, 0) - counter[n]
                if counter[i] < 0:
                    return False
            counter[n] = 0
            # print(counter)
        return True
        