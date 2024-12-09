from importlib import import_module
from pathlib import Path
from inspect import isfunction
import argparse


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
        return sorted(puzzles)

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


class Puzzle(object):
    def __init__(self, puzzle_path: Path):
        self.path = puzzle_path
        puzzle_package_name = f"{puzzle_path.parts[-2]}.{puzzle_path.stem}"
        self.mod = import_module(puzzle_package_name)
        self.day = int(puzzle_path.stem.split('-')[-1])
        self.year = puzzle_path.parent.name

    def _run(self, data_file_name: Path, part_func_name: str, step_name: str):
        result = {'success': True, 'answer': None, 'message': ''}
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

    def run_all(self):
        results = dict()

        results["Test 1"] = self.run_part_1_test()
        print("Test 1:", results["Test 1"]["answer"], results["Test 1"]["message"])

        if results["Test 1"]["success"]:
            results["Part 1"] = self.run_part_1()
            print("Part 1:", results["Part 1"]["answer"], results["Part 1"]["message"])

        if "Part 1" in results and results["Part 1"]["success"]:
            results["Test 2"] = self.run_part_2_test()
            print("Test 2:", results["Test 2"]["answer"], results["Test 2"]["message"])

        if "Test 2" in results and results["Test 2"]["success"]:
            results["Part 2"] = self.run_part_2()
            print("Part 2:", results["Part 2"]["answer"], results["Part 2"]["message"])

        return results


def run_puzzle(puzzle_path: Path):
    puzzle = Puzzle(puzzle_path)
    print("Year:", puzzle.year, "Day:", puzzle.day)
    puzzle.run_all()


def run_last_puzzle():
    repo = PuzzleRepo.create_instance()
    run_puzzle(repo.last_puzzle())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", type=str, help="Year")
    parser.add_argument("-d", "--day", type=str, help="Day")
    parser.add_argument("-q", "--query", help="Ask for remaining params", action="store_true")
    args = parser.parse_args()

    repo = PuzzleRepo.create_instance()
    if args.year and args.day:
        run_puzzle(repo.puzzle(args.year, args.day))
    elif not args.year and args.day:
        run_puzzle(repo.puzzle(repo.last_year, args.day))
    elif args.year and not args.day:
        if args.query:
            day = input("Which day?\n> ")
            if day.isnumeric():
                run_puzzle(repo.puzzle(args.year, day))
            else:
                print(f"Invalid input: {day} is not a number.")
        else:
            run_puzzle(repo.last_puzzle_for_year(args.year))
    else:
        if args.query:
            year = input("Which year?\n> ")
            day = input("Which day?\n> ")
            if day.isnumeric() and year.isnumeric():
                run_puzzle(repo.puzzle(year, day))
            else:
                print(f"Invalid input: {day} or {year} is not a number.")
        else:
            run_last_puzzle()
