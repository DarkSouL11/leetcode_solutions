'''
Author: Sundeep Babbur

Problem Link: https://leetcode.com/problems/zigzag-conversion/

Solution: Key to solving this problem is a every gap between two characters
  that appear in a row while going down is `numRows * 2 - 2`. Same rule can be
  applied for the characters which appear while going up but alter the numRows
  accordingly i.e numRows is given by (numRows - currRow).
'''

class Solution(object):
  def convert(self, s: 'str', numRows: 'int') -> 'str':
    size = len(s)
    if size <= numRows or numRows == 1:
      return s

    currRow = 0
    res = ''
    while currRow < numRows:
      currIndex = currRow
      while currIndex < size:
        res += s[currIndex]
        if (currRow > 0) and (currRow < numRows - 1):
          index = currIndex + (numRows - currRow) * 2 - 2
          if index < size:
            res += s[index]

        currIndex += (numRows * 2 - 2)

      currRow += 1
    return res


def main():
  solution = Solution()
  s = 'ABABABAB'
  numRows = 2
  print(solution.convert(s, numRows))


if __name__ == "__main__":
  main()