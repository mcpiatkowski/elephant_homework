num_of_elephants = 6
masses = [2400, 2000, 1200, 2400, 1600, 4000]
elephants = [1, 4, 5, 3, 6, 2]
final_positions = [5, 3, 2, 4, 6, 1]

effort = 0
elephants_masses = {}

cycles = []
cycle = []


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

first_method_only = 0
second_method_only = 0
min_mass = min(masses)
final_effort = 0

for cycle in cycles:
    if len(cycle) != 1:
        first_method_only += sum(cycle) + (len(cycle)-2) * min(cycle)
        second_method_only += sum(cycle) + min(cycle) + \
            (len(cycle)+1) * min_mass
        first_method = sum(cycle) + (len(cycle)-2) * min(cycle)
        second_method = sum(cycle) + min(cycle) + (len(cycle)+1) * min_mass
        final_effort += min(first_method, second_method)
        print("FIRST_METHOD IN LOOP: ", first_method)
        print("SECOND_METHOD IN LOOP: ", second_method)
        print("FINAL EFFORT IN LOOP: ", final_effort)

print("METHOD ONE EFFORT: ", first_method_only)
print("SECOND METHOD: ", second_method_only)
print("FINAL EFFORT: ", final_effort)
