import argparse
import pathlib

from neovim.neovim import NeoVim

parser = argparse.ArgumentParser(
    prog="Linux Configuration Utility",
    description="A configuration utility for linux systems to reduce time needed to setup.",
)

parser.add_argument("-r", "--remove", action="store_true")
parser.add_argument("-n", "--nvim", action="store_true")


class Configure:

    home_directory: pathlib.PosixPath

    args: argparse.Namespace

    def __init__(self) -> None:
        self.home_directory = pathlib.PosixPath.home()
        self.args = parser.parse_args()
        self.handle_args()

    def handle_args(self):
        if self.args.nvim and self.args.remove:
            print("Hello")

    def get_home_directory(self) -> pathlib.PosixPath:
        return self.home_directory


a = Configure()
