def solution() -> None:
    puzzle_input = open("puzzle-input.txt")
    puzzle_data: str = puzzle_input.read()
    puzzle_list: list[str] = puzzle_data.split("\n")

    print(get_calibration_sum(puzzle_list))


def get_calibration_sum(puzzle_list: list[str]) -> int:
    digits: dict[str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }
    calibration_values: list[int] = []

    for line in puzzle_list:
        first_cv: int = 0
        last_cv: int = 0

        if line[0].isdigit(): first_cv = line[0]
        if line[-1].isdigit(): last_cv = line[-1]

        for i in range(len(line)):
            for written_digit, numerical_digit in digits.items():
                if first_cv == 0 and line.startswith(written_digit, i):
                    first_cv = numerical_digit
                if line.startswith(written_digit, i):
                    last_cv = numerical_digit
                
            if line[i].isdigit():
                if first_cv == 0:
                    first_cv = line[i]
                last_cv = line[i]
        calibration_values.append(int("".join([first_cv, last_cv])))
        
    return(sum(calibration_values))

solution()