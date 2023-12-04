def solution() -> None: 
    puzzle_data: list[str] = get_puzzle_data()
    answer: int = get_power_sum(puzzle_data)

    print(answer)


def get_puzzle_data() -> list[str]:
    file: str = "puzzle-input.txt"
    puzzle_input = open(file)
    puzzle_data: list[str] = puzzle_input.readlines()

    return puzzle_data


def get_power_sum(puzzle_data: list[str]) -> int:
    powers: list[int] = []

    for game in puzzle_data:
        game_samples: dict[list] = {
            "red": [],
            "green": [],
            "blue": []
        }
        reveals: list[str] = get_reveals(game)

        for reveal in reveals:
            for color in game_samples.keys():
                if color in reveal:
                    cube_num: int = get_digits_from_string(reveal)
                    game_samples[color].append(cube_num)

        powers.append(get_power(game_samples))
    
    return sum(powers)


def get_reveals(game: str) -> list[str]:
    reveals: str = game.split(":")[1]
    return reveals.replace(";", ",").split(",")


def get_digits_from_string(s: str) -> int:
    digits: str = "".join([char for char in s if char.isdigit()])
    return int(digits)


def get_power(game_samples: dict[list]) -> int:
    power: int = 0
    for sample in game_samples.values():
        if power == 0: 
            power = max(sample)
        else: 
            power *= max(sample)

    return power


solution()