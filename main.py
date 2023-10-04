from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Dictionary to store the indices of numbers

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_indices:
                return [num_indices[complement], i]

            num_indices[num] = i