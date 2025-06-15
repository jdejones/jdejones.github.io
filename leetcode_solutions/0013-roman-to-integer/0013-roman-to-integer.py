class Solution:
    def romanToInt(self, s: str) -> int:
        lst = [item for item in s]
        val_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val_list = [val_dict[item] for item in lst]
        num = 0
        skip = False
        num_skips =0
        for item in lst:
            if skip == True:
                num_skips -= 1
                if num_skips == 0:
                    skip =False
                    continue
                continue
            if lst.index(item) != (len(lst) -1):
                if val_list[lst.index(item)] < val_list[lst.index(item) + 1]:
                    num += (val_list[lst.index(item) + 1] - val_list[lst.index(item)])
                    skip = True
                    num_skips += 1
                    continue
                if val_list[lst.index(item)] == val_list[lst.index(item) + 1]:
                    if (lst.index(item) + 2) != len(lst):
                        if val_list[lst.index(item)] == val_list[lst.index(item) + 2]:
                            num_skips += 2
                            skip = True
                            num += (3*val_dict[item])
                            continue
                        else:
                            num_skips += 1
                            skip = True
                            num += (2*val_dict[item])
                            continue
                    else:
                        num_skips += 1
                        skip = True
                        num += (2*val_dict[item])
                        continue
            num += val_dict[item]
        return num
