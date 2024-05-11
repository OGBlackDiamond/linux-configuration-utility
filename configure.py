import argparse
import pathlib
import shutil


class Configure:

    home_directory : pathlib.PosixPath

    def __init__(self) -> None:
        self.home_directory = pathlib.PosixPath.home()


