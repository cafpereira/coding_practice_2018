class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        grid = Cell(A + 1, B + 1, float('inf'))
        start, end = Cell(C, D, 0), Cell(E, F, 0)
        return self.bfs(start, end, grid)

    def bfs(self, start, end, grid):
        visited = [[False] * grid.x for l in range(grid.y)]

        queue = [start]
        visited[start.y][start.x] = True

        while queue:
            cur = queue.pop(0)
            if cur == end:
                return cur.dist

            moves = [[2, 1], [-2, 1], [1, 2], [1, -2], [2, -1], [-2, -1], [-1, 2], [-1, -2]]

            for m in moves:
                next = Cell(cur.x + m[0], cur.y + m[1], cur.dist + 1)
                if self.valid(next, grid) and not visited[next.y][next.x]:
                    visited[next.y][next.x] = True
                    queue.append(next)

        # Path not found
        return -1

    def valid(self, cell, grid):
        return 1 <= cell.x < grid.x and 1 <= cell.y < grid.y


class Cell:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


s = Solution()

print(s.knight(8,8,1,1,8,8)) # Expected: 6
# print(s.knight(4, 4, 1, 1, 4, 4))  # Expected: 3
