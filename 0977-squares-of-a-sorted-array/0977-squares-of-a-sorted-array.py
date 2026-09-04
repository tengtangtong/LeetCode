class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        i = 0 
        j = len(nums) - 1
        k = len(nums) - 1
        new = [0] * len(nums)
        
        while k >= 0:
            
            if (nums[i])**2 < (nums[j])**2:
                new[k] = (nums[j])**2
                j -=1
                
            else:
                new[k] = (nums[i])**2
                i += 1
                
            k-=1
            
        return new
        
        
        