def main() -> None:
    FILE: str = "day9/puzzle-input.txt"
    print(solution(FILE))


def solution(file_name: str) -> int:
    oasis_data: list[str] = get_puzzle_data(file_name)
    answer: int = get_backward_extrapolation_sum(oasis_data)

    return answer


def get_puzzle_data(file_name) -> list[str]:
    puzzle_data: list[str] = open(file_name).read().split("\n")

    return puzzle_data


def get_backward_extrapolation_sum(oasis_data: list[str]) -> int:
    backward_extrapolation_sum: int = 0

    for history in oasis_data:
        history_values: list[int] = [int(hv) for hv in history.split()]
        extratpolated_value: int = history_values[0]
        alternator: int = -1

        while len(set(history_values)) != 1:
            current_layer: list[int] = []

            for index, history_value in enumerate(history_values):
                if index + 1 < len(history_values):
                    inner_difference = history_values[index + 1] - history_value
                    current_layer.append(inner_difference)

            extratpolated_value += current_layer[0] * alternator
            alternator *= -1
            history_values = current_layer
            
        backward_extrapolation_sum += extratpolated_value
    
    return backward_extrapolation_sum


main()