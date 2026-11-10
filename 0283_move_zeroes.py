# LeetCode 283 - Move Zeroes
# Difficulty: Easy
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def moveZeroes(self, nums):
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
