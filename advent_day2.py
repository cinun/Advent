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
    def __init__(self):
        print("Day 2 on the books")
        self.dampner_list = []


    def calculator(self, values):
        order = int(values[1]) - int(values[0]) # Might be +ve or -ve based on the order
        stack = []
        for v in values:
            v = int(v)
            if not stack:
                stack.append(v)
            else: # Gave up on comments aftter this
                res = stack[-1] - v
                if (abs(res) >= 1 and abs(res) <= 3):
                    if order > 0:
                        if v < stack[-1]:
                           return 0
                    elif order < 0:
                        if v > stack[-1]:
                            return 0
                    stack.append(v)
                else:
                    return 0
        return 1


    def helper(self, line):
        values = line.strip("\n").split(" ")
        result = self.calculator(values)

        return result
    
    def helper_two(self, line): # If you need comments you need to get good
        values = line.strip("\n").split(" ")
        for i in range(len(values)):
            new_list = values[:i] + values[i+1:]
            if self.calculator(new_list) == 1:
                return 1
        return 0 

    
    def line_generator(self, filename):
        with open(filename, "r") as fr:
            while True:
                line = fr.readline() # Efficiency pt. 2
                if not line:  # End of file is reached
                    break
                yield line  # Yield the line read from the file
    
    def solver(self, filename):
        self.answer = 0
        for line in self.line_generator(filename):
            result = self.helper(line)
            if result != 1:
                self.dampner_list.append(line)
            self.answer += result
 
        return self.answer

    def solver_two(self):
        self.answer = 0
        print(len(self.dampner_list))
        for line in self.dampner_list:
            result = self.helper_two(line)
            self.answer += result
 
        return self.answer

    

def main():
    solve = Solution()
    ans = solve.solver("data.txt")
    ans2 = solve.solver_two() + ans

    
    print(f"Part 2: {ans2}")


if __name__ == "__main__":
    main()



