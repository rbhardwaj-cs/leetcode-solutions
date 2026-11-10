class Solution(object):
    def removeDuplicates(self, nums):
        write = 0

        for read in range(len(nums)):
            if read == 0 or nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write
