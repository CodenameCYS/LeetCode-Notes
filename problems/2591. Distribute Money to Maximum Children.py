'''
=== 2591. Distribute Money to Maximum Children ===

You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.
You have to distribute the money according to the following rules:
    - All money must be distributed.
    - Everyone must receive at least 1 dollar.
    - Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.

Example 1:
    Input: money = 20, children = 3
    Output: 1
    Explanation: 
    The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
    - 8 dollars to the first child.
    - 9 dollars to the second child. 
    - 3 dollars to the third child.
    It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.
Example 2:
    Input: money = 16, children = 2
    Output: 2
    Explanation: Each child can be given 8 dollars.
 
Constraints:
    1. 1 <= money <= 200
    2. 2 <= children <= 30
'''
# === 35ms && 13.8MB === #
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1
        n = money // 7
        r = money % 7 
        if r == 0:
            return n if n <= children else children - 1
        elif r != 3:
            return n if n < children else children - 1
        elif n == children-1:
            return n-1
        else:
            return n if n < children-1 else children - 1
        