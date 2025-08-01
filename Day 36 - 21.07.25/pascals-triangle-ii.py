# DP - Easy

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            for j in range(len(row) - 1, 0, -1):
                row[j] += row[j - 1]
            row.append(1)
        return row
