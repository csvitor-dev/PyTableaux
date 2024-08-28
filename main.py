""" 
    TRABALHO DE LÓGICA PARA COMPUTAÇÃO
Equipe:
    - Nicolas
    - Vitor Costa de Sousa (536678)[ES]
"""

import sys
from file_manipulation.FileContentValidator import FileContentValidator as FCV
from file_manipulation.FileManagerContent import FileContentManager

def main() -> None:
    raw: list[str] = sys.stdin.readlines()

    try:
        FCV.validate_file_content(raw)
    except ValueError as e:
        print(e.args[0])
        return
    build = FileContentManager(raw)
    formulas = build.get_formulas_on_file()
    
    if formulas is None:
        print("the formulas were not generated")

if __name__ == "__main__":
    main()
