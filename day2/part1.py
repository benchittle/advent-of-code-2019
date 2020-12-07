with open("input.txt") as file:
    data = list(map(int, file.read().split(",")))

data[1] = 12
data[2] = 2

for i, val in enumerate(data[::4]):
    index = i * 4
    if val == 1:
        data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
    elif val == 2:
        data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
    elif val == 99:
        break

print(data[0])