class PartOneDecider:
    BAD_PHRASES = ['ab', 'cd', 'pq', 'xy']
    VOWELS = ['a', 'e', 'i', 'o', 'u']

    def __init__(self):
        self.num_good_words = 0

    def process(self, line: str):
        success = True
        if success:
            success = self.three_vowel_finder(line)
        if success:
            success = self.twice_in_a_row(line)
        if success:
            success = self.does_not_contain(line)
        if success:
            self.num_good_words += 1

    def three_vowel_finder(self, line: str) -> bool:
        num_vowels = 0
        for char in line:
            if char in self.VOWELS:
                num_vowels += 1
        if num_vowels >= 3:
            return True
        return False

    @staticmethod
    def twice_in_a_row(line: str) -> bool:
        for idx in range(len(line) - 1):
            if line[idx] == line[idx + 1]:
                return True
        return False

    def does_not_contain(self, line: str) -> bool:
        """
        Doesn't contain the strings 'ab' 'cd' 'pq' 'xy'
        """
        for phrase in self.BAD_PHRASES:
            if phrase in line:
                return False
        return True


def main():
    p1decider = PartOneDecider()
    with open('input.txt') as f:
        for line in f:
            p1decider.process(line.strip())

    print("The number of valid words be:", p1decider.num_good_words)


if __name__ == "__main__":
    main()
