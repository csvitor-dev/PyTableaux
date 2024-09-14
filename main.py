""" 
    TRABALHO DE LÓGICA PARA COMPUTAÇÃO
Equipe:
    - Francisco Guilherme Ferreira Dias Martins (515106) [CC]
    - Nicolas Maurício Chaves                   (539802) [ES]
    - Vitor Costa de Sousa                      (536678) [ES]
"""

import sys
from file_manipulation.FileContentValidator import FileContentValidator as FCV
from file_manipulation.FileManagerContent import FileContentManager
from solver.Tableaux import Tableaux

def main() -> None:
    raw: list[str] = sys.stdin.readlines()

    try:
        FCV.validate_file_content(raw)
    except ValueError as e:
        print(e.args[0])
        return
    build = FileContentManager(raw)
    formulas, number_of_atoms = build.get_formulas_on_file()
    
    if formulas is None:
        print("the formulas were not generated")

    tableaux = Tableaux(formulas, number_of_atoms)
    tableaux.exec()

if __name__ == "__main__":
    main()
