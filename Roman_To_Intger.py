class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0

        for char in s:
            if char not in roman_map:
                return False
            else:
                curr_value = roman_map[char]
                if curr_value > prev_value:
                    total -= 2 * prev_value
        
                total += curr_value
                prev_value = curr_value

        
        return total   
