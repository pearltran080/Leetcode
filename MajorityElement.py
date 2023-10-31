class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d = {}

        for i in nums:
            key = str(i)
            if key not in d:
                d[key] = 1
            else:
                d[key] = d[key]+1

        for key, val in d.items():
            if val > len(nums) / 2:
                return int(key)