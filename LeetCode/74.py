class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = set.union(*map(set,matrix))
        return (target in a)