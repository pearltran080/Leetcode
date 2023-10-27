class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        currLength = 0
        wordFound = False
        
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                wordFound = True
                currLength += 1
            else:
                if wordFound:
                    return currLength

        return currLength
            