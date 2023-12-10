def main() -> None:
    FILE: str = "day9/puzzle-input.txt"
    print(solution(FILE))


def solution(file_name: str) -> int:
    oasis_data: list[str] = get_puzzle_data(file_name)
    return get_extrapolation_value_sum(oasis_data)



def get_puzzle_data(file_name: str) -> list[str]:
    puzzle_data: list[str] = open(file_name).read().split("\n")
    
    return puzzle_data


def get_extrapolation_value_sum(oasis_data: list[str]) -> int:
    extratpolated_value_sum: int = 0

    for history in oasis_data:
        history_values: list[int] = [int(hv) for hv in history.split()]
        extrapolated_value: int = history_values[-1]

        while len(set(history_values)) != 1:
            current_layer: list[int] = []
            
            for index, history_value in enumerate(history_values):
                if index + 1 < len(history_values):
                    inner_difference: int = history_values[index + 1] - history_value
                    current_layer.append(inner_difference)
            
            extrapolated_value += current_layer[-1]
            history_values = current_layer

        extratpolated_value_sum += extrapolated_value

    return extratpolated_value_sum

main()