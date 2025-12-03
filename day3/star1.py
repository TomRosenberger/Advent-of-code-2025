with open("day3/input.txt") as file:
    banks = [bank.strip() for bank in file]

output = []
for bank in banks:
    bank = [int(b) for b in bank]
    left = 0
    right = len(bank)-1
    max_left = -1
    max_left_index = 0
    max_right = -1
    while left < right:
        if bank[left] > max_left:
            max_left_index = left
            max_left = bank[left]
        if max_left == 9:
            break
        left += 1
    while right > max_left_index:
        if bank[right] > max_right:
            max_right = bank[right]
        if max_right == 9:
            break
        right -= 1
    output.append(max_left * 10 + max_right)

print(sum(output))