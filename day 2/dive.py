class Dive:
    def __init__(self, input_path: str) -> None:
        self.pos: int = 0
        self.depth: int = 0
        self.commands: list[tuple[str, int]] = self.get_data(input_path)

        # part two vars
        self.aim: int = 0

    def get_coords(self) -> tuple[int, int]:
        return self.pos, self.depth
        
    def move(self, dir: str, val: int) -> None:
        if dir == 'forward':
            self._move_horizontal(val)
        if dir == 'down':
            self._move_vertical(val)
        if dir == 'up':
            self._move_vertical(-val)

    def _move_horizontal(self, val: int) -> None:
        self.pos += val

    def _move_vertical(self, val: int) -> None:
        self.depth += val

    def get_data(self, input_path: str) -> list[tuple[str, int]]:
        data: list[tuple[str, int]] = []

        with open(input_path, 'r') as infile:
            lines = infile.readlines()
            for line in lines:
                line = line.strip()
                dir, val = line.split()
                data.append((dir, int(val)))

        return data

    def run(self) -> None:
        for dir, val in self.commands:
            self.move(dir, val)

    # part two funcs

    def move_2(self, dir: str, val: int) -> None:
        if dir == 'forward':
            self._move_forward(val)
        if dir == 'down':
            self._change_aim(val)
        if dir == 'up':
            self._change_aim(-val)

    def _move_forward(self, val: int) -> None:
        self.pos += val
        self.depth += self.aim * val

    def _change_aim(self, val: int) -> None:
        self.aim += val

    def run_2(self) -> None:
        for dir, val in self.commands:
            self.move_2(dir, val)

if __name__ == '__main__':
    # --- GET DATA ---
    input_path: str = 'day 2\input.txt'

    # --- PART ONE --- 
    dive = Dive(input_path)
    dive.run()
    pos, depth = dive.get_coords()
    print('Part one:')
    print(f'Position: {pos}, depth: {depth}, multiplied: {pos * depth}')

    # --- PART TWO ---
    dive_2 = Dive(input_path)
    dive_2.run_2()
    pos, depth = dive_2.get_coords()
    print('Part two:')
    print(f'Position: {pos}, depth: {depth}, multiplied: {pos * depth}')


