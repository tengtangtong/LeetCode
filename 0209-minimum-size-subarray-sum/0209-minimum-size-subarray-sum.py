class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left,curr = 0,0
        minimal_length = float('inf')

        # for loop and add 
        for right in range(len(nums)):

            curr += nums[right]

            # when the current sum more than target, record the minimal length
            while curr >= target:
                minimal_length = min(minimal_length, right-left + 1)
                curr -= nums[left]
                left += 1

        return 0 if minimal_length == float('inf') else minimal_length
                




        