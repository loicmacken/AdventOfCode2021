import numpy as np
import sys

class Treachery:
    def __init__(self, input_path: str) -> None:
        self.crabs: np.ndarray = np.zeros(0)
        self.get_data(input_path)

    def get_data(self, path: str) -> None:
        raw_data: list[int] = []

        with open(path, 'r') as infile:
            lines = infile.readlines()
            for line in lines:
                line = line.strip()
                for n in line.split(','):
                    raw_data.append(int(n))

        self.crabs = np.array(sorted(raw_data))

    def brute_force(self) -> tuple[int, int]:
        min_crab: int = self.crabs[0]
        max_crab: int = self.crabs[-1]
        min_dist: int = sys.maxsize
        min_i: int = -1

        for i in range(min_crab, max_crab + 1):
            dist: int = 0
            for crab in self.crabs:
                dist += abs(crab - i)
            
            if dist < min_dist:
                min_dist = dist
                min_i = i

        return min_i, min_dist

    @staticmethod
    def _get_sum(num: int) -> int:
        return round((num * (num + 1)) / 2)

    def brute_force_nonlinear(self) -> tuple[int, int]:
        min_crab: int = self.crabs[0]
        max_crab: int = self.crabs[-1]
        min_dist: int = sys.maxsize
        min_i: int = -1

        for i in range(min_crab, max_crab + 1):
            dist: int = 0
            for crab in self.crabs:
                dist += Treachery._get_sum(abs(crab - i))
            
            if dist < min_dist:
                min_dist = dist
                min_i = i

        return min_i, min_dist

if __name__ == '__main__':
    input_path: str = 'day 7\\input.txt'
    # input_path_test: str = 'day 7\\test_input.txt'

    # # test
    # treachery_test = Treachery(input_path_test)
    # print(treachery_test.crabs)
    # print(treachery_test.brute_force())
    # print(treachery_test.brute_force_nonlinear())

    # part one
    treachery_one = Treachery(input_path)
    print('Part one:')
    i_one, dist_one = treachery_one.brute_force()
    print(f'The optimal point is {i_one}, which costs {dist_one} fuel')

    # part two
    treachery_two = Treachery(input_path)
    print('Part two:')
    i_two, dist_two = treachery_two.brute_force_nonlinear()
    print(f'The optimal point is {i_two}, which costs {dist_two} fuel')
