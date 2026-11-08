class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            key = self.wordKey(word)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        
        return list(anagrams.values())
    
    def wordKey(self, word: str):
        key = [0] * 26

        for char in word:
            char_index = ord(char) - ord('a')
            key[char_index] += 1

        return tuple(key)
