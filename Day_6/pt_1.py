# Copyright 2024 Yathartha Regmi
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Solution:

    def __str__(self):
        pass

    def __init__(self):
        #print("Day 6 here I come")
        self.grid = []
        self.face = ""

        self.direction = {
            "^": (-1, 0), 
            "v": (1, 0), 
            "<": (0, -1), 
            ">": (0, 1)
        }

        self.rotation = {
            ">": "v",
            "v": "<", 
            "^": ">", 
            "<": "^"
        }

        self.R, self.C = 130, 130
        self.X, self.Y = 0, 0 

    def create_grid(self, line):
        self.grid.append([ch for ch in line])

    def find_start(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])): 
                if self.grid[r][c] in self.direction:
                    self.X, self.Y = r, c
                    self.face = self.grid[r][c]

        # self.R, self.C = len(self.grid), len(self.grid[0])

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
    

    def within_bounds(self, X, Y):
        return (0 <= X < self.R) and (0 <= Y < self.C)
        

    def helper(self):
        steps = 0
        while self.within_bounds(self.X, self.Y):
            x, y = self.direction[self.face]
            nx, ny = self.X + x, self.Y + y

            if not self.within_bounds(nx, ny):
                return steps
            

            if self.grid[nx][ny] == "#":
                self.face = self.rotation[self.face]
            else:
                self.grid[nx][ny] = "X"
                steps += 1
                self.X, self.Y = nx, ny
            
        return steps

    def part_one_solver(self, filename):

        for line in self.line_generator(filename):
            self.create_grid(line)
        self.find_start() # Find starting point
        ans = self.helper()
        x_count = 0
        for l in self.grid:
            for c in l:
                if c == "X":
                    x_count += 1
    
        #print(x_count)

        return x_count


        

def main(*args, **kwargs):
    solution = Solution()
    filename = "../temp.txt"
    print(solution.part_one_solver(filename))

   
    
if __name__ == "__main__":
    main()

