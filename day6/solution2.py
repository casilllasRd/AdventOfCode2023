def solution() -> None:
    race_data: list[str] = get_puzzle_data()
    answer: int = get_number_of_ways_to_beat_record(race_data)

    print(answer)


def get_puzzle_data() -> list[str]:
    file: str = "day6/puzzle-input.txt"
    puzzle_input = open(file).read()
    puzzle_data = puzzle_input.split("\n")

    return puzzle_data


def get_time_and_distance(race_data: list[str]) -> tuple[int, int]:
    time_row, distance_row = race_data
    race_time: int = get_row_entry(time_row)
    record_distance: int = get_row_entry(distance_row)

    return race_time, record_distance


def get_row_entry(row: str) -> int:
    row_digits: list[str] = [char for char in row.split(":")[1].split()]
    return int("".join(row_digits))


def get_number_of_ways_to_beat_record(race_data: list[str]) -> int:
    race_time, record_distance = get_time_and_distance(race_data)
    beats_record: int = 0

    for sec in range(1, race_time + 1):
        speed: int = sec
        time_left: int = race_time - sec
        possible_distance: int = speed * time_left

        if possible_distance > record_distance: beats_record += 1

    return beats_record


solution()