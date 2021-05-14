num_of_elephants = 6
elephants = [1, 4, 5, 3, 6, 2]
final_positions = [5, 3, 2, 4, 6, 1]

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
