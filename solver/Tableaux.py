from parser.PropositionalFormula import PropositionalFormula as PF
from solver.BranchsTree import BranchsTree
from solver.RulesExpander import RulesExpander
from _types.FormulaCollection import FormulaCollection

class Tableaux:
    def __init__(self, formulas: FormulaCollection) -> None:
        self.__atomic_formulas_list = []
        self.__branchs = BranchsTree(formulas)
        self.__rules_agent = RulesExpander()

    def solve(self) -> None:
        print(self.__branchs.root.formulas)
        for bind in self.__branchs.root.get_formulas():
            operator, subformulas = PF.get_main_conective_and_immediate_subformulas(bind[0])
            marking = bind[1]

            if operator == 'atom':
                self.__atomic_formulas_list.append(subformulas[0])
                continue
            sub1, sub2 = self.__rules_agent.expand(marking, operator, subformulas)
            self.__branchs.add_formulas_on_root(sub1)
            self.__branchs.add_formulas_on_root(sub2)
        print(self.__branchs.root.formulas)

    