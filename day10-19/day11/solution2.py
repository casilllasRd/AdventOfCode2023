def main() -> None:
    FILE: str = "day10-19/day11/puzzle-input.txt"
    answer: int = solution(FILE)

    print(answer)


def solution(file_name: str) -> int:
    space_data: list[str] = load_puzzle_data(file_name)

    galaxy_coords: dict[int, list[int]] = get_galaxy_coords(space_data)
    empty_rows, empty_cols = get_empty_rows_and_cols(space_data)

    expansion_factor: int = 1_000_000
    expanded_galaxy_coords: dict[int, list[int]] = get_expanded_coords(expansion_factor, galaxy_coords, empty_rows, empty_cols)

    galaxy_pairs: list[tuple[int, int]] = get_galaxy_pairs(len(expanded_galaxy_coords))
    galaxy_dist_sum: int = get_galaxy_dist_sum(expanded_galaxy_coords, galaxy_pairs)

    return galaxy_dist_sum


def load_puzzle_data(file_name: str) -> list[str]:
    puzzle_data: list[str] = open(file_name).read().split("\n")
    return puzzle_data


def get_empty_rows_and_cols(space_data: list[str]) -> tuple[list[int], list[int]]:
    EMPTY_SPACE_CHAR: str = "."

    empty_rows: list[int] = []
    for row_index, row in enumerate(space_data):
        row_empty: bool = (len(set(row)) == 1) and (EMPTY_SPACE_CHAR in set(row))
        if row_empty:
            empty_rows.append(row_index)

    empty_cols: list[int] = []
    for col_index in range(len(space_data[0])):
        column: list[str] = [space_data[i][col_index] for i in range(len(space_data))]
        column_empty: bool = (len(set(column)) == 1) and (EMPTY_SPACE_CHAR in set(column))
        if column_empty:
            empty_cols.append(col_index)

    return empty_rows, empty_cols


def get_galaxy_coords(space_data: list[str]) -> dict[int, list[int]]:
    GALAXY_CHAR: str = "#"

    galaxy_coords: dict[int, list[int]] = {}
    galaxy_count: int = 0
    for y_pos, row in enumerate(space_data):
        for x_pos, cell in enumerate(row):
            if cell == GALAXY_CHAR:
                galaxy_count += 1
                galaxy_coords[galaxy_count] = [y_pos, x_pos]

    return galaxy_coords


def get_expanded_coords(expansion_factor: int, galaxy_coords: dict[int, list[int]], empty_rows: list[int], empty_cols: list[int]) -> dict[int, list[int]]:
    for galaxy, coord in galaxy_coords.items():
        galaxy_row, galaxy_col = coord

        for empty_row in empty_rows:
            if empty_row < galaxy_row:
                galaxy_coords[galaxy][0] += (expansion_factor - 1)
        
        for empty_col in empty_cols:
            if empty_col < galaxy_col:
                galaxy_coords[galaxy][1] += (expansion_factor - 1)

    return galaxy_coords


def get_galaxy_pairs(galaxies_num: int) -> list[tuple[int, int]]:
    galaxy_pairs: list[tuple[int, int]] = []

    for i in range(1, galaxies_num + 1):
        for j in range(1, galaxies_num + 1):
            if i != j:
                pair: tuple[int, int] = min(i, j), max(i, j)
                galaxy_pairs.append(pair)

    unique_pairs: list[tuple[int, int]] = list(set(galaxy_pairs))
    return unique_pairs


def get_galaxy_dist_sum(galaxy_coords: dict[int, list[int]], galaxy_pairs: list[tuple[int, int]]) -> int:
    galaxy_dist_sum: int = 0

    for pair in galaxy_pairs:
        galaxy1, galaxy2 = pair
        y1, x1 = galaxy_coords[galaxy1]
        y2, x2 = galaxy_coords[galaxy2]
        galaxy_dist_sum += get_galaxy_dist(x1, y1, x2, y2)

    return galaxy_dist_sum


def get_galaxy_dist(x1: int, y1: int, x2: int, y2: int) -> int:
    distance: int = abs(x2 - x1) + abs(y2 - y1)
    return distance


main()