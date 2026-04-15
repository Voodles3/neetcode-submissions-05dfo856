class MinStack:

    def __init__(self):
        self.stack = []
        self._min = float("inf")
        self._min_history = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self._min:
            self._min_history.append(self._min)
            self._min = val

    def pop(self) -> None:
        if self.stack.pop() is self._min:
            self._min = self._min_history.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min
