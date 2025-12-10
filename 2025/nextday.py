import shutil
import os
import requests
import re

YEAR = 2025

max_puzzle_number = max([int(filename.split('.')[0].split('-')[2]) for filename in os.listdir(".") if filename.startswith('AoC')])
next_puzzle_number = max_puzzle_number + 1

print(f"Next Puzzle: {next_puzzle_number}")
if not os.path.exists(f"AoC-{YEAR}-{next_puzzle_number}.py"):
    shutil.copy(f"AoC-{YEAR}-0.py", f"AoC-{YEAR}-{next_puzzle_number}.py")
    print(f"Copied AoC-{YEAR}-{next_puzzle_number}.py")
else:
    print("Files for", f"AoC-{YEAR}-{next_puzzle_number}.py", "already exist!")

with open('../secret.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    cookie = {'session': lines[0]}

with open(f"AoC-{YEAR}-{next_puzzle_number}-input.txt", 'w') as f:
    r = requests.get(f'https://adventofcode.com/{YEAR}/day/{next_puzzle_number}/input', cookies=cookie)
    f.writelines(r.text)

print("Wrote", f"AoC-{YEAR}-{next_puzzle_number}-input.txt")

with open(f"AoC-{YEAR}-{next_puzzle_number}-test-input.txt", 'w') as f:
    r = requests.get(f'https://adventofcode.com/{YEAR}/day/{next_puzzle_number}')
    test_input = re.search(r'<pre><code>(.*)<\/code><\/pre>', r.text, re.DOTALL).group(1)
    f.writelines(test_input)

print("Wrote", f"AoC-{YEAR}-{next_puzzle_number}-test-input.txt")
