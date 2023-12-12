def solution() -> None:
    scratch_card_data: list[str] = get_puzzle_data()
    get_scratch_card_total(scratch_card_data)


def get_puzzle_data() -> list[str]:
    file: str = "day4/puzzle-input.txt"
    puzzle_input = open(file).read()
    puzzle_data: list[str] = puzzle_input.split("\n")

    return puzzle_data


def get_scratch_card_total(scratch_card_data: list[str]) -> int:
    scratch_cards: list[int] = [1 for scratch_card in scratch_card_data]
    
    for card_i, card in enumerate(scratch_card_data):
        winners, reveals = card.split(":")[1].split("|")

        winners = winners.split()
        reveals = reveals.split()

        matches: int = len([match for match in winners if match in reveals])
        if matches:
            for match_i in range(card_i + 1, card_i + matches + 1):
                scratch_cards[match_i] += scratch_cards[card_i]

    print(sum(scratch_cards))


solution()