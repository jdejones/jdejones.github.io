class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = ['(', '{', '[']
        close_bracket = [')', '}', ']']
        bracket_loc = [i for i in s if i in (open_bracket) or (close_bracket)]
        stack = []
        if len(s) <= 1:
            return False
        for i in bracket_loc:
            if i in open_bracket:
                stack.append(i)
            elif i in close_bracket:
                if len(stack) == 0:
                    return False
                if close_bracket.index(i) == open_bracket.index(stack[-1]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return 'true'
        else:
            return False