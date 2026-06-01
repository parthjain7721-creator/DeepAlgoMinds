class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        count = 0
        start = 0
        
        while count < n:
            current_idx = start
            prev_val = nums[start]
            
            while True:
                next_idx = (current_idx + k) % n
                # Swap the value into its new home
                nums[next_idx], prev_val = prev_val, nums[next_idx]
                
                current_idx = next_idx
                count += 1
                
                # If we cycled back to the start, break and move to the next index
                if start == current_idx:
                    break
            
            start += 1