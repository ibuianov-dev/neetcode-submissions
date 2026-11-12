class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        current_trie = self.trie
        for char in word:
            if char not in current_trie:
                current_trie[char] = {}
            current_trie = current_trie[char]
        current_trie['END'] = True

    def search(self, word: str) -> bool:
        current_trie = self.trie

        for char in word:
            if char not in current_trie:
                return False
            current_trie = current_trie[char]
        
        return 'END' in current_trie

    def startsWith(self, prefix: str) -> bool:
        current_trie = self.trie

        for char in prefix:
            if char not in current_trie:
                return False
            current_trie = current_trie[char]
        
        return True