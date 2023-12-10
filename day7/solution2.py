def main() -> None:
    FILE: str = "day7/puzzle-input.txt"
    answer: int = solution(FILE)

    print(answer)


def solution(file_name: str) -> int:
    hand_data: list[str] = get_puzzle_data(file_name)
    hand_types: dict[str, list[tuple[str, int]]] = get_cards_grouped_by_hand_type(hand_data)
    ranked_cards, hands_dict = get_ranked_cards(hand_types)
    bid_sum: int = get_bid_sum(ranked_cards, hands_dict)

    return bid_sum


def get_puzzle_data(file_name: str) -> list[str]:
    puzzle_data: list[str] = open(file_name).read().split("\n")

    return puzzle_data


def get_cards_grouped_by_hand_type(hand_data: list[str]) -> dict[str, list[tuple[str, int]]]:
    hand_types: dict[str, list[tuple[str, int]]] = {
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
        possible_hands: list[str] = get_possible_hands_with_wild_cards(hand)
        hand_type: str = compare_hand_type(possible_hands)
        hand_types[hand_type].append((hand, int(bid)))

    return hand_types


def get_possible_hands_with_wild_cards(hand: str) -> list[str]:
    JACK: str = "J"

    if JACK not in hand:
        return [hand]
    
    possible_hands: list[str] = [hand]
    for card in hand:
        if card is not JACK:
            possible_hands.append(hand.replace(JACK, card))

    return list(set(possible_hands))


def compare_hand_type(possible_hands: list[str]) -> str:
    FIVE_OF_A_KIND: tuple[str, int] = "FIVE", 7
    FOUR_OF_A_KIND: tuple[str, int] = "FOUR", 6
    FULL_HOUSE: tuple[str, int] = "FULL HOUSE", 5
    THREE_OF_A_KIND: tuple[str, int] = "THREE", 4
    TWO_PAIR: tuple[str, int] = "TWO", 3
    ONE_PAIR: tuple[str, int] = "ONE", 2
    HIGH_PAIR: tuple[str, int] = "HIGH CARD", 1

    current_best_hand: tuple[str, int] = "", 0

    for hand in possible_hands:
        hand_counts: list[tuple[str, int]] = sorted(
            list(set([(card, hand.count(card)) for card in hand])), 
            key=lambda card: card[1],
            reverse=True
        )
        highest_card_count = hand_counts[0][1]

        if len(hand_counts) == 1:
               current_best_hand = FIVE_OF_A_KIND if current_best_hand[1] <= FIVE_OF_A_KIND[1] else current_best_hand 
            
        
        elif len(hand_counts) == 2:
            if highest_card_count == 4:
                current_best_hand = FOUR_OF_A_KIND if current_best_hand[1] <= FOUR_OF_A_KIND[1] else current_best_hand
            elif highest_card_count == 3:
                current_best_hand = FULL_HOUSE if current_best_hand[1] <= FULL_HOUSE[1] else current_best_hand
            
        elif len(hand_counts) == 3:
            if highest_card_count == 3:
                current_best_hand = THREE_OF_A_KIND if current_best_hand[1] <= THREE_OF_A_KIND[1] else current_best_hand
            elif highest_card_count == 2:
                current_best_hand = TWO_PAIR if current_best_hand[1] <= TWO_PAIR[1] else current_best_hand
            
        elif len(hand_counts) == 4:
            current_best_hand = ONE_PAIR if current_best_hand[1] <= ONE_PAIR[1] else current_best_hand

        elif len(hand_counts) == 5:
            current_best_hand = HIGH_PAIR if current_best_hand[1] <= HIGH_PAIR[1] else current_best_hand
        
    return current_best_hand[0]


def get_ranked_cards(hand_types: dict[list]) -> tuple[list[str], dict[int]]:
    order: dict[str, str] = {
        "A": "a",
        "K": "b",
        "Q": "c",
        "T": "d",
        "9": "e",
        "8": "f",
        "7": "g",
        "6": "h",
        "5": "i",
        "4": "j",
        "3": "k",
        "2": "l",
        "J": "m"
    }
    ranked_cards: list[str] = []
    hands_dict: dict[str, int] = {}

    for rank_group in hand_types.values():
        rank_sorted: list[str] = []
        for hand_bid in rank_group:
            hand, bid = hand_bid
            converted_card: str = "".join([order[char] for char in hand])
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