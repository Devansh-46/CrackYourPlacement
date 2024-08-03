class SegmentTree:
    class Node:
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.left = None
            self.right = None
            self.sum = 0
    
    def __init__(self, start, end):
        def _build(start, end):
            if start > end:
                return None
            
            if start == end:
                return SegmentTree.Node(start, end)
            
            node = SegmentTree.Node(start, end)
            mid = (start + end) // 2
            node.left = _build(start, mid)
            node.right = _build(mid + 1, end)
            return node
        self.root = _build(start, end)
    
    def update(self, ind, val):
        def _update(node):
            if not node or node.start > ind or node.end < ind:
                return
            
            if node.start == node.end == ind:
                node.sum = val
                return
            
            _update(node.left)
            _update(node.right)
            node.sum = node.left.sum + node.right.sum
        _update(self.root)
    
    def query(self, query_start, query_end):
        def _query(node):
            if not node or node.start > query_end or node.end < query_start:
                return 0
            
            if node.start >= query_start and node.end <= query_end:
                return node.sum
            
            return _query(node.left) + _query(node.right)
        return _query(self.root)


class NumArray:
    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(0, len(nums) - 1)
        for i, num in enumerate(nums):
            self.segment_tree.update(i, num)

    def update(self, index: int, val: int) -> None:
        self.segment_tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.query(left, right)
