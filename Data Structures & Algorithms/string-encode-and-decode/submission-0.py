class Solution:
    def encode(self, strs: List[str]) -> str:
        strings = []
        for word in strs:
            strings.append(f'{len(word)}#{word}')
        return ''.join(strings)

    def decode(self, s: str) -> List[str]:
        strings = []
        p = 0

        num = ''
        while p < len(s):
            if s[p] != '#':
                num += s[p]
                p += 1
            else:
                num = int(num)
                strings.append(s[p + 1:p + 1 + num])
                p = p + 1 + num
                num = ''

        return strings