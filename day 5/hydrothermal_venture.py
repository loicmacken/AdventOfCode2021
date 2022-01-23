import numpy as np

class Venture:
    def __init__(self, input_path: str) -> None:
        self.coords: list[tuple[int, int, int, int]] = []
        self.init_data(input_path)

        self.diagram: dict[tuple[int, int], int] = dict()


    def init_data(self, path: str) -> None:
        with open(path, 'r') as infile:
            lines = infile.readlines()
            for line in lines:
                line = line.strip()
                start, end = [s.strip() for s in line.split('->')]
                x1, y1 = [int(s) for s in start.split(',')]
                x2, y2 = [int(s) for s in end.split(',')]
                coord = x1, y1, x2, y2
                self.coords.append(coord)

    def _set_diagram_val(self, coord: tuple[int, int]) -> None:
        x, y = coord

        if (x, y) in self.diagram:
            self.diagram[(x, y)] += 1
        else:
            self.diagram[(x, y)] = 1

    def lines_hor_ver(self) -> None:
        for coord in self.coords:
            x1, y1, x2, y2 = coord

            if y1 == y2:
                if x2 > x1:    
                    for x in range(x1, x2+1):
                        self._set_diagram_val((x, y1))
                elif x2 < x1:
                    for x in range(x2, x1+1):
                        self._set_diagram_val((x, y1))

            if x1 == x2:
                if y2 > y1:
                    for y in range(y1, y2+1):
                        self._set_diagram_val((x1, y))

                elif y2 < y1:
                    for y in range(y2, y1+1):
                        self._set_diagram_val((x1, y))

    def get_count(self) -> int:
        count: int = 0

        for _, v in self.diagram.items():
            if v > 1:
                count += 1

        return count

    # --- PART ONE ---

    def run_one(self) -> int:
        self.lines_hor_ver()
        return self.get_count()

    # --- PART TWO ---

    def lines_diag(self) -> None:
        for coord in self.coords:
            x1, y1, x2, y2 = coord
            
            if not x1 == x2 and not y1 == y2:
                if abs(x2 - x1) == abs(y2 - y1):
                    x_range = []
                    if x2 > x1:
                        x_range = range(x1, x2+1)
                    else:
                        x_range = range(x1, x2-1, -1)

                    y_range = []
                    if y2 > y1:
                        y_range = range(y1, y2+1)
                    else:
                        y_range = range(y1, y2-1, -1)

                    for x, y in zip(x_range, y_range):
                        self._set_diagram_val((x,y))

    def run_two(self) -> int:
        self.lines_hor_ver()
        self.lines_diag()
        return self.get_count()

if __name__ == '__main__':
    input_path: str = 'day 5\\input.txt'

    # part one
    venture_one = Venture(input_path)
    count_one = venture_one.run_one()
    print(f'Part one: there are {count_one} points with at least two crossing lines')

    # part two
    venture_two = Venture(input_path)
    count_two = venture_two.run_two()
    print(f'Part two: there are {count_two} points with at least two crossing lines')
