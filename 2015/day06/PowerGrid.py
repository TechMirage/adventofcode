import numpy as np
from abc import ABC, abstractmethod


class PowerGrid(ABC):
    def __init__(self):
        self._grid = np.zeros((1000, 1000), dtype=np.int)

    @property
    def grid(self):
        return self._grid

    @staticmethod
    def parse_text(line: str) -> (str, list, list):
        tmp = line.split(' ')
        if tmp[0] == 'turn':
            tmp.pop(0)
        command = tmp.pop(0)
        start = tmp.pop(0)
        end = tmp[-1]
        start = start.split(',')
        start = [int(start[0]), int(start[1])]
        end = end.split(',')
        end = [int(end[0]), int(end[1])]
        return command, start, end

    def process(self, line: str):
        cmd, start, end = self.parse_text(line.strip())
        list_of_lights = self.find_lights(start, end)
        for light in list_of_lights:
            if cmd == "on":
                self.turn_on(light)
            elif cmd == "off":
                self.turn_off(light)
            else:
                self.toggle(light)

    @staticmethod
    def find_lights(start: list, end: list) -> list:
        output = []
        for x in range(start[0], end[0]):
            for y in range(start[1], end[1]):
                output.append([x, y])
        return output

    @abstractmethod
    def turn_on(self, light: list) -> None:
        raise NotImplementedError

    @abstractmethod
    def turn_off(self, light: list) -> None:
        raise NotImplementedError

    @abstractmethod
    def toggle(self, light: list) -> None:
        raise NotImplementedError
