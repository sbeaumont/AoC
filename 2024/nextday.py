import shutil
import os

print(os.listdir("."))
max_puzzle_number = max([int(filename.split('.')[0].split('-')[2]) for filename in os.listdir(".") if filename.startswith('AoC')])
next_puzzle_number = max_puzzle_number + 1

shutil.copy("AoC-2024-0.py", f"AoC-2024-{next_puzzle_number}.py")
shutil.copy("AoC-2024-0-input.txt", f"AoC-2024-{next_puzzle_number}-input.txt")
shutil.copy("AoC-2024-0-test-input.txt", f"AoC-2024-{next_puzzle_number}-test-input.txt")