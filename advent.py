import heapq
from collections import Counter, defaultdict

class Solver:

    def __init__(self):
        print("And so it begins")

    # defaultdict to the rescue
    def part_two(self, filename):
        left_list = []
        right_dict = defaultdict(int)
        with open(filename, "r") as fr:
            for l in fr:
                l = l.strip("\n").split(" ")
                left, right = int(l[0]), int(l[-1])
                left_list.append(left)
                right_dict[right] += 1
        
        similar = 0
        for n in left_list:
            similar += n * right_dict.get(n, 0)
        
        return similar

    # Heaps is the way to go
    def part_one(self, filename):
        left_heap, right_heap = [], []

        with open(filename, "r") as fr:
            for l in fr:
                l = l.strip("\n").split(" ")
                left, right = int(l[0]), int(l[-1])
                heapq.heappush(left_heap, left)
                heapq.heappush(right_heap, right) 
        total_sum = 0

        while left_heap and right_heap:
            total_sum += abs(heapq.heappop(left_heap) - heapq.heappop(right_heap))
        
        return total_sum


def main():

    filename = "advent_input.txt"

    solution = Solver()
    ans = solution.part_one(filename)
    print("Answer is : ", ans)

    second_ans = solution.part_two(filename)
    print("Second ans is: ", second_ans)


if __name__ == "__main__":
    main()