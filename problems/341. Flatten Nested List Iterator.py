'''
=== 341. Flatten Nested List Iterator ===

Given a nested list of integers, implement an iterator to flatten it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
    Input: [[1,1],2,[1,1]]
    Output: [1,1,2,1,1]
    Explanation: By calling next repeatedly until hasNext returns false, 
                 the order of elements returned by next should be: [1,1,2,1,1].
Example 2:
    Input: [1,[4,[6]]]
    Output: [1,4,6]
    Explanation: By calling next repeatedly until hasNext returns false, 
                 the order of elements returned by next should be: [1,4,6].
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
# === 76ms(27.92%) && 17.6MB(92.11%) === #
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def get_elem(nested):
            res = []
            if nested.isInteger():
                res.append(nested.getInteger())
            else:
                tmp = nested.getList()
                for nested in tmp:
                    res.extend(get_elem(nested))
            return res

        self.cache = []
        for item in nestedList:
            self.cache.extend(get_elem(item))
        return
    
    def next(self) -> int:
        return self.cache.pop(0)
    
    def hasNext(self) -> bool:
        return self.cache != []
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())