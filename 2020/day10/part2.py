import time
from aocd import get_data
import networkx as nx


def input_format(puzzle_input: list):
    # Some basic formatting for the input.
    for i in range(len(puzzle_input)):
        puzzle_input[i] = int(puzzle_input[i])
    puzzle_input.append(0)
    puzzle_input.sort()
    puzzle_input.append(puzzle_input[-1] + 3)
    return puzzle_input


def process(puzzle_input: list):
    G = nx.DiGraph()
    puzzle_input = input_format(puzzle_input)
    for i in range(len(puzzle_input) - 1):
        for j in range(1, len(puzzle_input) - 2):
            try:
                if puzzle_input[i + j] - puzzle_input[i] <= 3:
                    # for this solution, we keep track of the number
                    # of paths going into a node as the path_num attr
                    # on the edge. Then, every time we make a new node, 
                    # we add up the paths coming in to see how many paths
                    # are going out. 
                    if i == 0:
                        weight = 1
                    else:
                        weight = 0
                        for edge in G.in_edges([puzzle_input[i]]):
                            weight += G.get_edge_data(*edge)['path_num']
                    G.add_edge(puzzle_input[i], puzzle_input[i + j], path_num=weight)
                else:
                    break
            except IndexError:
                break

    # Frankly, this will probably work (and does with test cases), 
    # but it was up to 24GB of RAM usage when I stopped it before it crashed
    # my computer when running on the real data. So we'll try something
    # else.
    # 1) len(list(nx.all_simple_paths(G, puzzle_input[0], puzzle_input[-1])))
    #           -OR-
    # 2) counter = 0
    # 2) for _ in nx.all_simple_paths(G, puzzle_input[0], puzzle_input[-1]):
    # 2)     counter += 1 

    num_of_paths = 0
    for edge in G.in_edges([puzzle_input[-1]]):
        num_of_paths += G.get_edge_data(*edge)['path_num']

    return num_of_paths 


def main():
    puzzle_input = get_data(day=10)
    puzzle_input = puzzle_input.split('\n')

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
