# LeetCode 167 - Two Sum II: Input Array Is Sorted
# Difficulty: Medium
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def twoSum(self, numbers, target):
        p1 = 0
        p2 = len(numbers) - 1

        while p1 < p2:
            current_sum = numbers[p1] + numbers[p2]

            if current_sum == target:
                return [p1 + 1, p2 + 1]
            elif current_sum > target:
                p2 -= 1
            else:
                p1 += 1
