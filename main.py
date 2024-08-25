import sys
# from parser.PropositionalFormula import PropositionalFormula
from file_manipulation.FileManager import FileManager

sys.path.append('..\\pyTableaux\\')

test = FileManager.get_formulas_on_file("example.tab")

print(test)

""" #EXEMPLO DE USO
conective, subformulas = PropositionalFormula.get_main_conective_and_immediate_subformulas("(p->(q->p))")
if conective is not None:
  print("valida")
  print(conective, subformulas)
else:
  print("malformulada") """