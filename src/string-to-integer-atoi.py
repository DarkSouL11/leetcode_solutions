'''
Author: Sundeep Babbur

Problem Link: https://leetcode.com/problems/string-to-integer-atoi.py/

Solution: Used regex
'''

import re


class Solution(object):
  def __init__(self):
    self.min = -1 * (2 ** 31)
    self.max = (2 ** 31) - 1

  def myAtoi(self, str: str) -> int:
    match = re.match('^\s*([-+]?[0-9]+)', str)
    if match:
      z = match.groups()
      if z:
        num = min(max(int(z[0]), self.min), self.max)
        return num
    return 0


def main():
  solution = Solution()
  print(solution.myAtoi(' +42'))


if __name__ == "__main__":
  main()