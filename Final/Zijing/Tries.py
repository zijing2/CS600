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
    
    # insert node to tries
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
                    
    # get reference by tries         
    def getRefByWord(self, word):
        current = self.root
        if len(word)==0:
            return None
        for i,c in enumerate(word):
            if current.children.has_key(c):
                current = current.children[c]
                if i == len(word)-1:
                    current.hit_num = current.hit_num + 1
                    return current.ref
            # no matching word
            else:
                return None
    
    # get the recommend keys when key in charactors
    def getRecommendKey(self, string):
        current = self.root
        for i,c in enumerate(string):
            if current.children.has_key(c):
                current = current.children[c]
            else:
                return []
        sub_keylist = self.dfs(current)
        keylist = []
            
        for i,word in enumerate(sub_keylist):
            s = string[:-1] + word
            keylist.append(s)
        return keylist
        
    # get key list by dfs the children of the current node
    def dfs(self, root):
        if root.key:
            current_letter = root.key
        else: 
            current_letter = ''
        keylist = []
        if root.children:
            for cnode in root.children:
                sub_keylist = self.dfs(root.children[cnode])
                if len(sub_keylist)==0:
                    keylist.append(current_letter)
                else:
                    for i,word in enumerate(sub_keylist):
                        s = current_letter + word
                        keylist.append(s)
        else:
            return [current_letter]
            
        return keylist
    
# tries = Tries()
# tries.insert(word="abcd", ref="http://abcd.com")
# tries.insert(word="acde", ref="http://acde.com")
# tries.insert(word="bcde", ref="http://acde.com")
# tries.insert(word="acddecxec", ref="http://acde.com")
# print tries.dfs(root=tries.root)
# print tries.getRecommendKey("")
# print Tries.root.children['a'].children['b'].hit_num
# print Tries.root.children


    




    
