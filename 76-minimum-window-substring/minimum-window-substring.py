from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        have = 0
        window = {}
        need = Counter(t)
        needed = len(need)
        best_len = float("inf")
        best_left = 0
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0)+1
            if window[ch] == need[ch]:
                have+=1
            while have == needed:
                if (right-left+1) < best_len:
                    best_len = right-left+1
                    best_left = left
                left_ch = s[left]
                window[left_ch] -= 1
                if window[left_ch] < need[left_ch]:
                    have -= 1
                left+=1
        return "" if best_len == float("inf") else s[best_left:best_left+best_len]
                        

