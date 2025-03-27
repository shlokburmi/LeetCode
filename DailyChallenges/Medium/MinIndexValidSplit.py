from typing import List
from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        most_common_element, count_most_common = Counter(nums).most_common(1)[0]
        current_count = 0
        for index, value in enumerate(nums):
            if value == most_common_element:
                current_count += 1
            current_index = index + 1
            if (current_count * 2 > current_index) and \
               ((count_most_common - current_count) * 2 > (len(nums) - current_index)):
                return index
        return -1