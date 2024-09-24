from process import Process


class Queue:
    def __init__(self, data: list[Process] = list()) -> None:
        self.__i = 0
        if all(type(obj) == Process for obj in data):
            self.__data: list[Process] = data
        else:
            raise ValueError

    def __getitem__(self, __i: int) -> Process:  # queue[2]
        return self.__data[__i]

    def __iter__(self):  # e.g.: print(*queue); for o in queue: print(o): ...
        # for value in self.__data:
        #     yield value
        return iter(self.__data)
    
    def pop(self) -> Process:
        return self.__data.pop()

    def add(self, process: Process | int) -> None:
        if isinstance(process, Process):
            self.__data.insert(0, process)
        if isinstance(process, int):
            self.__data.insert(0, Process(process))
        else:
            raise ValueError
