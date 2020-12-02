import re

class PasswordChecker():
    RE_MATCH = r"(\d+)-(\d+) ([a-z]): ([a-z]+)"
    def __init__(self):
        self.valid_passwords = 0

    def __call__(self, db_line: str):
        lower, upper, target, phrase = self.decode_db(db_line)
        valid = self.contains_target(lower, upper, target, phrase)
        if valid:
            self.valid_passwords += 1
            return True
        return False

    def decode_db(self, db_line: str):
        x = re.search(self.RE_MATCH, db_line)
        lower_range = int(x.group(1))
        upper_range = int(x.group(2))
        target_letter = x.group(3)
        password = x.group(4)
        return lower_range, upper_range, target_letter, password

    def contains_target(self, x1: int, x2: int, target: str, phrase: str):
        first = False
        second = False
        if phrase[x1 - 1] == target:
            first = True
        if phrase[x2 - 1] == target:
            second = True
        return first != second

