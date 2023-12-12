def main() -> None:
    FILE: str = "day8/puzzle-input.txt"
    answer: int = solution(FILE)

    print(answer)


def solution(file_name: str) -> int:
    instruction_data: list[str] = get_puzzle_data(file_name)
    instructions, nodes = get_instructions_and_nodes(instruction_data)
    steps: int = get_number_of_steps_required(instructions, nodes)

    return steps


def get_puzzle_data(file_name: str) -> list[str]:
    puzzle_data: list[str] = open(file_name).read().split("\n")

    return puzzle_data


def get_instructions_and_nodes(instruction_data: list[str]) -> tuple[str, dict[str, tuple[str, str]]]:
    instructions: str = instruction_data[0]
    nodes: list[str] = instruction_data[2:]
    nodes_dict: dict[str, tuple[str, str]] = {}

    for node in nodes:
        location, options = node.split(" = ")
        options = options.replace("(", "").replace(")", "").split(", ")
        nodes_dict[location] = tuple(options)

    return instructions, nodes_dict


def get_number_of_steps_required(instructions: str, nodes: dict[str, tuple[str, str]]) -> int:
    current_location: str = "AAA"
    final_location: str = "ZZZ" 
    LEFT: str = "L"
    RIGHT: str = "R"
    found_final_location: bool = False
    steps: int = 0

    while not found_final_location:
        for instruction in instructions:
            steps += 1

            if instruction == LEFT:
                current_location = nodes[current_location][0]
            elif instruction == RIGHT:
                current_location = nodes[current_location][1]

            if current_location == final_location:
                found_final_location = True
                break
                
    return steps


main()