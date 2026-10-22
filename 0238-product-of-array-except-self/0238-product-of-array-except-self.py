class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        res=[0]*n
        if n==0:
            return res
        leftproduct,rightproduct=[0]*n,[0]*n
        prefix=1
        for i in range(0,n):
            prefix*=nums[i]
            leftproduct[i]=prefix
        suffix=1
        for i in range(n-1,-1,-1):
            suffix*=nums[i]
            rightproduct[i]=suffix
        res[0]=rightproduct[1]
        res[n-1]=leftproduct[n-2]
        for i in range(1,n-1):
            res[i]=leftproduct[i-1]*rightproduct[i+1]
        return res


