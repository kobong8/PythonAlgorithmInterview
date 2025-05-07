from util import timefn


# %%
class Solution:
    @timefn
    def array_partition_01(self, nums: list[int]) -> int:
        print("array_partition_01")
        nums.sort()
        reps = len(nums) / 2
        sum = 0

        for idx in range(reps):
            min_value = min(nums[2 * idx - 1], nums[2 * idx])
            sum = sum + min_value

        return sum


# %%
if __name__ == "__main__":
    nums: list[int] = [1, 4, 3, 2]
    soln = Solution()
    print(soln.array_partition_01(nums))
