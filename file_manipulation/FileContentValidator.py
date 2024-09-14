import re

class FileContentValidator:
    '''
    Classe para validação do conteúdo do arquivo.
    :
    retona a confirmação (ou não) da veracidade do arquivo.
    '''
       
    @staticmethod
    def validate_file_content(arg: list[str]) -> bool:
        pattern: str = "^(?:¬?[\\(\\)\\w0-9_](?:->|&|\\|)?)*$"
        for line in arg:
            if not re.match(pattern, line):
                raise ValueError({'error': 'The input file does not match the processing'})
