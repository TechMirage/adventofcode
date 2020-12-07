import time
from aocd import get_data
import networkx as nx

OUR_BAG = "shiny gold"

def decode_rule(rule):
    tmp = rule.split(' ')
    dest = tmp[0] + ' ' + tmp[1]
    tmp = tmp[4:]
    num_of_contains = len(tmp) // 4
    start = []
    num = []
    for x in range(num_of_contains):
        num.append(tmp[4*x])
        start.append(tmp[4*x + 1] + ' ' + tmp[4*x + 2])
    return dest, start, num


def process(puzzle_input: str):
    puzzle_input = puzzle_input.split('\n')
    graph = nx.DiGraph()
    for rule in puzzle_input:
        dest, start, _ = decode_rule(rule)
        graph.add_edges_from([(x, dest) for x in start])
    leaves = []
    for node in graph.nodes:
        if graph.out_degree(node) == 0: # find the leaves
            leaves.append(node)
    valid_bags = set()
    for leaf in leaves:
        paths = nx.all_simple_paths(graph, OUR_BAG, leaf) 
        if paths: # check to see if there are any paths to this leaf
            for path in paths:
                tmp = set(path)
                valid_bags = valid_bags.union(tmp)
    return len(valid_bags) - 1 # Have to remove the 'shiny gold' bag from the set.


def main():
    puzzle_input = get_data(day=7)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
