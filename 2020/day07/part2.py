import time
from aocd import get_data
import networkx as nx
from functools import reduce

OUR_BAG = "shiny gold"

def decode_rule(rule):
    tmp = rule.split(' ')
    dest = tmp[0] + ' ' + tmp[1]
    tmp = tmp[4:]
    num_of_contains = len(tmp) // 4
    start = []
    num = []
    for x in range(num_of_contains):
        num.append(int(tmp[4*x]))
        start.append(tmp[4*x + 1] + ' ' + tmp[4*x + 2])
    return dest, start, num


def dfs_cost(graph, node):
    # A depth first search through the nodes for bag amounts.
    cost = 0
    for node, attrs in graph[node].items():
        cost += attrs['weight'] + attrs['weight'] * dfs_cost(graph, node)
    return cost


def process(puzzle_input: str):
    puzzle_input = puzzle_input.split('\n')
    graph = nx.DiGraph()
    for rule in puzzle_input:
        dest, start, num = decode_rule(rule)
        for x in range(len(start)):
            graph.add_edge(start[x], dest, weight=num[x])
    
    graph = graph.reverse()
    return dfs_cost(graph, OUR_BAG)


def main():
    puzzle_input = get_data(day=7)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
