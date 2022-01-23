import numpy as np
import pandas as pd

class Fish:
    def __init__(self, input_path: str, n_days: int, output: bool = False) -> None:
        self.n_days: int = n_days
        self.output: bool = output

        self.fish: np.ndarray = np.empty(0)
        self.get_fish(input_path)

        self.fish_counts: np.ndarray = np.zeros(9, dtype=np.longlong)
        self.set_fish_counts()

    def get_fish(self, path: str) -> None:
        with open(path, 'r') as infile:
            self.fish = np.array(pd.read_csv(infile, header=None), dtype=int).flatten() # type: ignore

    def set_fish_counts(self) -> None:
        for i in range(self.fish_counts.size):
            self.fish_counts[i] = np.count_nonzero(self.fish == i)

    def calculate_fish_from_counts(self) -> None:
        self.fish = np.zeros(0, dtype=int)
        for i in range(self.fish_counts.size):
            if self.fish_counts[i] > 0:
                self.fish = np.append(self.fish, i*np.ones(self.fish_counts[i], dtype=int))

    def output_state(self, day: int) -> str:
        fish_str: str = ','.join(str(n) for n in self.fish)

        if day == 0:
            return f'Initial state: {fish_str}'
        elif day == 1:
            return f'After {day:02} day:  {fish_str}'
        else:
            return f'After {day:02} days: {fish_str}'

    def update_fish(self) -> None:
        n_children: int = np.count_nonzero(self.fish == 0)
        self.fish[self.fish == 0] = 7
        self.fish = np.append(self.fish, 9*np.ones(n_children, dtype=int))
        self.fish -= 1

    def run(self) -> np.ndarray:
        print(self.output_state(0))

        for day in range(self.n_days):
            self.update_fish()

            if self.output:
                print(self.output_state(day + 1))
            else:
                print(f'Day {day}')

        return self.fish

    def update_count(self) -> None:
        n_children: int = self.fish_counts[0]
        self.fish_counts[7] += n_children
        for i in range(8):
            self.fish_counts[i] = self.fish_counts[i+1]
        self.fish_counts[8] = n_children

    def run_count(self) -> int:
        print(self.output_state(0))

        for day in range(self.n_days):
            self.update_count()
            if self.output:
                self.calculate_fish_from_counts()
                print(self.output_state(day + 1))
            else:
                print(f'Day {day}')

        return np.sum(self.fish_counts)

if __name__ == '__main__':
    input_path: str = 'day 6\\input.txt'

    # part one
    print('Part one:')
    n_days: int = 80
    fish_one: Fish = Fish(input_path, n_days)
    n_fish_one: int = fish_one.run_count()
    print(f'Number of fish after {n_days}: {n_fish_one}')

    # part two
    print('Part two:')
    n_days: int = 256
    fish_two: Fish = Fish(input_path, n_days)
    n_fish_two: int = fish_two.run_count()
    print(f'Number of fish after {n_days}: {n_fish_two}')

