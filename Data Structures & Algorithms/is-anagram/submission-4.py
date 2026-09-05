class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word_map = {}
        for char in s:
            if char not in word_map:
                word_map[char] = 0
            word_map[char] += 1
        for char in t:
            if char not in word_map:
                return False
            word_map[char] -= 1
            if word_map[char] == 0:
                del word_map[char]
        return not word_map
                