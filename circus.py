num_of_elephants = 6
masses = [2400, 2000, 1200, 2400, 1600, 4000]
elephants = [1, 4, 5, 3, 6, 2]
final_positions = [5, 3, 2, 4, 6, 1]

effort = 0
elephants_masses = {}

cycles = []
cycle = []

for counter in range(num_of_elephants):
    elephants_masses[elephants[counter]] = masses[counter]

print("ELEPHANTS MASSES: ", elephants_masses)
print('')
for outerindex in range(num_of_elephants-2):
    print('****** outerindex = {} ******'.format(outerindex))
    print("ELEPHANTS BEFORE SWAP: ", elephants)
    current_elephant = elephants[outerindex]
    position = outerindex

    for innerindex in range(outerindex+1, num_of_elephants):
        print('###### innerindex = {} ######'.format(innerindex))
        print("CURRENT ELEPHANT: ", current_elephant)
        final_position = final_positions.index(current_elephant)
        print('FINAL POSITION: ', final_position)
        if final_position != outerindex:
            print("MASA ZAMIENIANEGO",
                  elephants_masses[elephants[final_position]])
            print("MASA PIERWSZEGO",
                  elephants_masses[current_elephant])
            effort += (elephants_masses[elephants[final_position]
                                        ] + elephants_masses[current_elephant])
            current_elephant, elephants[final_position] = elephants[final_position], current_elephant

            print("CURRENT ELEPHANT AFTER SWAP: ", current_elephant)
            print("ELEPHANTS AFTER SWAP: ", elephants)
        else:
            elephants[final_position] = current_elephant
            print("CURRENT ELEPHANT AFTER SWAP: ", current_elephant)
            print("ELEPHANTS AFTER SWAP: ", elephants)
            print(28 * '*')
            print('')
            break

print("ELEPHANTS: ", elephants)
print("EFFORT NOT OPTIMIZED: ", effort)
