class Solution:

    def __str__(self):
        result = ""
        for row in self.graph:
            result += str(row)
        
        return result

    def __init__(self):
        print("Day 4 here I come")
        self.graph = []
        self.R, self.C = 10, 10
        up, down = (-1, 0), (1, 0)
        left, right = (0, -1), (0, 1)
        diag_left_up, diag_right_up = (-1, -1), (-1, 1)
        diag_left_down, diag_right_down = (1, -1), (1, 1)
        self.directions = [up, down, left, right, diag_left_up, diag_right_up, diag_left_down, diag_right_down]
        self.dir_two = [diag_left_down, diag_right_down, diag_left_up, diag_right_up]

        self.temp_graph = [[False for i in range(self.C)] for _ in range(self.R)]
        self.milo = ["X", "M", "A", "S"]
        self.milo_two = ["M", "A", "S"]

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


    def path_finder_two(self, row, col, direction):
        intersection = False
        path = []
        for i in range(1, 3):
            nx, ny = row + direction[0] * i, col + direction[1] * i # Cuz im smart like that
        
            if (nx < 0 or nx >= self.R) or (ny < 0 or ny >= self.C):
                return False

            if self.graph[nx][ny] != self.milo[i]:
                return False
            path.append((nx, ny))
        

        for r, c in path:
            if self.temp_graph[r][c] == True:
                intersection = True
            self.temp_graph[r][c] = True
 
        return intersection

    def path_finder(self, row, col, direction):

        for i in range(1, 4):
            nx, ny = row + direction[0] * i, col + direction[1] * i # Cuz im smart like that
        
            if (nx < 0 or nx >= self.R) or (ny < 0 or ny >= self.C):
                return False

            if self.graph[nx][ny] != self.milo[i]:
                return False
        
        return True
    
    def helper(self):
        ans = 0
        for i in range(self.R):
            for j in range(self.C):
                if self.graph[i][j] == "X":
                    for d in self.directions:
                        if self.path_finder(i, j, d):
                            ans += 1
        return ans
    
    def helper_two(self):
        ans = 0
        for i in range(self.R):
            for j in range(self.C):
                if self.graph[i][j] == "M":
                    for d in self.dir_two:
                        if self.path_finder_two(i, j, d):
                            ans += 1

        return ans

    def graph_generator(self, line):
        char_list = [ch for ch in line]
        self.graph.append(char_list)

    
    def part_one_solver(self, filename):
        for line in self.line_generator(filename):
            line = line.strip()
            self.graph_generator(line)

        # print(self.graph)
        for l in self.temp_graph:
            print(l)
        return self.helper()

    def part_two_solver(self, filename):
        self.graph = []
        for line in self.line_generator(filename):
            line = line.strip()
            self.graph_generator(line)

        # print(self.graph)
        
        result = self.helper_two()
        for l in self.temp_graph:
            print(l)
        return result

def main(*args, **kwargs):
    solution = Solution()
    filename = "../data.txt"
    print(solution.part_one_solver(filename))
    print(solution.part_two_solver(filename))
    


if __name__ == "__main__":
    main()

