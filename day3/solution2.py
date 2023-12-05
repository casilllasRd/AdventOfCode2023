def solution():
    puzzle_input = open("day3/puzzle-input.txt")
    puzzle_data = puzzle_input.read()
    engine_data = puzzle_data.split("\n")

    get_gear_ratio_sum(engine_data)


def get_gear_ratio_sum(data):
    gear_locations = []

    current_digits = []
    locations = []
    engine_numbers = []

    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "*":
                gear_locations.append([
                    (col - 1, row - 1), (col + 0, row - 1), (col + 1, row - 1),
                    (col - 1, row + 0), (col + 0, row + 0), (col + 1, row + 0),
                    (col - 1, row + 1), (col + 0, row + 1), (col + 1, row + 1),    
                ])

            if char.isdigit():
                current_digits.append(char)
                locations.append((col, row))

                if col == len(data[row]) - 1:
                    engine_numbers.append({
                        "num": "".join(current_digits),
                        "locations": locations,
                        "gear adjacent": False
                    })
                    current_digits = []
                    locations = []

                elif not data[row][col + 1].isdigit():
                    engine_numbers.append({
                        "num": "".join(current_digits),
                        "locations": locations,
                        "gear adjacent": False
                    })
                    current_digits = []
                    locations = []

    ratio_sum = 0
    for gear in gear_locations:
        adjacent_numbers = []
        for engine_number in engine_numbers:
            adjacent_cells = [l for l in engine_number["locations"] if l in gear]
            if adjacent_cells:
                adjacent_numbers.append(int(engine_number["num"]))
        
        print(adjacent_numbers)
        if len(adjacent_numbers) == 2:
            ratio_sum += (adjacent_numbers[0] * adjacent_numbers[1])

    print(ratio_sum)


solution();