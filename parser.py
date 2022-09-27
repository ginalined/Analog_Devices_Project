"""
Parser Class
author: Hao Ding
"""
import argparse
import os


def count_line(file_name):
    """
    count number of line in a file
    """
    with open(file_name, "rb") as file:
        return sum(1 for _ in file)
class Parser:
    """_summary_
    The class locate all files with the given extension
    in the given directory and all its subdirectories
    to produce a list of all matching files with the
    numbers of lines within the file.
    """

    def __init__(self, dir_name, ext_name):
        """
        Args:
            dir_name (str): directory name
            ext_name (str): extension name such as .txt
        """
        self.dir_name = str(dir_name)
        self.ext_name = str(ext_name)
        self.files = []
        self.lines = []

    def get_all_files(self):
        """_summary_
        Find all files under a directory recursively
        Returns:
            bool: whether the operation succeed or not
        """
        if not os.path.exists(self.dir_name) or not os.path.isdir(self.dir_name):
            print("Incorrect path name.")
            return False

        if not os.access(self.dir_name, os.R_OK):
            print("Permission deny.")
            return False

        for root, _, names in os.walk(self.dir_name, topdown=False):
            for name in names:
                real_name = os.path.join(root, name)
                if real_name.endswith(self.ext_name):
                    num_line = 0
                    try:
                        num_line = count_line(real_name)
                    except EnvironmentError as error:
                        print(error)
                        continue

                    self.files.append(real_name)
                    self.lines.append(num_line)
        return True


    def print_table(self):
        """
        print stats
        """
        max_name = max([len(x) for x in self.files]) + 4
        total_line = 0
        for file, line in zip(self.files, self.lines):
            total_line += line
            print(file + " " * (max_name - len(file)) + str(line))

        print("=" * (max_name + 6))
        print("Number of files found: " + str(len(self.files)))
        print("Total number of lines: " + str(total_line))
        print("Average lines per file: " +
              str(float(total_line) / len(self.files)))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--ext', '-e', type=str,  default='.txt',
                        help='file extension')
    parser.add_argument('--dir', '-d', type=str,
                        required=True, help='name of directory.')

    args = parser.parse_args()

    parser = Parser(args.dir, args.ext)
    if parser.get_all_files():
        parser.print_table()
