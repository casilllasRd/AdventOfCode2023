def main() -> None:
    puzzle_input_file: str = "puzzle-input.txt"
    answer: int = solution(puzzle_input_file)

    print(answer)


def solution(file_name: str) -> int:
    system_data: list[str] = load_puzzle_data(file_name)
    workflows, parts = parse_workflows_and_parts(system_data)
    accepted_part_rating_sum: int = calc_accepted_part_rating_sum(workflows, parts)

    return accepted_part_rating_sum


def load_puzzle_data(file_name: str) -> list[str]:
    puzzle_data: list[str] = open(file_name).read().split("\n")

    return puzzle_data


def parse_workflows_and_parts(system_data) -> tuple[dict[str, list[list[str]]], list[dict[str, str | int]]]:
    workflows: dict[str, list[list[str]]] = {}
    parts: list[dict[str, str | int]] = []

    for line in system_data:
        if line == "": continue

        if line[0].isalpha():
            workflow: list[str] = line.replace("}", "").split("{")
            workflow_name: str = workflow[0]
            workflow_steps: list[list[str]] = [step.split(":") for step in workflow[1].split(",")]
            workflows[workflow_name] = workflow_steps

        if line[0] == "{":
            INITIAL_WORKFLOW: str = "in"
            part: dict[str, str] = {"current workflow": INITIAL_WORKFLOW}
            part_categories: list[str] = line.replace("}", "").replace("{", "").split(",")
            for part_category in part_categories:
                category, category_value = part_category.split("=")
                part[category] = int(category_value)
            parts.append(part)            

    return workflows, parts

        
def calc_accepted_part_rating_sum(workflows: dict[str, list[list[str]]], parts: list[dict[str, str | int]]) -> int:
    ACCEPTED: str = "A"
    REJECTED: str = "R"
    accepted_part_rating_sum: int = 0

    for part in parts:
        destination_found: bool = False
        while not destination_found:
            current_workflow_name: str = part["current workflow"]
            current_workflow_steps: list[list[str]] = workflows[current_workflow_name]

            for step in current_workflow_steps:
                no_condition: bool = len(step) == 1
                if no_condition:
                    part["current workflow"] = step[0]
                    break

                condition, destination = step
                category, condition_value = condition.replace("<", ">").split(">")

                passes_less_than: bool = "<" in condition and part[category] < int(condition_value)
                passes_greater_than: bool = ">" in condition and part[category] > int(condition_value)

                if passes_less_than or passes_greater_than:
                    part["current workflow"] = destination
                    break

            if part["current workflow"] == ACCEPTED: 
                part_rating_sum: int = sum([part["x"], part["m"], part["a"], part["s"]])
                accepted_part_rating_sum += part_rating_sum
                destination_found = True

            elif part["current workflow"] == REJECTED:
                destination_found = True

    return accepted_part_rating_sum


main()