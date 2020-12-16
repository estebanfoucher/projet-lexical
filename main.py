from lexpp import lexpp

class Lexique(list):

    def filter_by_mask(self, mask):
        filtered_lexique = Lexique([])
        for word in self:
            if mask.is_compatible(word):
                filtered_lexique.append(word)
        return filtered_lexique

class Mask(str):

    def is_compatible(self, word):

        if len(word) != len(self):
            return False
        
        for elt1, elt2 in zip(self, word):
            
            if elt1 != "_" and elt1 != elt2:
                return False
                
        return True

class Question():

    def __init__(self, question, mask):
        self.question = question
        self.mask = mask
    
    def solve(self):
        lex = Lexique(lexpp)
        lex = lex.filter_by_mask(self.mask)
        return lex




#print(Lexique(lexpp).filter_by_mask(Mask("_a")))

# q = Question("blue", Mask("_a"))
# print(q.solve())



