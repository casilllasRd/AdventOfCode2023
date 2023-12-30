class Beam:
    def __init__(self, x_pos: int, y_pos: int, x_dir: int, y_dir: int):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.past_locations = []
        self.stopped = False

    def update_position(self):
        beam.x_pos += beam.x_dir
        beam.y_pos += beam.y_dir



contraption_data = open("puzzle-input.txt").read().split("\n")
energized_data = [list("." * len(line)) for line in contraption_data]

starting_beam = Beam(0, 0, 1, 0)
beams = [starting_beam]


EMPTY_SPACE = "."
VERTICAL_SPLITTER = "|"
HORIZONAL_SPLITTER = "-"
LEFT_MIRROR = "\\"
RIGHT_MIRROR = "/"

ENERGIZED = "#"

previous_splitters = []


while len(beams) != 0:
    for beam in beams:
        # check if at the edge
        passed_N_edge = beam.x_pos < 0
        passed_W_edge = beam.y_pos < 0
        passed_E_edge = beam.x_pos > len(contraption_data[0]) - 1
        passed_S_edge = beam.y_pos > len(contraption_data) - 1
        if passed_N_edge or passed_W_edge or passed_E_edge or passed_S_edge:
            beams.remove(beam)
            continue

        # check if been here before
        current_pos = beam.x_pos, beam.y_pos
        if current_pos in beam.past_locations:
            beams.remove(beam)
            continue
        
        beam.past_locations.append(current_pos)

        # Update Energized Table
        energized_data[beam.y_pos][beam.x_pos] = ENERGIZED

        # Check Spot 
        current_spot = contraption_data[beam.y_pos][beam.x_pos]

        if current_spot == VERTICAL_SPLITTER:
            if beam.x_dir != 0 and current_pos not in previous_splitters:
                beam.x_dir = 0
                beam.y_dir = 1

                new_beam = Beam(beam.x_pos, beam.y_pos - 1, 0, -1)
                new_beam.past_locations.append(current_pos)
                beams.append(new_beam)
                previous_splitters.append(current_pos)
                

        if current_spot == HORIZONAL_SPLITTER:
            if beam.y_dir != 0 and current_pos not in previous_splitters:
                beam.x_dir = 1
                beam.y_dir = 0

                new_beam = Beam(beam.x_pos - 1, beam.y_pos, -1, 0)
                new_beam.past_locations.append(current_pos)
                beams.append(new_beam)
                previous_splitters.append(current_pos)
                

        if current_spot == LEFT_MIRROR:
            if beam.x_dir == 1:
                beam.x_dir = 0
                beam.y_dir = 1
            elif beam.x_dir == -1:
                beam.x_dir = 0
                beam.y_dir = -1

            elif beam.y_dir == 1:
                beam.x_dir = 1
                beam.y_dir = 0
            elif beam.y_dir == -1:
                beam.x_dir = -1
                beam.y_dir = 0
        
        if current_spot == RIGHT_MIRROR:
            if beam.x_dir == 1:
                beam.x_dir = 0
                beam.y_dir = -1
            elif beam.x_dir == -1:
                beam.x_dir = 0
                beam.y_dir = 1

            elif beam.y_dir == 1:
                beam.x_dir = -1
                beam.y_dir = 0
            elif beam.y_dir == -1:
                beam.x_dir = 1
                beam.y_dir = 0

        beam.update_position()
        # print(len(beams))


energized_count = 0
for line in energized_data:
    energized_count += line.count(ENERGIZED)

print(energized_count)
