from puzzle_input import puzzle_input, test_input
import re

pattern = re.compile(r"move (.*) from (.*) to (.*)")

puzzle_board = [
    ['Z', 'T', 'F', 'R', 'W', 'J', 'G'],
    ['G', 'W', 'M'],
    ['J', 'N', 'H', 'G'],
    ['J', 'R', 'C', 'N', 'W'],
    ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
    ['S', 'R', 'T', 'D', 'V', 'W', 'C'],
    ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
    ['S', 'J', 'N', 'M', 'G', 'C'],
    ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L']
]

puzzle_board_2 = [
    ['Z', 'T', 'F', 'R', 'W', 'J', 'G'],
    ['G', 'W', 'M'],
    ['J', 'N', 'H', 'G'],
    ['J', 'R', 'C', 'N', 'W'],
    ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
    ['S', 'R', 'T', 'D', 'V', 'W', 'C'],
    ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
    ['S', 'J', 'N', 'M', 'G', 'C'],
    ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L']
]

test_board = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]

test_board_2 = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]


def part_one(instructions, board):
    for instruction in instructions:
        res = pattern.match(instruction)
        cnt = 0
        while cnt < int(res.group(1)):
            try:
                board[int(res.group(3)) - 1].append(board[int(res.group(2)) - 1].pop())
            except IndexError:
                print("Instruction that failed:", instruction)
                print("Board state currently:", board)
                print("And just for kicks, here's the cnt:", cnt)
                print("Confirmation that the res is working as intended:", res.group(1))
                raise(0)
            cnt += 1

    ans = ""
    for row in board:
        ans += row[-1]

    print("ANS: The final top crates are:", ans)


def part_two(instructions, board):
    for instruction in instructions:
        res = pattern.match(instruction)
        to_move = board[int(res.group(2)) - 1][-int(res.group(1)):]
        board[int(res.group(2)) - 1] = board[int(res.group(2)) - 1][:-int(res.group(1))]
        for crate in to_move:
            board[int(res.group(3)) - 1].append(crate)


    ans = ""
    for row in board:
        ans += row[-1]

    print("ANS: The final top crates are:", ans)


def main():
    print("--- TESTING PART ONE ---")
    instructions = test_input.split('\n')
    instructions = list(filter(pattern.match, instructions))
    part_one(instructions, test_board)
    print("--- TESTING PART TWO ---")
    part_two(instructions, list(test_board_2))    
    print("--- PART ONE SOLUTION ---")
    instructions = puzzle_input.split('\n')
    instructions = list(filter(pattern.match, instructions))
    part_one(instructions, list(puzzle_board))
    print("--- PART TWO SOLUTION ---")
    part_two(instructions, list(puzzle_board_2))

if __name__ == "__main__":
    main()