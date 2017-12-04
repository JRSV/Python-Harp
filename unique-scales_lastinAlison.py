

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


def l_unique(seq, idfun=None): 
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

def list_unique(seq):
		unique = set(seq)
		return unique

print list_unique([1,2,2,2,3,4,5,6,6,6,6]) 
		
def l_unique(seq): 
   # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

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
				print ': --------------------------------------------- Pedal Numero {}'.format(pedal_number)
				for ped_pos in range(len(pedal)):
					#print 'Value for unpack pedals: {}'.format(ped_pos)

					for pedal_idx in range(len(pedal)):
						rest_of_list =  list((unpack_pedals(pedals,ped_pos, pedal_number)))
						#note = pedal[inst]

						#print 'index of current_pedal {}'.format(pedal_idx)
						current_value =	pedals[pedal_number]
						#current_value = current_value[pedal_number]
						#print 'insert {} in position {}'.format(current_value[pedal_idx], pedal_idx )
						rest_of_list.insert(pedal_number, current_value[pedal_idx])
						rest_of_list = l_unique(rest_of_list)
						if len(rest_of_list) > 6:
								print 'PEDAL_SEQ:------------{}'.format(rest_of_list)


						#pedals[cycle] = [position_pedal]
	#print pedals
	return finalList


pedalCombination(argument)


list_unique(set(list))
list_unique(set(list))


def pack_uniques(packed,to_be_p):
		packed = list(packed)
		to_be_p = list(to_be_p)
		n = 0

		if len(packed) > 0:
				for pack in packed:
						for item in packed:
								if pack == item:
										n = n+1
		if n != len(to_be_p):
				packed.append(to_be_p)
				
										
