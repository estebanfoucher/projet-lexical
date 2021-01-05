import numpy as np
from .functions import *


class Lexique(list):

    def filter_by_mask(self, mask):
        filtered_lexique = Lexique([])
        for word in self:
            if mask.is_compatible(word):
                filtered_lexique.append(word)
        return filtered_lexique
    
    def order_by_def_0(self, question):

        ordered_lexique = Lexique([])
        for word in self:
            dist = distance(question, get_definition(word))
            ordered_lexique.append((word, dist))
        
        # sort list with key
        ordered_lexique.sort(key=takeSecond, reverse=True)
        return ordered_lexique

    def order_by_def_1(self, question):

        ordered_lexique = Lexique([])
        new_question = order1_synonyms(question)
        for word in self:
            dist = distance(new_question, get_definition(word))
            ordered_lexique.append((word, dist))
        
        # sort list with key
        ordered_lexique.sort(key=takeSecond, reverse=True)
        return ordered_lexique  

class Mask(str):

    def is_compatible(self, word):

        if len(word) != len(self):
            return False
        
        for elt1, elt2 in zip(self, word):
            
            if elt1 != "_" and elt1 != elt2:
                return False
                
        return True

class Question(object):

    def __init__(self, question, mask, vector:"line,column,index,direction"):
        self.question = question
        self.mask = mask 
        self.vector = vector

    def solve(self):
        lex = Lexique(lexpp)
        lex = lex.filter_by_mask(self.mask)
        return lex

    def write_in_grid(self, grid):
        i, j, index, direction = self.vector
        #cellule de question
        grid[i][j] = f"{index},{direction}"
        
        if direction == "r":
            for h in range(len(self.mask)):
                grid[i][j+1+h] = self.mask[h]
        
        if direction == "d":
            for h in range(len(self.mask)):
                grid[i+1+h][j] = self.mask[h]

class Jeu(object):

    def __init__(self, questions:list, shape):
        self.questions = questions
        self.shape = shape
        self.grid = self.generate_grid()
    
    def generate_grid(self):
        n, p = self.shape
        grid = [["@"for j in range(p)]for i in range(n)]
        return grid
    
    def __repr__(self):
        return repr(np.array(self.grid))
    
    def activate_questions(self):
        new_grid = self.grid
        for question in self.questions:
            question.write_in_grid(new_grid)
        self.grid = new_grid


    def update_question(self, index):
        mask = Mask("")
        question = self.questions[index]
        i, j, index, direction = question.vector
        
        if direction == "r":
            for h in range(len(question.mask)):
                mask += self.grid[i][j+1+h]
        
        if direction == "d":
            for h in range(len(question.mask)):
                mask += self.grid[i+1+h][j]
        
        if not mask.is_compatible(question.mask):
            print("answer not possible")
        else:
            question.mask = mask
        
    def update_grid(self):
        for i in range(len(self.questions)):
            update_question(question.vector[2])

