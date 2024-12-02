class Solution:
    def __init__(self):
        print("Day 2 on the books")
        self.dampener_list = []  # Corrected spelling from 'dampner_list' to 'dampener_list'

    def calculator(self, values):
        """
        Processes a list of string values by converting them to integers and applying specific logic.

        Args:
            values (List[str]): A list of string representations of integers.

        Returns:
            int: Returns 1 if the processing is successful based on the logic; otherwise, returns 0.
        """
        if len(values) < 2:
            print("Error: At least two values are required for calculation.")
            return 0

        try:
            order = int(values[1]) - int(values[0])  # Determine the initial order
        except ValueError as e:
            print(f"ValueError: {e} in values {values}")
            return 0

        stack = []
        for v in values:
            try:
                num = int(v)
            except ValueError as e:
                print(f"ValueError: {e} for value '{v}'")
                return 0

            if not stack:
                stack.append(num)
                continue

            difference = stack[-1] - num
            abs_diff = abs(difference)

            if 1 <= abs_diff <= 3:
                if order > 0 and num < stack[-1]:
                    print(f"Order > 0 but current number {num} is less than previous {stack[-1]}.")
                    return 0
                elif order < 0 and num > stack[-1]:
                    print(f"Order < 0 but current number {num} is greater than previous {stack[-1]}.")
                    return 0
                stack.append(num)
            else:
                print(f"Difference {abs_diff} out of range (1-3) between {stack[-1]} and {num}.")
                return 0

        return 1

    def helper(self, line):
        """
        Processes a single line by splitting it into values and passing them to the calculator.

        Args:
            line (str): A single line from the input file.

        Returns:
            int: Result from the calculator (1 or 0).
        """
        values = line.strip().split()
        result = self.calculator(values)
        return result

    def helper_two(self, line):
        """
        Attempts to find if removing any single value from the line results in a successful calculation.

        Args:
            line (str): A single line from the input file.

        Returns:
            int: Returns 1 if any removal leads to a successful calculation; otherwise, returns 0.
        """
        values = line.strip().split()

        for i in range(len(values)):
            new_list = values[:i] + values[i + 1:]
            if self.calculator(new_list) == 1:
                return 1
        return 0

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

    def solver(self, filename):
        """
        Processes each line in the file using the helper method.
        Collects lines that do not pass the calculator into dampener_list and sums the results.

        Args:
            filename (str): Path to the input file.

        Returns:
            int: Total sum of successful calculations.
        """
        total = 0
        for line in self.line_generator(filename):
            result = self.helper(line)
            if result != 1:
                self.dampener_list.append(line.strip())
            total += result
        return total

    def solver_two(self):
        """
        Processes the dampener_list using helper_two to attempt corrections and sum the results.

        Returns:
            int: Total sum of successful calculations after corrections.
        """
        total = 0
        print(f"Number of dampened lines: {len(self.dampener_list)}")
        for line in self.dampener_list:
            result = self.helper_two(line)
            total += result
        return total


def main():
    solution = Solution()
    initial_answer = solution.solver("data.txt")
    corrected_answer = solution.solver_two() + initial_answer
    print(f"Part 2: {corrected_answer}")


if __name__ == "__main__":
    main()
