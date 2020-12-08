import time
from aocd import get_data
import re

def run_code(code):
    successful_code_stop = len(code)
    acc = 0
    cur_index = 0
    continue_processing = True
    success = False
    while continue_processing:
        if cur_index == successful_code_stop:
            success = True
            break
        if code[cur_index]:
            tmp = re.match(r'(nop|acc|jmp) (.+)$', code[cur_index])
            code[cur_index] = False # Make sure we don't run the same command again.
            if tmp.group(1) == 'acc':
                acc += int(tmp.group(2))
                cur_index += 1
            elif tmp.group(1) == 'nop':
                cur_index += 1
            elif tmp.group(1) == 'jmp':
                cur_index += int(tmp.group(2))
        else:
            continue_processing = False
    if success:
        return acc
    else:
        return False


def process(puzzle_input: str):
    code = puzzle_input.split('\n')
    for x in range(len(code) - 1):
        code_changed = code.copy()
        tmp = re.match(r'(nop|acc|jmp) (.+)$', code[x])
        if tmp.group(1) == 'acc':
            continue
        elif tmp.group(1) == 'nop':
            code_changed[x] = 'jmp' + code[x][3:]
        elif tmp.group(1) == 'jmp':
            code_changed[x] = 'nop' + code[x][3:]
        acc = run_code(code_changed)
        if acc:
            break
    return acc


def main():
    puzzle_input = get_data(day=8)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
