init_seq = open("puzzle-input.txt").read().split(",")
hash_sum = 0
for string in init_seq:
    hash_val = 0
    for char in string:
        hash_val += ord(char)
        hash_val *= 17
        hash_val %= 256
    hash_sum += hash_val
print(hash_sum)