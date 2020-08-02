

class Solution(object):
    def two_sum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """
        t_dict = {}
        for i, x in enumerate(nums):
            if(x in t_dict):
                print([t_dict[x], i])
                return([t_dict[x], i])
            t_dict[target - x] = i

nums = [1,2,5,4]
target = 5

s = Solution()

assert(s.two_sum(nums, target) == [0,3])

