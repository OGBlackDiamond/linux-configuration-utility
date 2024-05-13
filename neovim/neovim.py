import os
import pathlib
import shutil

from configure import Configure


class NeoVim:

    nvim_directory: pathlib.PosixPath

    lua_directory: pathlib.PosixPath
    plugins_directory: pathlib.PosixPath

    def __init__(self, configure: Configure) -> None:
        self.nvim_directory = configure.get_home_directory().joinpath(".config/nvim/")

    def ensure_fs(self):
        self.nvim_directory.mkdir(parents=True, exist_ok=True)
        self.lua_directory = self.nvim_directory.joinpath("lua/")
        self.plugins_directory = self.lua_directory.joinpath("plugins/")
