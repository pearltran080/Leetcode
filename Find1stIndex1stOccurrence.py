# Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:    # to skip checking everything
                if haystack[i:i+len(needle)] == needle:
                    return i

        return -1
