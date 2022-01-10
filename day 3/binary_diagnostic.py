import numpy as np

# --- GET DATA ---

input_path: str = 'day 3\\input.txt'
raw_data: list[list[int]] = []

with open(input_path, 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        line = line.strip()
        row = [int(c) for c in line]
        raw_data.append(row)

data: np.ndarray = np.array(raw_data)

# --- PART ONE ---

gamma_lst: list = []
epsilon_lst: list = []

def bin_to_dec(input: list[int]) -> int:
    result: int = 0
    input.reverse()
    for i in range(len(input)):
        result += input[i] * 2**i
    return result

def get_most_least_common(input: np.ndarray, index: int) -> tuple[int, int]:
    values, counts = np.unique(input[:,index], return_counts=True)

    set_counts: set[int] = set(counts)

    if len(set_counts) == 1:
        return (1,0)

    ind_max: int = np.argmax(counts) # type: ignore
    ind_min: int = np.argmin(counts) # type: ignore

    return (values[ind_max], values[ind_min])

for i in range(data.shape[1]):
    most, least = get_most_least_common(data, i)
    gamma_lst.append(most)
    epsilon_lst.append(least)

gamma: int = bin_to_dec(gamma_lst)
epsilon: int = bin_to_dec(epsilon_lst)

print('Part one:')
print(f'Gamma: {gamma}, epsilon: {epsilon}, multiplied: {gamma * epsilon}')

# --- PART TWO ---

def get_filtered_most(arr: np.ndarray, index: int) -> np.ndarray:
    assert arr.shape[0] > 0
    
    if arr.shape[0] == 1:
        return arr

    most, _ = get_most_least_common(arr, index)
    
    filtered: np.ndarray = arr[np.where(arr[:,index] == most)]
    index += 1
    return get_filtered_most(filtered, index)

def get_filtered_least(arr: np.ndarray, index: int) -> np.ndarray:
    assert arr.shape[0] > 0
    
    if arr.shape[0] == 1:
        return arr

    _, least = get_most_least_common(arr, index)
    
    filtered: np.ndarray = arr[np.where(arr[:,index] == least)]
    index += 1
    return get_filtered_least(filtered, index)

oxygen_lst: list[int] = list(get_filtered_most(data, 0).flatten())
co2_lst: list[int] = list(get_filtered_least(data, 0).flatten())

oxygen: int = bin_to_dec(oxygen_lst)
co2: int = bin_to_dec(co2_lst)

print('Part two:')
print(f'Oxygen: {oxygen}, CO2: {co2}, multiplied: {oxygen * co2}')


