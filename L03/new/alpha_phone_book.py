#Alphabetizing the Phone Book.(last name, first name, phone number)
#sort according to last name then first name.O(kn)

#radix sort

C = [None,'a','b','c','d','e','f','g',
	'h','i','j','k','l','m','n',
	'o','p','q','r','s','t','u','v','w','x','y','z']
#helper function

#find longest last name . i=0 for last name
def find_max_last_name(l,i=0):
	k = 0
	for idx in range(len(l)):
		k = max(k,len(l[idx]))
	return k
#add Nones to longest k
def add_nones(l,i,k):
	for idx in range(len(l)):
		list(l[idx][i]).append([None]*(k-len(l[idx][i])))

#remove Nones
def rm_nones(l,i=0):
	for idx in range(len(l)):
		['' if v is None else v for v in l[idx][i]]
		#l[idx][i].replace(None,'')


def radix_sort(C,l,k,i,j):
	#dict character for caching l items
	character = {}

	for idx in range(len(l)):
		current_chr = l[idx][i][j]
		if not current_chr in character:
			character[current_chr] = [] #empty for sorting using C
		character[current_chr].append(l[idx]) #keep input order and append same
		#character to the array for sorting using C
	result = []
	#sorting by order of C,nothing to do with character dict
	for c in range(len(C)):
		if C[c] in character:
			for a in range(len(character[C[c]])):
				result.append(character[C[c]][a])
	return result

#using radix sort to sort last names in phone book
def alpha_phone_book(l,i=0):
	k = find_max_last_name(l,i)
	add_nones(l,i,k)
	#start from the last character of last name
	for j in range(k-1,-1,-1):
		l = radix_sort(C,l,k,i,j)
	rm_nones(l,i)
	return l

test = [('abc','dkkdd','1234'),('cba','dkkdd','1234'),
('def','dkkdd','1234'),('abc','dkkdd','12345'),('abb','dkkdd','1234')]
print alpha_phone_book(test,0)


#alpha_phone_book(test,1)
#alpha_phone_book(test,0)
