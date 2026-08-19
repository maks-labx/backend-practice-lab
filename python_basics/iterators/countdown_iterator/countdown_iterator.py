class CountdownIterator:
    def __init__(self, start):
        if start < 0:
            raise ValueError("Start must be greater than or equal to 0")

        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration

        number = self.current
        self.current -= 1

        return number
