#acient scrolls...to be continued...
def append_char(hash,c):
	return ((hash*len(A))+charToInt(c))%p

def remove_first(hash,c,L):
	return (hash-charToInt(c)*(len(A)**(L-1)%p))%p

def Hash(sig):
	hash = 0
	for i in range(len(sig)):
		hash = append_char(hash,sig[i])
	return hash

def find_author(scroll,sigatures):
	if len(scroll) < k:
		return None
	author_dict = {}
	for i in range(len(sigatures)):
		authorHash = Hash(sigatures[i])
		if not authorHash in author_dict:
			author_dict[authorHash] = []
		author_dict[authorHash].append(sigatures[i])
	hash = Hash(scroll[0:k])
	if hash in author_dict:
		if scroll[0:k-1] in author_dict[hash]:
			return scroll[0:k]

	for i in range(k,len(scroll)):
		hash = append_char(hash,scroll[i])
		hash = remove_first(hash,scroll[i-k],k+1)
		if hash in author_dict:
			if scroll[i-k+1:i] in author_dict[hash]:
				return scroll[i-k+1:i]
	return None