from typing import List
def twoSum(self, nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) -1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
