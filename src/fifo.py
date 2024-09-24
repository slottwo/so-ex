# import queue


from typing import Generator
from process import Process


class Queue:
    def __init__(self) -> None:
        self.__i = 0
        self.__data: list[Process] = list()

    def __getitem__(self, index: int) -> Process:
        return self.__data[index]

    def __iter__(self) -> Generator:
        for value in self.__data:
            yield value

    def __next__(self) -> Process:
        self.__i += 1
        try:
            return self[self.__i]
        except IndexError:
            self.__i = 0
            raise StopIteration

    def pop(self) -> Process:
        return self.__data.pop()

    def add(self) -> None:
        self.__data.insert(0)

    # next = __next__  # python 2.x

    ...


if __name__ == "__main__":
    # tests
    
