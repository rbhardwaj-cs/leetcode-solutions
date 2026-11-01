# LeetCode 217 - Contains Duplicate
# Difficulty: Easy
# Pattern: Hash Set
# Time Complexity: O(n) average
# Space Complexity: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False
