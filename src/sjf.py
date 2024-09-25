from numbers import Number
from typing import Iterable, Union
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
        self.__data: set[TimedProcess]
        if not data:
            self.__data = set()
        elif all(isinstance(obj, [Number, Process, TimedProcess]) for obj in data):
            self.__data: set[TimedProcess] = set(map(TimedProcess, data))
        else:
            raise ValueError

    def __init_subclass__(cls) -> None:
        pass

    def pop(self) -> TimedProcess:
        process = min(self.__data)
        self.__data.discard(process)
        return process

    # def add(self, process: Process | int) -> None:  # python 3.10
    def add(self, process: Union[Process, int]) -> None:
        if isinstance(process, Process):
            process = TimedProcess(Process)
        if isinstance(process, int):
            process = TimedProcess(process)
        elif not isinstance(process, TimedProcess):
            raise ValueError

        self.__data.insert(0, process)

    def run(self):
        yield self.pop()
