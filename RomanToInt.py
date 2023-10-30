class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol = dict()
        symbol["I"] = 1
        symbol["V"] = 5
        symbol["X"] = 10
        symbol["L"] = 50
        symbol["C"] = 100
        symbol["D"] = 500
        symbol["M"] = 1000

        result = 0
        for i in range(len(s)):
            result += symbol[s[i]]
            if i > 0 and symbol[s[i-1]] < symbol[s[i]]:
                result -= symbol[s[i-1]]*2
            
        return result