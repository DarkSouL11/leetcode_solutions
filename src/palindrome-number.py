'''
Author: Sundeep Babbur

Problem Link: https://leetcode.com/problems/palindrome-number.py/
'''

class Solution(object):
  def __init__(self):
    self.min = -1 * (2 ** 31)
    self.max = (2 ** 31) - 1

  def reverse(self, x: 'int') -> 'int':
    if x == 0:
      return x

    rev_num = 0
    num = abs(x)
    while num > 0:
      rev_num = rev_num * 10 + (num % 10)
      num //= 10
    if (rev_num < self.min) or (rev_num > self.max):
      return 0
    return rev_num * (x // abs(x))

  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False

    return x == self.reverse(x)


def main():
  solution = Solution()
  num = 10
  print(solution.isPalindrome(num))


if __name__ == "__main__":
  main()