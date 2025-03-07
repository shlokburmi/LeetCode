#2965. Find Missing and Repeated Values
def findMissingAndRepeatedValues(self, grid):
        count=[1]+[0]*len(grid)**2
        for row in grid:
            for num in row:
                count[num]+=1
        return [count.index(2),count.index(0)]

# find repeated and missing values in a grid defined in range of [1,n**2] where n is the length of the grid