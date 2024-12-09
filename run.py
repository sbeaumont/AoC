import argparse
import sys
from importlib import import_module
from inspect import isfunction
from pathlib import Path


class PuzzleRepo(object):
    @staticmethod
    def create_instance():
        return PuzzleRepo(Path(__file__).parent)

    def __init__(self, root_dir):
        self.root = Path(root_dir).resolve()
        all_directories = [p for p in self.root.iterdir() if p.is_dir()]
        self.dirs = sorted([d for d in all_directories if d.name.isnumeric()])
        self.last_year_dir = self.dirs[-1]
        self.last_year = self.last_year_dir.stem

    def puzzles_for_dir(self, puzzle_dir: Path) -> list[Path]:
        puzzles = []
        for file in puzzle_dir.iterdir():
            if file.is_file() and file.suffix == '.py' and file.name.startswith(f"AoC-{puzzle_dir.name}-"):
                puzzles.append(file)
        return sorted(puzzles, key=lambda p: int(p.stem.split('-')[-1]))

    def puzzles_for_year(self, year: str) -> list[Path]:
        return self.puzzles_for_dir(self.root / year)

    def last_puzzle_for_year(self, year: str) -> Path:
        return self.puzzles_for_year(year)[-1]

    def last_puzzle(self) -> Path:
        return self.puzzles_for_dir(self.last_year_dir)[-1]

    def puzzle(self, year: str, day: str) -> Path | None:
        for puzzle in self.puzzles_for_year(year):
            if day == puzzle.stem.split('-')[-1]:
                return puzzle
        return None

    def tests_for_puzzle(self, puzzle_path: Path) -> list[Path]:
        tests = []
        p_year, p_day = puzzle_path.stem.split('-')[1:3]
        for file in puzzle_path.parent.iterdir():
            if file.is_file() and file.name.startswith(f"AoC-{p_year}-{p_day}-test"):
                tests.append(file)
        return tests

class Puzzle(object):
    def __init__(self, puzzle_path: Path):
        self.path = puzzle_path
        puzzle_package_name = f"{puzzle_path.parts[-2]}.{puzzle_path.stem}"
        self.mod = import_module(puzzle_package_name)
        self.day = int(puzzle_path.stem.split('-')[-1])
        self.year = puzzle_path.parent.name

    def _run(self, data_file_name: Path, part_func_name: str, step_name: str):
        result = {'success': True, 'answer': None, 'message': ''}

        if self.has_override(step_name):
            override = getattr(self.mod, "overrides")[step_name]
            if "data file" in override:
                data_file_name = data_file_name.with_name(override["data file"])

        if hasattr(self.mod, part_func_name) and isfunction(getattr(self.mod, part_func_name)):
            result['answer'] = getattr(self.mod, part_func_name)(self.mod.read_puzzle_data(data_file_name))
            if self.has_assertion(step_name) and (result['answer'] != self.mod.assertions[step_name]):
                result['message'] = f"Incorrect: expected {self.mod.assertions[step_name]}, got {result['answer']}"
                result['success'] = False
        else:
            result['success'] = False
            result['message'] = f"Puzzle {self.year} does not have {part_func_name} function."
        return result

    def has_assertion(self, name):
        return hasattr(self.mod, "assertions") and self.mod.assertions.get(name, None) is not None

    def has_override(self, name):
        return hasattr(self.mod, "overrides") and self.mod.overrides.get(name, None) is not None

    @property
    def test_file(self):
        return self.path.with_name(f"AoC-{self.year}-{self.day}-test-input.txt")

    @property
    def data_file(self):
        return self.path.with_name(f"AoC-{self.year}-{self.day}-input.txt")

    def run_part_1_test(self):
        return self._run(self.test_file, "part_1", "Test 1")

    def run_part_1(self):
        return self._run(self.data_file, "part_1", "Part 1")

    def run_part_2_test(self):
        return self._run(self.test_file, "part_2", "Test 2")

    def run_part_2(self):
        return self._run(self.data_file, "part_2", "Part 2")

    def run_all(self, run_steps: tuple):
        results = dict()
        keep_running = True

        if "T1" in run_steps:
            results["Test 1"] = self.run_part_1_test()
            keep_running = results["Test 1"]["success"]
            print("Test 1:", results["Test 1"]["answer"], results["Test 1"]["message"])

        if ("P1" in run_steps) and keep_running:
            results["Part 1"] = self.run_part_1()
            keep_running = results["Part 1"]["success"]
            print("Part 1:", results["Part 1"]["answer"], results["Part 1"]["message"])

        if ("T2" in run_steps) and keep_running:
            results["Test 2"] = self.run_part_2_test()
            keep_running = results["Test 2"]["success"]
            print("Test 2:", results["Test 2"]["answer"], results["Test 2"]["message"])

        if ("P2" in run_steps) and keep_running:
            results["Part 2"] = self.run_part_2()
            print("Part 2:", results["Part 2"]["answer"], results["Part 2"]["message"])

        return results


def run_puzzle(puzzle_path: Path, run_steps: tuple=None):
    puzzle = Puzzle(puzzle_path)
    if not run_steps:
        run_steps = ("T1", "P1", "T2", "P2")
    print("Year:", puzzle.year, "Day:", puzzle.day)
    print("Running steps", *run_steps)
    puzzle.run_all(run_steps)


def run_last_puzzle(run_steps: tuple=None):
    repo = PuzzleRepo.create_instance()
    run_puzzle(repo.last_puzzle(), run_steps)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", type=str, help="Year")
    parser.add_argument("-d", "--day", type=str, help="Day")
    parser.add_argument("-q", "--query", help="Ask for remaining params", action="store_true")
    parser.add_argument("-s", "--steps", nargs="+", help="Steps to run")
    args = parser.parse_args()

    steps = tuple(args.steps) if args.steps else tuple()

    for step in steps:
        if step not in ("T1", "P1", "T2", "P2"):
            sys.exit(f"Step {step} is not T1, P1, T2 or P2.")

    repo = PuzzleRepo.create_instance()
    if args.year and args.day:
        run_puzzle(repo.puzzle(args.year, args.day), steps)
    elif not args.year and args.day:
        run_puzzle(repo.puzzle(repo.last_year, args.day), steps)
    elif args.year and not args.day:
        if args.query:
            day = input("Which day?\n> ")
            if day.isnumeric():
                run_puzzle(repo.puzzle(args.year, day), steps)
            else:
                print(f"Invalid input: {day} is not a number.")
        else:
            run_puzzle(repo.last_puzzle_for_year(args.year), steps)
    else:
        if args.query:
            year = input("Which year?\n> ")
            day = input("Which day?\n> ")
            if day.isnumeric() and year.isnumeric():
                run_puzzle(repo.puzzle(year, day), steps)
            else:
                print(f"Invalid input: {day} or {year} is not a number.")
        else:
            run_last_puzzle(steps)
