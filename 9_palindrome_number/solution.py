# x = normal number taken from arg
# x_rev = reverse x
# if x == rev_x return true, else false

# RUNTIME: 63ms (regarding leetcode)
class Solution_0:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        rev_x = [v for v in str(x)][::-1]
        rev_x = ''.join(rev_x)

        return True if x == rev_x else False

# RUNTIME: 59ms (regarding leetcode)
class Solution_1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

class Solution_2:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        rev_x = str(x)[::-1]

        return True if x == rev_x else False