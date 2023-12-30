def main() -> None:
    data_file: str = "puzzle-input.txt"
    answer: int = solution(data_file)

    print(answer)


def solution(file_name: str) -> int:
    dish: list[str] = load_puzzle_data(file_name)
    total_rows: int = len(dish)
    total_columns: int = len(dish[0])
    dish_transposed: list[str] = transpose_data(dish, total_rows, total_columns)
    total_load: int = calculate_total_load(dish_transposed, total_rows)

    return total_load


def load_puzzle_data(file_name: str) -> list[str]:
    return open(file_name).read().split("\n")


def transpose_data(dish: list[str], total_rows: int, total_columns) -> list[str]:
    return ["".join([dish[row][col] for row in range(total_rows)]) for col in range(total_columns)]


def calculate_total_load(dish_transposed: list[str], total_rows) -> int:
    EMPTY_SPOT: str = "."
    SQUARE_STONE: str = "#"
    total_load: int = 0
    
    for column in dish_transposed:
        for row_index, element in enumerate(column):
            if element == EMPTY_SPOT or element == SQUARE_STONE: continue
            total_load += calculate_stone_load(column, total_rows, row_index, EMPTY_SPOT, SQUARE_STONE)

    return total_load


def calculate_stone_load(column: str, total_rows: int, row_index: int, empty_spot: str, square_stone: str) -> int:
    stone_load: int = total_rows - row_index
    elements_above: str = column[:row_index][::-1]

    for element in elements_above:
        if element == empty_spot: stone_load += 1
        elif element == square_stone: break
    
    return stone_load


main()