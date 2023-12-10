def main() -> None:
    FILE: str = "day5/puzzle-input.txt"
    print(solution(FILE))


def solution(file_name: str) -> int:
    seed_data: list[str] = get_puzzle_data(file_name)
    answer: int = get_lowest_location(seed_data)

    return answer


def get_puzzle_data(file_name: str) -> list[str]:
    puzzle_data: list[str] = open(file_name).read().split("\n")
    
    return puzzle_data


def get_lowest_location(seed_data: list[str]) -> int:
    seeds, almanac = get_seeds_and_almanac(seed_data)
    almanac_maps: dict[list] = get_almanac_maps(almanac)
    locations: list[int] = get_locations_numbers(seeds, almanac_maps)
    
    return min(locations)


def get_seeds_and_almanac(seed_data: list[str]) -> tuple[list[int], list[str]]:
    seeds: list[int] = [int(seed) for seed in seed_data[0].split(":")[1].split()]
    almanac: list[str] = [line for line in seed_data[1:] if line != ""]

    return seeds, almanac


def get_almanac_maps(almanac: list[str]) -> dict[list]:
    almanac_maps: dict[list] = {}
    current_map: str = ""
    for line in almanac:
        if line[0].isalpha():
            current_map = line.split("-")[-1].replace(":", "")
            almanac_maps[current_map] = []
        else:
            almanac_maps[current_map].append([int(alm_num) for alm_num in line.split()])

    return almanac_maps


def get_locations_numbers(seeds: list[int], almanac_maps: dict[list]) -> list[int]:
    locations: list[int] = []

    for seed in seeds:
        current_source = seed
        for alm_map in almanac_maps:
            current_source = convert_source_to_dest(current_source, almanac_maps[alm_map])
        locations.append(current_source)

    return locations


def convert_source_to_dest(source: int, maps: list[list[int]]) -> int:
    dest: int = source
    for m in maps:
        dest_range_start, source_range_start, range_lenth = m
        if source_range_start <= source < source_range_start + range_lenth:
            diff = source - source_range_start
            dest = dest_range_start + diff
            return dest
        
    return dest


main()