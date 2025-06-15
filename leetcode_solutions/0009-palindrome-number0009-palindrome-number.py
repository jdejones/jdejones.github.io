class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstring = str(x)
        if len(xstring) == 1:
            return True
        if '-' in xstring:
            return False
        if len(xstring) == 3:
            if xstring[0] == xstring[-1]:
                return True
            else:
                 return False
        if len(xstring) % 2 == 0:
            even = True
        else:
            even = False
        if even == True:
            h1 = xstring[:round(len(xstring)/2)]
            h2 = xstring[round(len(xstring)/2):]
        elif even == False:
            h1 = xstring[:round((len(xstring)/2)-1)]
            h2 = xstring[round(len(xstring)/2)+1:]
        if h1 == h2[::-1]:
            return True
        else:
            return False
