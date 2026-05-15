# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = []
        curr = root

        serialize = []

        while curr:
            if curr != "none_node":
                serialize.append(str(curr.val))

                if curr.left:
                    queue.insert(0,curr.left)
                else:
                    queue.insert(0,"none_node")

                if curr.right:
                    queue.insert(0,curr.right)
                else:
                    queue.insert(0,"none_node")


            else:
                serialize.append("Null")

            if queue:
                curr = queue.pop()
            else:
                curr = None

        return ','.join(serialize)

        
    # Decodes your encoded data to tree.
    def deserialize(self, str_data: str) -> Optional[TreeNode]:
        if not str_data:
            return None

        data = str_data.split(',')
        
        root = TreeNode(val = int(data[0]))
        queue = [root]

        i = 1
        while queue and i<= len(data): 
            curr = queue.pop()

            if data[i] != "Null":
                curr.left = TreeNode(val=int(data[i]))
                queue.insert(0,curr.left)
            else:
                curr.left = None
            
            i+=1

            if data[i] != "Null":
                curr.right = TreeNode(val=int(data[i]))
                queue.insert(0,curr.right)
            else:
                curr.right = None

            i+=1

            
        return root

            



        


        

