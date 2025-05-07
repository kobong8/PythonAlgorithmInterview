from util import timefn


# %%
class Solution:
    @timefn
    def array_partition_01(self, nums: list[int]) -> int:
        print("array_partition_01")
        nums.sort()
        reps = int(len(nums) / 2)
        sum = 0

        for idx in range(reps):
            min_value = min(nums[2 * idx], nums[2 * idx + 1])
            sum = sum + min_value

        return sum

    @timefn
    def array_partition_02(self, nums: list[int]) -> int:
        print("array_partition_02")
        nums.sort()
        reps = int(len(nums) / 2)
        sum = 0

        for idx in range(reps):
            sum = sum + nums[2 * idx]

        return sum


# %%
if __name__ == "__main__":
    nums: list[int] = [1, 4, 3, 2]
    soln = Solution()
    print(soln.array_partition_01(nums))
    print()
    print(soln.array_partition_02(nums))
    print()
