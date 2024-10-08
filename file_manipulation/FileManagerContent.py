from utils.FormulaBuilder import FormulaBuilder as FB
from utils.Branch import Branch

class FileContentManager: 
    '''
    Classe de ajuste de fórmulas, alinhando os dados de dentro dos arquivos para análises.
    '''

    def __init__(self, raw_file_content: list[str]) -> None:
        self.__file_content: list[str] = self.__clear_content(raw_file_content)

    def __clear_content(self, arg: list[str]) -> list[str]:
        for index, line in enumerate(arg):
            arg[index] = line.replace('\n', '')
        return arg

    def get_formulas_on_file(self) -> tuple[Branch, int] | None:
        number_formulas = int(self.__file_content[0])
        formulas = self.__file_content[1:]
        return FB.build_marked_formulas(number_formulas, formulas)
