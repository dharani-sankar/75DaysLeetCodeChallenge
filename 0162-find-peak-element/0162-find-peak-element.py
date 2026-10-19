class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if(n==0):
            return -1
        
        max_ele=nums[0]
        max_ind=0
        for i in range(1,n):
            if nums[i]>max_ele:
                max_ele=nums[i]
                max_ind=i
        return max_ind
            