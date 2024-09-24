class Process:
    def __init__(self, PID: int, priority: int = 20) -> None:
        self.pid: int = PID
        self.priority: int = priority
        # self.user: str = user
        # self.cmd: str = cmd
        # self.parent: int = ppid
        # self.status: Status = ...

        # from random import randint
        # self.clk = randint(1, 1e5)

    @property
    def pid(self) -> int:
        return self.__pid

    @pid.setter
    def pid(self, value: int):
        if value > 0:
            self.__pid = int(value)
        else:
            raise ValueError("attribute 'pid' value must be greater then zero.")

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, value: int):
        if not isinstance(value, int):
            raise ValueError("")
        elif 140 > value > -1:
            self.__priority = int(value)
        else:
            raise ValueError("attribute 'priority' value must be between -1 and 140.")
