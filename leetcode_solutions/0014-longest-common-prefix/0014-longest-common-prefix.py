class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key= lambda x: (len(x), x))
        prefix = ''
        character_counter = 0
        string_counter = 0
        prefix_not_extended = False
        if len(strs) == 1:
            return strs[0]
        if strs[0] == strs[-1]:
            return strs[0]
        for i in strs[0]:
            if len(strs) == 2:
                if i == strs[1][character_counter]:
                        prefix += i
                        character_counter += 1
                else:
                    prefix_not_extended = True
                if prefix_not_extended == True:
                    break
            elif len(strs) > 2:
                for string in strs[1:]:
                    if i == string[character_counter]:
                        if string == strs[-1]:
                            prefix += i
                            #character_counter = 0
                            break
                        else:
                            continue
                    else:
                        prefix_not_extended = True
                        break
                if prefix_not_extended == True:
                    break
                elif character_counter == len(strs[0]):
                    break
                else:
                    character_counter += 1
                    continue
        if len(prefix) > 0:
            return prefix
        else:
            return ''
