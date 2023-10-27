class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if (digits[i] + carry) > 9:
                carry = 1
                digits[i] = 0
            else:
                digits[i] = digits[i] + carry
                return digits

        digits.insert(0, 1)
        return digits