class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            current_sum += num
            
            target_prefix = current_sum - k
            
            if target_prefix in prefix_sums:
                total_subarrays += prefix_sums[target_prefix]
                
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return total_subarrays
        