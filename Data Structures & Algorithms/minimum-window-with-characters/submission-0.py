class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l = 0
        match_count = 0
        min_len = float('inf')
        min_window = (-1, -1)
        s_freq = {}
        t_freq = Counter(t)

        for i in range(len(s)):
            if s[i] in t_freq:
                if s[i] not in s_freq:
                    s_freq[s[i]] = 0
                s_freq[s[i]] += 1
                if s_freq[s[i]] == t_freq[s[i]]:
                    match_count += 1

            while match_count == len(t_freq):
                current_len = i - l + 1
                if current_len < min_len:
                    min_len = current_len
                    min_window = (l, i)

                if s[l] in t_freq:
                    s_freq[s[l]] -= 1
                    if t_freq[s[l]] > s_freq[s[l]]:
                        match_count -= 1 
                l += 1

        if min_window == (-1, -1):
            return ""
            
        return s[min_window[0]:min_window[1] + 1]