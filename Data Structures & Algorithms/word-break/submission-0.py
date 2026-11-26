class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        seen_strs = set()

        def dfs(str_val):
            if str_val in wordDict:
                return True
            if str_val in seen_strs:
                return False
            
            can_break = False

            for word in wordDict:
                if len(word) >= len(str_val):
                    continue
                if str_val.startswith(word):
                    if dfs(str_val[len(word):len(str_val)]):
                        can_break = True
            
            seen_strs.add(str_val) 
            return can_break
        
        return dfs(s)
            