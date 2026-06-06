class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_seen = {}
        last_seen = {}
        counts = {}
        
        degree = 0
        
        for i, num in enumerate(nums):
            if num not in first_seen:
                first_seen[num] = i # Record the starting boundary
            last_seen[num] = i      # Continuously update the ending boundary
            counts[num] = counts.get(num, 0) + 1
            
            if counts[num] > degree:
                degree = counts[num]
                
        min_length = len(nums)
        
        for num in counts:
            if counts[num] == degree:
                current_length = last_seen[num] - first_seen[num] + 1
                min_length = min(min_length, current_length)
                
        return min_length