from parser.PropositionalFormula import PropositionalFormula as PF
from solver.BranchsTree import BranchsTree
from solver.RulesExpander import RulesExpander
from utils.Branch import Branch
from utils.mark_mapping import mark_mapping

class Tableaux:
    def __init__(self, formulas: Branch, number_of_atoms: int) -> None:
        self.__marked_atoms = Branch()
        self.__remove_formulas: list[str] = []
        self.__number_of_atoms = number_of_atoms
        self.__branchs = BranchsTree(formulas)
        self.__rules_agent = RulesExpander()

    def exec(self) -> None:
        while self.__branchs.has_open_branch:
            if self.__has_saturated_branch():
                print("unsatisfiable")
                self.__show_marked_atoms()
                return
            open_branch = self.__branchs.find_open_branch()
            self.__solve(open_branch)
        
        print("satisfiable")

    def __solve(self, formulas: Branch) -> None:
        for formula, marking in formulas.marked_formulas:
            operator, subformulas = PF.get_main_conective_and_immediate_subformulas(formula)
            
            if operator == "atom":
                has_conjugate_pair = self.__manipulate_atoms(subformulas[0], marking)
                if has_conjugate_pair:
                    self.__branchs.discard_closed_branch(formulas)
                    return
                continue

            self.__register_expandable_formula(formula)
            result, rule = self.__rules_agent.expand(marking, operator, subformulas)

            if rule == "alpha":
                for alpha in result:
                    self.__branchs.add_formulas_on_branch(alpha, formulas)
            else:
                for beta in result:
                    beta_formula = Branch(beta)
                    self.__branchs.add_branch(beta_formula, formulas)
                    self.__solve(beta_formula)
        self.__active_remove_expandable_formulas()
    
    def __has_saturated_branch(self) -> bool:
        return self.__marked_atoms.length == self.__number_of_atoms
    
    def __manipulate_atoms(self, atom: str, marking: bool) -> bool:
        if not self.__marked_atoms.contains(atom):
            self.__marked_atoms.add_formula((atom, marking))
            return False
        if marking != self.__marked_atoms.value(atom):
            self.__marked_atoms.drop_formula(atom)
            return True
        return False
    
    def __show_marked_atoms(self) -> None:
        marked_atoms =  [f"{mark_mapping[marking]}{atom}" for atom, marking in self.__marked_atoms.marked_formulas]

        for atom in marked_atoms:
            print(atom, end=" ")

    def __register_expandable_formula(self, formula: str) -> None:
        self.__remove_formulas.append(formula)

    def __active_remove_expandable_formulas(self) -> None:
        while len(self.__remove_formulas) > 0:
            formula = self.__remove_formulas.pop()
            self.__branchs.remove_formula_on_branch(formula)