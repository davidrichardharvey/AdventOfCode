from pprint import pprint
with open('day7input.txt') as file:
    lines = file.readlines()

def split_bags(rule_text):
    i = rule_text.find(' bags contain')
    outer = rule_text[:i]
    inner = rule_text[i + 14:]
    inner = inner.replace('no other bags.\n','')
    inner = inner.replace('.\n', '').replace(' bags','').replace(' bag','').split(', ')
    inner = list(map(lambda x: (int(x[0]),x[2:]) if len(x) > 0 else (), inner))
    # inner = list(map(lambda x: x[2:] if len(x) > 0 else x, inner))
    return [outer, inner]

split_rules = list(map(split_bags, lines))
graph = {}
for x in split_rules:
    if x[1] != [()]:
        graph[x[0]] = x[1]
# pprint(graph)
#pprint(graph)
# possible_bags = set()
# old_bags = ['shiny gold']
# while True:
#     new_bags = []
#     for x in split_rules:
#         for y in x[1]:
#             for bag in old_bags:
#                 if bag in y:
#                     new_bags.append(x[0])
#                     print(x)
#     if old_bags == new_bags:
#         break
#     old_bags = []
#     for x in new_bags:
#         possible_bags.add(x)
#         old_bags.append(x)

# Part 2
searched = set()
total_bags = 1
to_sum = []
def bag_search(bag_graph, bag_name, total_bags):
    # check if bag empty, return 0
    if bag_name in bag_graph.keys():
        rule = bag_graph[bag_name]
        print(rule)
        for new_bag in rule:
            if len(new_bag) > 0:
                print(bag_name, new_bag)
                for x in range(new_bag[0]):
                    print(new_bag)
                    to_sum.append(new_bag[1])
                    bag_search(bag_graph, new_bag[1], total_bags)


bag_search(graph, 'shiny gold', 1)
print(len(to_sum))



# all_bags = []
# possible_bags = set()
# old_bags = ['shiny gold']
# counter = 0
# while True:
#     new_bags = []
#     for bag in old_bags:
#         for rule in split_rules:
#             if rule[0] == bag:
#                 if len(rule[1][0]) > 0:
#                     all_bags.append(rule[1])
#                     for new_bag in rule[1]:
#                         if len(new_bag) > 0:
#                             new_bags.append(new_bag[1])
#     if old_bags == new_bags:
#         break
#     old_bags = []
#     for x in new_bags:
#         possible_bags.add(x)
#         old_bags.append(x)
#
# print(all_bags)
