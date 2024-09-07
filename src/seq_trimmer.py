

def kadaneMaxSubArray(arr, verbose=True):
	curr_sum = 0
	max_sum = 0
	first, last = -1, -1
	tmp_first = -1
	index_list = []
	zero_index_list = []
	
	for i, e in enumerate(arr):
		curr_sum += e
		if curr_sum >= max_sum:
			max_sum = curr_sum
			last = i
			first = tmp_first + 1
			
			if zero_index_list:
				for zi in zero_index_list:
					index_list.append((zi, last))
			
			if first != -1 and last != -1:
				tmp_list = []
				while index_list:
					f, l = index_list.pop()
					s = sum(arr[f:l+1])
					if s == curr_sum:
						tmp_list.append((f, l))
				if tmp_list: index_list.extend(tmp_list)
				index_list.append((first, last))
	
		if curr_sum <= 0 :
			curr_sum = 0
			tmp_first = i

		if e == 0:
			zero_index_list.append(i)
			tmp_list = []
			length = len(zero_index_list)
			le = zero_index_list[-1]
			for i in range(length-2, -1, -1):
				if zero_index_list[i] == le - 1:
					tmp_list.append(le)
					le = zero_index_list[i]
				else :
					tmp_list.append(le)
					break
			else:
				tmp_list.append(le)

			if tmp_list:
				zero_index_list = tmp_list[::-1]
						
	if verbose:
		print(f'{max_sum=}')
		# print(f'{first=} | {last=}')
		print(f'{index_list=}')
		print()
	return index_list


def get_max_range(index_list):
	if len(index_list) == 1:
		return index_list[0]
	
	max_range = 0
	first, last = 0, 0
	for values in index_list:
		f, l = values
		if (l-f) > max_range:
			first, last = f, l
	
	return (f, l)














