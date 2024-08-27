from pathlib import Path
from file_manipulation.FileReader import FileReader as FR
from solver.FormulaBuilder import FormulaBuilder as FB

class FileManager: 

    def __init__(self, file_name: str) -> None:
        self.__path_ = Path(f'../pyTableaux/inputs/{file_name}')
    
    def __path_is_valid(self) -> bool:
        return self.__path_.exists()

    def get_formulas_on_file(self) -> dict[str: bool] | None:
        if not self.__path_is_valid():
            raise FileNotFoundError({'error': f'file not found on path: {self.__path_}'})

        try:
            formulas = FR.get_lines_of_file(self.__path_)
        except IOError as e:
            print(e.args[0])
            return
        number_formulas = int(formulas[0])
        return FB.build_marked_formulas(number_formulas, formulas)
