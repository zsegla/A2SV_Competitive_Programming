# https://leetcode.com/problems/string-compression/



class Solution:
    def compress(self, chars: List[str]) -> int:
        chars += " "
        char_start = 0
        result_len = 0
        
        for i, c in enumerate(chars):
            if c != chars[char_start]:
                chars[result_len] = chars[char_start]
                result_len += 1

                seq_len = i - char_start
                if seq_len > 1:
                    digits = list(str(seq_len))
                    digits_len = len(digits)
                    chars[result_len:result_len + digits_len] = digits
                    result_len += digits_len
                char_start = i
        return result_len
