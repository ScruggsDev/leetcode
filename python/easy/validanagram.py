# Prompt

# Given two strings s and t,
# return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Prompt

# Solution


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for letter in t:
            if letter not in s:
                return False
            else:
                s = s.replace(letter, "", 1)

        return True
