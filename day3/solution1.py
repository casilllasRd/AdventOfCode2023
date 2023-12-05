def solution():
    puzzle_input = open("day3/puzzle-input.txt")
    puzzle_data = puzzle_input.read()
    engine_data = puzzle_data.split("\n")

    get_part_number_sum(engine_data)


def get_part_number_sum(puzzle_data: list[str]) -> int:
    part_number_sum = 0

    current_digits = []
    locations = []
    engine_numbers = []

    for row, line in enumerate(puzzle_data):
        for col, char in enumerate(line):
            if char.isdigit():
                current_digits.append(char)
                locations.append((col, row))

                if col == len(puzzle_data[row]) - 1:
                    engine_numbers.append({
                        "num": "".join(current_digits),
                        "locations": locations,
                        "part number": False
                    })
                    current_digits = []
                    locations = []
                elif not puzzle_data[row][col + 1].isdigit():
                    engine_numbers.append({
                        "num": "".join(current_digits),
                        "locations": locations,
                        "part number": False
                    })
                    current_digits = []
                    locations = []

    for engine_number in engine_numbers:
        for location in engine_number["locations"]:
            col, row = location

            if row - 1 >= 0:
                if col - 1 >= 0:
                    if not puzzle_data[row - 1][col - 1].isdigit() and not puzzle_data[row - 1][col - 1] == ".":
                        engine_number["part number"] = True

                if not puzzle_data[row - 1][col].isdigit() and not puzzle_data[row - 1][col] == ".":
                    engine_number["part number"] = True       

                if col + 1 <= len(puzzle_data[row - 1]) - 1:
                    if not puzzle_data[row - 1][col + 1].isdigit() and not puzzle_data[row - 1][col + 1] == ".":
                        engine_number["part number"] = True

            if row + 1 <= len(puzzle_data) - 1:
                if col - 1 >= 0:
                    if not puzzle_data[row + 1][col - 1].isdigit() and not puzzle_data[row + 1][col - 1] == ".":
                        engine_number["part number"] = True

                if not puzzle_data[row + 1][col].isdigit() and not puzzle_data[row + 1][col] == ".":
                    engine_number["part number"] = True

                if col + 1 <= len(puzzle_data[row + 1]) - 1:
                    if not puzzle_data[row + 1][col + 1].isdigit() and not puzzle_data[row + 1][col + 1] == ".":
                        engine_number["part number"] = True

            if col - 1 >= 0:
                if not puzzle_data[row][col - 1].isdigit() and not puzzle_data[row][col - 1] == ".":
                    engine_number["part number"] = True

            if col + 1 <= len(puzzle_data) - 1:
                if not puzzle_data[row][col + 1].isdigit() and not puzzle_data[row][col + 1] == ".":
                    engine_number["part number"] = True

        if engine_number["part number"]: 
            part_number_sum += int(engine_number["num"])
    
    print(part_number_sum)


solution()