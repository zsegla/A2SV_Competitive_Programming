# https://leetcode.com/problems/fizz-buzz/



class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for num in range(1,n+1):
            temp = ""
            if (num % 3 == 0):
                 temp += "Fizz"
            if (num % 5 == 0):
                 temp += "Buzz"
            if (num % 5 != 0) and (num % 3 != 0):
                 temp += f"{num}"
            result.append(temp)
        return result
            
        
