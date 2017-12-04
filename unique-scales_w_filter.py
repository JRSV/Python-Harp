def unpack_pedals(argument, position_pedals, pedal_number):

    pedals = list(argument)
    pos_pedal = position_pedals
    length = len(argument)
    rest_of_list = [ ]

    for pedal in pedals:
        rest_of_list.append(pedal[pos_pedal])

    rest_of_list.pop(pedal_number)

    return rest_of_list


def list_unique(seq, idfun=None):
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result


def compare_pedal_sets(a, b):
	for pos in a:
		for state in b:
			if pos != state:
				add_set_to_list = 1
			else:
				add_set_to_list = 0

	return add_set_to_list



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
					#print 'Value for unpack pedals: {}'.format(ped_pos)

					for pedal_idx in range(len(pedal)):
						rest_of_list =  list((unpack_pedals(pedals,ped_pos, pedal_number)))
						#note = pedal[inst]
						#print 'index of current_pedal {}'.format(pedal_idx)
						current_value = pedal[pedal_idx]
						#print 'insert {} in position {}'.format(pedal_number, current_value )
						rest_of_list.insert(pedal_number, current_value)
						#rest_of_list = list_unique(rest_of_list)
						#if len(finalList) == 0:
						finalList.append(rest_of_list)
						#print 'UNIQUE:::-------------- {}'.format(list_unique(rest_of_list))
						print 'UNIQUE:::-------------- {}'.format(rest_of_list)
						#else:
						#		for ped_seq in finalList:
						#				if compare_pedal_sets(ped_seq, rest_of_list) == 1:
						#						finalList.append(rest_of_list)
						#						print 'UNIQUE:::-------------- {}'.format(list_unique(rest_of_list))
						#print 'COMBINATION:------------{}'.format(rest_of_list)
		#pedals[cycle] = [position_pedal]
		#print pedals
	return finalList


argument = [(1,2,3),(11,0,1),(10,11,0),(3,4,5),(4,5,6),(6,7,8),(8,9,10)]

pedalCombination(argument)

a = [3, 8, 0, 5, 6, 8, 10]
b = [1, 11, 6, 3, 4, 6, 8]
c = [3, 8, 0, 5, 6, 8, 10]

print compare_pedal_sets(a,c)
print list_unique([1,2,2,2,3,4,5,6,6,6,6])
print unpack_pedals(argument, 1, 4)
