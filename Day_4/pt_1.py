
# from collections import deque 

class Solution:

    def __str__(self):
        result = ""
        for row in self.graph:
            result += str(row)
        
        return result

    def __init__(self):
        print("Day 3 here I come")
        self.graph = []
        self.R, self.C = 10, 10
        up, down = (-1, 0), (1, 0)
        left, right = (0, -1), (0, 1)
        diag_left_up, diag_right_up = (-1, -1), (-1, 1)
        diag_left_down, diag_right_down = (1, -1), (1, 1)
        self.directions = [up, down, left, right, diag_left_up, diag_right_up, diag_left_down, diag_right_down]
        self.cache = {} # To store the path that has been visited already
        # self.pattern = {"X": 1, "M": 2, "A": 3, "S": 4}
        # self.milo = {0: "X", 1: "M", 2: "A", 3: "S"}
        self.milo = ["X", "M", "A", "S"]

    def line_generator(self, filename):
        """
        Generator that yields lines from a file one at a time.

        Args:
            filename (str): Path to the input file.

        Yields:
            str: Next line from the file.
        """
        try:
            with open(filename, "r") as file:
                for line in file:
                    yield line.strip("\n")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return
    
    # def bfs(self, row, col, visited, count):

    #     queue = deque()
    #     queue.append((row, col))
    #     result = 0 
    #     visited.add((row, col))

    #     while queue:
    #         r, c = queue.popleft()

    #         for x, y in self.directions:
    #             nx, ny = r + x, y + c

    #             if 0 <= nx < self.R and 0 <= ny < self.C:
    #                 result += 


    def dfs(self, row, col, visited, count, path): # dfs might be better 
        if row < 0 or row >= self.R or col < 0 or col >= self.C:
            return 0
        
        if self.graph[row][col] == "#":
            return 0 

        if count < len(self.milo) and self.milo[count] != self.graph[row][col]:
            return 0

        if count == len(self.milo) - 1:
            print(f"Path Found: {path}")
            return 1

        result = 0 
        # visited.add((row, col))
        cur = self.graph[row][col]
        self.graph[row][col] = "#"
        for i, j in self.directions:
            nx, ny = row + i, col + j
            # print(self.graph[nx][ny])
            if 0 <= nx < self.R and 0 <= ny < self.C:
                result += self.dfs(row+i, col+j, visited, count+1, path + self.graph[nx][ny])
            
        # visited.remove((row, col))
        self.graph[row][col] = cur
        return result


    def helper(self):
        ans = 0
        for i in range(self.R):
            for j in range(self.C):
                if self.graph[i][j] == 'X':
                    visited = set()
                    ans += self.dfs(i, j, visited, 0, "X")
        
        return ans

    def graph_generator(self, line):
        char_list = [ch for ch in line]
        self.graph.append(char_list)

    
    def part_one_solver(self, filename):
        
        for line in self.line_generator(filename):
            self.graph_generator(line)
        
        print(self.graph)
        result = 0 
        result = self.helper()
        
        return result

def main(*args, **kwargs):
    solution = Solution()
    filename = "../data.txt"
    print(solution.part_one_solver(filename))


if __name__ == "__main__":
    main()