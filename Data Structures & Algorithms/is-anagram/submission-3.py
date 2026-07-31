class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_dict = {}
        for char in s :
            count_dict[char] = 1 + count_dict.get(char, 0)
        for char in t:
            if char not in count_dict:
                return False
            count_dict[char] -= 1
            if count_dict[char] == 0:
                del count_dict[char]
        return len(count_dict) == 0
        
        