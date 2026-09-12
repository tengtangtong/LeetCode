class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # create prefix sum
        prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        for i in range(len(nums)):
            
            left_sum = prefix_sum[i-1] if i != 0 else 0
            right_sum = prefix_sum[-1] - prefix_sum[i] if i != len(nums) - 1 else 0 

            if left_sum == right_sum:
                return i

        return -1
