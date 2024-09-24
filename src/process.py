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
        """A positive Integer"""  # 0 is not positive
        return self.__pid

    @pid.setter
    def pid(self, value: int):
        if not isinstance(value, int):
            raise ValueError("attribute 'pid' must be a integer")
        if value > 0:
            self.__pid = value
        else:
            raise ValueError("attribute 'pid' must be greater then zero.")

    @property
    def priority(self) -> int:
        """A Integer between -1 and 140"""
        return self.__priority

    @priority.setter
    def priority(self, value: int):
        if not isinstance(value, int):
            raise ValueError("attribute 'priority' must be a integer")
        if 140 > value > -1:
            self.__priority = value
        else:
            raise ValueError("attribute 'priority' must be between -1 and 140.")
