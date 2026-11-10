# LeetCode 80 - Remove Duplicates from Sorted Array II
# Difficulty: Medium
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        write = 0

        for read in range(len(nums)):
            if write < 2 or nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write
