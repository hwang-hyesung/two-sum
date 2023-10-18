from typing import List
 def even_list(int_list: List[int]) -> List[int]:
    even_nums = []
    for num in int_list:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

