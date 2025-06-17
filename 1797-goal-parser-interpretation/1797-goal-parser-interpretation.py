class Solution:
    def interpret(self, command: str) -> str:
        interpretation = ''
        goal = ['G', '()', '(al)']
        temp_str = ''
        for s in command:
            temp_str += s
            if temp_str in goal:
                if temp_str == 'G':
                    interpretation += 'G'
                elif temp_str == '()':
                    interpretation += 'o'
                elif temp_str == '(al)':
                    interpretation += 'al'
                temp_str = ''
        return interpretation