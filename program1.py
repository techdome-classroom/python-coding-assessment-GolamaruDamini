class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            # Boundary and condition checks
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W' or visited[r][c]:
                return
            # Mark cell as visited
            visited[r][c] = True
            # Explore the four possible directions (up, down, left, right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        island_count = 0

        # Traverse each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and not visited[r][c]:
                    # Found an unvisited land cell; initiate DFS
                    dfs(r, c)
                    island_count += 1

        return island_count

