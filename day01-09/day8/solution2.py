def main() -> None:
    FILE = "day8/puzzle-input.txt"
    answer: int = solution(FILE)

    print(answer)


def solution(file_name: str) -> int:
    instruction_data: list[str] = get_puzzle_data(file_name)
    instructions, nodes = get_instructions_and_nodes(instruction_data)
    steps: int = get_number_steps_required(instructions, nodes)

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


def get_number_steps_required(instructions: str, nodes: dict[str, tuple[str, str]]) -> int:
    current_nodes = [node for node in nodes if node[-1] == "A"]
    num_starting = len(current_nodes)
    print(F"Starting Nodes {current_nodes}")
    print(F"Starting Length: {num_starting}")
    found_all_Zs = False
    steps = 0

    while not found_all_Zs:
        
        for instruction in instructions:
            steps += 1
            Zs = []

            for i, node in enumerate(current_nodes):
                if instruction == "L":
                    # print(current_nodes[i], nodes[node][0])
                    current_nodes[i] = nodes[node][0]
                elif instruction == "R":
                    # print(current_nodes[i], nodes[node][1])
                    current_nodes[i] = nodes[node][1]

                if current_nodes[i][-1] == "Z": Zs.append(current_nodes[i])

            print(F"Step: {steps}")
            print(F"Zs: {Zs}")
            print(F"current nodes: {current_nodes}")

            if len(Zs) == num_starting:
                found_all_Zs = True
                break
        
        # found_all_Zs = True

    return steps
            

main()