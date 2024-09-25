from numbers import Number


class Process:
    # __processes: set['Process'] = set()

    def __init__(self, PID: int, priority: int = 20) -> None:
        self.pid: int = PID
        self.priority: int = priority
        # self.user: str = user
        # self.cmd: str = cmd
        # self.parent: int = ppid
        # self.status: Status = ...

    def __hash__(self) -> int:
        return ...

    def __str__(self) -> str:
        return str(self.pid)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Process):
            return self.pid == __value.pid
        if isinstance(__value, Number):
            return self.pid == __value
        raise NotImplementedError

    def __gt__(self, __value: object) -> bool:
        if isinstance(__value, Process):
            return self.priority < __value.priority
        if isinstance(__value, Number):
            return self.priority < __value
        raise NotImplementedError

    def __ge__(self, __value: object) -> bool:
        if isinstance(__value, Process):
            return self.priority <= __value.priority
        if isinstance(__value, Number):
            return self.priority <= __value
        raise NotImplementedError

    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, Process):
            return self.priority > __value.priority
        if isinstance(__value, Number):
            return self.priority > __value
        raise NotImplementedError

    def __le__(self, __value: object) -> bool:
        if isinstance(__value, Process):
            return self.priority >= __value.priority
        if isinstance(__value, Number):
            return self.priority >= __value
        raise NotImplementedError

    @property
    def pid(self) -> int:
        """A positive Integer"""  # 0 is not positive
        return self.__pid

    @pid.setter
    def pid(self, __value: int):
        if not isinstance(__value, int):
            raise ValueError("'pid' must be a integer")
        if __value > 0:
            self.__pid = __value
        else:
            raise ValueError("'pid' must be greater then zero")

    @property
    def priority(self) -> int:
        """A Integer between -1 and 140"""
        return self.__priority

    @priority.setter
    def priority(self, __value: int):
        if not isinstance(__value, int):
            raise ValueError("'priority' must be a integer")
        if 140 > __value > -1:
            self.__priority = __value
        else:
            raise ValueError("'priority' must be between -1 and 140")

    # @staticmethod
    # def processes():
    #     return Process.__processes
