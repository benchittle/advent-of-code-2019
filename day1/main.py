
def get_fuel_needed(current_fuel):
    if current_fuel <= 0:
        return 0
    return current_fuel + get_fuel_needed(current_fuel // 3 - 2)


with open("input.txt") as file:
    masses = [int(line[:-1]) for line in file]
    fuel = 0
    for i in masses:
        fuel += get_fuel_needed(i // 3 - 2)
    print(fuel)