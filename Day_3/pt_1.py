import re

class Solution:

    def __init__(self):
        print("Day 3 here I come")
    
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
                    yield line
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return

    def helper(self, line):
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern=pattern, string=line)

        total_product = 0

        for x, y in matches:
            total_product += int(x) * int(y)
        
        return total_product


    def part_one_solver(self, filename):
        result = 0
        for line in self.line_generator(filename):
            result += self.helper(line)
        
        return result
        



def main(*args, **kwargs):
    solution = Solution()
    filename = "../advent_input.txt"
    ans = solution.part_one_solver(filename)
    print(f"Part one: {ans}")

if __name__ == "__main__":
    main()



