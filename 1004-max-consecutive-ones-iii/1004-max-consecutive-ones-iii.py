class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        """longest ones if i can flip k bits"""
        
        left = 0 
        curr = 0  # counts the number of 0
        maximum = 0 
        
        for right in range(len(nums)):
            
            if nums[right] == 0:
                curr += 1
                
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
                
            maximum = max(maximum, right - left + 1)
            
        return maximum 
    