class WordDictionary:

    def __init__(self):
        self.root_trie = {}

    def addWord(self, word: str) -> None:
        current_level = self.root_trie
        for char in word:
            if char not in current_level:
                current_level[char] = {}
            current_level = current_level[char]
        current_level['#'] = True

    def search(self, word: str) -> bool:
        def dfs(current_level, idx):
            if idx == len(word):
                return '#' in current_level

            char = word[idx]
            if char != '.':
                if char not in current_level:
                    return False
                else:
                    return dfs(current_level[char], idx + 1)
            else:
                for child_key in current_level:
                    if child_key == '#':
                        continue
                    if dfs(current_level[child_key], idx + 1):
                        return True
                return False
        
        return dfs(self.root_trie, 0)

