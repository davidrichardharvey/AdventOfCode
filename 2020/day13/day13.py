from math import ceil, prod, gcd

with open('day13input.txt') as file:
    earliest = int(file.readline())
    buses = [int(bus) if bus != 'x' else bus for bus in file.readline().split(',')]

# print(earliest)
print(list(buses))
timetable = {}

for bus in [bus for bus in buses if bus != 'x']:
    timetable[bus] = buses.index(bus)

print(timetable)

#t = 100000476343444
t = 0
t_found = False
while not t_found:
    cont = False
    for k, v in timetable.items():
        if (t + v) % k != 0:
            cont = True
            break
    if not cont:
        t_found = True
        print(t)
        break
    t += buses[0]
    #print(t)

# waiting = earliest
# earliest_bus = None
# for bus in buses:
#     new_waiting = (bus * ceil(earliest / bus)) - earliest
#     if new_waiting < waiting:
#         earliest_bus = bus
#         waiting = new_waiting
#
# print(earliest_bus, waiting, earliest_bus * waiting)
