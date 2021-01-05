from mots_fleches import *


questions = [Question("beaucoup ou trop de gestes", Mask("ge______er"), (1, 0, 1, 'r')), Question("Manifester son mécontentement", Mask("r__e_"), (0, 10, 2, 'd'))]
jeu = Jeu(questions, (6, 12))
jeu.activate_questions()
 
print(jeu)

