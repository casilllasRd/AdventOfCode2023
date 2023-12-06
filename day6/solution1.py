import math

def solution() -> None:
    race_data: list[str] = get_puzzle_data()
    answer: int = get_record_margin_of_error(race_data)

    print(answer)


def get_puzzle_data() -> list[str]:
    file: str = "day6/puzzle-input.txt"
    puzzle_input = open(file).read()
    puzzle_data = puzzle_input.split("\n")

    return puzzle_data


def get_times_and_distances(race_data: list[str]) -> tuple[list[int], list[int]]:
    Ts, Ds = race_data
    race_times: list[int] = get_row_data(Ts)
    record_distances: list[int] = get_row_data(Ds)

    return race_times, record_distances


def get_row_data(row: str) -> list[int]:
    return [int(e) for e in row.split(":")[1].split()]


def get_record_margin_of_error(race_data: list[str]) -> int:
    race_times, record_distances = get_times_and_distances(race_data)
    beats_record: list[int] = [0 for d in record_distances]
    
    for race_num, time in enumerate(race_times):
        for sec in range(1, time + 1):
            speed: int = sec
            time_left: int = time - sec
            possible_distance: int = speed * time_left

            if possible_distance > record_distances[race_num]:
                beats_record[race_num] += 1

    return math.prod(beats_record)


solution()