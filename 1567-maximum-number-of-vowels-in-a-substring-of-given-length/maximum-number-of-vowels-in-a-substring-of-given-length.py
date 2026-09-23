class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = sum(1 for ch in s[:k] if ch in vowels)
        max_count = count

        for right in range(k, len(s)):
            if s[right] in vowels:
                count += 1
            if s[right-k] in vowels:
                count -= 1
            max_count = max(max_count, count)

        return max_count