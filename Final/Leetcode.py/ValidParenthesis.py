class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                # Check if the stack is not empty and the top of the stack matches the expected opening bracket
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()  # If it matches, pop the top of the stack
                else:
                    return False  # If it doesn't match, return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # After processing all characters, check if the stack is empty
        # not stack = True means stack is empty
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))      # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]"))      # Output: False
print(solution.isValid("({[]})"))  # Output: True