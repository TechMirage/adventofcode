class WrappingFactory():
    def __init__(self):
        self._total_wrapping_paper = 0
        self._total_ribbon = 0

    @property
    def total_wrapping_paper(self):
        return self._total_wrapping_paper

    @property
    def total_ribbon(self):
        return self._total_ribbon

    def process(self, line):
        dims = line.split('x')
        for idx in range(len(dims)):
            dims[idx] = int(dims[idx])
        self.calculate_wrapping_paper(dims)
        self.calculate_wrapping_ribbon(dims)

    def calculate_wrapping_paper(self, dims):
        tmp = []
        tmp.append(dims[0] * dims[1])
        tmp.append(dims[1] * dims[2])
        tmp.append(dims[0] * dims[2])
        tmp.sort()
        # Add the total surface area and then the extra
        for value in tmp:
            self._total_wrapping_paper += 2 * value
        self._total_wrapping_paper += tmp[0]

    def calculate_wrapping_ribbon(self, dims):
        dims.sort()
        self._total_ribbon += 2 * dims[0] + 2 * dims[1]
        self._total_ribbon += dims[0] * dims[1] * dims[2]


def main():
    factory = WrappingFactory()
    with open('input.txt') as f:
        for line in f:
            # We use the -1 to remove the line break, jsyk.
            factory.process(line[:-1])

    print("we have this many square feet of wrapping paper", factory.total_wrapping_paper)
    print("we have this many feet of ribbon", factory.total_ribbon)


if __name__ == "__main__":
    main()
