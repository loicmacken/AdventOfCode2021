
# --- GET DATA ---

input_path: str = 'day 1\input.txt'
data: list[int] = []

with open(input_path, 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        line = line.strip()
        num = int(line)
        data.append(num)

# --- PART ONE ---

num_increased: int = 0

for i in range(1, len(data)):
    if data[i] > data[i-1]:
        num_increased += 1

print(f'Part one: {num_increased}')

# --- PART TWO ---

num_sums: int = 0

sums: list[int] = []

for i in range(len(data)-2):
    sum: int = data[i] + data[i+1] + data[i+2]
    sums.append(sum)

for i in range(1, len(sums)):
    if sums[i] > sums[i-1]:
        num_sums += 1

print(f'Part two: {num_sums}')

