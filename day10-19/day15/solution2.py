def main() -> None:
    FILE: str = "puzzle-input.txt"
    answer: int = solution(FILE)

    print(answer)


def solution(file_name: str) -> int:
    initialization_sequence: list[str] = load_puzzle_data(file_name)
    boxes: list[dict[str, int]] = fill_boxes_with_labels(initialization_sequence)
    focusing_power: int = get_focusing_power(boxes)

    return focusing_power
    

def load_puzzle_data(file_name: str) -> list[str]:
    puzzle_data: list[str] = open(file_name).read().split(",")
    
    return puzzle_data


def init_boxes() -> list[dict[str, int]]:
    BOX_TOTAL: int = 256
    boxes = [{} for _ in range(BOX_TOTAL)]
    
    return boxes


def fill_boxes_with_labels(initialization_sequence: list[str]) -> list[dict[str, int]]:
    boxes: list[dict[str, int]] = init_boxes()
    for string in initialization_sequence:
        label, focal_length = get_label_and_focal_length(string)
        box_number: int = get_box_number(label)
        current_box: dict[str, int] = boxes[box_number]
        
        if focal_length:
            current_box[label] = int(focal_length)
        elif label in current_box:
            current_box.pop(label)

    return boxes

def get_label_and_focal_length(string: str) -> tuple[str, str]:
    label, focal_length = string.replace("-", "=").split("=")
    
    return label, focal_length


def get_box_number(label: str) -> int:
    box_number: int = 0

    for char in label:
        box_number += ord(char)
        box_number *= 17
        box_number %= 256
    
    return box_number


def get_focusing_power(boxes: list[dict[str, int]]) -> int:
    focusing_power: int = 0

    for box_index, box in enumerate(boxes):
        if box == {}: continue

        for slot_index, label in enumerate(box):
            box_number: int = box_index + 1
            slot_number: int = slot_index + 1
            focal_length: int = box[label]
            focusing_power += (box_number * slot_number * focal_length)

    return focusing_power


main()