import argparse
import pathlib
import shutil


class Configure:

    home_directory : pathlib.PosixPath

    def __init__(self) -> None:
        self.home_directory = pathlib.PosixPath.home()

    def get_home_directory(self) -> pathlib.PosixPath:
        return self.home_directory
