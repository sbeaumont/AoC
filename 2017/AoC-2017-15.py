GENERATOR_A_START = 873
GENERATOR_A_FACTOR = 16807
GENERATOR_B_START = 583
GENERATOR_B_FACTOR = 48271

DIVISOR = 2147483647

PAIRS_TO_TRY = 40000000


def generator(start_value, factor):
    value = start_value
    while True:
        value = value * factor % DIVISOR
        yield value


gen_a = generator(GENERATOR_A_START, GENERATOR_A_FACTOR)
gen_b = generator(GENERATOR_B_START, GENERATOR_B_FACTOR)
matches = 0
for i in range(PAIRS_TO_TRY):
    gen_a_bits = bin(gen_a.next())[-16:]
    gen_b_bits = bin(gen_b.next())[-16:]
    if i % 100000 == 0:
        print(i)
    if gen_a_bits == gen_b_bits:
        matches += 1

print("I found {} matches in {} pairs.".format(matches, PAIRS_TO_TRY))