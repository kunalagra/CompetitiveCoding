class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r=len(grid)
        c=len(grid[0])
        l = [x for a in grid for x in a]
        k= k%(r*c)
        l = l[-k:]+l
        i=0
        for x in range(r):
            for y in range(c):
                grid[x][y] = l[i]
                i+=1
        return(grid)

        '''
        Better Approach by @ythoncode
        k=k%(len(grid)*len(grid[0]))
        for i in range(k):
            j = -1
            for i in grid:
                i.insert(0,grid[j][-1])
                j += 1
            for i in grid:
                i.pop()
        return grid
        '''