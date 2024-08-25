from pathlib import Path
from parser.PropositionalFormula import PropositionalFormula

class FileManager: # construir a classe para manipular o arquivos de entrada (.tab)
    @staticmethod    
    def _get_lines_of_file(path: Path) -> list[str] | None:
        with open(path, 'r') as extract_lines:
            if extract_lines:
                return extract_lines.readlines()
        return None
    
    @staticmethod
    def _clear_lines(line_list: list[str]) -> list[str]:
        for i, line in enumerate(line_list):
            line_list[i] = line.replace('\n', '')
            if not PropositionalFormula.formula_is_valid(line_list[i]):
                raise ValueError({'error': 'has an invalid formula'})
        return line_list
    
    @staticmethod
    def _build_marked_formulas(quantity_formulas: int, formulas: list[str]) -> dict[str: bool]:
        marked_formulas = dict()
        for i in range(quantity_formulas - 1):
            marked_formulas[formulas[i]] = True
        marked_formulas[formulas[quantity_formulas - 1]] = False
        return marked_formulas
        
    @staticmethod
    def get_formulas_on_file(file_name: str) -> dict[str: bool] | None:
        path_file = Path(f'../pyTableaux/file_manipulation/inputs/{file_name}')

        if not path_file.exists():
            raise ValueError()
        lines = FileManager._get_lines_of_file(path_file)

        if lines == None:
            return
        try:
            number_formulas = int(lines[0])
            lines = FileManager._clear_lines(lines[1:])
            print(number_formulas, lines)
        except ValueError as e:
            print(e.args[0])
            return
        return FileManager._build_marked_formulas(number_formulas, lines)