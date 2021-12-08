from statistics import mean, median

with open("input.txt") as input_file:
    crabs = [int(x) for x in input_file.readline().strip().split(',')]

print(mean(crabs), median(crabs))

print(sum((abs(x - median(crabs)) for x in crabs)))

min_fuel = None
for i in range(max(crabs)):
    dists = (abs(x - i) for x in crabs)
    fuel = sum((((n + 1) * n) / 2 for n in dists))
    if min_fuel:
        if fuel < min_fuel:
            min_fuel = fuel
            print(i, fuel)
    else:
        min_fuel = fuel

print(f"Winner: {min_fuel}")
