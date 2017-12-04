

argument = [(1,2,3),(11,0,1),(10,11,0),(3,4,5),(4,5,6),(6,7,8),(8,9,10)]

######################################################################

def unpack_pedals(argument, position_pedals, pedal_number):

    pedals = list(argument)
    pos_pedal = position_pedals
    length = len(argument)
    rest_of_list = [ ]

    for pedal in pedals:
        rest_of_list.append(pedal[pos_pedal])

    rest_of_list.pop(pedal_number)

    return rest_of_list

#######################################################################

def l_unique(seq): 
   # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

########################################################################

# ####### TEST FILTER ##########
# packed = []
# to_be_p = [1, 11, 10, 3, 4, 6, 8]
# print pack_uniques(packed, to_be_p)

# packed = [[1, 11, 10, 3, 4, 6, 8],[1, 11, 10, 3, 5, 6, 8]]
# to_be_p = [1, 11, 10, 3, 4, 6, 8]
# print pack_uniques(packed, to_be_p)


# packed = [[1, 11, 10, 3, 4, 6, 8]]
# to_be_p = [1, 11, 10, 3, 5, 6, 8]
# print pack_uniques(packed, to_be_p)

####################################

def pack_uniques(packed,to_be_p):
		packed = list(packed)
		to_be_p = list(to_be_p)
		hits = 0
		
		#function looks to see if the list that is going to be added,
		#is already in the final list.
		
		for pack in packed:
				n = 0

				if len(packed) > 0:
						for b in pack:
								for a in to_be_p:
										if b == a:
												n = n + 1
										else:
												n = n
						if n == 7:
								n=0
								hits += 1
						else:
								hits = hits
		if hits == 0:
			    packed.append(to_be_p)
		return packed	

####################################################################################
# This function, return all possible unique 7 pedal combinations of the Harp pedals

def pedalCombination(argument):

	finalList = [ ]
	pedals = list(argument)
	numPedals = len(argument)

	for cycle in range(numPedals): #count from 0 to number of pedals
		#print 'cycle: *************************************************** CYCLE: {}'.format(cycle)
		for pedal in pedals:
			for pedal_number in range(numPedals):
				#print ':------------------------------- Pedal Numero {}'.format(pedal_number)
				for ped_pos in range(len(pedal)):
					#print 'Value for unpack pedals: {}'.format(ped_pos)

					for pedal_idx in range(len(pedal)):
						rest_of_list =  list((unpack_pedals(pedals,ped_pos, pedal_number)))
						#print 'index of current_pedal {}'.format(pedal_idx)
						current_value =	pedals[pedal_number]
						#current_value = current_value[pedal_number]
						#print 'insert {} in position {}'.format(current_value[pedal_idx], pedal_idx )
						rest_of_list.insert(pedal_number, current_value[pedal_idx])
						rest_of_list = l_unique(rest_of_list)
						rest_of_list = sorted(rest_of_list)

						if len(rest_of_list) >= 7:
								#print ':-----{}'.format(rest_of_list)
								finalList = pack_uniques(finalList,rest_of_list)

		return finalList

finalList = pedalCombination(argument)
print len(finalList)
print finalList

