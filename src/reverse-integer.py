'''
Author: Sundeep Babbur

Problem Link: https://leetcode.com/problems/reverse-integer.py/
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


def main():
  solution = Solution()
  n = -123120
  print(solution.reverse(n))


if __name__ == "__main__":
  main()