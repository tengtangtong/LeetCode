class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        lowest = 0 
        curr = 0 
        
        for num in nums:
            curr += num
            lowest = min(lowest, curr)
            
        return 1- lowest
        