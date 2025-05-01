from util import timefn


# %%
class Solution:
    @timefn
    def zero_sum_triplets_01(self, nums: list[int]) -> list[int]:
        # brute force
        nums.sort()

        zero_list: list[int] = []
        soln_list: list[int] = []

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        zero_list = [nums[i], nums[j], nums[k]]
                        if zero_list not in soln_list:
                            soln_list.append([nums[i], nums[j], nums[k]])

        return soln_list

    @timefn
    def zero_sum_triplets_02(self, nums: list[int]):
        # brute force
        nums.sort()
        print("zero_sum_triplets_02")

        zero_list: list[int] = []
        soln_list: list[int] = []

        return 0


# %%
if __name__ == "__main__":
    nums: list[int] = [-1, 0, 1, 2, -1, 4]

    soln = Solution()
    print(soln.zero_sum_triplets_01(nums))
    print(soln.zero_sum_triplets_02(nums))
