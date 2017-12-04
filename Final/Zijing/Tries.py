class TreeNode():
    children = {}
    hit_num = 0
    # key in the node
    key = None
    # a reference to the matching occurrence lists
    ref = None
    
    def __init__(self):
        self.children = {}

class Tries(object):
    
    root = TreeNode()
    
    def insert(self, word, ref):
        current = self.root
        if len(word)==0:
            return
        for i,c in enumerate(word):
            if current.children.has_key(c):
                current = current.children[c]
            else:
                newNode = TreeNode()
                newNode.key = c
                current.children[c] = newNode
                current = current.children[c]
        
        if current.ref == None:
            current.ref = ref
        return 
                    
            
    def getRefByWord(self, word):
        current = self.root
        if len(word)==0:
            return None
        for i,c in enumerate(word):
            if current.children.has_key(c):
                current = current.children[c]
                if i == len(word)-1:
                    return current.ref
            # no matching word
            else:
                return None
            

    
    
# tries = Tries()


# tries.insert(word="abcd")
# tries.insert(word="acde")
# print Tries.root.children['a'].children['b'].hit_num
# print Tries.root.children

    




    
