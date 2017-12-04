argument = [(1,2,3),(11,0,1),(10,11,0),(3,4,5),(4,5,6),(6,7,8),(8,9,10)]

def unpack_pedals(argument, position_pedals, pedal_number):

    pedals = list(argument)
    pos_pedal = position_pedals
    length = len(argument)
    rest_of_list = [ ]

    for pedal in pedals:
        rest_of_list.append(pedal[pos_pedal])

    rest_of_list.pop(pedal_number)

    return rest_of_list


print unpack_pedals(argument, 1, 4)

#print len(argument)

def pedalCombination(argument):

		finalList = [ ]
		pedals = list(argument)
		numPedals = len(argument)
		order = [ ]

		for cycle in range(numPedals): #count from 0 to number of pedals
				print 'cycle: ******************************************************** CYCLE: {}'.format(cycle)
				for pedal in pedals:
						for pedal_number in range(numPedals):
								print 'Pedal: ------------------------------- Pedal Numero {}'.format(pedal_number)
								for ped_pos in range(len(pedal)):
										print 'Value for unpack pedals: {}'.format(ped_pos)

										for pedal_idx in range(len(pedal)):
												rest_of_list =  list((unpack_pedals(pedals,ped_pos, pedal_number)))
												#note = pedal[inst]
																											
												#print 'index of current_pedal {}'.format(pedal_idx)
												current_value = pedal[pedal_idx]
												#print 'insert {} in position {}'.format(pedal_number, current_value )
												rest_of_list.insert(pedal_number, current_value)
												print 'COMBINATION:------------{}'.format(rest_of_list)
										

            #pedals[cycle] = [position_pedal]
		print pedals
		return finalList


pedalCombination(argument)
