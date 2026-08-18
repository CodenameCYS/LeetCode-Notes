'''
=== 599. Minimum Index Sum of Two Lists ===

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    Output: ["Shogun"]
    Explanation: The only restaurant they both like is "Shogun".
Example 2:
    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    Output: ["Shogun"]
    Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Note:
    1. The length of both lists will be in the range of [1, 1000].
    2. The length of strings in both lists will be in the range of [1, 30].
    3. The index is starting from 0 to the list length minus 1.
    4. No duplicates in both lists.
'''
# === 152ms(86.05%) && 12.7MB(100%) === #
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1 = {k:v for v,k in enumerate(list1)}
        l2 = {k:v for v,k in enumerate(list2)}
        l = {k:l1[k] + l2[k] for k in l1.keys() & l2.keys()}
        l = sorted(l.items(), key= lambda x: x[1])
        return [k for k, v in l if v == l[0][1]]