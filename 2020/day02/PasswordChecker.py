import re

class PasswordChecker():
    RE_MATCH = r"(\d*)-(\d*) (.): ([a-z]*)"
    def __init__(self):
        self.valid_passwords = 0

    def __call__(self, db_line: str):
        lower, upper, target, phrase = self.decode_db(db_line)
        occurrences = self.how_many_times(target, phrase)
        if lower <= occurrences <= upper:
            print(phrase, " is a valid password")
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

    def how_many_times(self, target: str, phrase: str):
        tmp = '%s' % phrase
        tmp = tmp.replace(target, "")
        occurence_number = len(phrase) - len(tmp)
        return occurence_number