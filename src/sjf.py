from typing import Iterable
from process import Process


class TimedProcess(Process):
    def __init__(self, PID: int, priority: int = 20, time=None) -> None:
        super().__init__(PID, priority)

        if time == None:
            from random import randint
            self.time = randint(10000)
        else:
            self.time = time

    @property
    def time(self) -> int:
        """Number of clocks. 0 is infinity"""
        return self.__clk

    @time.setter
    def time(self, __value: int):
        if not isinstance(__value, int):
            raise ValueError("'clk' must be a integer")
        if __value > 0:
            self.__clk = __value
        else:
            raise ValueError("'clk' must be non-negative")

    def __gt__(self, __value: object) -> bool:
        if isinstance(__value, TimedProcess):
            if self.time == __value.time:
                return super().__gt__(__value)
            return self.time < __value.time
        raise NotImplementedError

    def __ge__(self, __value: object) -> bool:
        if isinstance(__value, TimedProcess):
            return self.time <= __value.time
        raise NotImplementedError

    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, TimedProcess):
            return self.time > __value.time
        raise NotImplementedError

    def __le__(self, __value: object) -> bool:
        if isinstance(__value, TimedProcess):
            return self.time >= __value.time
        raise NotImplementedError


class SJF:
    def __init__(self, data: Iterable[TimedProcess] = None) -> None:
        self.__i = 0
        if not data:
            self.__data = set()
        if all(type(obj) == TimedProcess for obj in data):
            self.__data: set[TimedProcess] = set(data)
        else:
            raise ValueError

    def pop(self) -> Process:
        process = min(self.__data)
        self.__data.discard(process)
        return process
