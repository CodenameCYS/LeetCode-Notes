'''
=== 705. Design HashSet ===

Design a HashSet without using any built-in hash table libraries.
To be specific, your design should include these functions:
    1. add(value): Insert a value into the HashSet. 
    2. contains(value) : Return whether the value exists in the HashSet or not.
    3. remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:
    MyHashSet hashSet = new MyHashSet();
    hashSet.add(1);         
    hashSet.add(2);         
    hashSet.contains(1);    // returns true
    hashSet.contains(3);    // returns false (not found)
    hashSet.add(2);          
    hashSet.contains(2);    // returns true
    hashSet.remove(2);          
    hashSet.contains(2);    // returns false (already removed)

Note:
    1. All values will be in the range of [0, 1000000].
    2. The number of operations will be in the range of [1, 10000].
    3. Please do not use the built-in HashSet library.
'''
# === 164ms(79.86%) && 17.4MB(53.85%) === #
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = set()

    def add(self, key: int) -> None:
        self.hashset.add(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.hashset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)