from parser.PropositionalFormula import PropositionalFormula as PF
from solver.BranchsTree import BranchsTree
from solver.RulesExpander import RulesExpander
from _types.FormulaCollection import FormulaCollection

class Tableaux:
    def __init__(self, formulas: FormulaCollection) -> None:
        self.__atomic_formulas_list = []
        self.__branchs = BranchsTree(formulas)
        self.__formulas = formulas
        self.__rules_agent = RulesExpander()

    def solve(self) -> None:
        for formula in self.__formulas.get_formulas():
            print(PF.get_main_conective_and_immediate_subformulas(formula))
    