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

print("ELEPHANTS MASSES: ", elephants_masses)
print('')
for outerindex in range(num_of_elephants):
    print('****** outerindex = {} ******'.format(outerindex))

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
        print('###### innerindex = {} ######'.format(innerindex))
        final_position = final_positions.index(current_elephant)
        cycle.append(current_elephant)
        print("CYCLE: ", cycle)
        if final_position != outerindex:
            effort += (elephants_masses[elephants[final_position]
                                        ] + elephants_masses[current_elephant])
            current_elephant, elephants[final_position] = elephants[final_position], current_elephant
        else:
            elephants[final_position] = current_elephant
            print(28 * '*')
            print('')
            break

print("ELEPHANTS: ", elephants)
print("EFFORT NOT OPTIMIZED: ", effort)
print("CYCLES: ", cycles)

for cycle in cycles:
    for index, elephant in enumerate(cycle):
        cycle[index] = elephants_masses[elephant]

print("CYCLES WITH MASSES: ", cycles)
