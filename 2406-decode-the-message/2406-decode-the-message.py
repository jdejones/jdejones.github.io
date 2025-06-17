import string
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        chars = ''
        for c in key:
            if (c not in chars) and (c != ' '):
                chars += c
        decoded = ''
        for c in message:
            if c == ' ':
                decoded += ' '
                continue
            decoded += string.ascii_lowercase[chars.index(c)]
        return decoded