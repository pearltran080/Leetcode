class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height)-1

        maxVol = 0
        volume = 0

        while left != right:
            dist = right - left
            if height[left] < height[right]:
                volume = height[left] * dist
                left += 1
            elif height[left] >= height[right]:
                volume = height[right] * dist
                right -= 1

            if volume > maxVol:
                maxVol = volume

        return maxVol