""" 
    TRABALHO DE LÓGICA PARA COMPUTAÇÃO
Equipe:
    - Nicolas
    - Vitor Costa de Sousa (536678)[ES]
"""

import sys
from file_manipulation.FileManagerContent import FileContentManager

def main() -> None:
    raw: list[str] = sys.stdin.readlines()

    build = FileContentManager(raw)
    formulas = build.get_formulas_on_file()
    
    if not formulas is None:
        print(formulas)

if __name__ == "__main__":
    main()
