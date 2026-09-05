class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """max average value given subarray of length k"""
        
        left = 0 
        curr = 0 
        curr_ave = 0
        maximum = float('-inf')
        
        for right in range(len(nums)):
            
            curr += nums[right]
            
            if right - left + 1 > k:
                curr -= nums[left]
                left += 1
                
                
            if right - left + 1 == k :
                curr_ave = curr / k
                maximum = max(maximum, curr_ave)
                
        return maximum
            
            
        