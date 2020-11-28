import hashlib


def check_hash(zeros: int, str_to_check: str) -> bool:
    tmp = hashlib.md5(str_to_check.encode())
    tmp = tmp.hexdigest()
    tmp2 = str(tmp[:zeros])
    if tmp2 == '00000' or tmp2 == '000000':
        return True
    return False


def process(line: str, zeros: int, starting_pt: int = 0) -> int:
    winning = False
    counter = starting_pt - 1
    while not winning:
        counter += 1
        if check_hash(zeros, line + str(counter)):
            winning = True
    return counter


def main():
    with open('input.txt') as f:
        for line in f:
            ans = process(line[:-1], 5)
            ans2 = process(line[:-1], 6, starting_pt=ans)

    print("The earliest number for 5 zeros is:", ans)
    print("The earliest number for 6 zeros is:", ans2)


if __name__ == "__main__":
    main()
