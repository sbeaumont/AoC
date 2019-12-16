from math import ceil


class Reaction(object):
    def __init__(self, name, output_amount, reactions):
        self.name = name
        self.in_stock = 0
        self.output_amount = output_amount
        self.preq = dict()
        self.reactions = reactions

    def add_input(self, chem, amount):
        self.preq[chem] = amount

    def deliver(self, amount):
        if self.in_stock < amount:
            self.produce(amount - self.in_stock)
        self.in_stock -= amount
        assert self.in_stock >= 0
        # print(f"{self.name} delivered {amount} (in stock {self.in_stock})")
        return amount

    def produce(self, amount_to_produce):
        production_runs_needed = int(ceil(amount_to_produce / self.output_amount))
        for chem, amount_per_unit in self.preq.items():
            self.reactions[chem].deliver(production_runs_needed * amount_per_unit)
        self.in_stock += production_runs_needed * self.output_amount

    def __repr__(self):
        preqs = ','.join([f"{n}:{a}" for n, a in self.preq.items()])
        return f"Reaction({self.name}, {self.output_amount}, {self.in_stock} ({preqs}))"


class InfiniteSource(Reaction):
    def __init__(self, name):
        super().__init__(name, 1, None)
        self.delivered = 0
        self.in_stock = 'Infinite'

    def add_input(self, chem, amount):
        raise Exception("Should not call this on a source")

    def deliver(self, amount):
        self.delivered += amount
        # print(f"{self.name} delivered {amount}")
        return amount

    def produce(self, amount_to_produce):
        pass


def load_test(test_nr):
    with open(f"AoC-2019-test-14-{test_nr}.txt") as testfile:
        data = [line.strip() for line in testfile.readlines()]
        expected_result = int(data[-1].split(' ')[-1])
        return data[:-1], expected_result


def parse_data(data):
    reactions = dict()
    reactions['ORE'] = InfiniteSource('ORE')
    for line in data:
        inputs, output = line.split('=>')
        output_amount, name = output.strip().split(' ')
        reaction = Reaction(name, int(output_amount), reactions)
        reactions[reaction.name] = reaction
        for chem in inputs.strip().split(','):
            in_amount, in_name = chem.strip().split(' ')
            reaction.add_input(in_name, int(in_amount))
    return reactions


def do(data, amount_to_deliver=1):
    reactions = parse_data(data)
    reactions['FUEL'].deliver(amount_to_deliver)
    return reactions['ORE'].delivered


def test(nr):
    test_data, expected_result = load_test(nr)
    test_result = do(test_data)
    assert test_result == expected_result, f"Test {nr}: expected {expected_result}, got {test_result}."


def load_input():
    with open(f"AoC-2019-input-14.txt") as infile:
        return [line.strip() for line in infile.readlines()]


if __name__ == '__main__':
    for i in range(1, 6):
        test(i)

    result = do(load_input())
    print("Part 1:", result)
    assert result == 378929

    total_ore = 1000000000000
    ore_consumed = 0
    fuel_to_produce = 3445249
    while ore_consumed < total_ore:
        ore_consumed = do(load_input(), fuel_to_produce)
        print(f"Producing {fuel_to_produce} consumed {ore_consumed} ore.")
        fuel_to_produce += 1
    print("Part 2 was discovered by manually manipulating fuel_to_produce and its increments.")
    print("Part 2: 3445249")



