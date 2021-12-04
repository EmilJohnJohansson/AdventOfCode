PUZZLE_INPUT_PATH = ".\puzzleInput.txt"

def run():
    orders = parse_input()
    sub1 = Submarine()
    sub2 = Submarine()
    for order in orders:
        sub1.apply_order(order)
        sub2.apply_new_order(order)
    print(sub1.get_multiplied_position())
    print(sub2.get_multiplied_position())

class Submarine:
    def __init__(self):
        self.aim = 0
        self.depth = 0
        self.distance = 0

    def apply_order(self, order):
        if order.direction in ['u']:
            self.depth = self.depth - order.magnitude
        elif order.direction in ['d']:
            self.depth = self.depth + order.magnitude
        elif order.direction in ['f']:
            self.distance = self.distance + order.magnitude

    def apply_new_order(self, order):
        if order.direction in ['d']:
            self.aim = self.aim + order.magnitude
        elif order.direction in ['u']:
            self.aim = self.aim - order.magnitude
        elif order.direction in ['f']:
            self.distance = self.distance + order.magnitude
            self.depth = self.depth + self.aim * order.magnitude

    def get_multiplied_position(self):
        return self.depth * self.distance

class Order:
    def __init__(self, order):
        order_split = order.split()
        self.direction = order_split[0][0]
        self.magnitude = int(order_split[1])

def parse_input():
    return [Order(i) for i in get_input()]

def get_input():
    with open(PUZZLE_INPUT_PATH) as f:
        return f.readlines()

if __name__ == "__main__":
    run()
