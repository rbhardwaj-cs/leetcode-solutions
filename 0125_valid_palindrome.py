
# LeetCode 125 - Valid Palindrome
# Difficulty: Easy
# Approach: String Cleaning + Reversal
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        result = ""

        for char in s:
            if char.isalnum():
                result += char

        reversed_text = result[::-1]

        return reversed_text == result
