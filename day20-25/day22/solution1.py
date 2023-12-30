class Pos:
    def __init__(self, coord: list[int]):
        self.x, self.y, self.z = coord


class Brick:
    def __init__(self, first_coords: str, second_coords: str):
        self.pos1: Pos = Pos([int(coord) for coord in first_coords.split(",")])
        self.pos2: Pos = Pos([int(coord) + 1 for coord in second_coords.split(",")])
        self.settled: bool = False
        self.bricks_supporting: list = []
        self.supported_by: list = []


def main() -> None:
    input_file: str = "test-input.txt"
    answer: int = solution(input_file)

    print(answer)


def solution(input_file: str) -> int:
    snapshot_of_bricks: list[str] = load_puzzle_data(input_file)
    bricks: list[Brick] = get_bricks(snapshot_of_bricks)
    settled_bricks: list[Brick] = settle_bricks(bricks)
    number_of_eligible_bricks: int = count_eligble_bricks(settled_bricks)

    return number_of_eligible_bricks


def load_puzzle_data(input_file: str) -> list[str]:
    puzzle_data: list[str] = open(input_file).read().split("\n")
    return puzzle_data


def get_bricks(snapshot_of_bricks: list[str]) -> list[Brick]:
    bricks: list[Brick] = []

    for set_of_coords in snapshot_of_bricks:
        first_coord, second_coord = set_of_coords.split("~")
        bricks.append(Brick(first_coord, second_coord))

    return bricks


def settle_bricks(bricks: list[Brick]) -> list[Brick]:
    settled_bricks: list[Brick] = []
    bricks_sorted = sorted(bricks, key = lambda brick: brick.pos1.z)

    for brick in bricks_sorted:
        while not brick.settled:
            move_brick(brick, settled_bricks)
        settled_bricks.append(brick)

    return settled_bricks


def move_brick(current_brick: Brick, settled_bricks: list[Brick]) -> None:
    if current_brick.pos1.z == 1 or current_brick.pos2.z == 1:
        current_brick.settled = True
    
    for settled_brick in settled_bricks:
        if check_collision(current_brick, settled_brick):
            current_brick.supported_by.append(settled_brick)
            settled_brick.bricks_supporting.append(current_brick)

    if len(current_brick.supported_by) != 0:
        current_brick.settled = True
    
    current_brick.pos1.z += 1
    current_brick.pos2.z += 1


def check_collision(brick1: Brick, brick2: Brick) -> bool:
    if brick1.pos1.z == brick2.pos2.z:
        left: bool = brick1.pos1.x < brick2.pos2.x
        right: bool = brick1.pos2.x > brick2.pos1.x
        top: bool = brick1.pos1.y < brick2.pos2.y
        bottom: bool = brick1.pos2.y > brick2.pos1.y
        
        return left and right and top and bottom
    
    return False


def count_eligble_bricks(settled_bricks: list[Brick]) -> int:
    eligible_bricks = 0

    for brick in settled_bricks:
        eligible: bool = True
        for supported_brick in brick.bricks_supporting:
            if len(supported_brick.supported_by) == 1:
                eligible: bool = False

        eligible_bricks += eligible

    return eligible_bricks


main()