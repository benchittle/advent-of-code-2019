with open("input.txt") as file:
    original_data = list(map(int, file.read().split(",")))

for n in range(100):
    for v in range(100):
        data = original_data[:]
        data[1] = n
        data[2] = v

        for i, val in enumerate(data[::4]):
            index = i * 4
            if val == 1:
                data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
            elif val == 2:
                data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
            elif val == 99:
                break

        if data[0] == 19690720:
            print(n * 100 + v)
