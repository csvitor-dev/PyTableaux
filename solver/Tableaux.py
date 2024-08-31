from parser.PropositionalFormula import PropositionalFormula as PF
from solver.BranchsTree import BranchsTree
from solver.RulesExpander import RulesExpander
from _types.FormulaCollection import FormulaCollection
from _types.mark_mapping import mark_mapping

class Tableaux:
    def __init__(self, formulas: FormulaCollection, number_of_atoms: int) -> None:
        self.__marked_atoms = FormulaCollection()
        self.__number_of_atoms = number_of_atoms
        self.__branchs = BranchsTree(formulas)
        self.__rules_agent = RulesExpander()

    def solve(self) -> None:
        i = 0
        while self.__branchs.has_open_branch:
            
            if self.__marked_atoms.length == self.__number_of_atoms:
                print("unsatisfiable")
                self.__show_marked_atoms()
                return
            
            # root = self.__branchs.root
            if self.__sat():
                print("satisfiable")
                return

    def __sat(self) -> bool:
        return self.__marked_atoms.length < self.__number_of_atoms
    
    def __show_marked_atoms(self) -> None:
        marked_atoms =  [f"{mark_mapping[marking]}{atom}" for atom, marking in self.__marked_atoms.get_formulas()]

        for atom in marked_atoms:
            print(atom, end=" ")

