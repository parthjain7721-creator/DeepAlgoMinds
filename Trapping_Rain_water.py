class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]  # Update new peak on left
                else:
                    total_water += left_max - height[left]  # Trap water!
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]  # Update new peak on right
                else:
                    total_water += right_max - height[right]  # Trap water!
                right -= 1
                
        return total_water