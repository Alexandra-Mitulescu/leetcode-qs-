class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(len(nums)):
            needed_num = target - nums[i]
            print(f"Needed number for reaching target with {nums[i]}: ",needed_num)
            if needed_num in hash_map:
                return(i, hash_map[needed_num])
            hash_map[nums[i]] = i



solution = Solution()
result = solution.twoSum([2,7,8],9)
print(result)