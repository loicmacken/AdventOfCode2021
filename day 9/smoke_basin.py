import numpy as np

input_data: list[list[int]] = []

path = './day 9/input.txt'

with open(path, 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        row: list[int] = [int(c) for c in line.strip()]
        input_data.append(row)

heightmap: np.ndarray = np.array(input_data, dtype=int)

def get_neighbors(index: tuple[int, int]) -> list[int]:
    x, y = index
    output: list[int] = []
    neighbor_ids: list[tuple[int, int]] = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]

    for id in neighbor_ids:
        if id[0] < heightmap.shape[0] and id[1] < heightmap.shape[1]:
            output.append(heightmap[id])

    return output

def is_low_point(index: tuple[int, int]) -> bool:
    val: int = heightmap[index]

    for n in get_neighbors(index):
        if n <= val:
            return False

    return True

def get_risk_level(index: tuple[int, int]) -> int:
    if not is_low_point(index):
        return 0

    return heightmap[index] + 1

def part_one() -> int:
    sum_risk: int = 0

    shape_x, shape_y = heightmap.shape
    for x in range(shape_x):
        for y in range(shape_y):
            sum_risk += get_risk_level((x, y))

    return sum_risk

print(f'--- PART ONE ---')
print(f'The sum of all the risk levels is {part_one()}')   

borders: np.ndarray = np.where(heightmap == 9, 1, 0)

def get_clusters(row: np.ndarray) -> list[np.ndarray]:
    return [arr[:-1] for arr in np.split(range(row.shape[0]), np.where(row != 0)[0]+1)]

def is_valid(n: tuple[int, int]) -> bool:
    if n[0] >= borders.shape[0] or n[0] < 0 or n[1] >= borders.shape[1] or n[1] < 0 or borders[n] != 0:
        return False
    return True

def count_neighbors(size: int, coord: tuple[int, int]) -> int:
    if not is_valid(coord):
        return size

    size += get_size([coord])
    r, c = coord
    neighbors: list[tuple[int, int]] = [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]
    
    for n in neighbors:
        if is_valid(n):
            size = count_neighbors(size, n)

    return size

def get_size(coords: list[tuple[int, int]]) -> int:
    for c in coords:
        borders[c] = 2
    return len(coords)

def navigate_cluster(cluster: np.ndarray, row_idx: int) -> int:
    # size: int = get_size([(row_idx, n) for n in cluster])
    size: int = 0

    for n in cluster:
        size = count_neighbors(size, (row_idx, n))
    return size

def get_sizes() -> list[int]:
    sizes: list[int] = []

    for row_idx in range(borders.shape[0]):
        row: np.ndarray = borders[row_idx, :]
        clusters: list[np.ndarray] = get_clusters(row)

        for c in clusters:
            size = navigate_cluster(c, row_idx)
            if size > 0:
                sizes.append(size)

    return sizes

def part_two() -> int:
    sizes: list[int] = get_sizes()

    sizes_sorted = sorted(sizes, reverse=True)
    print(sizes_sorted)
    return sizes_sorted[0] * sizes_sorted[1] * sizes_sorted[2]
    # return 1

print(f'--- PART TWO ---')
print(f'The product of the three largest basins is {part_two()}')   

with open('./day 9/output.txt', 'w') as outfile:
    for row in borders:
        outfile.write(''.join([str(n).strip() for n in row]))
        outfile.write('\n')