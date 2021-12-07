from aoc_func import read_input_text

course = read_input_text("example.txt")


def plot_course(course_list):
    d, h = 0, 0
    for step in course_list:
        direction, dist = step.split(" ")
        dist = int(dist)
        if direction == "up":
            d -= dist
        elif direction == "down":
            d += dist
        elif direction == "forward":
            h += dist
    return d, h


# depth, horizontal = plot_course(course)
# print(depth * horizontal)


def plot_course_aim(course_list):
    d, h, a = 0, 0, 0
    for step in course_list:
        direction, dist = step.split(" ")
        dist = int(dist)
        if direction == "up":
            a -= dist
        elif direction == "down":
            a += dist
        elif direction == "forward":
            h += dist
            d += dist * a
    return d, h


depth, horizontal = plot_course_aim(course)
print(depth * horizontal)

