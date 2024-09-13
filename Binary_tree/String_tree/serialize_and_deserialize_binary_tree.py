from Binary_tree.BSTNode import TreeNode


'''
All you are doing here is basically trying to convert 
[1, 2, 3, null, null, 4, 5] into the following -> "1,2,3,null,null,4,5"     for serialize 
"1,2,3,null,null,4,5"  into the following -> [1, 2, 3, null, null, 4, 5]      for deserialize 

And that's it here 

'''
class Codec:

    def serialize(s, root):
        def rserialize(s, r, str):
            if not r:
                str += 'None',
            else:
                str+= str(r.value) + ','
                str+= s.rserialize(r.l, str)
                str+= s.rserialize(r.l, str)

            return str

        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.l = rdeserialize(l)
            root.r = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root