#3394. Check if Grid can be Cut into Sections
from typing import List
class Solution:
    def countLineIntersections(self, coordinates: List[tuple]) -> bool:
        lines = 0
        overlap = 0
        for coord in coordinates:
            if coord[1] == 0:
                overlap -= 1
            else:
                overlap += 1
            if overlap == 0:
                lines += 1
        return lines >= 3
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        y_coordinates = []
        x_coordinates = []
        for rectangle in rectangles:
            y_coordinates.append((rectangle[1], 1))
            y_coordinates.append((rectangle[3], 0))
            x_coordinates.append((rectangle[0], 1))
            x_coordinates.append((rectangle[2], 0))
        y_coordinates.sort()
        x_coordinates.sort()
        return self.countLineIntersections(y_coordinates) or self.countLineIntersections(x_coordinates)