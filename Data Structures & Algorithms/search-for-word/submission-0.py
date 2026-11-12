class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def find_word(r, c, char_idx, added_chars):
            if char_idx == len(word):
                return True
            if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS):
                return False
            if (r, c) in added_chars:
                return False
            if board[r][c] != word[char_idx]:
                return False

            added_chars.add((r, c))

            found = (
                find_word(r + 1, c, char_idx + 1, added_chars) or
                find_word(r - 1, c, char_idx + 1, added_chars) or
                find_word(r, c + 1, char_idx + 1, added_chars) or
                find_word(r, c - 1, char_idx + 1, added_chars)
            )

            added_chars.remove((r, c))
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if find_word(r, c, 0, set()):
                    return True
        
        return False