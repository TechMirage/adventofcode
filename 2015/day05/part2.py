class PartTwoDecider:
    def __init__(self):
        self.num_good_words = 0

    def process(self, line: str):
        success = True
        if success:
            success = self.repeating_phrase_finder(line)
        if success:
            success = self.twice_in_a_rowish(line)
        if success:
            self.num_good_words += 1

    @staticmethod
    def repeating_phrase_finder(line: str) -> bool:
        for idx in range(len(line) - 2):
            # Cut out each two letter section, and then see how long the string still is.
            # If it's more than the 2 that you've cut out, then another section has been cut, which
            # means that there were more versions of this 'phrase'.
            test = line[idx:idx + 2]
            tmp = line.replace(test, '')
            if len(line) - 2 > len(tmp):
                return True
        return False

    @staticmethod
    def twice_in_a_rowish(line: str) -> bool:
        for idx in range(len(line) - 2):
            if line[idx] == line[idx + 2]:
                return True
        return False


def main():
    p2decider = PartTwoDecider()
    with open('input.txt') as f:
        for line in f:
            p2decider.process(line.strip())

    print("The number of valid words be:", p2decider.num_good_words)


if __name__ == "__main__":
    main()
