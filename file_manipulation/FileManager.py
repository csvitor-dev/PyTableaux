from pathlib import Path
from file_manipulation.FormulaBuilder import FormulaBuilder as FB
from file_manipulation.FileReader import FileReader as FR

class FileManager:  
    @staticmethod
    def get_formulas_on_file(file_name: str) -> dict[str: bool] | None:
        try:
            lines = FR.get_lines_of_file(Path(f'../pyTableaux/file_manipulation/inputs/{file_name}'))
        except FileNotFoundError as e:
            print(e.args[0])
            return
        except IOError as e:
            print(e.args[0])
            return
        
        try:
            number_formulas = int(lines[0])
            lines = FR.clear_lines(lines[1:])
        except ValueError as e:
            print(e.args[0])
            return
        return FB.build_marked_formulas(number_formulas, lines)