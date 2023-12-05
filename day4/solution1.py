def solution() -> None:
    scratch_card_data: list[str] = get_puzzle_data()
    answer: int = get_scratch_card_total(scratch_card_data)

    print(answer)


def get_puzzle_data() -> list[str]:
    file: str = "day4/puzzle-input.txt"
    puzzle_input = open(file).read()
    puzzle_data: list[str] = puzzle_input.split("\n")

    return puzzle_data


def get_scratch_card_total(scratch_card_data: list[str]) -> int:
    scratch_card_total: int = 0

    for card in scratch_card_data:
        winners, card_reveals = card.split(":")[1].split("|")
        
        winners = winners.split()
        card_reveals = card_reveals.split()

        matches: int = len([match for match in winners if match in card_reveals])
        points: int = 2 ** (matches - 1) if matches else 0

        scratch_card_total += points

    return scratch_card_total
        

solution()