class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pt1 = nums[0]
        pt2 = nums[0]
        
        while True:
            pt1 = nums[pt1]         
            pt2 = nums[nums[pt2]]            
            if pt1 == pt2:
                break                         
                
        pt1 = nums[0]
        
        while pt1 != pt2:
            pt1 = nums[pt1]
            pt2 = nums[pt2]
         
        return pt1