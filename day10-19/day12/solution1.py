hot_springs_field = open("test-input.txt").read().split("\n")

DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"

# for hot_springs_row in hot_springs_field:
#     # print(hot_springs_row)

#     permutations = []

#     hot_springs, continuous_groups = hot_springs_row.split()

#     print()
#     print(hot_springs)
#     # print(continuous_groups)
#     # print()

#     continuous_groups = [int(g) for g in continuous_groups.split(",")]
#     print(continuous_groups)
#     print()


sample_springs = ".??..??...?##."
sample_groups = [1, 1, 3]

print(sample_springs.split("."))