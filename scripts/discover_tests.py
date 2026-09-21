import re
import sys
from pathlib import Path

# Match TEST, TEST_F, TEST_P
TEST_PATTERN = re.compile(
    r"^\s*TEST(?:_F|_P)?\s*\(\s*([a-zA-Z0-9_]+)\s*,\s*([a-zA-Z0-9_]+)\s*\)"
)


def scan_tests(tests_dir):
    tests_path = Path(tests_dir)

    for cpp_file in tests_path.glob("*.cpp"):
        with open(cpp_file, "r", encoding="utf-8") as f:
            line_number = 0
            for line in f:
                line_number += 1
                match = TEST_PATTERN.match(line)
                if match:
                    suite, name = match.groups()
                    # Output line format: filename.cpp:Suite.TestName:Line
                    print(f"{cpp_file.name}:{suite}.{name}:{line_number}")


if __name__ == "__main__":
    tests_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    scan_tests(tests_dir)