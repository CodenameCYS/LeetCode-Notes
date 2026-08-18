'''
=== 2589. Minimum Time to Complete All Tasks ===

There is a computer that can run an unlimited number of tasks at the same time. You are given a 2D integer array tasks where tasks[i] = [starti, endi, durationi] indicates that the ith task should run for a total of durationi seconds (not necessarily continuous) within the inclusive time range [starti, endi].
You may turn on the computer only when it needs to run a task. You can also turn it off if it is idle.
Return the minimum time during which the computer should be turned on to complete all tasks.

Example 1:
    Input: tasks = [[2,3,1],[4,5,1],[1,5,2]]
    Output: 2
    Explanation: 
    - The first task can be run in the inclusive time range [2, 2].
    - The second task can be run in the inclusive time range [5, 5].
    - The third task can be run in the two inclusive time ranges [2, 2] and [5, 5].
    The computer will be on for a total of 2 seconds.
Example 2:
    Input: tasks = [[1,3,2],[2,5,3],[5,6,2]]
    Output: 4
    Explanation: 
    - The first task can be run in the inclusive time range [2, 3].
    - The second task can be run in the inclusive time ranges [2, 3] and [5, 5].
    - The third task can be run in the two inclusive time range [5, 6].
    The computer will be on for a total of 4 seconds.
    
Constraints:
    1. 1 <= tasks.length <= 2000
    2. tasks[i].length == 3
    3. 1 <= starti, endi <= 2000
    4. 1 <= durationi <= endi - starti + 1
'''
# === 689ms && 15.3MB === #
class SegmentTreeNode:
	def __init__(self, val, lbound, rbound, lchild=None, rchild=None):
		self.val = val
		self.lbound = lbound
		self.rbound = rbound
		self.lchild = lchild
		self.rchild = rchild

class SegmentTree:
	def __init__(self, arr):
		self.length = len(arr)
		self.root = self.build(0, self.length-1, arr)
		self.vals = arr

	def feature_func(self, lval, rval):
		return lval + rval

	def build(self, lbound, rbound, arr):
		if lbound == rbound:
			root = SegmentTreeNode(arr[lbound], lbound, rbound)
		else:
			mid = (lbound+rbound) // 2
			lchild = self.build(lbound, mid, arr)
			rchild = self.build(mid+1, rbound, arr)
			val = self.feature_func(lchild.val, rchild.val)
			root = SegmentTreeNode(val, lbound, rbound, lchild, rchild)
		return root

	def update(self, idx, val):
		self.vals[idx] = val
		self._update(idx, val, self.root)
		return

	def _update(self, idx, val, root):
		if root.lbound == root.rbound:
			assert(root.lbound == idx)
			root.val = val
			return
		mid = (root.lbound + root.rbound) // 2
		if idx <= mid:
			self._update(idx, val, root.lchild)
		else:
			self._update(idx, val, root.rchild)
		root.val = self.feature_func(root.lchild.val, root.rchild.val)
		return

	def query(self, lb, rb):
		return self._query(lb, rb, self.root)	

	def _query(self, lb, rb, root):
		if lb == root.lbound and rb == root.rbound:
			return root.val
		mid = (root.lbound+root.rbound) // 2
		if rb <= mid:
			return self._query(lb, rb, root.lchild)
		elif lb > mid:
			return self._query(lb, rb, root.rchild)
		else:
			lval = 	self._query(lb, mid, root.lchild)
			rval = self._query(mid+1, rb, root.rchild)
			return self.feature_func(lval, rval)

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        max_t = max(x[1] for x in tasks)
        tasks = sorted(tasks, key=lambda x: x[1])
        status = [0 for _ in range(max_t+1)]
        status = SegmentTree(status)
        res = 0
        for st, ed, du in tasks:
            t = status.query(st, ed)
            if t >= du:
                continue
            delta = du-t
            for t in range(ed, st-1, -1):
                if delta == 0:
                    break
                if status.vals[t] == 0:
                    status.update(t, 1)
                    delta -= 1
                    res += 1
        return res
        