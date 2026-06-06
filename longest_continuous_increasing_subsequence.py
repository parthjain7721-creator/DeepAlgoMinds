class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        max_length = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_streak += 1
            else:
                current_streak = 1
                
            max_length = max(max_length, current_streak)
            
        return max_length