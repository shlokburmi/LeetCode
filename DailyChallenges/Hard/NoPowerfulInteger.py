#2999. Count the Number of Powerful Integers
from functools import lru_cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # Cache the results of the recursive calls to avoid redundant calculations
        @lru_cache(None)
        def dfs(position: int, is_limited: int):
            # If the generated number is shorter than the searched term, there are no powerful ints here
            if len(temp_string) < num_length:
                return 0
            # If we reached the end of the temporary number being constructed
            if len(temp_string) - position == num_length:
                # If we are limited by the "finish" number, compare substrings
                return int(s <= temp_string[position:]) if is_limited else 1
            # Determine the digit limit; if we're not at the limit, we can go up to 9
            upper_limit = min(int(temp_string[position]) if is_limited else 9, limit)
            # Initialize counter for powerful integers
            counter = 0
            # Recursively calculate counts for all digits up to the upper limit
            for i in range(upper_limit + 1):
                counter += dfs(position + 1, is_limited and i == int(temp_string[position]))
            return counter

        # Get the length of the search term to know when we've built a comparable number
        num_length = len(s)
        # Convert start number to a string and subtract 1 to handle inclusive counting
        temp_string = str(start - 1)
        # Compute number of powerful integers starting from 'start-1' to set a base
        count_start = dfs(0, True)
        # Clear the cache to avoid interference with the next computation
        dfs.cache_clear()
        # Convert finish number to a string; this is the actual upper bound
        temp_string = str(finish)
        # Compute number of powerful integers up to 'finish'
        count_finish = dfs(0, True)
        # Subtract the two counts to get the number of powerful integers in the range
        return count_finish - count_start