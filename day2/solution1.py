def solution() -> None:
    puzzle_input = open("puzzle-input.txt")
    puzzle_data: list[str] = puzzle_input.readlines()
    answer: int = get_valid_game_sum(puzzle_data)

    print(answer)


def get_valid_game_sum(puzzle_data: list[str]) -> int:
    game_params: dict[int] = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    valid_games_sum = 0

    for game in puzzle_data:
        game_label, reveals = game.split(":")

        if check_valid_game(reveals, game_params):
            game_number: int = get_digits_from_string(game_label)
            valid_games_sum += game_number
    
    return valid_games_sum
        

def check_valid_game(reveals: str, game_params: dict[int]) -> bool:
    reveals: list[str] = get_reveals(reveals)

    for reveal in reveals:
        cubes: int = get_digits_from_string(reveal)

        for color, max_cubes in game_params.items():
            if color in reveal and cubes > max_cubes:
                return False

    return True
        

def get_reveals(reveals: str) -> list[str]:
    return reveals.replace(";", ",").split(",")


def get_digits_from_string(s: str) -> int:
    digits: str = "".join([char for char in s if char.isdigit()])
    return int(digits)


solution()
