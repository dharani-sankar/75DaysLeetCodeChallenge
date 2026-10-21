class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        major=None
        for num in nums:
            if count==0:
                major=num
            if num == major:
                count+=1
            else:
                count-=1
        return major