import sys

masses = []
elephants = []
final_positions = []
effort = 0
elephants_masses = {}

cycles = []
cycle = []

input_data = sys.stdin.readlines()

str_num_of_elephants = input_data[0].strip().split(' ')
str_masses = input_data[1].strip().split(' ')
str_elephants = input_data[2].strip().split(' ')
str_final_positions = input_data[3].strip().split(' ')

num_of_elephants = int(str_num_of_elephants[0])

for counter in range(num_of_elephants):
    masses.append(int(str_masses[counter]))
    elephants.append(int(str_elephants[counter]))
    final_positions.append(int(str_final_positions[counter]))

for counter in range(num_of_elephants):
    elephants_masses[counter+1] = masses[counter]

for outerindex in range(num_of_elephants):
    current_elephant = elephants[outerindex]
    position = outerindex

    if outerindex != 0:
        cycles.append(cycle)
        for appended in cycles:
            if appended == cycle:
                break
            for number in cycle:
                if number in appended:
                    cycles.pop()
                    break
        cycle = []

    for innerindex in range(outerindex+1, num_of_elephants):
        final_position = final_positions.index(current_elephant)
        cycle.append(current_elephant)
        if final_position != outerindex:
            effort += (elephants_masses[elephants[final_position]
                                        ] + elephants_masses[current_elephant])
            current_elephant, elephants[final_position] = elephants[final_position], current_elephant
        else:
            elephants[final_position] = current_elephant
            break

for cycle in cycles:
    for index, elephant in enumerate(cycle):
        cycle[index] = elephants_masses[elephant]

min_mass = min(masses)
final_effort = 0

for cycle in cycles:
    if len(cycle) != 1:
        first_method = sum(cycle) + (len(cycle)-2) * min(cycle)
        second_method = sum(cycle) + min(cycle) + (len(cycle)+1) * min_mass
        final_effort += min(first_method, second_method)

print(final_effort)
