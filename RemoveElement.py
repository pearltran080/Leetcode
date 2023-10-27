class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        count = 0
        k = 0
        i = 0
        while i < len(nums):
            if (nums[i] == val):
                count += 1
            else:
                nums[i-count] = nums[i]
                k += 1
            i += 1
        
        return k