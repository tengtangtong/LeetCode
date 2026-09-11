class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int: 
        
        # two pointers one for each list
        pointer_a, pointer_b = 0,0

        # while none of them exceed their list end index
        while pointer_a <= len(nums1) - 1 and pointer_b <= len(nums2) - 1:

            # get values of each pointer
            a_value = nums1[pointer_a]
            b_value = nums2[pointer_b]

            # if a value is lesser, move a pointer up 
            if a_value < b_value:
                pointer_a +=1
            elif b_value < a_value:
                pointer_b +=1
            elif a_value == b_value:
                return a_value

        return -1


        