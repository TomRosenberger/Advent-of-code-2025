with open("day3/input.txt") as file:
    banks = [bank.strip() for bank in file]

output = []
for bank in banks:
    bank_joltage = [0] * 12
    bank = [int(b) for b in bank]
    battery_number = 11
    starting_point = 0
    while battery_number >= 0:
        end_point = -battery_number
        if end_point == 0:
            search_slice = bank[starting_point:]
        else:
            search_slice = bank[starting_point:end_point]
        
        max_index = 0 
        for i, battery in enumerate(search_slice):
            if battery > bank_joltage[-(battery_number+1)]:
                bank_joltage[-(battery_number+1)] = battery
                max_index = starting_point + i + 1
            if battery == 9:
                break
        starting_point = max_index
        battery_number -= 1
    
    output.append(int("".join([str(b) for b in bank_joltage])))

print(sum(output))