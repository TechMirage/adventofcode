import time

def process(line: str):
    return ""


def main():
    start_time = time.time()

    with open('input.txt') as f:
        for line in f:
            output = process(line)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")



if __name__ == "__main__":
    main()
