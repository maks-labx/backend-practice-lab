class Store:
    network = "StoreCheck"

    def __init__(self, name):
        self.name = name
        self.problems = []

    def add_problem(self, problem):
        self.problems.append(problem)

    def get_summary(self):
        return  f"{self.name}: {len(self.problems)} problems"

class PriorityStore(Store):
    def __init__(self, name, priority):
        super().__init__(name)
        self.priority = priority

    def get_summary(self):
        return super().get_summary() + f", priority: {self.priority}"

store1 = Store("A")
store2 = Store("B")
priority_store = PriorityStore("C", "HIGH")

store1.add_problem("Broken fridge")
store1.add_problem("Leaking roof")

store2.add_problem("Broken floor")

priority_store.add_problem("Power outage")

print(store1.get_summary())
print(store2.get_summary())
print(priority_store.get_summary())

