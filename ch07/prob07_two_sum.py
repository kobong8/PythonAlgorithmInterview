# %%
from typing import List

# %%
class Solution:
    # soln kobong
    def twoSum_kb(self, nums: list[int], target: int) -> list[int]:
        ret_sum = 0
        target_i = 0
        for i in range(len(nums)):
            ret_sum += nums[i]

            if ret_sum == target:
                target_i = i
                break

        return [0, target_i]
    
    # soln Brute-Force
    def twoSum_bf(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    # soln search using in
    def twoSum_in(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
    
    # soln first value
    def twoSum_fv(self, nums: List[int], target: int) -> List[int]:
        nums_map: dict = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
    
    # soln for-loop
    def twoSum_fl(self, nums: List[int], target: int) -> List[int]:
        nums_map: dict = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
    
    # soln two points
    def twoSum_tp(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]


# %%
if __name__ == "__main__":
    nums: list[int] = [2, 7, 11, 15]
    target: int = 17
    
    soln = Solution()
    ret = soln.twoSum_kb(nums, target)
    print(ret)
    
    ret = soln.twoSum_bf(nums, target)
    print(ret)
    
    ret = soln.twoSum_in(nums, target)
    print(ret)

    ret = soln.twoSum_fv(nums, target)
    print(ret)

    ret = soln.twoSum_fl(nums, target)
    print(ret)

    ret = soln.twoSum_tp(nums, target)
    print(ret)


