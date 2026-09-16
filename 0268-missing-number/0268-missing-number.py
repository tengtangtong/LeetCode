class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        # only number missing from the array
        nums = set(nums)
        
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
                
        