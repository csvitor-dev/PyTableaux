from pathlib import Path

class FileReader:

    @staticmethod
    def get_lines_of_file(path: Path) -> list[str] | IOError:        
        with open(path, 'r') as extract_lines:
            if not extract_lines:
                raise IOError({'error': 'could not open file'})
            raw = extract_lines.readlines()
        return FileReader.__clear_lines(raw)
    
    @staticmethod
    def __clear_lines(file_lines: list[str]) -> list[str]:
        for i, line in enumerate(file_lines):
            file_lines[i] = line.replace('\n', '')
        return file_lines