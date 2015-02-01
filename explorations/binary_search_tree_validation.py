# Check that a binary tree is a binary search tree
# Need a tree here to work with...
# See book and whiteboard photos for more details.

def depth_search(root, cbn, csn)
	toggle = True
	if cbn = None:
		cbn = root
	if csn = None:
		csn = root
	if root.left.value < csn:
		depth_search(root.left, cbn, root.left.value)
	else: 
		toggle = False
	if csn < root.right.value < cbn:
		depth_search(root.right, root.right.value, csn)
	else: 
		toggle = False
	if not root.left and not root.right:
		return toggle

