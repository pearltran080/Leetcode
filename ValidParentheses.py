class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  # stores the order of parentheses that need to be closed
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            #   if there are no more parentheses to close but there are still chars in the string
            #   or if the char is not the same as the latest opened parenthesis
            elif len(stack) == 0 or stack.pop() != i:
                return False

        # if all opened parentheses have been closed
        return len(stack) == 0