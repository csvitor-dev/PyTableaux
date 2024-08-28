import re

class FileContentValidator:
    
    @staticmethod
    def validate_file_content(arg: list[str]) -> bool:
        pattern: str = "^(?:¬?[\\(\\)\\w0-9_](?:->|&|\\|)?)*$"
        for line in arg:
            if not re.match(pattern, line):
                raise ValueError({'error': 'The input file does not match the processing'})
