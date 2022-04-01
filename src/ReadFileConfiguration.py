import os

class ReadFileConfiguration:
    def __init__(self):
        self.directory_name = "../tests"
        self.puzzles = self.get_puzzles()

    def get_all_files_in_directory(self, directory):
        """
        This method returns a list of all files in a directory
        :param directory:
        :return:
        """
        with os.scandir(directory) as files:
            return [file.name for file in files if file.is_file()]

    def read_puzzle(self, file_name):
        """
        This method reads a file and returns the content of the file
        :param file_name:
        :return:
        """
        puzzle = []
        with open(self.directory_name + "/" + file_name, 'r') as f:
            data = f.read()
            for line in data.splitlines():
                # get rid of whitespace)
                row = [number for number in line.split()]
                puzzle.append(row)
        return puzzle
            
    def get_puzzles(self):
        """
        This method returns a list of all puzzle files
        :return:
        """
        return [self.read_puzzle(file) for file in self.get_all_files_in_directory(self.directory_name)]
    

    
