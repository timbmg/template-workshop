class Fibonacci:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        ##### YOUR CODE HERE #####
        if n <= 2:
            return 1
        return self.fib(n-1) + self.fib(n-2)
        ##########################
