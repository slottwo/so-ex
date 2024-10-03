from process import Process
from typing import Iterable


class Heap:
    def __init__(self, data: Iterable[Process | int | Iterable[int]] = None) -> None:
        self.__data: list[Process] = list()
        if data:
            if isinstance(data, Iterable):
                for _ in data:
                    self.add(_)
            else:
                raise ValueError

    def add(self, process: Process | int | Iterable[int]) -> None:
        match type(process):
            case int():
                process = Process(process)
            case Iterable():
                process = Process(*process)
            case _:
                raise ValueError

        # self.__data.add(process)

    def __update(self):
        ...

    def __up(self):
        ...

    def __down(self):
        ...
