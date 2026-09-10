class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        # ansewr array
        ans=[]
        
        # create prefix sum array
        prefix_sum = [nums[0]]
    
        for i in range(1,len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
            
        # loop and get the answer
        for i in range(len(nums)):
            
            # check if there are k radius
            if i - k < 0 or i + k > len(nums) - 1:
                ans.append(-1)
            
            # else we just look ahead by k and take the prefix sum
            else: 
                total = prefix_sum[i + k] 
                if i > k  :
                    total -= prefix_sum[i- (k+1)]
                average = total // (k*2 + 1)
                ans.append(average)
                
        return ans