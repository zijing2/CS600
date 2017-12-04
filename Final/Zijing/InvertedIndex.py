from Tries import Tries

# implement a dictionary, storing key-value pairs (w, L) 
# where w is a word and L is a collection of references to pages containing word w.
class InvertedIndex(object):
    
    tries = Tries()
    occurence_list = []
    
    # get a collection of references to pages containing word w by sending a word
    def get(self, key):
        ref = self.tries.getRefByWord(key)
        if ref > 0 and ref < len(self.occurence_list):
            return self.occurence_list[ref]
        else:
            return None
    
    # put a collection of references to pages containing word w mapping with a word
    def put(self, key, value):
        occurence_collection = self.get(key)
        if(occurence_collection == None):
            self.occurence_list.append({value: 1})
            ref = len(self.occurence_list)
            self.tries.insert(key, ref)
        else:
            if occurence_collection.has_key(value):
                occurence_collection[value] = occurence_collection[value]+1
            else:
                occurence_collection[value] = 1
        return 
            
            
