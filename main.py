from parser.PropositionalFormula import PropositionalFormula

#EXEMPLO DE USO
conective, subformulas = PropositionalFormula.get_main_conective_and_immediate_subformulas("(p->(q->p))")
if conective is not None:
  print("valida")
  print(conective, subformulas)
else:
  print("malformulada")