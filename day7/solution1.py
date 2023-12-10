def main() -> None:
    FILE: str = "day7/puzzle-input.txt"
    print(solution(FILE))


def solution(file_name: str) -> int:
    hand_data: list[str] = get_puzzle_data(file_name)
    hand_types: dict[list] = get_cards_grouped_by_hand_type(hand_data)
    ranked_cards, hands_dict = get_ranked_cards(hand_types)
    bid_sum: int = get_bid_sum(ranked_cards, hands_dict)

    return bid_sum


def get_puzzle_data(file_name) -> list[str]:
    puzzle_data = open(file_name).read().split("\n")

    return puzzle_data


def get_cards_grouped_by_hand_type(hand_data: list[str]) -> dict[list]:
    hand_types: dict[str, list] = {
        "FIVE": [],
        "FOUR": [],
        "FULL HOUSE": [],
        "THREE": [],
        "TWO": [],
        "ONE": [],
        "HIGH CARD": []
    }

    for hand_bid in hand_data:
        hand, bid = hand_bid.split()
        hand_type: str = compare_hand_type(hand)
        hand_types[hand_type].append([hand, int(bid)])

    return hand_types


def compare_hand_type(hand: str) -> str:
    FIVE_OF_A_KIND: str = "FIVE"
    FOUR_OF_A_KIND: str = "FOUR"
    FULL_HOUSE: str = "FULL HOUSE"
    THREE_OF_A_KIND: str = "THREE"
    TWO_PAIR: str = "TWO"
    ONE_PAIR: str =  "ONE"
    HIGH_CARD: str = "HIGH CARD"
    hand_counts: list[tuple[str, int]]= list(set([(h, hand.count(h)) for h in hand]))
    
    if len(hand_counts) == 1:
        return FIVE_OF_A_KIND
    elif len(hand_counts) == 2: 
        first_card_count = hand_counts[0][1]
        if first_card_count == 1 or first_card_count == 4:
            return FOUR_OF_A_KIND
        elif first_card_count == 2 or first_card_count == 3:
            return FULL_HOUSE
    elif len(hand_counts) == 3:
        set_of_counts: set[int] = set([hand_counts[0][1], hand_counts[1][1], hand_counts[2][1]])
        THREE_OF_A_KIND_SET: set[int] = set([1, 3])
        TWO_PAIR_SET: set[int] = set([1, 2])
        if set_of_counts == THREE_OF_A_KIND_SET:
            return THREE_OF_A_KIND
        elif set_of_counts == TWO_PAIR_SET:
            return TWO_PAIR
    elif len(hand_counts) == 4:
        return ONE_PAIR
    elif len(hand_counts) == 5:
        return HIGH_CARD


def get_ranked_cards(hand_types: dict[list]) -> tuple[list[str], dict[int]]:
    order: dict[str, int] = {
        "A": "a",
        "K": "b",
        "Q": "c",
        "J": "d",
        "T": "e",
        "9": "f",
        "8": "g",
        "7": "h",
        "6": "i",
        "5": "j",
        "4": "k",
        "3": "l",
        "2": "m"
    }
    ranked_cards: list[str] = []
    hands_dict: dict[str, int] = {}

    for rank_group in hand_types.values():
        rank_sorted: list = []
        for hand_bid in rank_group:
            hand, bid = hand_bid
            converted_card = "".join([order[char] for char in hand])
            rank_sorted.append(converted_card)
            hands_dict[converted_card] = bid
        ranked_cards += sorted(rank_sorted)

    return ranked_cards, hands_dict


def get_bid_sum(ranked_cards: list[str], hands_dict: dict[str, int]) -> int:
    bid_sum: int = 0
    ranks = len(ranked_cards)

    for rank_index, hand in enumerate(ranked_cards):
        bid_sum += (hands_dict[hand] * (ranks - rank_index))

    return bid_sum


main()