class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        behind = 0
        for ahead in range(len(nums)):
            if nums[ahead] != 0:
                nums[behind], nums[ahead] = nums[ahead], nums[behind]
                behind += 1


            
            