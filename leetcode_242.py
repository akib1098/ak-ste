class Solution:
    def validAnagram(self, s, t):
        x = set(s)
        y = set(t)
        if x == x.intersection(y):
            return True
        else:
            return False

s = "anagram"
t = "nagaram"
print(Solution().validAnagram(s, t))