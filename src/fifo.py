# import queue


from typing import Generator
from process import Process


class Queue:
    def __init__(self, data: list[Process] = list()) -> None:
        self.__i = 0
        if all(type(obj) == Process for obj in data):
            self.__data: list[Process] = data
        else:
            raise ValueError

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

    # def __str__(self) -> str:
    #     pass

    def pop(self) -> Process:
        return self.__data.pop()

    def add(self, process: Process) -> None:
        if isinstance(process, Process):
            self.__data.insert(0, process)
        else:
            raise ValueError

    # next = __next__  # python 2.x


if __name__ == "__main__":
    # tests

    q = Queue()
    del q

    q = Queue([Process(i) for i in range(1, 5)])
    print(*q)
    q.add(Process(3))
    print(*q)
    print(q.pop())
    print(*q)
