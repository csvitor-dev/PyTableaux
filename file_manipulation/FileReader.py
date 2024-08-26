from pathlib import Path
from parser.PropositionalFormula import PropositionalFormula as PF

class FileReader:
    @staticmethod
    def _path_is_valid(path: Path) -> bool:
        return path.exists()

    @staticmethod
    def get_lines_of_file(path: Path) -> list[str] | FileExistsError | IOError:
        if not FileReader._path_is_valid(path):
            raise FileNotFoundError({'error': f'file not found on path: {path}'})
        
        with open(path, 'r') as extract_lines:
                if not extract_lines:
                    raise IOError({'error': 'could not open file'})
                return extract_lines.readlines()
    
    @staticmethod
    def clear_lines(line_list: list[str]) -> list[str] | ValueError:
        for i, line in enumerate(line_list):
            line_list[i] = line.replace('\n', '')
            if not PF.formula_is_valid(line_list[i]):
                raise ValueError({'error': f'has an invalid formula {line_list[i]}'})
        return line_list