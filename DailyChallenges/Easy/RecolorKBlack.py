#2379. Minimum Recolors to Get K Consecutive Black Blocks

def minimumRecolors(self, blocks, k):
        countB = 0
        maxcountB = 0
        for i, block in enumerate(blocks):
            if block == 'B':
                countB += 1
            if i >= k and blocks[i - k] == 'B':
                countB -= 1
            maxcountB = max(maxcountB, countB)
        return k - maxcountB