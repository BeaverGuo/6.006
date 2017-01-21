#tree_insert recurse version

def tree_insert(self, T, z):
	y = None
	if z.key < T.key:
		y = T.left
		tree_insert(T.left, z) #递归应该是到T为None时
	else:
		y = T.right
		tree_insert(T.right, z)
	z.p = y
	if y == None:
		T.root = z
	elif z.key < y.key:
		y.left = z
	else:
		y.right = z

#right answer
def tree_insert(T,z):
	if T = None:
		T.key = z
		T.left = None
		T.right = None
	elif z < T.key:
		tree_insert(T.left,z)
	else
		tree_insert(T.right,z)

