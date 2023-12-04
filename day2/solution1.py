def solution() -> None:
    puzzle_input = open("puzzle-input.txt")
    puzzle_data: str = puzzle_input.read()
    puzzle_list: list[str] = puzzle_data.split("\n")
    answer: int = get_calibration_sum(puzzle_list)

    print(answer)

def get_calibration_value(word: str) -> int:
    digit_list: list[str] = [char for char in word if char.isdigit()]
    first_and_last: list[str] = [digit_list[0], digit_list[-1]]
    calibration_value: str = "".join(first_and_last)

    return int(calibration_value)

def get_calibration_sum(puzzle_list: list[str]) -> int:
    calibration_values: list[int] = [get_calibration_value(word) for word in puzzle_list]

    return sum(calibration_values)

solution()