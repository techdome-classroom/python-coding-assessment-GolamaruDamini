class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:  # Check for an empty grid
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]  # Visited cells grid

        # Directions: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            # Boundary and condition checks
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W' or visited[r][c]:
                return
            # Mark cell as visited
            visited[r][c] = True
            # Explore all 4 possible directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        island_count = 0
        # Traverse each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and not visited[r][c]:  # Unvisited land cell
                    dfs(r, c)  # Initiate DFS from this cell
                    island_count += 1  # Increment island count

        return island_count
