from PowerGrid import PowerGrid
import numpy as np


class PowerGrid1(PowerGrid):
    def turn_on(self, light: list) -> None:
        self._grid[light[0]][light[1]] = 1

    def turn_off(self, light: list) -> None:
        self._grid[light[0]][light[1]] = 0

    def toggle(self, light: list) -> None:
        self._grid[light[0]][light[1]] = (self._grid[light[0]][light[1]] + 1) % 2


def main():
    grid = PowerGrid1()
    with open('input.txt') as f:
        for line in f:
            grid.process(line)

    print("We have this many lights on:", np.count_nonzero(grid.grid == 1))


if __name__ == "__main__":
    main()
