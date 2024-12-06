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


'''
must be #printed in a very specific order
X|Y means x must be #printed before y
'''

from collections import defaultdict

class Solution:

    def __str__(self):
        pass

    def __init__(self):
        #print("Day 5 here I come")
        # self.x_rank = 999999
        self.collect = []
        self.updates = []
        # self.y_rank = 1
        # self.x_dict = defaultdict(int)
        # self.y_dict = defaultdict(int)
       

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

    # def attempt_one(self, line):
        
    #     x, y = line.split("|")

    #     x_rank, y_rank = self.x_dict.get(x, -1), self.y_dict.get(y, -1)
        
    #     if x_rank == -1 or y_rank == -1:
    #         self.x_dict[x], self.y_dict[y] = self.x_rank, self.y_rank
    #     elif x_rank > y_rank:
    #         return
    #     else:
    #         #print(x, y)
    #         self.x_dict[x], self.y_dict[y] = self.y_dict[y], self.x_dict[x]
    #     self.x_rank -= 1
    #     self.y_rank += 1


    def helper_one(self, line):
        self.collect.append(line.split("|"))
    
    def check_rules(self, l):
        temp = l.split(",")
        updates = {update: rank for rank, update in enumerate(temp) } # Damn im really good


        for X, Y in self.collect:
            if X in updates and Y in updates:
                x_rank, y_rank = updates[X], updates[Y]
                
                if x_rank > y_rank:
                    return -1
        
        #print(updates)
        return int(temp[len(temp)//2])

    
    def part_one_solver(self, filename):
        is_update = False
        for line in self.line_generator(filename):
            if line == "":
                is_update = True
            elif is_update:
                self.updates.append(line)
            else:
                self.helper_one(line)

        ans, res = 0, 0
        for l in self.updates:
            
            res = self.check_rules(l)
            ##print(res)
            ans += res if res >= 0 else 0

        #print(ans)
        return ans
        

def main(*args, **kwargs):
    solution = Solution()
    filename = "../temp.txt"
    print(solution.part_one_solver(filename))
   
    
if __name__ == "__main__":
    main()

