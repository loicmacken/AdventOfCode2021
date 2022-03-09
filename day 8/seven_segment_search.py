import numpy as np

path: str = './day 8/input.txt'

input_data: list[list[str]] = []
input_right: list[list[str]] = []

unique_numbers: dict[int, int] = {
    2: 1, 
    4: 4, 
    3: 7, 
    7: 8
}

with open(path, 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        left, right = line.split('|')
        # input_data.append(left.strip().split(' '))
        # input_data.append(right.strip().split(' '))
        input_data.append(left.strip().split(' ') + right.strip().split(' '))
        input_right.append(right.strip().split(' '))

def part_one(data_right: list[list[str]]) -> int:
    count_unique: int = 0

    for line in data_right:
        for n in line:
            if len(n) in unique_numbers.keys():
                count_unique += 1

    return count_unique

print(f'--- PART ONE ---')
print(f'There are {part_one(input_right)} unique numbers in the output values')       

default_nums: np.ndarray = np.array([
    [1,1,1,0,1,1,1], 
    [0,0,1,0,0,1,0], 
    [1,0,1,1,1,0,1], 
    [1,0,1,1,0,1,1], 
    [0,1,1,1,0,1,0], 
    [1,1,0,1,0,1,1], 
    [1,1,0,1,1,1,1], 
    [1,0,1,0,0,1,0], 
    [1,1,1,1,1,1,1], 
    [1,1,1,1,0,1,1], 
], dtype=int)

def vec_to_idx(input: np.ndarray) -> set[int]:
    return set(np.where(input)[0])

def idx_to_vec(input: set[int]) -> np.ndarray:
    output: np.ndarray = np.zeros((7,), dtype=int)
    for n in input:
        output[n] = 1
    return output

default_nums_set: list[set[int]] = [vec_to_idx(x) for x in default_nums]

def str_to_vec(input: str) -> np.ndarray:
    vec: np.ndarray = np.zeros((7,), dtype=int)
    letters: str = 'abcdefg'

    for i in range(7):
        if letters[i] in input:
            vec[i] = 1

    return vec

def is_equal(arr1: np.ndarray, arr2: np.ndarray) -> bool:
    return vec_to_idx(arr1) == vec_to_idx(arr2)

def exists(arr: np.ndarray) -> bool:
    for s in default_nums_set:
        if vec_to_idx(arr) == s:
            return True

    return False

def get_num(arr: np.ndarray) -> int:
    return default_nums_set.index(vec_to_idx(arr))

def create_matrices() -> list[np.ndarray]:
    matrices: list[np.ndarray] = []

    rows_i = [x for x in range(7)]
    for i in rows_i:
        rows_j = rows_i[:]
        rows_j.remove(i)
        for j in rows_j:
            rows_k = rows_j[:]
            rows_k.remove(j)
            for k in rows_k:
                rows_l = rows_k[:]
                rows_l.remove(k)
                for l in rows_l:
                    rows_m = rows_l[:]
                    rows_m.remove(l)
                    for m in rows_m:
                        rows_n = rows_m[:]
                        rows_n.remove(m)
                        for n in rows_n:
                            rows_o = rows_n[:]
                            rows_o.remove(n)
                            for o in rows_o:
                                M: np.ndarray = np.zeros((7,7), dtype=int)
                                M[0,i] = 1
                                M[1,j] = 1
                                M[2,k] = 1
                                M[3,l] = 1
                                M[4,m] = 1
                                M[5,n] = 1
                                M[6,o] = 1
                                matrices.append(M)

    return matrices

def verify_solution(P: np.ndarray, line: list[str]) -> bool:
    for n in line:
        input: np.ndarray = str_to_vec(n)
        output: np.ndarray = P.dot(input)

        if not exists(output):
            return False

    return True


def brute_force(line: list[str], matrices: list[np.ndarray]) -> np.ndarray:
    for M in matrices:
        if verify_solution(M, line):
            return M

    raise ValueError

def compute_p_matrices(input_data: list[list[str]], matrices: list[np.ndarray]) -> list[np.ndarray]:
    p_matrices: list[np.ndarray] = []

    for line in input_data:
        P = brute_force(line, matrices)

        p_matrices.append(P)

    return p_matrices

def get_outputs(p_matrices: list[np.ndarray], input_right: list[list[str]]) -> list[int]:
    outputs: list[int] = []

    for P, inputs in zip(p_matrices, input_right):
        num: str = ''

        for n in inputs:
            input: np.ndarray = str_to_vec(n)
            output: np.ndarray = P.dot(input)

            if not exists(output):
                print(n, input, output)

            val: int = get_num(output)
            num = num + str(val)

        outputs.append(int(num))

    return outputs

def part_two(input_data: list[list[str]], input_right: list[list[str]]) -> int:
    matrices: list[np.ndarray] = create_matrices()

    p_matrices: list[np.ndarray] = compute_p_matrices(input_data, matrices)

    outputs: list[int] = get_outputs(p_matrices, input_right)

    return sum(outputs)

print(f'--- PART TWO ---')
print(f'The sum of the numbers is {part_two(input_data, input_right)}')   
