class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        result = ""
        for char in s:
            if char.isalnum():
                result += char
        reversed_text = result[::-1]
        if reversed_text == result:
            return True 
        else: 
            return False 
