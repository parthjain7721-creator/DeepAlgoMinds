from collections import Counter
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_counts = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        
        self.nums2[index] = new_val
        
        self.nums2_counts[old_val] -= 1
        self.nums2_counts[new_val] += 1

    def count(self, tot: int) -> int:
        pair_count = 0
        
        for x in self.nums1:
            target = tot - x
            if target in self.nums2_counts:
                pair_count += self.nums2_counts[target]
                
        return pair_count
    