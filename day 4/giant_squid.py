import numpy as np

class Squid:
    def __init__(self, input_path: str) -> None:
        # numbers to call out
        self.numbers: list[int] = []
        # the bingo boards, each being a tuple with a 2d array of numbers and a 2d array of bools,
        # that are true if the number has been called
        self.boards: list[tuple[np.ndarray, np.ndarray]] = []
        self.init_data(input_path)

        # part two vars
        self.wins: list[tuple[np.ndarray, np.ndarray]] = []

    def init_data(self, path: str) -> None:
        raw_data: list[list[list[int]]] = []

        with open(path, 'r') as infile:
            lines = infile.readlines()
            for line in lines:
                line = line.strip()
                if ',' in line:
                    # starting numbers
                    for n in line.split(','):
                        self.numbers.append(int(n))
                else:
                    if not line:
                        raw_data.append([])
                        continue
                    nums: list[str] =  line.split(' ')
                    nums_int: list[int] = []
                    for n in nums:
                        n = n.strip()
                        if not n:
                            continue
                        nums_int.append(int(n))
                    raw_data[-1].append(nums_int)

        for lst in raw_data:
            # the board of numbers in array form
            arr: np.ndarray = np.array(lst, dtype=int)
            # bool to denote whether the number has been called, initialize with only True
            bools: np.ndarray = np.full_like(arr, False)
            self.boards.append((arr, bools))

    def update_boards(self, num: int) -> None:
        for board in self.boards:
            ids: tuple[np.ndarray, np.ndarray] = np.where(board[0] == num)
            if ids:
                board[1][ids] = True

    @staticmethod
    def _check_bingo(bools: np.ndarray) -> bool:
        # check for bingo in rows
        for row in bools:
            if all(row):
                return True

        # check for bingo in columns:
        for col in bools.transpose():
            if all(col):
                return True

        return False

    def check_wins(self) -> tuple[np.ndarray, np.ndarray] | None:
        for board in self.boards:
            _, bools = board

            if Squid._check_bingo(bools):
                return board

        return None

    @staticmethod
    def get_value(board: tuple[np.ndarray, np.ndarray], win_value: int) -> int:
        nums, bools = board
        uncalled: np.ndarray = np.where(1-bools, nums, 0)
        sum_uncalled: int = np.sum(uncalled)

        return win_value * sum_uncalled

    # --- PART ONE ---

    def run(self) -> int:
        for n in self.numbers:
            self.update_boards(n)
            win_board: tuple[np.ndarray, np.ndarray] | None = self.check_wins()
            if (win_board):
                val: int = Squid.get_value(win_board, n)
                return val
        return -1

    # --- PART TWO ---

    def check_losses(self) -> tuple[np.ndarray, np.ndarray] | None:
        losses: list[tuple[np.ndarray, np.ndarray]] = []

        for board in self.boards:
            _, bools = board

            if Squid._check_bingo(bools):
                self.wins.append(board)
                continue

            losses.append(board)

        if not losses:
            return self.wins[-1]
            
        self.boards = losses
        return None
    
    def run_2(self) -> int:
        for n in self.numbers:
            self.update_boards(n)
            losing_board: tuple[np.ndarray, np.ndarray] | None = self.check_losses()
            if (losing_board):
                val: int = Squid.get_value(losing_board, n)
                return val
        return -1

if __name__ == '__main__':
    input_path: str = 'day 4\\input.txt'

    # part one
    squid = Squid(input_path)
    value: int = squid.run()
    print(f'The value of part one: {value}')

    # part two
    squid_2 = Squid(input_path)
    value_2: int = squid_2.run_2()
    print(f'The value of part two: {value_2}')
