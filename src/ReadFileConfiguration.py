import os

class ReadFileConfiguration:
    def __init__(self, file_name=None):
        self.file_name = file_name
        self.directory_name = "../tests"
        self.puzzles = self.get_puzzles()

    def get_all_files_in_directory(self):
        """
        This method returns a list of all files in a directory
        :param directory: string
        :return: file_name: list of string
        """
        with os.scandir(self.directory_name) as files:
            return [file.name for file in files if file.is_file()]

    def get_spesific_file(self, file_name):
        """
        This method returns a spesific puzzle file
        :param file_name: string
        :return: puzzle: list of list of char
        """
        return self.read_puzzle(file_name)

    def read_puzzle(self, file_name):
        """
        This method reads a file and returns the puzzle
        :param file_name: string
        :return: puzzle: list of list of char
        """
        puzzle = []
        with open(self.directory_name + "/" + file_name, 'r') as f:
            data = f.read()
            for line in data.splitlines():
                # get rid of whitespace
                row = [number for number in line.split()]
                puzzle.append(row)
        return puzzle
            
    def get_puzzles(self):
        """
        This method returns a list of all puzzle files
        :return: list of puzzle
        """
        if(self.file_name is not None):
            return [self.get_spesific_file(self.file_name)]
        return [self.read_puzzle(file_name) for file_name in self.get_all_files_in_directory()]
    

    
