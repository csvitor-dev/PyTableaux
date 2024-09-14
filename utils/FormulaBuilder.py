import re
from parser.PropositionalFormula import PropositionalFormula as PF
from utils.Branch import Branch

class FormulaBuilder:
    """ a classe `FormulaBuilder` contém dois métodos estáticos (__validate_formulas e build_marked_formulas). A função principal dessa classe é construir e validar fórmulas proposicionais e marcá-las com valores booleanos, retornando-as em um objeto Branch junto com o número de átomos presentes nas fórmulas."""
    @staticmethod
    def __validate_formulas(formulas: list[str]) -> ValueError | None:
        for sentence in formulas:    
            if not PF.formula_is_valid(sentence):
                raise ValueError({'error': f'has an invalid formula {sentence}'})

    @staticmethod
    def build_marked_formulas(amount: int, formulas: list[str]) -> tuple[Branch, int] | None:
        try:
            FormulaBuilder.__validate_formulas(formulas)
        except ValueError as e:
            print(e.args[0])
            return
        
        number_of_atoms = FormulaBuilder.__number_of_atoms(formulas)

        marked_formulas = Branch()
        for i in range(amount - 1):
            marked_formulas.add_formula((formulas[i], True))
        marked_formulas.add_formula((formulas[amount - 1], False))
        return marked_formulas, number_of_atoms
    
    @staticmethod
    def __number_of_atoms(formulas: list[str]) -> int:
        atoms_set = set()

        for formula in formulas:
            atom_list = re.sub(r"\W+", ' ', formula).split()
            for atom in atom_list:
                atoms_set.add(atom)
        return len(atoms_set)