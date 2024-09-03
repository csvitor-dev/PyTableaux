from parser.PropositionalFormula import PropositionalFormula as PF
from solver.BranchsTree import BranchsTree
from solver.RulesExpander import RulesExpander
from _types.FormulaCollection import FormulaCollection
from _types.mark_mapping import mark_mapping

class Tableaux:
    def __init__(self, formulas: FormulaCollection, number_of_atoms: int) -> None:
        self.__marked_atoms = FormulaCollection()
        self.__remove_formulas = []
        self.__number_of_atoms = number_of_atoms
        self.__branchs = BranchsTree(formulas)
        self.__rules_agent = RulesExpander()

    def exec(self) -> None:

        if self.__branchs.has_open_branch:
            open_branch = self.__branchs.find_open_branch()
            self.__solve(open_branch)

        if self.__marked_atoms.length == self.__number_of_atoms:
            print("unsatisfiable")
            self.__show_marked_atoms()
            return
            
        if self.__sat():
            print("satisfiable")
            return
        self.exec()
            
    def __solve(self, formulas: FormulaCollection) -> None:
        for formula, marking in formulas.get_formulas():
            operator, subformulas = PF.get_main_conective_and_immediate_subformulas(formula)
            self.__register_expandable_formula(marking, operator, formula)

            result, rule = self.__rules_agent.expand(marking, operator, subformulas)

            if rule == "atom":
                if not self.__marked_atoms.contains(formula):
                    ...
                self.__marked_atoms.add_formula((formula, marking))

            if rule == "beta":
                ...
            print(result)
        self.__active_remove_expandable_formulas()

    def __sat(self) -> bool:
        return self.__marked_atoms.length < self.__number_of_atoms
    
    def __show_marked_atoms(self) -> None:
        marked_atoms =  [f"{mark_mapping[marking]}{atom}" for atom, marking in self.__marked_atoms.get_formulas()]

        for atom in marked_atoms:
            print(atom, end=" ")

    def __register_expandable_formula(self, operator: str, formula: str) -> None:
        if operator == "atom":
            return
        self.__remove_formulas.append(formula)

    def __active_remove_expandable_formulas(self) -> None:
        while len(self.__remove_formulas) > 0:
            formula = self.__remove_formulas.pop()
            self.__branchs.remove_formula_on_branchs(formula)